import numpy as np
import math

def inner_prod(v, w):
    result = 0.0
    if len(v) != len(w):
        print('error')
        return
    for index in range(len(v)):
        result += v[index]*w[index]
    return result

def gram_schmidt(V:list):
    W = list()
    for v in V:
        w_new = v.copy()
        for w in W:
            prod = inner_prod(w, w_new)
            w_new = w_new - prod*w
        norm = math.sqrt(inner_prod(w_new, w_new))
        if norm > 0.000000001:
            w_new = w_new/norm
            W.append(w_new)
    return W

def main():
    rg = np.random.default_rng(1)
    k = 3
    d = 2
    V = list()
    for i in range(k):
        v = rg.random((1,d))[0]
        V.append(v)
    W = gram_schmidt(V)
    for w in W:
        print(w)
    #result = inner_prod(v,w)
    #print("result: ", result)
    return

if __name__ == '__main__':
    main()
    quit()