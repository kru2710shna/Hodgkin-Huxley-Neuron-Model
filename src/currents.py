from parameters import gNa_max, gK_max, gL, ENa, EK, EL

def I_Na(V, m, h):
    return gNa_max * (m**3) * h * (V - ENa)

def I_K(V, n):
    return gK_max * (n**4) * (V - EK)

def I_L(V):
    return gL * (V - EL)
