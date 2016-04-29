These are public-domain jumbo index playing card decks.  
Everything in this repository has been placed by the author in the public domain.
You can copy, modify, distribute, bend, spindle, and mutilate the work, even for 
commercial puposes, all without asking permission

It is difficult to find public domain playing cards, let alone ones with jumbo indexes.
Particularly for solitaire games, jumbo index decks are desirable.
These decks are in two flavors: vertical, which means that the indexes are in the 
traditional format, with the suit symbol below the rank symbol, and horizontal, 
with the suit symbol to the right of the rank symbol.  I have found that in solitaire 
games like spider, where the piles can get very long, that I prefer the horizontal
layout so that the vertcal offset between two cards in a pile can be smaller.

I am not an artist, and I did not make any of the graphics on the picture cards,
the jokers, or the backs.  The pictures come from
https://commons.wikimedia.org/wiki/Category:Playing_cards_set_by_Byron_Knoll
and the backs and jokers come from 
www.openclipart.org.  I may have made small changes to some of these elements.  
All the assets I retrieved from the Web were stated to be in the public domain.

The suits on the decks come in four colors.  No doubt, better choices are possible;
once again, I am not an artist.  The python script cardColors.py, detailed below,
can be used to modify the suit colors.  If you are an artist, and come up with a 
better scheme, I would urge you to make it freely available, though of course, 
you need not.

Two other python scripts are included: 

+    exportSVG.py for extracting individual cards as SVG files from the sprite sheets, 
+    exportPNG.py for extracting the individual cards as PNG files. 

In order for these scripts to be useful, Inkscape must be installed.  
Inkscape is free, open-source software, and may be downloaded from https://inkscape.org.

Details are given below.

###GRAPHICS FILES

The Decks fold contains two subfolders, Vertical and Horizontal, containing cards
with the pips arranged traditionally and side-by-side.  Each of the folders contains
a sprite sheet named "sprite.svg," and folders named "pngs", "svgs", and "gifs"
containing PNG, SVG, and GIF images of the individual cards.  The pngs and gifs
folder each contain a sprite file also.     

###EDITING

If you just want to change the colors of the suits, it's best to use cardColors.py.
If you want to make more basic changes, using Inkscape, you should note that
each card has an ID such as "heart6" or "diamondQueen".  When you ungroup
the card to work on its elements, this ID is lost.  You should restore it after 
re-grouping the elements, as exportSVG.py depends on their existence.  (I imagine
that Illustrator works similarly, but I've never used it.)

To edit the graphics, edit the sprite.svg files in the Horizontal and Vertical 
subfolders of the Decks folder.

###CHANGING COLORS

    python cardColors.py [-h] [-C CLUB] [-D DIAMOND] [-H HEART] [-S SPADE] [-B BACKGROUND] oldFile newFile  

positional arguments:  

     oldFile            source sprite file path  
     newFile            target sprite file path  

optional arguments: 

    -h, --help                             show this help message and exit  
    -C CLUB, --clubs CLUB                  New club color  
    -D DIAMOND, --diamonds DIAMOND         New diamond color  
    -H HEART, --hearts HEART               New heart color  
    -S SPADE, --spades SPADE               New spade color  
    -B BACKGROUND, --background BACKGROUND New card background color  
                        
The new colors should be given in six-character RGB format.  You can change as
many colors as you like.  

Example:

    python cardColors.py [path1]/sprite.svg [path2]/sprite.svg -C 00ff00 -B ffffff

will create a new sprite sheet with bright green clubs and white card backgrounds,
where path1 and path2 are appropriate paths to the input and output folders.

###EXPORTING PNG FILES

    python exportPNG.py [-h] [-s] [-o] [-w WIDTH] [-i INKSCAPE] source folder

Export SVG cards to PNG files

positional arguments:  

    source    source sprite file path  
    folder    parent directory for png folder 

optional arguments:

    -h, --help                       show this help message and exit  
    -s, --sprite                     create sprite sheet also   
    -o, --sprite_only                create sprite sheet only  
    -w WIDTH, --width WIDTH          image width (default 75 pixels)  
    -i INKSCAPE, --inkscape INKSCAPE path to inkscape  

The folder argument is the name folder that will contain a "pngs" subfolder into which
the PNG files will be written.  It will be created if it doesn't exist.  The --width
argument controls the width of the cards, both for individual files and for sprite 
sheets.  The --sprite parameter indicates that a sprite sheet should be produced in
addition to the individual cards.  If the --sprite_only parameter is given, only the 
sprite sheet will be produced. 

###EXPORTING SVG FILES

    python exportSVG.py [-h] [-i INKSCAPE] source folder

Extract individual SVG cards

positional arguments:

    source                source sprite file path
    folder                parent directory for svg folder

optional arguments:

    -h, --help                          show this help message and exit  
    -i INKSCAPE, --inkscape INKSCAPE    path to inkscape  
                        
The folder argument is the name folder that will contain a "svgs" subfolder into which
the SVG files will be written.  It will be created if it doesn't exist.  Due to known bug
number [#1306662] (https://bugs.launchpad.net/inkscape/+bug/1306662) the extracted
drawings are not correctly positioned on the page.  Until this is fixed, you can correct
it by opening the file in Inkscape, finding the drawing, (View/Zoom/Drawing from the
menu) changing the Y-coordinate to 0 on the toolbar at the top of the window, and saving
the file.

This process is, unfortunately, very slow, but it's still better than manually copying 
and pasting all the cards.

###EXTRACTING GIFS

Inkscape does not provide a way to extract objects as GIF files; you have to make PNG
files and convert them to GIF.  There are lots of free programs available to do this:
Irfanview, Imagemagick, and the Gimp, to name a few.  I have posted GIF files, but
not attempted to provide a conversion script, precisely because of the large number
of choices.      

 



