wrongKeypressPrevention is an experimental low-level Python study for 'Prevention Wrong KeyPresses/KeyStrokes' in limited keyboard layouts. 

Example:
Bir tuşa basınız: g\
(1, 4) #Current Location on EnglishQ Keyboard\
9 #Number of possible keys which are near to key pressed\
[(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)] #Position of possible keys\
['r', 't', 'y', 'f', 'g', 'h', 'v', 'b', 'n'] #possible keys

Note that the special keys such as CTRL, ALT, and SHIFT are not included to the layout\
and also there are only two layouts can be used are TurkishQ and EnglishQ, I plan to use every possible layout in this study.

Enjoy it.