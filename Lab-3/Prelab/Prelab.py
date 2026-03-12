import numpy as np
import matplotlib.pyplot as plt
import pysmithchart as smith

def save_smith_chart(Z_0: complex, Z_L: complex, S_21: float, label: str, filename: str):
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection="smith")
    gamma = (Z_L - Z_0) / (Z_L + Z_0)

    ax.plot([Z_L], color="blue", marker="o", ms=6, label=label)
    ax.legend(loc="upper right")

    ax.set_title(f'Gamma = {gamma}, |Gamma| = {np.abs(gamma):.2f}, S_21 = {S_21} dB')
    plt.savefig(filename + '.png')
    plt.close()

if __name__ == "__main__":

    Z_0 = 50 # ohms

    # Reflection Coefficients
    ZL_matched = 50
    ZL_shorted = 0
    ZL_open = np.inf

    # Corrected S_21 values
    save_smith_chart(Z_0 = 50,Z_L=ZL_shorted,S_21=-100, label='Short', filename='Short_Terminated')
    save_smith_chart(Z_0 = 50,Z_L=ZL_open, S_21=-100, label='Open', filename='Open_Terminated')
    save_smith_chart(Z_0 = 50,Z_L=ZL_matched, S_21=-100, label='50 Ohm Match', filename='Matched')
    save_smith_chart(Z_0 = 50,Z_L=50, S_21=0, label='50 Ohm Line', filename='Ports_Terminated')
