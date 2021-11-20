import numpy as np
from matplotlib import pyplot as plt
from multiprocessing import Pool
import time

def timestep_i(args):
	"""Computes the next position and velocity for the ith mass
	"""
	i, x0, v0, G, m, dt = args
	a_i0 = a(i, x0, G, m)
	v_i1 = a_i0 * dt + v0[i]
	x_i1 = a_i0 * dt**2 + v0[i] * dt + x0[i]
	return i, x_i1, v_i1

def a(i, x, G, m):
	"""The acceleration of the ith mass."""
	x_i = x[i]
	x_j = remove_i(x, i)
	m_j = remove_i(m, i)
	diff = x_j - x_i
	mag3 = np.sum(diff**2, axis=1)**1.5
	result = G*np.sum(diff * (m_j / mag3)[:, np.newaxis], axis=0)
	return result

def remove_i(x, i):
	"""Drops the ith element of an array."""
	shape = (x.shape[0]-1,) + x.shape[1:]
	y = np.empty(shape, dtype=float)
	y[:i] = x[:i]
	y[i:] = x[i+1:]
	return y

def timestep(x0, v0, G, m, dt, pool):
	"""Computes the next position and velocity for all masses given
	initial conditions and a time step size.
	"""
	N = len(x0)
	tasks = [(i, x0, v0, G, m, dt) for i in range(N)]
	results = pool.map(timestep_i, tasks)
	x1 = np.empty(x0.shape, dtype=float)
	v1 = np.empty(v0.shape, dtype=float)
	for i, x_1, v_1 in results:
		x1[i] = x_1
		v1[i] = v_1
	return x1, v1

def initial_cond(N, D):
	"""Generates initial conditions for N unity masses at rest
	starting at random positions in D-dimensional space."""
	x0 = np.random.rand(N, D)
	v0 = np.zeros((N, D), dtype=float)
	m = np.ones(N, dtype=float)
	return x0, v0, m

def simulate(P, N, D, S, G, dt):
	x0, v0, m = initial_cond(N, D)
	pool = Pool(P)
	for s in range(S):
		x1, v1 = timestep(x0, v0, G, m, dt, pool)
		x0, v0 = x1, v1
if __name__ == '__main__':
	Ps = [1, 2, 4, 8, 16]
	runtimes = []
	for P in Ps:
		start = time.time()
		simulate(P, 256, 3, 100, 1.0, 1.0e-3)
		stop = time.time()
		runtimes.append(stop - start)

	plt.figure(figsize=(5,5))
	plt.plot(np.array(Ps), runtimes[0]/np.array(runtimes), '.-')
	plt.show()
