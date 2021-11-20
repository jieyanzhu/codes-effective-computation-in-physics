import numpy as np
from pytictoc import TicToc

a = np.arange(9)
a.shape = (3,3)
m = (a < 5)
m_where = np.where(a < 5)
t = TicToc()

t.tic()
a[m]
t.toc()

t.tic()
a[m_where]
t.toc()
