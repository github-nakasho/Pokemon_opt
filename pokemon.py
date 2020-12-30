#!/usr/bin/env python3

import make_energy as me
import make_instance as mi
import solve_problem as sop
import visualize_solution as vs


if __name__ == '__main__':
    # set problem
    type_matrix, weak_matrix, enemy, skill = mi.make_instance()
    # set costs & constraints
    model = me.make_energy(type_matrix=type_matrix, weak_matrix=weak_matrix, enemy=enemy, skill=skill)
    # set hyper parameters
    parameters = {'h_a': 2*len(enemy)+1, 'h_b': 4*len(enemy)+1, 'h_c': 4*len(enemy)+1}
    # solve with OpenJij
    solution, broken = sop.solve_problem(model=model, **parameters)
    # check broken 
    print(broken)
    # visualize result
    vs.visualize_solution(solution, enemy, skill)
