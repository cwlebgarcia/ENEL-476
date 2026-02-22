import numpy as np
from scipy.constants import mu_0, epsilon_0, c

calc_general_alpha = lambda angular_frequency, relative_permeability, relative_permittivity, conductivity: (
        angular_frequency * np.sqrt(mu_0 * relative_permeability * epsilon_0 * relative_permittivity / 2 * 
        (np.sqrt(1 + np.power(conductivity / (angular_frequency * epsilon_0 * relative_permittivity), 2) - 1)))
        )

calc_general_beta = lambda angular_frequency, relative_permittivity, conductivity, relative_permeability: (
        angular_frequency * np.sqrt(mu_0 * relative_permeability * epsilon_0 * relative_permittivity / 2 * 
        (np.sqrt(1 + np.power(conductivity / (angular_frequency * epsilon_0 * relative_permittivity), 2) + 1)))
        )

calc_general_eta = lambda relative_permeability, relative_permittivity, angular_frequency, conductivity: (
        np.sqrt(mu_0 * relative_permeability / epsilon_0 * relative_permittivity) 
        / np.power(1 + np.power(conductivity / (angular_frequency * epsilon_0 * relative_permittivity), 2), 1/4)
        )

calc_general_theta_eta = lambda conductivity, angular_frequency, relative_permittivity: (
        1/2 * np.atan(conductivity / (angular_frequency * epsilon_0 * relative_permittivity))
        )

if __name__ == "__main__":
    
    f = 10e6 # Hz
    angular_frequency = 2 * np.pi * f
    relative_permittivity = 4
    relative_permeability = 1
    conductivity = 2e-3 # S / m

    alpha = calc_general_alpha(
            angular_frequency=angular_frequency,
            relative_permeability=relative_permeability,
            relative_permittivity=relative_permittivity,
            conductivity=conductivity,
            )
    
    beta = calc_general_beta(
            angular_frequency=angular_frequency,
            relative_permeability=relative_permeability,
            relative_permittivity=relative_permittivity,
            conductivity=conductivity,
            )
    
    eta = calc_general_eta(
            angular_frequency=angular_frequency,
            relative_permeability=relative_permeability,
            relative_permittivity=relative_permittivity,
            conductivity=conductivity,          
            )
    
    theta_eta = calc_general_theta_eta(
            conductivity=conductivity,
            angular_frequency=angular_frequency,
            relative_permittivity=relative_permittivity,
            )
    
    print(f'Alpha: {alpha} Np/m')
    print(f'Beta: {beta} rad/m')
    print(f'Eta: {eta} ohms')
    print(f'Eta Phase: {theta_eta} rad')