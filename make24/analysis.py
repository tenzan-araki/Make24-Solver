"""Additional analysis of Make 24."""

import matplotlib.pyplot as plt
from .solver import make24_solver

def make24_analysis_1():
    r"""Answers the question: given any 4 cards, what is the probability that there is no solution?
    """
    M = 13; # numbers in a deck of cards
    count = 0; # number of solutions initialized to 0
    for A1 in range(1,M+1):
        for A2 in range(1,A1+1):
            for A3 in range(1,A2+1):
                for A4 in range(1,A3+1):
                    count += make24_solver(A1, A2, A3, A4, mode='one-fixed', print_ok=False);
    prob = round(1 - count/1820, 3);
    prob_pc = prob * 100;
    print('Pr(No Solution) =', prob_pc, '%');

def make24_analysis_2():
    r"""Obtain number of solutions for each combination of four cards.
    
    Returns:
        A list of the number of counts for each combination of four cards.
    """
    M = 13; # numbers in a deck of cards
    count = []; # number of solutions initialized to 0
    for A1 in range(1,M+1):
        for A2 in range(1,A1+1):
            for A3 in range(1,A2+1):
                for A4 in range(1,A3+1):
                    count.append(make24_solver(A1, A2, A3, A4, mode='all', print_ok=False));

    n, bins, patches = plt.hist(x=count, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Number of Solutions')
    plt.ylabel('Occurrence')

    return count;
