import matplotlib.pyplot as plt

import numpy as np
import pprint

x = np.arange(2,50)

y = (2**(x)-1)/(2**(x+1))  + (2**(x)-2)/(2**(x+1)) 

pprint.pprint(y)

ans = 1
for i in range(10):
    ans = ans * y[i]
print(ans)

plt.plot(x,y)
plt.savefig("./figures/1.png")
