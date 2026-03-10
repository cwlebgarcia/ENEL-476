import numpy as np
import matplotlib.pyplot as plt
import pysmithchart as smith

def save_smith_chart(gamma: complex, S_21: float, label: str, filename: str):
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection="smith")
    # Convert gamma to normalized impedance for pysmithchart
    if abs(1 - gamma) < 1e-12:
        z_norm = 1e6  # approximate open circuit
    else:
        z_norm = (1 + gamma) / (1 - gamma)
    ax.plot([z_norm], color="blue", marker="o", ms=6, label=label)
    ax.legend(loc="upper right")
    ax.set_title(f'Gamma = {gamma}, |Gamma| = {np.abs(gamma):.2f}, S_21 = {S_21} dB')
    plt.savefig(filename + '.png')
    plt.close()


if __name__ == "__main__":

    Z_0 = 50 # ohms

    # Reflection Coefficients
    matched_gamma = 0 
    shorted_gamma = -1
    open_gamma = 1

    # Corrected S_21 values
    save_smith_chart(gamma=shorted_gamma,S_21=-100, label='Short', filename='Short_Terminated')
    save_smith_chart(gamma=open_gamma, S_21=-100, label='Open', filename='Open_Terminated')
    save_smith_chart(gamma=matched_gamma, S_21=-100, label='50Ω Match', filename='Matched')
    save_smith_chart(gamma=0, S_21=0, label='50Ω Line', filename='Ports_Terminated')
