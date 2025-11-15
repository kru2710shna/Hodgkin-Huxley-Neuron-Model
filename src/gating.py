import numpy as np

# ----------------------------------------------------
#  SODIUM ACTIVATION GATE (m)
# ----------------------------------------------------

# αm(V)  =  0.1 * (V + 40) / (1 - exp(-(V + 40)/10))
def alpha_m(V):
    return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))

# βm(V)  =  4 * exp(-(V + 65)/18)
def beta_m(V):
    return 4.0 * np.exp(-(V + 65) / 18)


# ----------------------------------------------------
#  SODIUM INACTIVATION GATE (h)
# ----------------------------------------------------

# αh(V) = 0.07 * exp(-(V + 65)/20)
def alpha_h(V):
    return 0.07 * np.exp(-(V + 65) / 20)

# βh(V) = 1 / (1 + exp(-(V + 35)/10))
def beta_h(V):
    return 1.0 / (1 + np.exp(-(V + 35) / 10))


# ----------------------------------------------------
#  POTASSIUM ACTIVATION GATE (n)
# ----------------------------------------------------

# αn(V) = 0.01 * (V + 55) / (1 - exp(-(V + 55)/10))
def alpha_n(V):
    return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))

# βn(V) = 0.125 * exp(-(V + 65)/80)
def beta_n(V):
    return 0.125 * np.exp(-(V + 65) / 80)



def dm_dt(V, m):
    return alpha_m(V)*(1 - m) - beta_m(V)*m

def dh_dt(V, h):
    return alpha_h(V)*(1 - h) - beta_h(V)*h

def dn_dt(V, n):
    return alpha_n(V)*(1 - n) - beta_n(V)*n



# ----------------------------------------------------
#  SUMMARY OF ROLES (for documentation)
# ----------------------------------------------------

# αm(V): Opening rate of Na activation gate (fast)
# βm(V): Closing rate of Na activation gate

# αh(V): Opening rate of Na inactivation gate (slow recovery)
# βh(V): Closing/inactivation rate of Na channel (inactivation)

# αn(V): Opening rate of K activation gate (slow)
# βn(V): Closing rate of K activation gate
