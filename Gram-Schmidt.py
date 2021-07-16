import numpy
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
            #prod = inner_prod(w, w_new)
            prod = np.vdot(w, w_new)
            w_new = w_new - prod*w
        #norm = math.sqrt(inner_prod(w_new, w_new))
        norm = math.sqrt(np.vdot(w_new, w_new))
        if norm > 0.000000001:
            w_new = w_new/norm
            W.append(w_new)
    return W

def main():
    rg = np.random.default_rng(1)
    k = 6
    d = 6
    V = list()
    for i in range(k):
        v = rg.random((1,d))[0]
        V.append(v)

    W = gram_schmidt(V)
    #for w in W:
        #print(w)

    #result = inner_prod(v,w)
    #print("result: ", result)
    z = rg.random((1, d))[0]
    alpha = list()
    for w in W:
        alpha.append(numpy.vdot(z,w))
    print(alpha)
    z_test = z.copy()
    for index in range(len(alpha)):
        z_test = z_test - alpha[index] * W[index]

    print(z_test)
    return

if __name__ == '__main__':
    main()
    quit()