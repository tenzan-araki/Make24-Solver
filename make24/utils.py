"""Utility functions to solve Make 24."""

import numpy as np
from sympy import *
import csv


# define six operations
def f_add(a, b):
    return a + b


def f_multiply(a, b):
    return a * b


def f_subtract_1(a, b):
    return a - b


def f_subtract_2(a, b):
    return b - a


def f_divide_1(a, b):
    if b != 0.0:
        return a / b
    else:
        return np.infty


def f_divide_2(a, b):
    if a != 0.0:
        return b / a
    else:
        return np.infty


def get_nonequiv_eqs_array():
    r"""This function identifies which equations are equivalent, so that they can be left out in the solver.
    This code takes about 16 to 18 seconds to run on my laptop, so if I do this within my solver then I will lose against my cousin.
    Fortunately, one can just run this function once in a lifetime and store the output.

    Returns:
        15 by 3888 array of True/False values. True if no equivalent equation has previously appeared.
        There are 15 cases considering same cards, and 3888 is the total number of possible combinations.
    """

    N = 4
    # number of cards
    N_f = 6
    # number of types of operations
    f_list = [f_add, f_multiply, f_subtract_1, f_subtract_2, f_divide_1, f_divide_2]
    # list of operations

    neq_eqs_TF_all = []
    for i in range(15):
        # i == 0 : no same cards
        # i == 1-6 : a pair of same cards
        # i == 7-9 : two pairs of same cards
        # i == 10-13 : three same cards
        # i == 14 : all same
        a1, a2, a3, a4 = symbols("a1 a2 a3 a4")
        # symbols corresponding to cards
        if i == 1:
            a1 = a2
        elif i == 2:
            a1 = a3
        elif i == 3:
            a1 = a4
        elif i == 4:
            a2 = a3
        elif i == 5:
            a2 = a4
        elif i == 6:
            a3 = a4
        elif i == 7:
            a1 = a2
            a3 = a4
        elif i == 8:
            a1 = a4
            a2 = a3
        elif i == 9:
            a1 = a3
            a2 = a4
        elif i == 10:
            a2 = a3
            a1 = a2
        elif i == 11:
            a2 = a4
            a1 = a2
        elif i == 12:
            a3 = a4
            a2 = a3
        elif i == 13:
            a3 = a4
            a1 = a3
        elif i == 14:
            a3 = a4
            a2 = a3
            a1 = a2

        neq_eqs_list = []
        # list of simplified equations used to avoid equivalent equations
        neq_eqs_TF = np.zeros(3888, dtype=int)

        eqs_idx = 0
        for F1idx in range(N_f):
            for F2idx in range(N_f):
                for F3idx in range(N_f):
                    # iteration over all combinatins of operations
                    f_seq = [f_list[F1idx], f_list[F2idx], f_list[F3idx]]
                    for Iidx in range(N - 1):
                        for Jidx in range(Iidx + 1, N):
                            # iteration over all combination of two cards in four cards
                            cards_A = [a1, a2, a3, a4]
                            card_Aa, card_Ab = cards_A[Iidx], cards_A[Jidx]
                            B1 = f_seq[0](card_Aa, card_Ab)
                            cards_A.remove(card_Aa)
                            cards_A.remove(card_Ab)
                            B2 = cards_A[0]
                            B3 = cards_A[1]
                            for Kidx in range(N - 2):
                                for Lidx in range(Kidx + 1, N - 1):
                                    # iteration over all combination of two cards in three cards
                                    cards_B = [B1, B2, B3]
                                    card_Ba, card_Bb = cards_B[Kidx], cards_B[Lidx]
                                    C1 = f_seq[1](card_Ba, card_Bb)
                                    cards_B.remove(card_Ba)
                                    cards_B.remove(card_Bb)
                                    C2 = cards_B[0]
                                    card_Ca, card_Cb = C1, C2
                                    D_eq = expand(f_seq[2](card_Ca, card_Cb))

                                    if not (D_eq in neq_eqs_list):
                                        # only runs if an equivalent equation has never appeared before
                                        neq_eqs_list.append(D_eq)
                                        neq_eqs_TF[eqs_idx] = 1

                                    eqs_idx += 1
        neq_eqs_TF_all.append(neq_eqs_TF)

        file_name = "neq_eqs_TF.csv"
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in neq_eqs_TF_all:
                writer.writerow(row)

    return neq_eqs_TF_all
