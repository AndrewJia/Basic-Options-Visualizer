import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class Option:
    def __init__(self, id, optype, buying, cost, strike):
        self.id = id
        self.optype = optype
        self.buying = buying
        self.cost = cost
        self.strike = strike

    def getNPArray(self):
        arr = []
        for i in range(0, 100):
            arr.append(self.valueAt(i))
        print(arr)
        return np.array(arr)

    # find intrinsic value + cost of this option at given underlying value
    # helper for getNPArray
    def valueAt(self, underlying):
        total = -self.cost
        
        if self.optype == 'call':
            total += max(0, underlying - self.strike)
        else:
            total += max(0, self.strike - underlying)

        if self.buying == False:
            total *= -1
        
        return total

    def toString(self):
        if self.buying:
            return f"buy {self.strike} {self.optype} for {self.cost}"
        #selling
        return f"sell {self.strike} {self.optype} for {self.cost}"
        
