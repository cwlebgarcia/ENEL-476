import numpy as np
from numpy.polynomial import Polynomial
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.constants import mu_0

data_path: str = 'Lab-1/raw_csv_data'
graphs_path: str = 'Lab-1/Graphs'

resistance: float = 100e3 # 100k resistor
diameter: float = 33.5e-3
area: float = np.pi * diameter ** 2 / 4

for file in os.listdir(data_path):
    if file.endswith('.csv'):  
        file_path = os.path.join(data_path, file) 
        df = pd.read_csv(file_path)  
    print(file)

    x = df['second']
    y = df['Volt']

    finite_mask = np.isfinite(y) # Mask to remove NaNs and infs

    x = x[finite_mask]
    y = y[finite_mask]

    time_mask = np.abs(x) < 0.06 # Truncate large time values

    x = x[time_mask]
    y = y[time_mask]
    
    # Polynomial fit for denoising
    coefficients = Polynomial.fit(x=x, y=y, deg=200)
    fit_polynomial = coefficients.convert()
    voltage = fit_polynomial(x)
    
    flux = -1 * np.cumsum(voltage)

    # Plot voltage
    ax = sns.lineplot(x=x, y=voltage)
    plt.title(f'Voltage vs. Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.savefig(f'{graphs_path + '/' + file} voltage.png')
    plt.close()

    # Plot current
    ax = sns.lineplot(x=x, y=voltage / resistance)
    plt.title(f'Current vs. Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.savefig(f'{graphs_path + '/' + file} current.png')
    plt.close()

    # Plot flux
    ax = sns.lineplot(x=x, y=flux)
    plt.title(f'Magnetic Flux vs. Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Magnetic Flux (Wb)')
    plt.savefig(f'{graphs_path + '/' + file} Flux.png')
    plt.close()

    # Plot magnetic field
    ax = sns.lineplot(x=x, y=flux * area / mu_0)
    plt.title(f'Magnetic Field vs. Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Magnetic Field (T)')
    plt.savefig(f'{graphs_path + '/' + file} Magnetic Field.png')
    plt.close()