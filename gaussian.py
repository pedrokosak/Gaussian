from typing import Counter
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import randint

def GetRandonValue(minValue,maxValue,qty):
    values = []
    for i in range(qty):
        values.append(randint(minValue, maxValue))
    return(sum(values))

def GetCountValues(values):
    c = []
    for val in set(values):
        c.append(values.count(val))
    return c

times = int(input("how many times?"))
qty = int(input("how many random values?"))
maxValue = int(input("what is the maximum value of these values?"))
minValue = int(input("what is the minimum value of these values?"))
values = []
for i in range(times):
    values.append(int(GetRandonValue(minValue,maxValue,qty))) 
values.sort()
distinct = list(set(values))
distinct.sort()
GetCountValues(values)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(distinct, GetCountValues(values))  # Plot some data on the axes.
plt.show()

