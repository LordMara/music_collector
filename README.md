# music_collector

## Story
Do you like to listen to music? Mate loves it! He is the owner of a music store CoolMusic. Business developes really fast and he has a problem with arrangement the albums. Please, help him to create the catalog of all albums.

## Description
* Create a list music for storing his music albums. 
* Every element is a complex of two tuples - name and information
* Tuple name contains two strings - a name of artist and a name of album.
* Tuple information contains integer and two strings - year of release, genre and length.

### Example:
<code> music = [(("Pink Floyd", "The Dark Side Of The Moon"), (1973, "psychodelic rock", "43:00")),
         (("Britney Spears", "Baby One More Time"), (1999, "pop", "42:20"))] </code>
         
Below is a the example menu. Your program should carry out the following functionalities.
> Welcome in the CoolMusic! Choose the action:<br>
> 1) Add new album<br>
> 2) Find albums by artist<br>
> 3) Find albums by year<br>
> 4) Find musician by album<br>
> 5) Find albums by letter(s)<br>
> 6) Find albums by genre<br>
> 7) Calculate the age of all albums<br>
> 8) Choose a random album by genre<br>
> 9) Show the amount of albums by an artist *<br>
> 10) Find the longest-time album *<br>
> 0) Exit <br>
> \* additional features (for 12 pts)

## Details
1. The catalog has to be read from and written into CSV file music.csv You don't have to push it into repository, your program will be tested with our file.
2. Your script should be based on custom functions.
3. The name of album should be printed with the name of artist.
4. Album should be find by letters in any place of title. For example, if user input "the", program will print
every albums with "the" in the title - "The Dark Side of The Moon" and "Music of the Sun".
