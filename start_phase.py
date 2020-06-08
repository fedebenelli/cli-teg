#!/usr/bin/env python3

import json
import sys
import random
import subprocess
import os

with open('countries.json') as f:
    countries = json.loads(f.read())

country = sys.argv[1]

def get_players():
    """
    Function that asks for players's names and colors and returns a dictionary with the names as keys
    """
    
    # Asign the variables players and a list with the available colors to chose
    players = dict()
    available_colors = ['red','black','blue','yellow','green']

    # Loop until some internal condition is satisfied:
    #  - No more available colors
    #  - Exit condition because there are no more players

    while True:
        if available_colors == []:
            print('\n\n No more available colors!\n-------------')
        # Get the player's name
        player = input("Insert the player's name: ")
        # Print the available colors
        print(f'\nAvailable colors: {available_colors}')
        # Get the chosen color
        color = input("\nInsert the player's color: ")
        
        # If the color ain't in the avilable colors list send a message and go to the start of the loop
        # Else assing the player and color, also remove the color from the list
        if color not in available_colors:
            print()
            print('Color not available!')
            continue
        else:
            players[player] = {"color":color, "provinces":[]}
            available_colors.remove(color)

        condition = input('\n\nIf no more players are to be added write "end", else just send whatever: ')
        
        if condition.lower() == 'end':
            return players

def assing_countries(players_list, countries, country):
    province_list = [province for province in countries[country]]
    random.shuffle(province_list)
    while province_list != []:
        for player in players_list:
            if province_list == []:
                return players_list
            players_list[player]['provinces'].append(province_list[0])
            province_list.pop(0)
    return players_list

def start_values(players,country):
    with open('countries.json') as f:
        countries = json.loads(f.read())
    for player in players:
        for province in players[player]['provinces']:
            countries[country][province]['units'] = "1"
            countries[country][province]['owner'] = players[player]['color']
    with open('countries.json','w') as w:
        w.write(json.dumps(countries))

def give_objetives(players):
    with open(f'objectives_{country}.txt') as f:
        objectives_list = f.readlines()
    for player in players:
        objective = random.choice(objectives_list)
        players[player]['objective'] = objective
        objectives_list.remove(objective)
    return players

#players = get_players()
players = {
        "roter":{
            "color":"red",
            "provinces":[]
            },
        "aldi":{
            "color":"green",
            "provinces":[]
            },
        "manu":{
            "color":"yellow",
            "provinces":[]
            },
        }

players = assing_countries(players,countries,country)
players = give_objetives(players)
for player in players:
    print(player, ': ',players[player]['objective'])
start_values(players,country)
os.system(f'./map_editing.py {country}')
