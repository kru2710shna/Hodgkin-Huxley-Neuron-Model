from .gating import dm_dt, dh_dt, dn_dt
from .parameters import Cm
from .currents import I_Na, I_K, I_L

def hh_derivatives(t, y, I_ext):
    V, m, h, n = y

    # -----------------------------
    # STEP 6: Compute ionic currents
    # -----------------------------
    INa = I_Na(V, m, h)    # Na current
    IK  = I_K(V, n)        # K current
    IL  = I_L(V)           # Leak current

    # MAIN HH EQUATION (dV/dt)
    dVdt = (I_ext(t) - (INa + IK + IL)) / Cm

    # Gating variables
    dmdt = dm_dt(V, m)
    dhdt = dh_dt(V, h)
    dndt = dn_dt(V, n)

    return [dVdt, dmdt, dhdt, dndt]
