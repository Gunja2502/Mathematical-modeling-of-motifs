import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial state: [PhoQ, PhoP, PhoQ-P, PhoP-P, MgrB, Mg2+]
init_state = np.array([20, 10, 0, 0, 0, 1.0])  # Initial concentrations (µM), Mg2+ starts high (1.0)

# Modified ODE model
def diffEq(X, t):
    dX = np.zeros(6)
    PhoQ, PhoP, PhoQ_P, PhoP_P, MgrB, Mg2 = X  # Unpack variables

    # Mg2+ decay over time (simulating environmental change)
    dX[5] = -0.01 * Mg2  # Linear decay

    # Mg2+ effects on PhoQ activity (phosphatase vs kinase)
    inhibition_factor = Mg2 / (Ki + Mg2)  # High Mg2+ inhibits kinase activity

    # PhoQ dynamics
    dX[0] = -k1 * PhoQ * (1 - inhibition_factor) + k2 * PhoQ_P  # Kinase vs phosphatase

    # PhoP dynamics
    dX[1] = -k3 * PhoP * PhoQ_P + k4 * PhoP_P  # Phosphorylation/dephosphorylation

    # PhoQ-P dynamics
    dX[2] = k1 * PhoQ * (1 - inhibition_factor) - k2 * PhoQ_P  # Kinase vs phosphatase

    # PhoP-P dynamics
    dX[3] = k3 * PhoP * PhoQ_P - k4 * PhoP_P  # Phosphorylation/dephosphorylation

    # MgrB dynamics (regulated by PhoP-P)
    dX[4] = ksynM * PhoP_P / (Kprom2 + PhoP_P) - kd * MgrB  # Production and decay

    return dX

# Parameters
k1 = 1.0      # PhoQ kinase rate
k2 = 0.5      # PhoQ phosphatase rate
k3 = 1.5      # PhoP phosphorylation by PhoQ-P
k4 = 0.8      # PhoP-P dephosphorylation by PhoQ
ksynM = 0.02  # MgrB synthesis rate
Kprom2 = 0.5  # PhoP-P activation threshold for MgrB
kd = 0.01     # MgrB decay rate
Ki = 0.5      # Mg2+ inhibition constant for PhoQ

# Time grid
t_min, t_max, dt = 0, 300, 0.1
times = np.arange(t_min, t_max + dt, dt)

# Solve ODE
X = odeint(diffEq, init_state, times)

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(times, X[:, 0], label="PhoQ", linestyle="--", linewidth=2)
plt.plot(times, X[:, 1], label="PhoP", linestyle="--", linewidth=2)
plt.plot(times, X[:, 2], label="PhoQ-P (Kinase)", linestyle="-", linewidth=2)
plt.plot(times, X[:, 3], label="PhoP-P (Phosphorylated PhoP)", linestyle="-", linewidth=2)
plt.plot(times, X[:, 4], label="MgrB", linestyle="-.", linewidth=2)
plt.plot(times, X[:, 5], label="Mg2+", linestyle=":", linewidth=2)

# Labeling the plot
plt.xlabel("Time (s)")
plt.ylabel("Concentration (µM)")
plt.legend()
plt.title("PhoQ-PhoP Induction Kinetics")
plt.grid(True)
plt.show()
