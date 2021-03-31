#!/usr/bin/env python3

import numpy as np
from pyqubo import Array, Constraint, Placeholder

def make_energy(type_matrix, weak_matrix, resist_matrix, enemy, skill):
    # set the number of enemies
    num_enemies = len(enemy)
    # set the number of my pokemon
    num_my_team = num_enemies
    # set the number of types
    num_types = len(type_matrix)
    # set the number of skills
    num_skills = 4
    # set placeholder
    lambda_a = Placeholder('h_a')
    lambda_b = Placeholder('h_b')
    lambda_c = Placeholder('h_c')
    lambda_d = Placeholder('h_d')
    # set binary variables
    x = Array.create('x', shape=(num_my_team, num_types), vartype='BINARY')
    y = Array.create('y', shape=(num_my_team, num_skills, num_types), vartype='BINARY')
    s = Array.create('s', shape=(num_enemies, num_skills, 2), vartype='BINARY')
    t = Array.create('t', shape=(num_enemies, num_skills, 2*num_my_team-1), vartype='BINARY')
    # convert to numpy array
    x = np.array(x)
    y = np.array(y)
    s = np.array(s)
    t = np.array(t)
    z = np.array(enemy)
    w = np.array(skill)
    # set one-hot encoding constraint for pokemon type
    h_a = 0
    for i in range(num_my_team):
        tmp = sum([x[i][j] for j in range(num_types)])
        h_a += (tmp-1) * (tmp-2)
    h_a = Constraint(h_a, label='h_a')
    # set one-hot encoding constraint for skill type
    h_b = 0
    for i in range(num_my_team):
        for k in range(num_skills):
            tmp = sum([y[i][k][l] for l in range(num_types)])
            h_b += (tmp-1) ** 2
    h_b = Constraint(h_b, label='h_b')
    # set a constraint that weak pokemon is less than 2
    h_c = 0
    h_c2 = 0
    tmp_sum = 0
    for i in range(num_enemies):
        for j in range(num_skills):
            for l in range(num_my_team):
                tmp = np.dot(w[i][j], np.dot(weak_matrix, x[l]))
                h_c2 += tmp * (tmp-1)
                tmp_sum += tmp
            h_c += (2-sum(s[i][j])-tmp_sum) ** 2
    h_c = Constraint(h_c+h_c2, label='h_c')
    # set a constraint that resist pokemon is greather than 1
    h_d = 0
    for i in range(num_enemies):
        for j in range(num_skills):
            tmp = sum([np.dot(w[i][j], np.dot(resist_matrix, x[l])) for l in range(num_my_team)])
            h_d += (2*num_my_team-sum(t[i][j])-tmp) ** 2
    h_d = Constraint(h_d, label='h_d')
    # set cost function
    atk_damage = 0
    for i in range(num_my_team):
        for j in range(num_skills):
            for l in range(num_enemies):
                tmp = np.dot(y[i][j], np.dot(type_matrix, z[l]))
                atk_damage += tmp
    def_damage = 0
    for i in range(num_enemies):
        for j in range(num_skills):
            for l in range(num_my_team):
                tmp = np.dot(w[i][j], np.dot(type_matrix, x[l]))
                def_damage += tmp
    obj = - atk_damage + def_damage
    # compute total energy
    energy = obj + lambda_a * h_a + lambda_b * h_b + lambda_c * h_c + lambda_d * h_d
    # compile
    model = energy.compile()
    return model
