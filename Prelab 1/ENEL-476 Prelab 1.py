import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0, pi
import seaborn as sns

########################################################################

# Question 1 

########################################################################

def Q1() -> None:

    num_point = int(5e5)

    Z = np.linspace(start=0, stop=L, num=num_point)

    mid = num_point // 2

    ax = sns.lineplot(x = Z[0:mid], y=np.abs(-2 * H / L * Z[0:mid]), color='blue')
    ax = sns.lineplot(x = Z[mid:], y=np.abs(-2 * H / L * ( L - Z[mid:])), color='blue')

    plt.title('Magnitude of Magnetic Field Strength vs. z\'')
    plt.xlabel('z\' (m)')
    plt.ylabel('|H(z\')| (T)')
    plt.savefig('Magnitude of Magnetic Field Strength vs. Z.png')
    plt.close()

    return

########################################################################

# Question 2

########################################################################
def Q2() -> None:

    num_point = int(5e5)

    T = np.linspace(start=0, stop=L, num=num_point)

    mid = num_point // 2

    ax = sns.lineplot(x=T[0:mid], y=np.abs(-2 * H / L * V * T[0:mid]), color='blue')
    ax = sns.lineplot(x=T[mid:], y=np.abs(-2 * H / L * (L - V * T[mid:])), color='blue')

    plt.title('Magnitude of Magnetic Field Strength vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('|H(t)| (T)')
    plt.savefig('Magnitude of Magnetic Field Strength vs. Time.png')
    plt.close()

    return

########################################################################

# Question 3

########################################################################

def Q3() -> None:

    num_point = int(5e5)

    T = np.linspace(start=0, stop=L, num=num_point)

    mid = num_point // 2

    ax = sns.lineplot(x=T[0:mid], y=-2 * H * mu_0 * pi * a ** 2/ L * V * T[0:mid], color='blue')
    ax = sns.lineplot(x=T[mid:], y=-2 * H * mu_0 * pi * a ** 2/ L * (L - V * T[mid:]), color='blue')

    plt.title('Magnetic Flux vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('Magnetic Flux (Wb)')
    plt.grid(True)
    plt.axis()
    plt.savefig('Magnitude of Magnetic Flux vs. Time.png')
    plt.close()

    return

########################################################################

# Question 4

########################################################################

def Q4() -> None:
    
    num_point = int(5e5)

    T = np.linspace(start=0, stop=L, num=num_point)

    mid = num_point // 2

    ax = sns.lineplot(x=T[1:mid], y=-1 * np.diff(-2 * H * mu_0 * pi * a ** 2/ L * V * T[0:mid]), color='blue')
    ax = sns.lineplot(x=T[mid:-1], y=-1 * np.diff(-2 * H * mu_0 * pi * a ** 2/ L * (L - V * T[mid:])), color='blue')

    plt.title('Induced Voltage vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('Induced Voltage (V)')
    plt.grid(True)
    plt.axis()
    plt.savefig('Induced Voltage vs. Time.png')
    plt.close()

    return

########################################################################

# Question 5/6/7/8

########################################################################

def Q5() -> None:

    # #6
    # Current starts counterclockwise to opposed changing magnetic field and switches to clockwise
    # as the bar is leaving the loop.

    # #7
    # Stacking N loops will multiply the EMF voltage by N times.

    # #8
    # If the magnet were flipped nothing about the situation would change as it is the change magnetic field that
    # defines the EMF, not the polarity.

    num_point = int(5e5)

    T = np.linspace(start=0, stop=L, num=num_point)

    mid = num_point // 2

    ax = sns.lineplot(x=T[1:mid], y=-1 * np.diff(-2 * H * mu_0 * pi * a ** 2/ L * V * T[0:mid]) / R, color='blue')
    ax = sns.lineplot(x=T[mid:-1], y=-1 * np.diff(-2 * H * mu_0 * pi * a ** 2/ L * (L - V * T[mid:])) / R, color='blue')

    plt.title('Current vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('Counterclockwise Current (A)')
    plt.grid(True)
    plt.axis()
    plt.savefig('Current vs. Time.png')
    plt.close()

    return

if __name__ == '__main__':
    L, H, V, a, R = 1, 1, 1, 1, 1

    Q1()
    Q2()
    Q3()
    Q4()
    Q5()