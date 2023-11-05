import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

import option as op

buycall1 = op.Option(1, 'call', True, 2, 55)
sellcall1 = op.Option(3, 'call', False, 0.5, 65)

#sellput1 = op.Option(2, 'put', False, 4, 44)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.set(xlim=(-5, 105), ylim=(-55, 55))
ax.plot(buycall1.getNPArray(), label=buycall1.toString())  # Plot some data on the axes.
ax.plot(sellcall1.getNPArray(), label=sellcall1.toString())
ax.plot(buycall1.getNPArray() + sellcall1.getNPArray(), label="55/65 call spread")
ax.set_xlabel('Price Underlying')  # Add an x-label to the axes.    
ax.set_ylabel('P & L')  # Add a y-label to the axes.
ax.legend()  # Add a legend.
plt.show()