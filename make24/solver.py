"""Solver for Make 24."""

import numpy as np
import random
import csv
from .utils import f_add, f_multiply, f_subtract_1, f_subtract_2, f_divide_1, f_divide_2

# obtain array computed from get_nonequiv_eqs_array in utils.py when importing from make24
neq_eqs_TF_all = []
file_name = 'neq_eqs_TF.csv'
with open(file_name, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row_list = []
        for col in row:
            row_list.append(int(col))
        neq_eqs_TF_all.append(row_list)

def make24_solver(A1, A2, A3, A4, mode='one-rand', print_ok=True):
    r"""finds a sequence of operations (if there exists) that makes 24 out of four numbers A1, A2, A3, and A4
    The solver checks all non-equivalent possibilities to see which ones produce 24
    
    Args:
        A1: number on the first card.
        A1: number on the second card.
        A1: number on the third card.
        A1: number on the fourth card.
        mode: the mode of the solver. The default is set to produce one random solution if there exist at least one.
        print_ok: boolean flag to choose whether or not to print solutions.

    Mode options:
        mode == 'one-rand' : finds only one random solution even if multiple solutions exist (same speed as 'all')
        mode == 'one-fixed' : finds only one fixed solution even if multiple solutions exist (fastest)
        mode == 'all' : finds all solutions
    
    Returns:
        The number of solutions found (returns 1 if mode == 'one_fixed' because only one is solved).
    """
    num_sol = 0; # number of solutions initialized to 0
    sol_list = []; # list of solutions for 'all' mode

    N = 4; # number of cards
    N_f = 6; # number of types of operations
    f_list = [f_add, f_multiply, f_subtract_1, f_subtract_2, f_divide_1, f_divide_2]; # list of operations
    
    # avoid calculating equivalent equations
    if (A1 == A2):
        if (A2 == A3):
            if (A3 == A4):
                neq_eqs_TF = neq_eqs_TF_all[14];
            else:
                neq_eqs_TF = neq_eqs_TF_all[10];
        elif (A2 == A4):
            neq_eqs_TF = neq_eqs_TF_all[11];
        elif (A3 == A4):
            neq_eqs_TF = neq_eqs_TF_all[7];
        else:
            neq_eqs_TF = neq_eqs_TF_all[1];
    elif (A1 == A3):
        if (A3 == A4):
            neq_eqs_TF = neq_eqs_TF_all[13];
        elif (A2 == A4):
            neq_eqs_TF = neq_eqs_TF_all[9];
        else:
            neq_eqs_TF = neq_eqs_TF_all[2];
    elif (A1 == A4):
        if (A2 == A3):
            neq_eqs_TF = neq_eqs_TF_all[8];
        else:
            neq_eqs_TF = neq_eqs_TF_all[3];
    elif (A2 == A3):
        if (A3 == A4):
            neq_eqs_TF = neq_eqs_TF_all[12];
        else:
            neq_eqs_TF = neq_eqs_TF_all[4];
    elif (A2 == A4):
        neq_eqs_TF = neq_eqs_TF_all[5];
    elif (A3 == A4):
        neq_eqs_TF = neq_eqs_TF_all[6];
    else:
        neq_eqs_TF = neq_eqs_TF_all[0];
        
    eqs_idx = 0
    for F1idx in range(N_f):
        for F2idx in range(N_f):
            for F3idx in range(N_f):
                # iteration over all combinatins of operations
                f_seq = [f_list[F1idx], f_list[F2idx], f_list[F3idx]];
                for Iidx in range(N-1):
                    for Jidx in range(Iidx+1,N):
                        # iteration over all combination of two cards in four cards
                        cards_A = [A1, A2, A3, A4];
                        card_Aa, card_Ab = cards_A[Iidx], cards_A[Jidx];
                        B1 = f_seq[0](card_Aa, card_Ab);
                        cards_A.remove(card_Aa);
                        cards_A.remove(card_Ab);
                        B2 = cards_A[0];
                        B3 = cards_A[1];
                        for Kidx in range(N-2):
                            for Lidx in range(Kidx+1,N-1):
                                # iteration over all combination of two cards in three cards
                                if neq_eqs_TF[eqs_idx] == 1:
                                    # leaving out equivalent equations
                                    cards_B = [B1, B2, B3];
                                    card_Ba, card_Bb = cards_B[Kidx], cards_B[Lidx];
                                    C1 = f_seq[1](card_Ba, card_Bb);
                                    cards_B.remove(card_Ba);
                                    cards_B.remove(card_Bb);
                                    C2 = cards_B[0];
                                    card_Ca, card_Cb = C1, C2;
                                    D = f_seq[2](card_Ca, card_Cb);

                                    if (D == 24.0):
                                        # if a solution was found
                                        num_sol += 1;

                                        # writing out this solution as an understandable equation
                                        if (f_seq[0].__name__ == 'f_add'):
                                            text_1 = '( '+ str(card_Aa) + ' + ' + str(card_Ab) + ' )';
                                        elif (f_seq[0].__name__ == 'f_multiply'):
                                            text_1 = '( '+ str(card_Aa) + ' × ' + str(card_Ab) + ' )';
                                        elif (f_seq[0].__name__ == 'f_subtract_1'):
                                            text_1 = '( '+ str(card_Aa) + ' - ' + str(card_Ab) + ' )';
                                        elif (f_seq[0].__name__ == 'f_subtract_2'):
                                            text_1 = '( '+ str(card_Ab) + ' - ' + str(card_Aa) + ' )';
                                        elif (f_seq[0].__name__ == 'f_divide_1'):
                                            text_1 = '( '+ str(card_Aa) + ' ÷ ' + str(card_Ab) + ' )';
                                        elif (f_seq[0].__name__ == 'f_divide_2'):
                                            text_1 = '( '+ str(card_Ab) + ' ÷ ' + str(card_Aa) + ' )';

                                        if Kidx == 0:
                                            if (f_seq[1].__name__ == 'f_add'):
                                                text_2 = '( '+ text_1 + ' + ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_multiply'):
                                                text_2 = '( '+ text_1 + ' × ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_subtract_1'):
                                                text_2 = '( '+ text_1 + ' - ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_subtract_2'):
                                                text_2 = '( '+ str(card_Bb) + ' - ' + text_1 + ' )';
                                            elif (f_seq[1].__name__ == 'f_divide_1'):
                                                text_2 = '( '+ text_1 + ' ÷ ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_divide_2'):
                                                text_2 = '( '+ str(card_Bb) + ' ÷ ' + text_1 + ' )';

                                            if (f_seq[2].__name__ == 'f_add'):
                                                text_3 = text_2 + ' + ' + str(card_Cb);
                                            elif (f_seq[2].__name__ == 'f_multiply'):
                                                text_3 = text_2 + ' × ' + str(card_Cb);
                                            elif (f_seq[2].__name__ == 'f_subtract_1'):
                                                text_3 = text_2 + ' - ' + str(card_Cb);
                                            elif (f_seq[2].__name__ == 'f_subtract_2'):
                                                text_3 = str(card_Cb) + ' - ' + text_2;
                                            elif (f_seq[2].__name__ == 'f_divide_1'):
                                                text_3 = text_2 + ' ÷ ' + str(card_Cb);
                                            elif (f_seq[2].__name__ == 'f_divide_2'):
                                                text_3 = str(card_Cb) + ' ÷ ' + text_2;

                                        else:
                                            if (f_seq[1].__name__ == 'f_add'):
                                                text_2 = '( '+ str(card_Ba) + ' + ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_multiply'):
                                                text_2 = '( '+ str(card_Ba) + ' × ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_subtract_1'):
                                                text_2 = '( '+ str(card_Ba) + ' - ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_subtract_2'):
                                                text_2 = '( '+ str(card_Bb) + ' - ' + str(card_Ba) + ' )';
                                            elif (f_seq[1].__name__ == 'f_divide_1'):
                                                text_2 = '( '+ str(card_Ba) + ' ÷ ' + str(card_Bb) + ' )';
                                            elif (f_seq[1].__name__ == 'f_divide_2'):
                                                text_2 = '( '+ str(card_Bb) + ' ÷ ' + str(card_Ba) + ' )';

                                            if (f_seq[2].__name__ == 'f_add'):
                                                text_3 = text_2 + ' + ' + text_1;
                                            elif (f_seq[2].__name__ == 'f_multiply'):
                                                text_3 = text_2 + ' × ' + text_1;
                                            elif (f_seq[2].__name__ == 'f_subtract_1'):
                                                text_3 = text_2 + ' - ' + text_1;
                                            elif (f_seq[2].__name__ == 'f_subtract_2'):
                                                text_3 = text_1 + ' - ' + text_2;
                                            elif (f_seq[2].__name__ == 'f_divide_1'):
                                                text_3 = text_2 + ' ÷ ' + text_1;
                                            elif (f_seq[2].__name__ == 'f_divide_2'):
                                                text_3 = text_1 + ' ÷ ' + text_2;

                                        if (mode == 'one-fixed'):
                                            # print solution and return number of solutions found (always 1 for 'one-fixed' mode)
                                            if print_ok:
                                                print(text_3 + ' = 24');
                                            return 1;
                                        elif ((mode == 'one-rand') or (mode == 'all')):
                                            # append solution into list of independent solutions
                                            sol_list.append(text_3 + ' = 24');
                                        else:
                                            if print_ok:
                                                print('Error : Undefined mode.');
                                            return None;
                                eqs_idx += 1
    if print_ok:
        if num_sol == 0:
            # if none of the 3888 possibilities made 24
            print('Cannot make 24.');
        else:
            if mode == 'one-rand':
                sol_idx = random.randint(0, num_sol - 1);
                print(sol_list[sol_idx]);
            elif mode == 'all':
                if num_sol == 1:
                    # if only one equation made 24
                    print('Found ' + str(num_sol) + ' independent solution.');
                    for solidx, sols in enumerate(sol_list):
                        num_space = 6 - len(str(solidx+1));
                        spaces = ' '*num_space;
                        print('[' + str(solidx+1) + ']' + spaces + sols);
                else:
                    # if two or more equations made 24
                    print('Found ' + str(num_sol) + ' independent solutions.');
                    for solidx, sols in enumerate(sol_list):
                        num_space = 6 - len(str(solidx+1));
                        spaces = ' '*num_space;
                        print('[' + str(solidx+1) + ']' + spaces + sols);
                
    # return number of solutions found
    return num_sol;
