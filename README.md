# cli-TEG Argentina

This is a partialy cli-based game that mimics the playstyle of TEG/Risk.  

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
