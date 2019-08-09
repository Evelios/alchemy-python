''' Spyglass Module '''

import math
import atum.geometry as geo
from . import TransmutationNode

class Spyglass(TransmutationNode):
    ''' A spyglass like interior continuation simiar to the inset class '''
    def __init__(self, parent, polygon, strength):
        super().__init__(parent, polygon)

        self.strength = strength
        self.angle_offset = strength * (math.pi - 2*math.pi / polygon.n)

    def get_interior_polygon(self):
        return self._interior()

    def get_clipping_geometry(self):
        return self.polygon

    def get_rendering_geometry(self):
        return [geo.Line2(interior, exterior) for exterior, interior in
                zip(self.polygon.points, self._interior().points)]

    def _interior(self):
        # TODO Implement both clockwise and counterclockwise directionality
        interior_poly = self.polygon.copy()
        interior_poly.angle += self.strength * 2*math.pi / interior_poly.n
        interior_poly.radius *= 1 - self.strength
