#!/usr/bin/env python3

import make_energy as me
import make_instance as mi
import solve_problem as sop
import visualize_solution as vs


if __name__ == '__main__':
    # set problem
    type_matrix, enemy, skill = mi.make_instance()
    # set costs & constraints
    model = me.make_energy(type_matrix=type_matrix, enemy=enemy, skill=skill)
    # set hyper parameters
    parameters = {'h_a': 2.0, 'h_b': 5.0}
    # solve with OpenJij
    solution, broken = sop.solve_problem(model=model, **parameters)
    # check broken 
    print(broken)
    # visualize result
    vs.visualize_solution(solution, enemy, skill)
