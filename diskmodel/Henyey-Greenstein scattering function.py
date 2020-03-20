#!/usr/bin/env python
# coding: utf-8

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

# Define Henyey-Greenstein scattering function


def draw_Henyey_Greenstein(g, phi):
    p = []
    for i in range(len(g)):
        p.append((1 - g[i]**2) / (1 + g[i]**2 -
                                  2 * g[i] * np.cos(phi))**(3 / 2))
    norm = [i / sum(p) for i in p]

    plt.figure(figsize=(10, 7))
    plt.xlabel(r'$\theta$[radian]', fontsize=18)
    plt.ylabel(r'p($\theta$)', fontsize=18)
    # plt.yscale('log')

    for j in range(len(norm)):
        plt.plot(phi, norm[j], label=g[j])
    plt.legend(loc=0)
    plt.show()


# Define g parameter and scattering angle
g = np.round(np.arange(-0.9, 1.0, 0.1), 2)
phi = np.linspace(0, 2 * np.pi, 1000)

if __name__ == '__main__':
    sys.exit(draw_Henyey_Greenstein(g, phi))
