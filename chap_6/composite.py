# composite.py
from particle import Particle

class CompositeParticle(Particle):
    
    def __init__(self, parts):
        self.constituents = parts
