#!/usr/bin/env python3

import json
import sys
import random
import subprocess
import os

with open('countries.json') as f:
    countries = json.loads(f.read())

country = sys.argv[1]
objectives_file = f'./objectives/objectives_{country}.txt'
maps_folder = './maps/'
first_add_units = 4


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
            return players
        
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
    """
    Makes a list of all the provinces, shuffles it and then it assings them to the players by cycling through the players
    """
    province_list = [province for province in countries[country]]
    random.shuffle(province_list)
    while province_list != []:
        for player in players_list:
            if province_list == []:
                return players_list
            players_list[player]['provinces'].append(province_list[0])
            province_list.pop(0)
    return players_list


def update_countries_file(countries):
    with open('countries.json','w') as w:
        w.write(json.dumps(countries, indent=4, sort_keys=True))

def start_values(players,country):
    """
    Checks the file with all the countries and, for the selected country and players dictionary, it will assing the corresponding color and unit number as 1
    """
    with open('countries.json') as f:
        countries = json.loads(f.read())
    for player in players:
        for province in players[player]['provinces']:
            countries[country][province]['units'] = "1"
            countries[country][province]['owner'] = players[player]['color']

    update_countries_file(countries)
    return countries

def give_objetives(players):
    """
    Cycles through each player and assings them an objective
    """
    with open(objectives_file) as f:
        objectives_list = f.readlines()
    for player in players:
        objective = random.choice(objectives_list)
        players[player]['objective'] = objective
        objectives_list.remove(objective)
    return players

def add_units(player, players, countries, max_amount):
    amount = max_amount
    while amount > 0:
        province = input('Where do you want to add units?\n> ')

        if province in players[player]['provinces']:
            amount_toadd = int(float(input('How many units?\n> ')))
            if amount_toadd <= amount:
                amount -= amount_toadd
                current_amount = int(countries[country][province]['units'])
                current_amount += amount_toadd
                countries[country][province]['units'] = str(current_amount)
            else:
                print('You can\'t add that amount of units! Try again!')
        else:
            print('You don\'t own that province! Try again!')
    return countries

def first_add(players, countries):
    for player in players:
        print(players[player]['provinces'])
        print(f'Turno de {player}')
        units = first_add_units 
        countries = add_units(player, players, countries, units)
    for player in players:
        print(players[player]['provinces'])
        print(f'Turno de {player}')
        units = first_add_units
        countries = add_units(player, players, countries, units)
    update_countries_file(countries)
    return countries

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

players   = assing_countries(players,countries,country)
players   = give_objetives(players)
countries = start_values(players,country)
countries = first_add(players,countries)

os.system(f'./map_editing.py {country} {maps_folder}')

