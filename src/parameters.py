# paramemters.py

Cm = 1.0 # uF/cm^2 Membrane Capacitance Higher Cm - Voltage chnages more Quickly, Lower Cm - Voltage changes Slowly, Cm dv/dt= ... 

# Max Conductance 
gNa_max = 120.0 # High - BEACUSE na rushes at the start of the spike and upstroke of action potantial is fast
gK_max = 36 # Smaller - K Flows Slower and they control the failing phase, and not the rising phase
gL= 0.3 # Sets rest setting potantial 

# Equilibrium Potantial (mv)
ENa = 50 # High Outside and low inside , Chemical and Ellectrical both pushes Na IN so, it is strong 
EK = -77.0 # INisde has huge K potential and chemical pushes it out and leaving makes inside negative - electrical pushes K In 
EL = -54.4 # small ionic leaks, this is the resting always has to end up between -65 and -77