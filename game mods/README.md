![Untitled](https://github.com/mindsetpro/DragonBallLegends/assets/138173273/76b48f80-59fa-4391-b547-fd1974ba27b8)

# Game modding with files

### main parts of the 89bb file

| File Parts                        | Description                                                                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------------|
| `characterShards_`               | Character stars. Edit the count under the unit ID to 9999 for 14 stars. `"count": {zpowernum}` is the Z Power.  |
| `characterPlentyShards_`         | Character Zenkai Power. Edit the count to a maximum of 7000 for Zenkai 7.                                   |
| `equipItems_`                     | Equip data. You can edit the rank and other attributes.                                                     |
| `unlockItems_`                    | Items you have unlocked.                                                                                   |
| `invisibleUnlockItems_`          | Unobtained items.                                                                                          |
| `otherItems_`                     | Other items.                                                                                                |
| `unit`                            | Characters' information. Edit the level, artsboost, soulboost, etc. (Level can be edited to anything).    |
| `party`                           | Your party information. You can change the characters as long as you have them.                            |
| `tutorial`                        | Tutorial progress. Replace all the 0's with 1's if any, and the tutorial should be complete.             |
| `backGroundId`                    | The game's background ID (this is changeable i don't know the IDs yet).                                                                                  |
