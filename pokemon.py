#!/usr/bin/env python3

import make_energy as me
import make_instance as mi
import solve_problem as sop
import visualize_solution as vs


if __name__ == '__main__':
    # set problem
    type_matrix, weak_matrix, resist_matrix, enemy, skill = mi.make_instance()
    # set costs & constraints
    model = me.make_energy(type_matrix=type_matrix, 
                            weak_matrix=weak_matrix, 
                            resist_matrix=resist_matrix,
                            enemy=enemy, 
                            skill=skill)
    # set hyper parameters
    n_enemies = len(enemy)
    n_skills = 4
    parameters = {'h_a': n_enemies+1, 
                    'h_b': 2*n_enemies+1, 
                    'h_c': 2/n_skills+0.1, 
                    'h_d': 2/n_skills*4}
    # solve with OpenJij
    solution, broken = sop.solve_problem(model=model, **parameters)
    # check broken 
    print(broken)
    # visualize result
    vs.visualize_solution(solution, enemy, skill)
