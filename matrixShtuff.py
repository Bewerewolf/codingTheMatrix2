import numpy as np
import copy

def main():
    A = [[2, 2, 3], [4, 5, 6], [2, 3, 4]]
    print(A)
    print(solve_matrix(A))
    print(A)

def solve_matrix(A):
    V = copy.deepcopy(A)
    #print(V[0])
    for row in range(len(V[0])):
        value = V[row][row]
        # Dividing by the first non-zero element
        for column in range(row, len(V[row])):
            V[row][column] = V[row][column] / value

        # Elimination
        #for jindex in range(index, len(V[index])-1):
           # new_val = V[index + 1][index]
            #print(new_val)
        for row2 in range(row+1, len(V[row])):
            new_val = V[row2][row]
            #print("new value = ", new_val)
            #print('index: ', index, ' jindex: ', jindex, ' new_val: ', new_val)
            for column in range(row, len(V[row])):
                V[row2][column] = V[row2][column] - new_val * V[row][column]
            #print(V[row2])

    return V


if __name__ == '__main__':
    main()
    quit()