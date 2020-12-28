#!/usr/bin/env python3

def type_display(pokemon, pokemon_str):
    for i, j in pokemon.items():
        if j == 1:
            if i == 0:
                pokemon_str += ' ノーマル'
            elif i == 1:
                pokemon_str += ' ほのお'
            elif i == 2:
                pokemon_str += ' みず'
            elif i == 3:
                pokemon_str += ' でんき'
            elif i == 4: 
                pokemon_str += ' くさ'
            elif i == 5:
                pokemon_str += ' こおり'
            elif i == 6: 
                pokemon_str += ' かくとう'
            elif i == 7: 
                pokemon_str += ' どく'
            elif i == 8: 
                pokemon_str += ' じめん'
            elif i == 9: 
                pokemon_str += ' ひこう'
            elif i == 10: 
                pokemon_str += ' エスパー'
            elif i == 11: 
                pokemon_str += ' むし'
            elif i == 12: 
                pokemon_str += ' いわ'
            elif i == 13: 
                pokemon_str += ' ゴースト'
            elif i == 14: 
                pokemon_str += ' ドラゴン'
            elif i == 15: 
                pokemon_str += ' あく'
            elif i == 16:
                pokemon_str += ' はがね'
            elif i == 17:
                pokemon_str += ' フェアリー'
    return pokemon_str

def visualize_solution(solution, z, w):
    print('##########')
    print('じぶんのポケモン')
    for i in range(len(z)):
        print('*****')
        my_pokemon = {}
        for j in range(18):
            my_pokemon[j] = solution.array('x', (i, j))
        my_pokemon_type = ''
        my_pokemon_type = type_display(my_pokemon, my_pokemon_type)
        print(my_pokemon_type)
        my_skills = {}
        for j in range(4):
            my_skills[j] = {}
            for k in range(18):
                my_skills[j][k] = solution.array('y', (i, j, k))
        my_skill_str = ''
        for j, k in my_skills.items():
            my_skill_str = 'わざ' + str(j) + ':'
            my_skill_str = type_display(k, my_skill_str)
            print(my_skill_str)
    print('##########')
    print('あいてのポケモン')
    for i in range(len(z)):
        print('*****')
        enemy_pokemon = {j: k for j, k in enumerate(z[i])}
        enemy_pokemon_type = ''
        enemy_pokemon_type = type_display(enemy_pokemon, enemy_pokemon_type)
        print(enemy_pokemon_type)
        enemy_skills = w[i]
        for j, k in enumerate(enemy_skills):
            enemy_skill_str = 'わざ' + str(j) + ':'
            k = {l: m for l, m in enumerate(k)}
            enemy_skill_str = type_display(k, enemy_skill_str)
            print(enemy_skill_str)
    