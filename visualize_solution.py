#!/usr/bin/env python3

def type_display(pokemon, pokemon_str):
    types = ['ノーマル', 'ほのお', 'みず', 'でんき', 'くさ', 'こおり', 
                'かくとう', 'どく', 'じめん', 'ひこう', 'エスパー', 'むし', 
                'いわ', 'ゴースト', 'ドラゴン', 'あく', 'はがね', 'フェアリー']
    for i, j in enumerate(pokemon):
        if j == 1:
            pokemon_str += ' ' + types[i]
    return pokemon_str

def visualize_solution(solution, z, w):
    print('##########')
    print('じぶんのポケモン')
    for i in range(len(z)):
        print('*****')
        my_pokemon = []
        for j in range(18):
            my_pokemon.append(solution.array('x', (i, j)))
        my_pokemon_type = ''
        my_pokemon_type = type_display(my_pokemon, my_pokemon_type)
        print(my_pokemon_type)
        my_skills = []
        for j in range(4):
            my_skills.append([])
            for k in range(18):
                my_skills[j].append(solution.array('y', (i, j, k)))
        my_skill_str = ''
        for j, k in enumerate(my_skills):
            my_skill_str = 'わざ' + str(j) + ':'
            my_skill_str = type_display(k, my_skill_str)
            print(my_skill_str)
    print('##########')
    print('あいてのポケモン')
    for i in range(len(z)):
        print('*****')
        enemy_pokemon_type = ''
        enemy_pokemon_type = type_display(z[i], enemy_pokemon_type)
        print(enemy_pokemon_type)
        enemy_skills = w[i]
        for j, k in enumerate(enemy_skills):
            enemy_skill_str = 'わざ' + str(j) + ':'
            enemy_skill_str = type_display(k, enemy_skill_str)
            print(enemy_skill_str)
    