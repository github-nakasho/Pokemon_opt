#!/usr/bin/env python3

import numpy as np
from pyqubo import Array, Constraint, Placeholder

def make_energy(type_matrix, enemy, skill):
    # set the number of types
    num_types = len(type_matrix)
    # set the number of skills
    num_skills = 4
    # set placeholder
    lambda_a = Placeholder('h_a')
    lambda_b = Placeholder('h_b')
    # set binary variables
    x = Array.create('x', shape=(num_types), vartype='BINARY')
    y = Array.create('y', shape=(num_skills, num_types), vartype='BINARY')
    # convert to numpy array
    x = np.array(x)
    y = np.array(y)
    z = np.array(enemy)
    w = np.array(skill)
    # set cost function
    atk_damage = sum([np.dot(0.5*x+y[i], np.dot(type_matrix, z)) for i in range(num_skills)])
    def_damage = sum([np.dot(0.5*z+w[i], np.dot(type_matrix, x)) for i in range(num_skills)])
    # atk_damage = sum([np.dot(y[i], np.dot(type_matrix, z)) for i in range(num_skills)])
    # def_damage = sum([np.dot(w[i], np.dot(type_matrix, x)) for i in range(num_skills)])
    # set one-hot encoding constraint
    h_a = Constraint((sum(x)-1)*(sum(x)-2), label='h_a')
    y_const = [0] * num_skills
    for i in range(num_skills):
        y_const[i] = (sum([y[i][j] for j in range(num_types)])-1) ** 2
    h_b = Constraint(sum(y_const), label='h_b')
    # compute total energy
    energy = - (atk_damage-def_damage) + lambda_a * h_a + lambda_b * h_b
    # compile
    model = energy.compile()
    return model
