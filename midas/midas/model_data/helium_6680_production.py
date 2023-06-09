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
    9.47E-14, 1.39E-13, 2.10E-13, 3.36E-13, 4.67E-13, 7.01E-13, 7.77E-13, 6.85E-13,
    5.37E-13, 3.73E-13, 2.76E-13, 1.72E-13, 9.29E-14, 6.69E-14, 6.27E-14, 8.17E-14,
    9.68E-14, 1.01E-13, 7.82E-14, 5.83E-14, 4.00E-14, 2.18E-14, 1.40E-14, 7.52E-15,
    7.69E-14, 1.11E-13, 1.63E-13, 2.52E-13, 3.44E-13, 5.03E-13, 5.56E-13, 4.90E-13,
    3.84E-13, 2.67E-13, 1.98E-13, 1.24E-13, 6.74E-14, 5.06E-14, 5.25E-14, 7.57E-14,
    9.27E-14, 9.82E-14, 7.70E-14, 5.75E-14, 3.95E-14, 2.15E-14, 1.38E-14, 7.42E-15,
    6.39E-14, 8.93E-14, 1.27E-13, 1.91E-13, 2.54E-13, 3.61E-13, 3.97E-13, 3.50E-13,
    2.75E-13, 1.93E-13, 1.44E-13, 8.99E-14, 5.00E-14, 3.95E-14, 4.56E-14, 7.16E-14,
    8.96E-14, 9.63E-14, 7.59E-14, 5.68E-14, 3.91E-14, 2.13E-14, 1.37E-14, 7.33E-15,
    5.61E-14, 7.55E-14, 1.03E-13, 1.48E-13, 1.91E-13, 2.61E-13, 2.84E-13, 2.49E-13,
    1.96E-13, 1.38E-13, 1.04E-13, 6.50E-14, 3.71E-14, 3.13E-14, 4.03E-14, 6.80E-14,
    8.69E-14, 9.43E-14, 7.46E-14, 5.59E-14, 3.85E-14, 2.10E-14, 1.35E-14, 7.23E-15,
    5.19E-14, 6.67E-14, 8.70E-14, 1.18E-13, 1.46E-13, 1.91E-13, 2.04E-13, 1.78E-13,
    1.40E-13, 1.01E-13, 7.60E-14, 4.79E-14, 2.82E-14, 2.56E-14, 3.64E-14, 6.48E-14,
    8.39E-14, 9.18E-14, 7.28E-14, 5.46E-14, 3.76E-14, 2.05E-14, 1.32E-14, 7.08E-15,
    5.25E-14, 6.31E-14, 7.67E-14, 9.57E-14, 1.12E-13, 1.36E-13, 1.41E-13, 1.23E-13,
    9.68E-14, 7.06E-14, 5.40E-14, 3.44E-14, 2.12E-14, 2.09E-14, 3.27E-14, 6.10E-14,
    7.98E-14, 8.77E-14, 6.97E-14, 5.24E-14, 3.61E-14, 1.97E-14, 1.27E-14, 6.82E-15,
    5.50E-14, 6.37E-14, 7.43E-14, 8.85E-14, 1.00E-13, 1.17E-13, 1.19E-13, 1.03E-13,
    8.13E-14, 5.97E-14, 4.59E-14, 2.94E-14, 1.85E-14, 1.90E-14, 3.11E-14, 5.89E-14,
    7.73E-14, 8.51E-14, 6.77E-14, 5.08E-14, 3.50E-14, 1.92E-14, 1.23E-14, 6.63E-15,
    6.05E-14, 6.70E-14, 7.46E-14, 8.43E-14, 9.19E-14, 1.02E-13, 1.01E-13, 8.72E-14,
    6.89E-14, 5.10E-14, 3.95E-14, 2.54E-14, 1.64E-14, 1.74E-14, 2.95E-14, 5.67E-14,
    7.45E-14, 8.21E-14, 6.53E-14, 4.90E-14, 3.38E-14, 1.85E-14, 1.19E-14, 6.40E-15,
    7.02E-14, 7.38E-14, 7.78E-14, 8.26E-14, 8.62E-14, 9.07E-14, 8.72E-14, 7.45E-14,
    5.89E-14, 4.41E-14, 3.44E-14, 2.24E-14, 1.47E-14, 1.61E-14, 2.80E-14, 5.43E-14,
    7.13E-14, 7.86E-14, 6.27E-14, 4.71E-14, 3.25E-14, 1.78E-14, 1.15E-14, 6.16E-15,
    8.92E-14, 8.74E-14, 8.54E-14, 8.33E-14, 8.18E-14, 7.97E-14, 7.31E-14, 6.18E-14,
    4.89E-14, 3.71E-14, 2.93E-14, 1.94E-14, 1.31E-14, 1.47E-14, 2.61E-14, 5.11E-14,
    6.70E-14, 7.38E-14, 5.90E-14, 4.44E-14, 3.06E-14, 1.68E-14, 1.08E-14, 5.84E-15,
    1.20E-13, 1.09E-13, 9.82E-14, 8.74E-14, 8.04E-14, 7.20E-14, 6.24E-14, 5.21E-14,
    4.12E-14, 3.17E-14, 2.54E-14, 1.71E-14, 1.17E-14, 1.34E-14, 2.43E-14, 4.78E-14,
    6.25E-14, 6.87E-14, 5.50E-14, 4.14E-14, 2.85E-14, 1.57E-14, 1.01E-14, 5.47E-15,
    1.78E-13, 1.48E-13, 1.21E-13, 9.68E-14, 8.25E-14, 6.68E-14, 5.36E-14, 4.39E-14,
    3.47E-14, 2.71E-14, 2.20E-14, 1.52E-14, 1.06E-14, 1.22E-14, 2.24E-14, 4.41E-14,
    5.73E-14, 6.28E-14, 5.04E-14, 3.80E-14, 2.61E-14, 1.44E-14, 9.28E-15, 5.01E-15,
    2.72E-13, 2.07E-13, 1.55E-13, 1.12E-13, 8.89E-14, 6.53E-14, 4.83E-14, 3.87E-14,
    3.05E-14, 2.40E-14, 1.98E-14, 1.38E-14, 9.72E-15, 1.12E-14, 2.06E-14, 4.04E-14,
    5.23E-14, 5.72E-14, 4.60E-14, 3.47E-14, 2.38E-14, 1.32E-14, 8.50E-15, 4.59E-15,
    4.66E-13, 3.23E-13, 2.19E-13, 1.41E-13, 1.03E-13, 6.78E-14, 4.51E-14, 3.48E-14,
    2.71E-14, 2.14E-14, 1.78E-14, 1.27E-14, 8.92E-15, 1.01E-14, 1.85E-14, 3.61E-14,
    4.63E-14, 5.05E-14, 4.09E-14, 3.09E-14, 2.12E-14, 1.18E-14, 7.59E-15, 4.11E-15,
    8.04E-13, 5.11E-13, 3.16E-13, 1.83E-13, 1.24E-13, 7.39E-14, 4.41E-14, 3.27E-14,
    2.50E-14, 1.97E-14, 1.64E-14, 1.17E-14, 8.16E-15, 9.08E-15, 1.63E-14, 3.17E-14,
    4.04E-14, 4.40E-14, 3.60E-14, 2.73E-14, 1.87E-14, 1.04E-14, 6.72E-15, 3.65E-15,
    1.48E-12, 8.61E-13, 4.83E-13, 2.51E-13, 1.57E-13, 8.37E-14, 4.44E-14, 3.15E-14,
    2.34E-14, 1.81E-14, 1.49E-14, 1.05E-14, 7.11E-15, 7.67E-15, 1.35E-14, 2.61E-14,
    3.32E-14, 3.63E-14, 3.02E-14, 2.31E-14, 1.58E-14, 8.87E-15, 5.75E-15, 3.13E-15,
    2.65E-12, 1.41E-12, 7.20E-13, 3.36E-13, 1.95E-13, 9.37E-14, 4.47E-14, 3.02E-14,
    2.18E-14, 1.63E-14, 1.32E-14, 9.02E-15, 5.79E-15, 6.02E-15, 1.04E-14, 2.01E-14,
    2.56E-14, 2.84E-14, 2.43E-14, 1.89E-14, 1.30E-14, 7.39E-15, 4.82E-15, 2.64E-15,
    5.25E-12, 2.50E-12, 1.14E-12, 4.66E-13, 2.47E-13, 1.05E-13, 4.39E-14, 2.80E-14,
    1.93E-14, 1.37E-14, 1.07E-14, 6.93E-15, 4.08E-15, 4.01E-15, 6.76E-15, 1.33E-14,
    1.71E-14, 1.93E-14, 1.72E-14, 1.37E-14, 9.60E-15, 5.58E-15, 3.69E-15, 2.05E-15,
    1.09E-11, 4.62E-12, 1.87E-12, 6.66E-13, 3.21E-13, 1.19E-13, 4.39E-14, 2.63E-14,
    1.71E-14, 1.13E-14, 8.37E-15, 5.00E-15, 2.65E-15, 2.47E-15, 4.09E-15, 8.17E-15,
    1.06E-14, 1.22E-14, 1.13E-14, 9.18E-15, 6.52E-15, 3.87E-15, 2.62E-15, 1.48E-15,
    3.40E-11, 1.25E-11, 4.35E-12, 1.31E-12, 5.56E-13, 1.75E-13, 5.56E-14, 3.05E-14,
    1.80E-14, 1.05E-14, 7.08E-15, 3.83E-15, 1.86E-15, 1.60E-15, 2.41E-15, 4.59E-15,
    5.91E-15, 6.85E-15, 6.42E-15, 5.26E-15, 3.78E-15, 2.29E-15, 1.59E-15, 9.14E-16,
    1.57E-10, 5.03E-11, 1.51E-11, 3.83E-12, 1.45E-12, 3.89E-13, 1.06E-13, 5.27E-14,
    2.77E-14, 1.40E-14, 8.68E-15, 4.45E-15, 1.99E-15, 1.48E-15, 1.73E-15, 2.82E-15,
    3.49E-15, 3.94E-15, 3.63E-15, 2.95E-15, 2.11E-15, 1.28E-15, 9.16E-16, 5.30E-16,
    1.19E-09, 3.24E-10, 8.15E-11, 1.70E-11, 5.58E-12, 1.25E-12, 2.87E-13, 1.25E-13,
    5.72E-14, 2.49E-14, 1.44E-14, 6.85E-15, 2.68E-15, 1.70E-15, 1.41E-15, 1.68E-15,
    1.90E-15, 2.03E-15, 1.81E-15, 1.46E-15, 1.04E-15, 6.34E-16, 4.69E-16, 2.72E-16,
    5.94E-09, 1.44E-09, 3.18E-10, 5.75E-11, 1.71E-11, 3.32E-12, 6.53E-13, 2.52E-13,
    1.01E-13, 3.91E-14, 2.10E-14, 9.38E-15, 3.33E-15, 1.94E-15, 1.28E-15, 1.09E-15,
    1.07E-15, 1.03E-15, 8.70E-16, 6.93E-16, 4.93E-16, 3.01E-16, 2.32E-16, 1.36E-16,
    1.89E-08, 4.26E-09, 8.74E-10, 1.45E-10, 4.03E-11, 7.13E-12, 1.19E-12, 4.07E-13,
    1.47E-13, 5.14E-14, 2.64E-14, 1.13E-14, 3.76E-15, 2.11E-15, 1.24E-15, 7.99E-16,
    6.48E-16, 5.19E-16, 3.87E-16, 2.97E-16, 2.07E-16, 1.26E-16, 9.94E-17, 5.83E-17
])




excitation_pec = array([
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.02E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.03E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.07E-31, 2.07E-25,
    1.06E-20, 4.97E-17, 3.38E-15, 2.20E-13, 5.47E-12, 1.96E-11, 4.66E-11, 8.29E-11,
    1.04E-10, 1.23E-10, 1.27E-10, 1.22E-10, 1.13E-10, 9.99E-11, 9.03E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.79E-46, 1.07E-31, 2.06E-25,
    1.06E-20, 4.97E-17, 3.37E-15, 2.20E-13, 5.46E-12, 1.95E-11, 4.66E-11, 8.28E-11,
    1.04E-10, 1.22E-10, 1.27E-10, 1.22E-10, 1.13E-10, 1.00E-10, 9.03E-11, 7.66E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.49E-46, 1.07E-31, 2.06E-25,
    1.06E-20, 4.95E-17, 3.36E-15, 2.19E-13, 5.43E-12, 1.95E-11, 4.64E-11, 8.26E-11,
    1.04E-10, 1.22E-10, 1.27E-10, 1.22E-10, 1.13E-10, 1.00E-10, 9.04E-11, 7.67E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.34E-46, 1.07E-31, 2.05E-25,
    1.05E-20, 4.90E-17, 3.32E-15, 2.15E-13, 5.35E-12, 1.92E-11, 4.58E-11, 8.18E-11,
    1.03E-10, 1.22E-10, 1.27E-10, 1.22E-10, 1.13E-10, 1.00E-10, 9.06E-11, 7.69E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.37E-46, 1.05E-31, 2.02E-25,
    1.03E-20, 4.77E-17, 3.22E-15, 2.08E-13, 5.15E-12, 1.85E-11, 4.44E-11, 7.99E-11,
    1.01E-10, 1.21E-10, 1.26E-10, 1.22E-10, 1.14E-10, 1.01E-10, 9.13E-11, 7.75E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.33E-46, 1.02E-31, 1.93E-25,
    9.77E-21, 4.45E-17, 2.97E-15, 1.90E-13, 4.66E-12, 1.68E-11, 4.07E-11, 7.46E-11,
    9.64E-11, 1.17E-10, 1.26E-10, 1.23E-10, 1.15E-10, 1.03E-10, 9.37E-11, 7.97E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.23E-46, 9.40E-32, 1.77E-25,
    8.81E-21, 3.94E-17, 2.58E-15, 1.61E-13, 3.89E-12, 1.41E-11, 3.46E-11, 6.56E-11,
    8.73E-11, 1.11E-10, 1.25E-10, 1.25E-10, 1.20E-10, 1.09E-10, 9.96E-11, 8.53E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.03E-46, 7.78E-32, 1.45E-25,
    7.10E-21, 3.09E-17, 1.98E-15, 1.18E-13, 2.77E-12, 1.01E-11, 2.57E-11, 5.21E-11,
    7.32E-11, 1.01E-10, 1.24E-10, 1.30E-10, 1.30E-10, 1.22E-10, 1.15E-10, 1.00E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 8.25E-47, 6.00E-32, 1.09E-25,
    5.24E-21, 2.19E-17, 1.35E-15, 7.65E-14, 1.75E-12, 6.64E-12, 1.80E-11, 4.01E-11,
    6.03E-11, 9.03E-11, 1.22E-10, 1.35E-10, 1.42E-10, 1.41E-10, 1.38E-10, 1.25E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 7.06E-47, 4.60E-32, 7.95E-26,
    3.57E-21, 1.35E-17, 7.75E-16, 4.21E-14, 1.02E-12, 4.22E-12, 1.26E-11, 3.07E-11,
    4.88E-11, 7.87E-11, 1.16E-10, 1.35E-10, 1.50E-10, 1.58E-10, 1.63E-10, 1.57E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 6.65E-47, 3.81E-32, 6.15E-26,
    2.52E-21, 8.50E-18, 4.73E-16, 2.69E-14, 6.97E-13, 2.99E-12, 9.27E-12, 2.34E-11,
    3.82E-11, 6.38E-11, 9.87E-11, 1.20E-10, 1.38E-10, 1.52E-10, 1.67E-10, 1.67E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 6.38E-47, 3.27E-32, 4.85E-26,
    1.76E-21, 5.45E-18, 3.01E-16, 1.73E-14, 4.34E-13, 1.86E-12, 5.81E-12, 1.48E-11,
    2.45E-11, 4.19E-11, 6.73E-11, 8.39E-11, 9.98E-11, 1.14E-10, 1.34E-10, 1.41E-10,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 6.30E-47, 3.03E-32, 4.08E-26,
    1.31E-21, 3.67E-18, 1.94E-16, 1.07E-14, 2.51E-13, 1.07E-12, 3.32E-12, 8.52E-12,
    1.42E-11, 2.45E-11, 4.00E-11, 5.07E-11, 6.14E-11, 7.20E-11, 8.91E-11, 9.60E-11,
    1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 1.00E-74, 6.08E-47, 2.88E-32, 3.48E-26,
    9.74E-22, 2.38E-18, 1.18E-16, 6.07E-15, 1.34E-13, 5.60E-13, 1.72E-12, 4.41E-12,
    7.32E-12, 1.27E-11, 2.10E-11, 2.68E-11, 3.28E-11, 3.90E-11, 4.96E-11, 5.44E-11
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




savez('He_6680_pec_data.npz',
      ln_ne = log_density_axis,
      ln_te = log_temperature_axis,
      exc_ln_pec = log_excitation_pec,
      rec_ln_pec = log_recombination_pec)



from midas.emission import AdasLineModel

model = AdasLineModel.build('He_6680')



print( model(1.2, 2e19, 5e18) )
print( model(6.5, 3.5e19, 8e18) )