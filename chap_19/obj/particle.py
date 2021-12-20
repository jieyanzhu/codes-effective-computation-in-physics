# particle.py
from scipy import constants
from math import sqrt

def add_is_particle(cls):
    cls.is_particle = True
    return cls

def add_distance(cls):
    def distance(self, other):
        d2 = 0.0
        for axis in ['x', 'y', 'z']:
            d2 += (self.r[axis] - other.r[axis])**2
        d = sqrt(d2)
        return d
    cls.distance = distance
    return cls

class IsParticle(type):
    pass

@add_is_particle
@add_distance
class Particle(object):
    """A particle is a consitituent unit of the universe.

    Attributes
    ----------
    c: charge in units of [e]
    m: mass in units of [kg]
    r: position in units of [meters]
    """
    
    roar = "I am a particle!"
    
    def __init__(self, charge, mass, position):
        """Initializes the particle with default values for 
        charge c, mass m, and position r.
        """
        self.c = charge
        self.m = mass
        self.r = position

    def hear_me(self):
        my_roar = self.roar + (
             "\n My charge is:     " + str(self.c) +
             "\n My mass is:       " + str(self.m) +
             "\n My x position is: " + str(self.r['x']) +
             "\n My y position is: " + str(self.r['y']) +
             "\n My z position is: " + str(self.r['z']))
        print(my_roar)
    
    def delta_x_min(self, delta_p_x):
        hbar = constants.hbar
        delx_min = hbar / (2.0 * delta_p_x)
        return delx_min
    
    @staticmethod
    def possible_flavors():
        return ["up", "down", "top", "bottom", "strange", "charm"]

def Proton():
    return Particle(constants.e, constants.m_p, 0)

def Electron():
    return Particle(-constants.e, constants.m_e, 0)
