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
www.openclipart.org.  
I may have made small changes to some of these elements.  All the assets I 
retrieved from the Web are stated to be in the public domain.

The suits on the decks come in four colors.  No doubt, better choices are possible;
once again, I am not an artist.  The python script changeColor.py, detailed below,
can be used to modify the suit colors.  If you are an artist, and come up with a 
better scheme, I would urge you to make it freely available, though of course, 
you need not.

There is another python script, exportSVG.py, for converting the cards from SVG
format to PNG.  Details are given below.

EDITING:

If you just want to change the colors of the suits, it's best to use changeColor.py.
If you want to make more basic changes, using Inkscape, you should note that
each card has an ID such as "heart6" or "diamondQueen".  When you ungroup
the card to work on its elements, this ID is lost.  You should restore it after 
re-grouping the elements, as exportSVG.py depends on their existence.  (I imagine
that Photoshop works similarly, but I've never used it.)

To edit the graphics, edit the sprite.svg files.
