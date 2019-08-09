''' Inscribe Module '''

import math
from . import TransmutationNode

class Inscribe(TransmutationNode):
    ''' Inscribe a regular polygon inside another regular polygon '''
    def __init__(self, parent, polygon):
        super().__init__(self, parent, polygon)

    def get_interior_polygon(self):
        return self._inscribe()

    def get_rendering_geometry(self):
        return [self._inscribe()]

    def get_clipping_geometry(self):
        return self.polygon

    def _inscribe(self):
        inscribed_poly = self.polygon.copy()
        inscribed_poly.radius *= math.cos(math.pi / inscribed_poly.n)
        inscribed_poly.rotation *= math.pi / inscribed_poly.n

        return inscribed_poly
