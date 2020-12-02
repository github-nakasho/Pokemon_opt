#!/usr/bin/env python3

import openjij as oj


def solve_problem(model, h_a, h_b):
    # set dictionary of hyper parameters
    feed_dict = {'h_a': h_a, 'h_b': h_b, }
    # convert to qubo
    qubo, offset = model.to_qubo(feed_dict=feed_dict)
    # solve with OpenJij (SA)
    num_reads = 100
    sampler = oj.SASampler(num_reads=num_reads)
    response = sampler.sample_qubo(Q=qubo)
    # take mininum state
    dict_solution = response.first.sample
    # decode for analysis
    solution, broken, energy = model.decode_solution(dict_solution, vartype='BINARY', feed_dict=feed_dict)
    return solution, broken