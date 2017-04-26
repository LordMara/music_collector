#!/usr/bin/python3

import csv
import random
import datetime
from datetime import date


def menu():     # Print menu
    """Print menu for application"""
    menu = """Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s)
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose a random album by genre
         9) Show the amount of albums by an artist
        10) Find the longest-time album
         0) Exit"""
    return menu


def is_number(number):
    """Check if input is an int"""
    try:
        int(number)
        return True
    except ValueError:
        pass


def good_lenght(time):
    """Check if album lenght have correct format"""
    time_of_album = list(time.split(":"))
    try:
        int(time_of_album[0])
        int(time_of_album[1])
        if int(time_of_album[0]) > 0:
            return True
        pass
    except (ValueError, IndexError):
        pass


def music():        # read csv file with database
    """Read csv file and convert information to good format, return list with full collection in good format"""
    music = []      # establish list for use
    with open('music.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:     # what with this coding
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            if len(row) != 5:     # pass problem with empty row
                continue
            else:
                row[0] = row[0].strip()     # eliminate leading whitespaces
                row[1] = row[1].strip()
                name = (row[0], row[1])     # make tuplet with artist and album name
                if not is_number(row[2]):      # pass problem with change empty element (str) into 0
                    row[2] = 0
                else:
                    row[2] = int(row[2])        # change date of album to int
                row[3] = row[3].strip().lower()
                if not good_lenght(row[4]):
                    row[4] = "00:00"
                else:
                    row[4] = row[4].strip()
                information = (row[2], row[3], row[4])      # make tuplet with year of release, genre and length
                name_and_information = (name, information)      # make tuplet with 2 tuplets
                music.append(name_and_information)      # add all information to 1 list
        return music


def numer_albums(artist):
    """Count number of albums of given artist"""
    mus = music()
    count = 0
    for x in range(0, len(mus)):
        if artist.lower() == mus[x][0][0].lower():
            count += 1
    return count


def add(artist, album, year, genre, time):
    """Add new entry to collection (csv file)"""
    with open('music.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        new_music = csv.writer(csvfile, delimiter='|')
        new_music.writerow([artist] + [album] + [year] + [genre] + [time])


def any_phrase(phrase):
    """Check if given phrase is in any album name and show that album, return list of matched entries"""
    mus = music()
    music_list = []
    for index in range(0, len(mus)):
        if phrase.lower() in mus[index][0][1].lower():
            music_list.append("Artist: " + " - Album: ".join(mus[index][0]))
    return music_list


def album_artist(ask, command):
    """Made dictionary with proper key depend from argument and return result as output from search by argument ask"""
    mus = music()
    search_output = None
    my_music = {}       # establish dictionary to later use
    for index in range(len(mus)):     # made proper key and entry for it
        if command == "2":        # Find albums by artist
            key = mus[index][0][0]      # key artist name
            search_output = mus[index][0]
            # if key present add new value to it, if not add pair key-value to dictionary
            my_music.setdefault(key.lower(), []).append("Artist: " + " - Album: ".join(search_output))
        elif command == "4":      # Find musician by album
            key = mus[index][0][1]      # album name
            search_output = mus[index][0][0]
            my_music.setdefault(key.lower(), "Artist: " + search_output)
        elif command == "6":      # Find album by genre
            key = mus[index][1][1]      # key genre
            search_output = mus[index][0]
            my_music.setdefault(key.lower(), []).append("Artist: " + " - Album: ".join(search_output))
        ask = ask.lower()
    return my_music.get(ask)


def search_year(year):
    """Find album by year, return all albums from given year"""
    mus = music()
    search_output = 0
    my_music = {}       # establish dictionary to later use
    for index in range(len(mus)):     # made proper key and entry for it
        key = mus[index][1][0]      # key year of publishing album
        search_output = mus[index][0]
        my_music.setdefault(key, []).append("Artist: " + " - Album: ".join(search_output))
    return my_music.get(year)


def ages():
    """Sume age of all albums in csv file"""
    mus = music()
    now = date.today()      # current date (year month, day)
    now_year = now.year     # current year as int
    age_sum = 0
    for index in range(0, len(mus)):
        if not mus[index][1][0]:
            continue
        else:
            age_sum += (now_year - mus[index][1][0])
    return age_sum


def random_album(genre):
    """Pick random album by genere"""
    mus = music()
    album_genre = None
    random_list = []
    not_in_database = "No such genre in data base"
    my_music = {}       # establish dictionary to later use
    for index in range(len(mus)):     # made proper key and entry for it
        key = mus[index][1][1]        # key genre
        album_genre = mus[index][0]
        my_music.setdefault(key, []).append("Artist: " + " - Album: ".join(album_genre))
    list_of_picks = (my_music.get(genre, [not_in_database]))        # add all albums that are choosen genre
    random_pick = (random.randint(0, len(list_of_picks) - 1))       # choose random index number for list_of_picks
    return list_of_picks[random_pick]


def the_biggest():
    """Return the longest album name with artist"""
    mus = music()
    calc_time = []      # list where calculated "lenght" use to sort will be "created"
    to_sort = []        # list where data will be sorted by key
    for index in range(len(mus)):
        calc_time.append(mus[index][1][2])
        calc_time[index] = list(calc_time[index].split(":"))
        calc_time[index][0] = int(calc_time[index][0]) + (int(calc_time[index][1])/60)
        temp = (mus[index], calc_time[index][0])
        to_sort.append(temp)
    to_sort = sorted(to_sort, key=lambda temp: temp[1])     # key "calculated lenght""
    return "Artist: " + " - Album: ".join(to_sort[-1][0][0])


def menu_check(command):
    """Check if input in menu have correct format and is in range"""
    try:
        int(command)
        if int(command) in range(0, 11):
            return True
        pass
    except (ValueError, IndexError):
        pass


def main():
    """Main function"""
    while True:
        print(menu())
        menu_use = input().strip()
        while not menu_check(menu_use):
                menu_use = input("Wrong command. Enter new one: ").strip()

        if menu_use == "1":     # add new entry to csv file
            new_artis = input("Add artist: ")
            new_album = input("Add album: ")
            new_year = input("Add year: ")
            while not is_number(new_year):
                new_year = input("Invalid input. Add year: ")
            new_genre = input("Add genre: ")
            new_lenght = input("Add lenght: ")
            while not good_lenght(new_lenght):
                new_lenght = input("Invalid input. Add lenght: ")
            add(new_artis, new_album, new_year, new_genre, new_lenght)
            print("")

        elif menu_use == "2":     # Find albums by artist
            artist = input("Enter name of the artist: ").strip()
            print("")
            collection = album_artist(artist, menu_use)
            if not artist:
                print("Invalid input", '\n')
                continue
            if collection is not None:
                for ask in range(len(collection)):
                        print(collection[ask])
            else:
                print("No such artst in databse")
            print("")

        elif menu_use == "3":       # Find albums by year
            year = input("Enter year you want to find albums from: ")
            print("")
            if not is_number(year):
                print("Invalid input", '\n')
                continue
            else:
                year = int(year)
                collection = search_year(year)
                if collection is not None:
                    for ask in range(len(collection)):
                        print(collection[ask])
                else:
                    print("No albums from that year in database")
            print("")

        elif menu_use == "4":       # Find musician by albume
            album_name = input("Enter name of the album: ").strip()
            print("")
            collection = album_artist(album_name, menu_use)
            if not album_name:
                print("Invalid input", '\n')
                continue
            if collection is not None and len(collection) != 0:
                print(collection)
            else:
                print("No such album in thata base")
            print("")

        elif menu_use == "5":       # Find album by letter(s)
            phrase = input("Enter phrase you want to use to search: ").strip()
            print("")
            collection = any_phrase(phrase)
            if not phrase:
                print("Invalid input", '\n')
                continue
            if collection is not None and len(collection) != 0:
                for ask in range(len(collection)):
                        print(collection[ask])
            else:
                print("No such entry in any album name")
            print("")

        elif menu_use == "6":       # Find album by genre
            genre = input("Enter genre you want to choose: ").strip()
            print("")
            collection = album_artist(genre, menu_use)
            if not genre:
                print("Invalid input", '\n')
                continue
            if collection is not None:
                for ask in range(len(collection)):
                        print(collection[ask])
            else:
                print("No such genre in data base")
            print("")

        elif menu_use == "7":       # Sume of all albums age
            print("Sume age of all albums is:", ages(), '\n')

        elif menu_use == "8":       # Find album by genre
            genre_random = input("Enter genre you want to choose: ").strip()
            print("")
            if not genre_random:
                print("Invalid input", '\n')
                continue
            print(random_album(genre_random), '\n')

        elif menu_use == "9":       # Find amoutn albums by artist
            number_artist = input("Enter artsist name: ").strip()
            print("")
            if not number_artist:
                print("Invalid input", '\n')
                continue
            print("Amount of albums by", number_artist, ":", numer_albums(number_artist), '\n')

        elif menu_use == "10":       # Find the longest album
            print("The longest albums is:", the_biggest(), '\n')

        elif menu_use == "0":       # Exit
            exit()

main()
