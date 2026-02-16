Readme
Tek-Phase Pink, Blue, Green, Yellow
Falkon web browser Theme 

Goals 
Make a theme using text instead of icons where possible. 
Make it look high-tech like custom gaming PCs using neon/led color highlights.
Try to keep it from looking too busy; keep it simple and somewhat flat looking.

Setting Up the theme (Linux) Install

--“control H” to un-hide hidden folders. Place themes in /home/yourcomputername/.config/falkon/themes/

--Install the included font “Play” by Jonas Hecksher. You can look up how to install fonts on your OS, but here’s a brief how to on Linux. In your main folder hit “control H” to un-hide hidden folders, make a folder called .fonts (if there isn’t one there yet). Then place the font folder in there so it looks like home/”yourcomputername”/.fonts/play/

--In Falkons “Preferences” go to “Browsing” then turn on “Use native scrollbars” this will change the scroll bars in the main browser window to match this theme.

--Optional: Uncheck “Menus have icons” in your “Qt5 Configuration Tool” under the “Interface” tab.-this will get rid of icons in the browsers menu. Alternatively, changing the Icon theme in the “Icon Theme” tab of the “Qt5 Configuration Tool” to something like “Papirus” looks nice if you like having the icons.

--There is a line that separates the navigation bar and the main browser window that I could not figure out how to set the color on.  If this is a light color by default it doesn’t really look that nice with this theme. So the fix at the moment is to change your main Qt theme to a dark theme – Go to your “Qt5 Configuration Tool” and in the “Appearance” tab change the style to “Fusion” and the Color scheme to “darker”.

--Bookmarks Folder Icon – looks best if its a Grey folder icon - In the “Icon Theme” tab of the “Qt5 Configuration Tool” change it to “Papirus”. Here is a link https://github.com/PapirusDevelopmentTeam/papirus-icon-theme

(The “Qt5 Configuration Tool” is located in my computers start menu under settings then “Qt5 settings”. In the repositories its called “qt5ct” -not sure if this helps :)
________________________________________________________________________
Things I still want to change but not sure how yet…
-when status bar is disabled – the link pop up tool tip when you hover over a link(the popup when the status bar is off)
-bookmarks sidebar horizontal separators (to separate bookmarks)
-boarder line that shows at the bottom of navigation bar and above main window, 
noticeable on light qt themes and square in corner when there is a vertical and horizontal scroll bar.
-bookmarks sidebar, change or disable the loading/active highlight effects, also happens in download menu.
this can cause the dotted line bug if the highlight is a dotted line effect (certain Qt themes) – see bugs.
-Folder icon in bookmarks- would like to make my own folder icon to overriding the master qt icon theme (have to use qt theme for now)
-adblock icon change to custom color version

Bugs
Under certain Qt themes scroll bars may have a dotted line screw up.
(Status Bar)  adblock icon sometimes gets replaced with X - same with downloads when activated

Notes: When switching themes thing may be screwed up until you restart Falkon.

Theme by Aaron Swanson  "Ektophase" 
ektophase.com


Other credit
I looked at “Cyanotype” theme for QupZilla by by cranes bill (Okvardz Votim) and the default themes by David Rosca for some code.
I used some of the icons from the default Linux theme by David Rosca
Font “Play” by Jonas Hecksher (Link:  https://fonts.google.com/specimen/Play )

Main Colors
Yellow 			#F5CE0A
Dark Yellow		#806B05

Pink 			#EE82EE
Dark Pink		#855689

Blue			#0AB6F5
Dark Blue		#05688C

Green			#9DF50A
Dark Green		#639906

Changelog
Apr 20 2018 - 1.0 first release version was made for Falkon 3.0.0 so there could be some bugs when newer versions get released.
May 23 2018 - Fixed add tab button. the svg was messed up (appeared normal to me in Antergos) and I changed the code for this a tad (line 378, 380, at this time)
