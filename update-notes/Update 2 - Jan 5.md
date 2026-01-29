#OOT Update Jan-5-26

This change was intended to change the rupee amounts for the wallets, as a max of 99 is a bit too low. So I updated the default from 99 to 200, the first upgrade from 200 to 500, and the second upgrade from 500 to 1000.

Now the actual change was extremely simple, I just had to change a few values related to the wallet in the z_inventory.c file. However what proved to be more tricky was updating the in game user interface to reflect this change, because initially when the player had 99 rupees and picked up another one instead of going to 100 rupees like it should it went to 01 rupees. It still kept track of all the rupees the player had, as I was able to buy the 40 rupee deku shield without issue despite the counter at the time saying 01, but nonetheless I wanted it to accurately display the real number of rupees.

After fiddling around and testing various changes in the z_parameter.c, mostly related to the Rupee Counter, I was eventually able to get the game to display 000 by default instead of 00. However when I picked up a rupee while the numbers lit up like they're supposed to they remained stuck at 000.

After some more tweaks I wondered if perhaps I had changed too much, and so pulled up an older commit and after backing up a copy of the altered code I reverted the code in z_parameter.c to what it had originally been to try to figure out which changes affected which part. I started by simply adjusting the values of rupeeDigitsFirst and rupeeDigitsCount and then recompiled and tested the ROM to see if that would suffice. As it turned out my instincts were correct, and this one change to the code produced the change I wanted, with 000 being the default, accurately counting Rupees as Link picks them up, and maxing out at 200.

Admittedly I might have to return to this at some point because I do not yet know if the biggest wallet upgrade, 1000, works properly, but for now I am happy with the change I made. It still involved a bit of stress and frustration, but significantly less than the earlier textbox update.
