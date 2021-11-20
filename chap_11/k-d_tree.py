class Node(object):

	def __init__(self, point, left=None, right=None):
		self.point = point
		self.left = left
		self.right = right

	def __repr__(self):
		isleaf = self.left is None and self.right is None
		s = repr(self.point)
		if not isleaf:
			s = "[" + s + ":"
		if self.left is not None:
			s += "\n left = " + "\n ".join(repr(self.left).split('\n'))
		if self.right is not None:
			s += "\n right = " + "\n ".join(repr(self.right).split('\n'))
		if not isleaf:
			s += "\n ]"
		return s

def kdtree(points, depth=0):
	if len(points) == 0:
		return None
	k = len(points[0]) # set the dimensionality of the k-d tree
	a = depth % k
	points = sorted

