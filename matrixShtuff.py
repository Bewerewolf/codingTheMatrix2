import numpy as np

def main():
    A = [[2, 2, 3], [4, 5, 6], [2, 3, 4]]
    print(A)
    print(solve_matrix(A))

def solve_matrix(A):
    V = A
    print(V[0])
    for index in range(len(V[0])):
        value = V[index][index]
        # Dividing by the first non-zero element
        for jindex in range(index, len(V[index])):
            V[index][jindex] = V[index][jindex] / value

        # Elimination
        if index > 0 and index < V[index]:
            new_val = V[index + 1][index]
        for jindex in range(index+1, len(V[index])):
            print('index: ', index, ' jindex: ', jindex, ' new_val: ', new_val)
            V[index+1][index] = V[index+1][index] - new_val * V[index][index]

    return V


if __name__ == '__main__':
    main()
    quit()