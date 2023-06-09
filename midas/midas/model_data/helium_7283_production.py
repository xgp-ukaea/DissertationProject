from numpy import array, log, meshgrid, linspace, savez


density_axis = array([
    1.00E+01, 1.00E+02, 1.00E+03, 1.00E+04, 1.00E+05, 1.00E+06, 3.00E+06, 1.00E+07,
    3.00E+07, 1.00E+08, 3.00E+08, 1.00E+09, 3.00E+09, 1.00E+10, 3.00E+10, 1.00E+11,
    3.00E+11, 1.00E+12, 3.00E+12, 1.00E+13, 3.00E+13, 1.00E+14, 3.00E+14, 1.00E+15
])

temperature_axis = array([
    4.31E-02, 6.03E-02, 8.62E-02, 1.29E-01, 1.72E-01, 2.59E-01, 4.31E-01, 6.03E-01,
    8.62E-01, 1.29E+00, 1.72E+00, 2.59E+00, 4.31E+00, 6.03E+00, 8.62E+00, 1.29E+01,
    1.72E+01, 2.59E+01, 4.31E+01, 6.03E+01, 8.62E+01, 1.29E+02, 1.72E+02, 2.59E+02
])

recombination_pec = array([
    1.17E-14, 1.73E-14, 2.60E-14, 4.15E-14, 5.77E-14, 8.65E-14, 9.68E-14, 8.69E-14,
    7.02E-14, 5.06E-14, 3.83E-14, 2.42E-14, 1.31E-14, 9.67E-15, 9.23E-15, 1.12E-14,
    1.27E-14, 1.29E-14, 9.97E-15, 7.47E-15, 5.15E-15, 2.84E-15, 1.83E-15, 9.91E-16,
    9.58E-15, 1.38E-14, 2.02E-14, 3.13E-14, 4.26E-14, 6.23E-14, 6.97E-14, 6.28E-14,
    5.11E-14, 3.74E-14, 2.85E-14, 1.81E-14, 9.86E-15, 7.61E-15, 7.95E-15, 1.05E-14,
    1.22E-14, 1.26E-14, 9.81E-15, 7.37E-15, 5.09E-15, 2.80E-15, 1.81E-15, 9.79E-16,
    8.00E-15, 1.12E-14, 1.59E-14, 2.37E-14, 3.16E-14, 4.49E-14, 5.01E-14, 4.55E-14,
    3.75E-14, 2.80E-14, 2.16E-14, 1.38E-14, 7.68E-15, 6.22E-15, 7.08E-15, 9.93E-15,
    1.18E-14, 1.23E-14, 9.68E-15, 7.28E-15, 5.04E-15, 2.77E-15, 1.79E-15, 9.68E-16,
    7.04E-15, 9.47E-15, 1.30E-14, 1.85E-14, 2.39E-14, 3.27E-14, 3.62E-14, 3.31E-14,
    2.77E-14, 2.12E-14, 1.66E-14, 1.07E-14, 6.06E-15, 5.18E-15, 6.42E-15, 9.49E-15,
    1.15E-14, 1.21E-14, 9.52E-15, 7.17E-15, 4.96E-15, 2.73E-15, 1.76E-15, 9.55E-16,
    6.53E-15, 8.40E-15, 1.10E-14, 1.48E-14, 1.84E-14, 2.41E-14, 2.64E-14, 2.43E-14,
    2.08E-14, 1.64E-14, 1.31E-14, 8.57E-15, 4.94E-15, 4.47E-15, 5.92E-15, 9.09E-15,
    1.11E-14, 1.18E-14, 9.31E-15, 7.02E-15, 4.86E-15, 2.68E-15, 1.73E-15, 9.37E-16,
    6.60E-15, 7.95E-15, 9.69E-15, 1.21E-14, 1.42E-14, 1.74E-14, 1.87E-14, 1.75E-14,
    1.54E-14, 1.27E-14, 1.04E-14, 6.87E-15, 4.06E-15, 3.88E-15, 5.45E-15, 8.61E-15,
    1.06E-14, 1.13E-14, 8.95E-15, 6.75E-15, 4.68E-15, 2.59E-15, 1.67E-15, 9.06E-16,
    6.89E-15, 8.01E-15, 9.39E-15, 1.13E-14, 1.28E-14, 1.51E-14, 1.60E-14, 1.50E-14,
    1.34E-14, 1.13E-14, 9.37E-15, 6.25E-15, 3.73E-15, 3.64E-15, 5.24E-15, 8.36E-15,
    1.03E-14, 1.10E-14, 8.71E-15, 6.58E-15, 4.56E-15, 2.52E-15, 1.63E-15, 8.85E-16,
    7.52E-15, 8.39E-15, 9.41E-15, 1.07E-14, 1.18E-14, 1.33E-14, 1.39E-14, 1.31E-14,
    1.19E-14, 1.03E-14, 8.58E-15, 5.76E-15, 3.46E-15, 3.44E-15, 5.04E-15, 8.09E-15,
    9.97E-15, 1.07E-14, 8.44E-15, 6.37E-15, 4.41E-15, 2.44E-15, 1.58E-15, 8.57E-16,
    8.62E-15, 9.17E-15, 9.78E-15, 1.05E-14, 1.11E-14, 1.19E-14, 1.22E-14, 1.16E-14,
    1.07E-14, 9.41E-15, 7.95E-15, 5.38E-15, 3.25E-15, 3.27E-15, 4.84E-15, 7.79E-15,
    9.60E-15, 1.03E-14, 8.14E-15, 6.15E-15, 4.26E-15, 2.36E-15, 1.53E-15, 8.30E-16,
    1.08E-14, 1.07E-14, 1.07E-14, 1.06E-14, 1.06E-14, 1.05E-14, 1.04E-14, 1.00E-14,
    9.49E-15, 8.56E-15, 7.33E-15, 5.01E-15, 3.04E-15, 3.08E-15, 4.60E-15, 7.40E-15,
    9.10E-15, 9.71E-15, 7.72E-15, 5.84E-15, 4.05E-15, 2.25E-15, 1.46E-15, 7.93E-16,
    1.41E-14, 1.31E-14, 1.21E-14, 1.11E-14, 1.04E-14, 9.59E-15, 9.16E-15, 8.87E-15,
    8.58E-15, 7.92E-15, 6.86E-15, 4.73E-15, 2.87E-15, 2.91E-15, 4.36E-15, 7.00E-15,
    8.57E-15, 9.14E-15, 7.28E-15, 5.51E-15, 3.81E-15, 2.12E-15, 1.38E-15, 7.51E-16,
    2.04E-14, 1.74E-14, 1.47E-14, 1.22E-14, 1.06E-14, 8.95E-15, 8.12E-15, 7.92E-15,
    7.84E-15, 7.39E-15, 6.46E-15, 4.49E-15, 2.73E-15, 2.75E-15, 4.10E-15, 6.55E-15,
    7.98E-15, 8.48E-15, 6.77E-15, 5.13E-15, 3.54E-15, 1.98E-15, 1.28E-15, 7.00E-16,
    3.05E-14, 2.40E-14, 1.86E-14, 1.40E-14, 1.14E-14, 8.78E-15, 7.53E-15, 7.35E-15,
    7.38E-15, 7.06E-15, 6.21E-15, 4.34E-15, 2.62E-15, 2.61E-15, 3.86E-15, 6.12E-15,
    7.41E-15, 7.87E-15, 6.30E-15, 4.78E-15, 3.29E-15, 1.84E-15, 1.20E-15, 6.53E-16,
    5.21E-14, 3.73E-14, 2.62E-14, 1.75E-14, 1.32E-14, 9.11E-15, 7.20E-15, 6.98E-15,
    7.07E-15, 6.80E-15, 6.00E-15, 4.20E-15, 2.52E-15, 2.46E-15, 3.57E-15, 5.60E-15,
    6.73E-15, 7.14E-15, 5.75E-15, 4.37E-15, 3.00E-15, 1.69E-15, 1.10E-15, 6.01E-16,
    9.33E-14, 6.08E-14, 3.87E-14, 2.31E-14, 1.60E-14, 9.97E-15, 7.19E-15, 6.85E-15,
    6.91E-15, 6.62E-15, 5.83E-15, 4.06E-15, 2.40E-15, 2.30E-15, 3.27E-15, 5.05E-15,
    6.04E-15, 6.40E-15, 5.20E-15, 3.96E-15, 2.72E-15, 1.54E-15, 1.00E-15, 5.49E-16,
    1.94E-13, 1.14E-13, 6.44E-14, 3.38E-14, 2.14E-14, 1.17E-14, 7.49E-15, 6.87E-15,
    6.78E-15, 6.35E-15, 5.52E-15, 3.79E-15, 2.19E-15, 2.04E-15, 2.81E-15, 4.28E-15,
    5.10E-15, 5.42E-15, 4.46E-15, 3.42E-15, 2.35E-15, 1.34E-15, 8.80E-16, 4.85E-16,
    4.23E-13, 2.22E-13, 1.12E-13, 5.12E-14, 2.95E-14, 1.41E-14, 7.89E-15, 6.82E-15,
    6.41E-15, 5.73E-15, 4.83E-15, 3.21E-15, 1.79E-15, 1.61E-15, 2.15E-15, 3.25E-15,
    3.88E-15, 4.18E-15, 3.52E-15, 2.73E-15, 1.90E-15, 1.11E-15, 7.34E-16, 4.09E-16,
    1.18E-12, 5.30E-13, 2.27E-13, 8.63E-14, 4.35E-14, 1.74E-14, 7.89E-15, 6.11E-15,
    5.21E-15, 4.22E-15, 3.35E-15, 2.07E-15, 1.07E-15, 9.37E-16, 1.21E-15, 1.84E-15,
    2.23E-15, 2.48E-15, 2.17E-15, 1.73E-15, 1.23E-15, 7.44E-16, 5.08E-16, 2.92E-16,
    3.58E-12, 1.33E-12, 4.68E-13, 1.43E-13, 6.13E-14, 1.97E-14, 6.98E-15, 4.67E-15,
    3.49E-15, 2.47E-15, 1.79E-15, 9.98E-16, 4.77E-16, 4.15E-16, 5.44E-16, 8.54E-16,
    1.06E-15, 1.21E-15, 1.10E-15, 8.98E-16, 6.53E-16, 4.07E-16, 2.88E-16, 1.71E-16,
    1.32E-11, 3.96E-12, 1.11E-12, 2.60E-13, 9.27E-14, 2.32E-14, 6.27E-15, 3.48E-15,
    2.14E-15, 1.23E-15, 7.88E-16, 3.92E-16, 1.83E-16, 1.62E-16, 2.22E-16, 3.63E-16,
    4.57E-16, 5.28E-16, 4.82E-16, 3.94E-16, 2.87E-16, 1.80E-16, 1.29E-16, 7.75E-17,
    5.19E-11, 1.34E-11, 3.18E-12, 6.21E-13, 1.95E-13, 4.09E-14, 9.15E-15, 4.26E-15,
    2.16E-15, 1.02E-15, 6.07E-16, 2.97E-16, 1.31E-16, 1.04E-16, 1.26E-16, 1.96E-16,
    2.43E-16, 2.76E-16, 2.49E-16, 2.01E-16, 1.45E-16, 8.92E-17, 6.43E-17, 3.80E-17,
    3.61E-10, 7.93E-11, 1.59E-11, 2.55E-12, 6.97E-13, 1.22E-13, 2.28E-14, 9.12E-15,
    3.90E-15, 1.60E-15, 8.95E-16, 4.14E-16, 1.58E-16, 1.03E-16, 8.95E-17, 1.10E-16,
    1.27E-16, 1.38E-16, 1.23E-16, 9.90E-17, 7.09E-17, 4.35E-17, 3.23E-17, 1.89E-17,
    1.81E-09, 3.52E-10, 6.20E-11, 8.61E-12, 2.12E-12, 3.22E-13, 5.15E-14, 1.82E-14,
    6.84E-15, 2.50E-15, 1.31E-15, 5.67E-16, 1.95E-16, 1.14E-16, 7.69E-17, 6.80E-17,
    6.86E-17, 6.82E-17, 5.83E-17, 4.67E-17, 3.35E-17, 2.07E-17, 1.61E-17, 9.49E-18,
    5.84E-09, 1.05E-09, 1.71E-10, 2.17E-11, 5.02E-12, 6.92E-13, 9.38E-14, 2.93E-14,
    9.90E-15, 3.30E-15, 1.65E-15, 6.84E-16, 2.21E-16, 1.23E-16, 7.24E-17, 4.76E-17,
    3.95E-17, 3.27E-17, 2.50E-17, 1.94E-17, 1.37E-17, 8.40E-18, 6.74E-18, 4.00E-18
])

excitation_pec = array([
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.54E-46, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.32E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.54E-46, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.31E-15, 1.26E-13, 2.62E-12, 8.90E-12, 2.16E-11, 4.26E-11,
    6.01E-11, 8.47E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.79E-46, 1.45E-31, 2.32E-25,
    1.00E-20, 3.88E-17, 2.31E-15, 1.26E-13, 2.62E-12, 8.89E-12, 2.16E-11, 4.26E-11,
    6.00E-11, 8.46E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.71E-46, 1.45E-31, 2.32E-25,
    9.99E-21, 3.87E-17, 2.31E-15, 1.26E-13, 2.61E-12, 8.87E-12, 2.15E-11, 4.25E-11,
    5.99E-11, 8.45E-11, 1.10E-10, 1.21E-10, 1.28E-10, 1.30E-10, 1.29E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.71E-46, 1.45E-31, 2.31E-25,
    9.95E-21, 3.85E-17, 2.30E-15, 1.25E-13, 2.59E-12, 8.80E-12, 2.13E-11, 4.22E-11,
    5.95E-11, 8.39E-11, 1.09E-10, 1.20E-10, 1.27E-10, 1.29E-10, 1.28E-10, 1.24E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.70E-46, 1.43E-31, 2.28E-25,
    9.82E-21, 3.79E-17, 2.26E-15, 1.22E-13, 2.53E-12, 8.60E-12, 2.09E-11, 4.13E-11,
    5.83E-11, 8.24E-11, 1.07E-10, 1.18E-10, 1.25E-10, 1.28E-10, 1.27E-10, 1.23E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.65E-46, 1.39E-31, 2.20E-25,
    9.41E-21, 3.60E-17, 2.13E-15, 1.14E-13, 2.35E-12, 7.97E-12, 1.93E-11, 3.84E-11,
    5.44E-11, 7.73E-11, 1.01E-10, 1.13E-10, 1.20E-10, 1.23E-10, 1.23E-10, 1.19E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.52E-46, 1.29E-31, 2.01E-25,
    8.40E-21, 3.14E-17, 1.83E-15, 9.62E-14, 1.94E-12, 6.56E-12, 1.59E-11, 3.19E-11,
    4.57E-11, 6.58E-11, 8.79E-11, 9.87E-11, 1.07E-10, 1.11E-10, 1.12E-10, 1.10E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 2.14E-46, 1.02E-31, 1.52E-25,
    6.09E-21, 2.16E-17, 1.21E-15, 6.09E-14, 1.19E-12, 4.00E-12, 9.82E-12, 2.02E-11,
    2.97E-11, 4.40E-11, 6.10E-11, 7.03E-11, 7.81E-11, 8.41E-11, 8.77E-11, 8.85E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.50E-46, 6.43E-32, 8.99E-26,
    3.38E-21, 1.12E-17, 5.96E-16, 2.84E-14, 5.42E-13, 1.87E-12, 4.78E-12, 1.04E-11,
    1.57E-11, 2.42E-11, 3.51E-11, 4.16E-11, 4.76E-11, 5.31E-11, 5.72E-11, 5.97E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 7.52E-47, 2.82E-32, 3.70E-26,
    1.31E-21, 3.97E-18, 2.00E-16, 9.35E-15, 1.93E-13, 7.23E-13, 1.99E-12, 4.63E-12,
    7.28E-12, 1.18E-11, 1.78E-11, 2.16E-11, 2.53E-11, 2.89E-11, 3.19E-11, 3.39E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 3.34E-47, 1.16E-32, 1.47E-26,
    4.96E-22, 1.42E-18, 7.26E-17, 3.71E-15, 8.58E-14, 3.43E-13, 1.00E-12, 2.44E-12,
    3.93E-12, 6.56E-12, 1.03E-11, 1.28E-11, 1.52E-11, 1.75E-11, 1.98E-11, 2.11E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.48E-47, 5.08E-33, 6.36E-27,
    2.05E-22, 5.81E-19, 3.08E-17, 1.68E-15, 3.97E-14, 1.64E-13, 4.92E-13, 1.23E-12,
    2.03E-12, 3.47E-12, 5.62E-12, 7.11E-12, 8.62E-12, 1.01E-11, 1.20E-11, 1.30E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 9.22E-48, 3.27E-33, 3.92E-27,
    1.17E-22, 3.12E-19, 1.62E-17, 8.66E-16, 1.98E-14, 8.17E-14, 2.48E-13, 6.26E-13,
    1.04E-12, 1.79E-12, 2.95E-12, 3.77E-12, 4.63E-12, 5.53E-12, 6.90E-12, 7.60E-12,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 7.07E-48, 2.62E-33, 2.88E-27,
    7.58E-23, 1.78E-19, 8.67E-18, 4.38E-16, 9.40E-15, 3.85E-14, 1.16E-13, 2.93E-13,
    4.85E-13, 8.40E-13, 1.39E-12, 1.78E-12, 2.19E-12, 2.63E-12, 3.41E-12, 3.79E-12
])


# conversion from cm^-3 to m^-3
density_axis *= 1e6
recombination_pec *= 1e-6
excitation_pec *= 1e-6

log_density_axis = log(density_axis)
log_temperature_axis = log(temperature_axis)
log_recombination_pec = log(recombination_pec)
log_excitation_pec = log(excitation_pec)


print(log_temperature_axis.shape, log_density_axis.shape, log_recombination_pec.shape)


log_recombination_pec = log_recombination_pec.reshape([log_temperature_axis.size, log_density_axis.size])
log_excitation_pec = log_excitation_pec.reshape([log_temperature_axis.size, log_density_axis.size])


from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*meshgrid(log_temperature_axis, log_density_axis), log_recombination_pec, c = log_recombination_pec)

ax.set_xlabel('log-temperature')
ax.set_ylabel('log-density')
ax.set_zlabel('log-PEC')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*meshgrid(log_temperature_axis, log_density_axis), log_excitation_pec, c = log_excitation_pec)

ax.set_xlabel('log-temperature')
ax.set_ylabel('log-density')
ax.set_zlabel('log-PEC')
plt.show()



savez('He_7283_pec_data.npz',
      ln_ne = log_density_axis,
      ln_te = log_temperature_axis,
      exc_ln_pec = log_excitation_pec,
      rec_ln_pec = log_recombination_pec)



from midas.emission import AdasLineModel

model = AdasLineModel.build('He_7283')



print( model(1.2, 2e19, 5e18) )
print( model(6.5, 3.5e19, 8e18) )