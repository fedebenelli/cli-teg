# cli-TEG Argentina

This is a partialy cli-based game that mimics the playstyle of TEG/Risk.  

## Functionality

### Data storage

- The current status of the game is stored in the file `countries.json`, where each entry object is a country object with the attributes:

```json
"province"{
	"x":"<x position in the map>",
	"y":"<y position in the map>",
	"owner":"<color of the owner>",
	"units":"<number of units>"
}
```

- The players are stored as a dictionary like:

```json
"playername":{
	"color":"<player's color'>",
	"provinces":["<list of provinces>"],
	"objective":"<player's objective>"
}
```

- All the maps must be in `.png` format and stored in the "maps" folder, with the naming `countryname.png`

- All the objectives are stored as individual text files in the "objectives" folder with the naming `objectives_<countryname>.txt`, where each line represents an objective

## Start phase

- Recieve the amount of players as a list of names.
- Ask to each player the desired color (from a list of colors).
- Shuffle the provinces and assing them to each player.
- Draw the initial map.
- Give each player their objective.
- Adding round:
	- Each player add a total of 3 armies on their units.
	- Another round to add another 3 armies.

## Hostility phase

- Each player can attack it's neighbour province.
- When the attacks are over, the player can move their units between neighbour provinces.
- If the player conquered a province he will get a country card.

## Add phase

- Each player will add an amount of armies equal to 60% (rounded up) of the amount of conquered provinces.

----

After the add phase, the hostility phase begins again.
