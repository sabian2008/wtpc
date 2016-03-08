""" 
Print polynomial, it's derivative and local min/max
"""

# Load libraries
import numpy as np
import matplotlib.pyplot as plt

# Load polynomial, calculate derivative
p = np.poly1d([1,2,-4,4])
dot_p = p.deriv()

# -------- Graph --------------
x = np.linspace(-10,10,200)

# Generate figure
fig = plt.figure()
fig.suptitle("Polinomio  y derivada", fontsize="16")

# Plot, labelling, grid
plt.plot(x,p(x), "b", label="Polinomio")
plt.plot(x, dot_p(x), "r--", label="Derivada")
plt.xlabel(r"$x$", fontsize="12")
plt.ylabel(r"$y$", fontsize="12")
plt.grid(True)
plt.legend(loc="upper left")
plt.show()

# Save function evaluation
handler = open("resultados.txt", "w")
output = np.c_[x,p(x)]
np.savetxt(handler, output, fmt="%f", delimiter='\t', header="x\t\t f(x)")
handler.close()	
