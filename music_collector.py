#!/usr/bin/python3

import csv
import random
import datetime
from datetime import date


def menu():     # Print menu
    """Print menu for application"""
    a = """Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s)
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose a random album by genre
         9) Show the amount of albums by an artist
        10) Find the longest-time album *   # in dev
         0) Exit"""
    return a


def is_number(a):
    """Check if input is an int"""
    try:
        int(a)
        return True
    except ValueError:
        pass


def good_lenght(a):
    """Check if input have correct format"""
    x = list(a.split(":"))
    try:
        int(x[0])
        int(x[1])
        if int(x[0]) > 0:
            return True
        pass
    except (ValueError, IndexError):
        pass


def music():        # read csv file with database
    """Read csv file and convert information to good format"""
    music = []      # establish list for use
    with open('music.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:     # what with this coding
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            if len(row) != 5:     # pass problem with empty list
                continue
            else:
                row[0] = row[0].strip()     # eliminate leading whitespaces
                row[1] = row[1].strip()
                name = (row[0], row[1])     # make tuplet with artist and album name
                if not is_number(row[2]):      # pass problem with change empty element (str) into 0
                    row[2] = 0       # more tests needed!!! 0 or None
                else:
                    row[2] = int(row[2])        # change date of album to int
                row[3] = row[3].strip().lower()
                if not good_lenght(row[4]):
                    row[4] = "00:00"       # more tests needed!!! 0 or None
                else:
                    row[4] = row[4].strip()
                information = (row[2], row[3], row[4])      # make tuplet with year of release, genre and length
                name_and_information = (name, information)      # make tuplet with 2 tuplets
                music.append(name_and_information)      # add all information to 1 list
        return music


def numer_albums(a):
    """Count number of albums of given artist"""
    z = music()
    i = 0
    for x in range(0, len(z)):
        if a.lower() == z[x][0][0].lower():
            i += 1
    return i


def add(a, b, c, d, e):
    """Add new entry to csv file"""
    with open('music.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        new_music = csv.writer(csvfile, delimiter='|')
        new_music.writerow([a] + [b] + [c] + [d] + [e])
    return None


def any_phrase(a):
    """Check if given phrase is in any album name and show that album"""
    z = music()
    x = []
    for i in range(0, len(z)):
        if a.lower() in z[i][0][1].lower():
            x.append("Artist: " + " - Album: ".join(z[i][0]))
    return x


def album_artist(a, b):
    """Made dictionary with proper key depend from argument and give result as outp from search"""
    z = music()
    x = 0
    my_music = {}       # establish dictionary to later use
    for i in range(len(z)):     # made proper key and entry for it
        if b == "2":        # Find albums by artist
            key = z[i][0][0]
            x = z[i][0]
            my_music.setdefault(key.lower(), []).append("Artist: " + " - Album: ".join(x))      # if entry add key
        elif b == "3":      # Find albums by year
            key = z[i][1][0]
            x = z[i][0]
            my_music.setdefault(key.lower(), []).append("Artist: " + " - Album: ".join(x))      # if entry add key
        elif b == "4":      # Find musician by album
            key = z[i][0][1]
            x = z[i][0][0]
            my_music.setdefault(key.lower(), "Artist: " + x)
        elif b == "6":      # Find album by genre
            key = z[i][1][1]
            x = z[i][0]
            my_music.setdefault(key.lower(), []).append("Artist: " + " - Album: ".join(x))      # if entry add key
        a = a.lower()
    return my_music.get(a)


def search_year(a):
    z = music()
    c = "No albums from that year in database or invalid input"
    x = 0
    my_music = {}       # establish dictionary to later use
    for i in range(len(z)):     # made proper key and entry for it
        key = z[i][1][0]
        x = z[i][0]
        my_music.setdefault(key, []).append("Artist: " + " - Album: ".join(x))      # if entry add key and information
    return my_music.get(a)


def ages():
    """Sume age of all albums in csv file"""
    z = music()
    now = date.today()      # current date (year month, day)
    now_year = now.year     # current year as int
    age_sume = 0
    for i in range(0, len(z)):
        if not z[i][1][0]:
            continue
        else:
            age_sume += (now_year - z[i][1][0])
    return age_sume


def random_album(a):
    """Pick random album by genere"""
    z = music()
    x = 0
    random_list = []
    c = "No such genre in data base"
    my_music = {}       # establish dictionary to later use
    for i in range(len(z)):     # made proper key and entry for it
        key = z[i][1][1]        # key genre
        x = z[i][0]
        my_music.setdefault(key, []).append("Artist: " + " - Album: ".join(x))
    random_list = (my_music.get(a, [c]))        # add all albums that are choosen genre
    g = (random.randint(0, len(random_list) - 1))       # choose random index number for random_list
    return random_list[g]


def menu_check(a):
    """Check if input in menu have correct format and is in range"""
    try:
        int(a)
        if int(a) in range(0, 10):
            return True
        pass
    except (ValueError, IndexError):
        pass


while True:     # body of our application
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
        v = album_artist(artist, menu_use)
        if not artist:
            print("Invalid input", '\n')
            continue
        if v is not None:
            for x in range(0, len(v)):
                    print(v[x])
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
            v = search_year(year)
            if v is not None:
                for x in range(0, len(v)):
                    print(v[x])
            else:
                print("No albums from that year in database")
        print("")

    elif menu_use == "4":       # Find musician by albume
        album_name = input("Enter name of the album: ").strip()
        print("")
        v = album_artist(album_name, menu_use)
        if not album_name:
            print("Invalid input", '\n')
            continue
        if v is not None and len(v) != 0:
            print(v)
        else:
            print("No such album in thata base")
        print("")

    elif menu_use == "5":       # Find album by letter(s)
        phrase = input("Enter phrase you want to use to search: ").strip()
        print("")
        v = any_phrase(phrase)
        if not phrase:
            print("Invalid input", '\n')
            continue
        if v is not None and len(v) != 0:
            for x in range(0, len(v)):
                    print(v[x])
        else:
            print("No such entry in any album name")
        print("")

    elif menu_use == "6":       # Find album by genre
        genre = input("Enter genre you want to choose: ").strip()
        print("")
        v = album_artist(genre, menu_use)
        if not genre:
            print("Invalid input", '\n')
            continue
        if v is not None:
            for x in range(0, len(v)):
                    print(v[x])
        else:
            print("No such genre in data base")
        print("")

    elif menu_use == "7":       # Sume of all albums age
        print('\n', "Sume age of all albums is:", ages(), '\n')

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

    elif menu_use == "0":       # Exit
        exit()
