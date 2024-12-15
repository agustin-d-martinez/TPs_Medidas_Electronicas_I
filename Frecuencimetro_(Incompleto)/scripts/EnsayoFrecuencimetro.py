# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:59:27 2024

@organization: UTN FRBA
@department: Sistemas de Control - R5052
@title: Guia de Ejercicios 2024 - TP N°2 - Ejercicio N°4
@subtitle: Consigna A) - Verificacion de funcion transferencia
@author: Tomas Agustin Albanesi

@description:
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.signal as dsp

plt.close("all")

# Importacion de datos de trazos
data_tono1 = np.genfromtxt('F0001CH1.CSV', delimiter=',')