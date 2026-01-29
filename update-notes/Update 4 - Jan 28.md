#OOT Update Jan-28-26

So after changing the animation for the chests I wanted to make a couple of relatively simple changes to the first dungeon. However when I tried to do this I ran into a brick wall, because while the files for the dungeons and all the other maps in the game existed they were not in a format that allowed anyone to see or change any of the contents of the maps.

After running through a lot of various internal and external tools to try to fix this and having all of them fail and wanting to bang my head against a wall for several weeks, I finally figured out the solution.

The version of the decompilation project I had originally cloned was designed primarily around preservation, which meant that it was accommodating for some changes but a complete dead end for others. After cloning a different decompilation project that was designed to be more mod friendly the maps were finally in a format that made changes possible, and after some more fiddling I was able to decode the in game text as well.

Of course having it be smooth sailing from there would be too easy, so when I tried to run the compiled ROM that the new project had made it kept crashing immediately. After painstaking trial and error I was eventually able to figure out that I needed to go into the config_graphics.h file located in the include folder and change one line from this [#define ENABLE_F3DEX3 true] to this [#define ENABLE_F3DEX3 false] and as soon as I did the compiled ROM worked fine.

After that I carefully changed the code in the new project to match the changes I had made in the old project, compiled the ROM again, and tested it again just to make sure that the changes were still in place and worked properly, and thankfully they did.

After verifying that the new project was working correctly I then replaced most of the files from the old project with files from the new one, since that's the one I'll be working with from now on. I'm hoping the worst is over now but only time will tell.
