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
    my_pokemon = solution['x']
    my_pokemon_str = 'じぶんのポケモン:'
    my_pokemon_str = type_display(my_pokemon, my_pokemon_str)
    enemy_pokemon = z
    enemy_pokemon = {i: j for i, j in enumerate(z)}
    enemy_pokemon_str = 'あいてのポケモン:'
    enemy_pokemon_str = type_display(enemy_pokemon, enemy_pokemon_str)
    my_skills = solution['y']
    my_skill_str = [0] * 4
    for i, j in my_skills.items():
        my_skill_str[i] = 'わざ' + str(i) + ':'
        my_skill_str[i] = type_display(j, my_skill_str[i])
    enemy_skills = w
    enemy_skill_str = [0] * 4
    for i, j in enumerate(enemy_skills):
        enemy_skill_str[i] = 'わざ' + str(i) + ':'
        j = {k: l for k, l in enumerate(j)}
        enemy_skill_str[i] = type_display(j, enemy_skill_str[i])
    print('**********')
    print(my_pokemon_str)
    for i in range(4):
        print(my_skill_str[i])
    print('**********')
    print(enemy_pokemon_str)
    for i in range(4):
        print(enemy_skill_str[i])
    