SVGCards
========

Public-domain jumbo index playing card decks with two- and four-color suits.  Decks are available with both traditional vertical indices and also with side-by-side indices.  

It is difficult to find public domain playing cards, let alone ones with jumbo indexes.  Particularly for solitaire games, jumbo index decks are desirable.  These decks are in two flavors: vertical, which means that the indexes are in the traditional format, with the suit symbol below the rank symbol, and horizontal, with the suit symbol to the right of the rank symbol.  I have found that in solitaire games like spider, where the piles can get very long, that I prefer the horizontal layout so that the vertical offset between two cards in a pile can be smaller.

The suits on some of the decks come in four colors.  No doubt, better choices are  possible; once again, I am not an artist.  The python script cardColors.py, detailed below, can be used to modify the suit colors.  If you are an artist, and come up with a better scheme, I would urge you to make it freely available, though of course, you need not.

Three python scripts are included: 

+    cardColors.py for editing the suit colors, 
+    exportSVG.py for extracting individual cards as SVG files from the sprite sheets, 
+    exportPNG.py for extracting the individual cards as PNG files. 

In order for the last two scripts to be useful, Inkscape must be installed. Inkscape is free, open-source software, and may be downloaded from https://inkscape.org.

Details are given below.

Graphics Files
============== 

The Decks folder contains five subfolders:

+    Vertical2 
+    Vertical4 
+    Horizontal2 
+    Horizontal4
+    Accessible

As you've guessed, the folders ending in "2" contain two-color suits, and those ending in "4" have four-color suits.  The "Vertical" folders have the indices arranged traditionally the "Horizontal" folders have them side-by-side.  The Accessible folder also has four-color suits, but with greater contrast among the colors, and is itself divided into Horizontal and Vertical subfolders.  Each folder contains  folders named "pngs" and "svgs" containing PNG, and SVG images of the individual cards and a sprite sheet.  The SVG cards are 210 pixels wide by 315 pixels high.  The PNG cards are 75 pixels wide by 315 pixels high.     

Editing
-------

If you just want to change the colors of the suits, it's easiest to use cardColors.py.  If you want to make more basic changes, using Inkscape say, you should note that each card has an ID such as "heart6" or "diamondQueen".  When you ungroup the card to work on its elements, this ID is lost.  You should restore the ID's after re-grouping the elements, as exportSVG.py and exportPNG.py depend on them.  (I imagine that Illustrator works similarly, but I've never used it.)

To edit the graphics, edit the sprite.svg files in the subfolders of the Decks folder.

CardColors.py
=============

Edit the suit colors on the SVG sprite sheets.

usage
-----

    cardColors.py oldFile newFile [options]

arguments
---------  

**positional arguments:**  

     oldFile            source sprite file path  
     newFile            target sprite file path  

**optional arguments:** 

    -h, --help                             show this help message and exit  
    -C CLUB, --clubs CLUB                  New club color  
    -D DIAMOND, --diamonds DIAMOND         New diamond color  
    -H HEART, --hearts HEART               New heart color  
    -S SPADE, --spades SPADE               New spade color  
    -B BACKGROUND, --background BACKGROUND New card background color  
                        
    The new colors should be given in six-character RGB format.  You can change as many colors as you like. 

requirements
------------

This program requires python.  It has been tested under python 3.8. 

example
-------

    cardColors.py [path1]/sprite.svg [path2]/sprite.svg -C 00ff00 -B ffffff

will create a new sprite sheet with bright green clubs and white card backgrounds, where path1 and path2 are appropriate paths to the input and output folders.

exportPNG.py
============

Export SVG cards files from sprite sheet to PNG files, or make a PNG sprite sheet.

usage
-----

    exportPNG.py source folder [options]

arguments
---------

**positional arguments:**  

    source    source sprite file path  
    folder    parent directory for png folder 
    
    The folder argument is the name folder that will contain a "pngs" subfolder into 
    which the PNG files will be written.  It will be created if it doesn't exist.

**optional arguments:**

    -h, --help                       show this help message and exit  
    -s, --sprite                     create sprite sheet also   
    -o, --sprite_only                create sprite sheet only  
    -w WIDTH, --width WIDTH          image width (default 75 pixels)  
    -i INKSCAPE, --inkscape INKSCAPE path to inkscape  
    
    The --width argument controls the width of the cards, both for individual files and 
    for sprite sheets.  
    The --sprite parameter indicates that a sprite sheet should be produced in addition 
    to the individual cards.  
    If the --sprite_only parameter is given, only the sprite sheet will be produced.

requirements
------------

This program requires python and Inkscape.  It has been tested with python 3.8, and with Inkscape 1.1.  All testing has been on Xubuntu 20.

exportSVG.py
============

Extract individual SVG cards from sprite sheet.

usage
-----

    python exportSVG.py [-h] [-i INKSCAPE] source folder

arguments
---------

**positional arguments:**

    source                source sprite file path
    folder                parent directory for svg folder
    
    The folder argument is the name folder that will contain a "svgs" subfolder into 
    which the SVG files will be written.  It will be created if it doesn't exist.

**optional arguments:**

    -h, --help                          show this help message and exit  
    -i INKSCAPE, --inkscape INKSCAPE    path to inkscape  

rename.py
========

Rename the files to have names like TD.ext and AS.ext instead of diamondTen.ext and spadeAce.ext, for example.

usage
-----

    rename.py [-h] source target

arguments
--------

**positional arguments:**


        source      source directory
        target      target directory

**optional arguments:**

        -h, --help  show this help message and exit

requirements
------------------

This program requires python.

Other Formats
================

Inkscape allows extraction in many other formats.  If you need one of them, you can edit the source of exportPNG.py.  I've tried to make the format a program parameter, but so far, I've been unsuccessful, for reasons that aren't clear to me.

Inkscape does not provide a way to extract objects as GIF files; you have to make PNG files and convert them to GIF.  There are lots of free programs available to do this: Irfanview, Imagemagick, and the Gimp, to name a few.  

Acknowledgements
================

I am not an artist, and I did not make any of the graphics on the picture cards, the jokers, or the backs.  The pictures come from [a playing card set by Byron Knoll](https://commons.wikimedia.org/wiki/Category:Playing_cards_set_by_Byron_Knoll) and the backs and come from  www.openclipart.org.  The jokers also are by Brian Kroll, and are also available on [Wikimedia commons.](https://commons.wikimedia.org/wiki/File:Black_joker.svg)  I made small changes to some of these elements, but no consequential ones other than colors.  All the assets I retrieved from the Web were stated to be in the public domain.

License
=======

[Saul Spatz](https://github.com/saulspatz) created these scripts and graphics.  Everything in this repository has been placed by the author in the public domain.  You can copy, modify, distribute, fold, spindle, and mutilate the work, even for commercial purposes, all without asking permission.

 



