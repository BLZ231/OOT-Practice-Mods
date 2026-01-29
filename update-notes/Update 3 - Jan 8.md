#OOT Update Jan-8-26

This change was intended to get rid of the long chest opening animation for the dungeon map, compass, and boss key, since I feel that the long chest opening animation is fine for important items, but for things that are more common it's just kind of a pace killer.

After carefully scrutinizing the files for a while and trying to figure out precisely which page controlled the chest animations, I eventually found a page that seemed to be what I was looking for, as it had a table of items where at the end all of them either had CHEST_ANIM_SHORT for items that have a short chest opening animation and CHEST_ANIM_LONG for items that had a long one, though confusingly a lot of items that are not found in chests have the long chest animation.

For the compass, dungeon map, and boss key I changed the long animation to the short animation. I then loaded a save file in the Deku Tree and checked to see if it worked, and it did. I then loaded a save file in Dodongo's cavern to check to make sure it wasn't a fluke, and it wasn't, it worked there too. I don't have a save file to any of the adult dungeons at the moment so I can't yet verify if the boss key change worked, but hopefully it did.

After the long stressful crap I had to deal with in the previous changes I'm both relieved but also suspicious that this time the very first thing I tried worked like a charm. Though I suppose this was a comparatively simpler change.

I also tested a trick I saw online which involved using an Armos statue to reach a gold skulltula that you aren't supposed to be able to reach yet, and it worked. It was a little tedious, but honestly less annoying than the "official" way you're supposed to get it, so I might look into making it so that Link can climb the statues the same way he can climb the blocks, and put two active Armos just below the gold skulltula as a hint for what to do to get it.
