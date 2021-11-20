from pytictoc import TicToc
import numpy as np

# Compare time cost of (a+1)^2
a = np.arange(6)
t = TicToc()
t.tic()
a**2+2*a+1
t.toc()

t.tic()
(a+1)**2
t.toc()
