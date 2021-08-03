import numpy as np
import copy

def main():
    A = [[2.0, 2.0, 3.0], [4.0, 5.0, 6.0], [2.0, 3.0, 4.0]]
    numpA = np.array(A)
    print(numpA)
    print(solve_matrix(numpA))
    print(numpA)

def solve_matrix(A):
    V = copy.deepcopy(A)
    print(V[0])
    for row in range(len(V[0])):
        V[row] = V[row]/V[row][row]

        # Elimination
        for row2 in range(row+1, len(V[row])):
            new_val = V[row2][row]
            V[row2] = V[row2] - new_val*V[row]

    return V


if __name__ == '__main__':
    main()
    quit()
