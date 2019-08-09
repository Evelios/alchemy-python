''' Ring module '''

import math
import atum.geometry as geo
from . import TransmutationNode

class RingInsetEndpoint(TransmutationNode):
    '''
    Create a ring with an inset polygon with the endpoints of the exterior
    polygon attached to the interior polygon
    '''

    def __init__(self, parent, polygon, strength):
        assert 0 < strength < 1
        super().__init__(parent, polygon)

        self.strength = strength
        self.interior_polygon = self._interior_polygon()

    def get_interior_polygon(self):
        return self.interior_polygon

    def get_rendering_geometry(self):
        return _connect_points(self.polygon.points,
                               self.interior_polygon.points)

    def _interior_polygon(self):
        interior = self.polygon.copy()
        interior.radius *= self.strength
        return interior

class RingInsetMidpoint(TransmutationNode):
    '''
    Create a ring with an inset polygon with the endpoints of the exterior
    polygon attached to the interior polygon
    '''

    def __init__(self, parent, polygon, strength):
        assert 0 < strength < 1
        super().__init__(parent, polygon)

        self.strength = strength
        self.interior_polygon = self._interior_polygon()

    def get_interior_polygon(self):
        return self.interior_polygon

    def get_rendering_geometry(self):
        return _connect_points(self.polygon.mid_points,
                               self.interior_polygon.mid_points)

    def _interior_polygon(self):
        interior = self.polygon.copy()
        interior.radius *= self.strength
        return interior

class RingRotatedEndpoint(TransmutationNode):
    '''
    Create a ring with an inset polygon with the endpoints of the exterior
    polygon attached to the interior polygon
    '''

    def __init__(self, parent, polygon, strength):
        assert 0 < strength < 1
        super().__init__(parent, polygon)

        self.strength = strength
        self.interior_polygon = self._interior_polygon()

    def get_interior_polygon(self):
        return self.interior_polygon

    def get_rendering_geometry(self):
        return _connect_points(self.polygon.points,
                               self.interior_polygon.mid_points)

    def _interior_polygon(self):
        interior = self.polygon.copy()
        interior.radius *= self.strength
        interior.angle -= 2*math.pi / self.polygon.n
        return interior

class RingRotatedMidpoint(TransmutationNode):
    '''
    Create a ring with an inset polygon with the endpoints of the exterior
    polygon attached to the interior polygon
    '''

    def __init__(self, parent, polygon, strength):
        assert 0 < strength < 1
        super().__init__(parent, polygon)

        self.strength = strength
        self.interior_polygon = self._interior_polygon()

    def get_interior_polygon(self):
        return self.interior_polygon

    def get_rendering_geometry(self):
        return _connect_points(self.polygon.mid_points,
                               self.interior_polygon.points)

    def _interior_polygon(self):
        interior = self.polygon.copy()
        interior.radius *= self.strength
        interior.angle += 2*math.pi / self.polygon.n
        return interior

def _connect_points(points1, points2):
    return [geo.Line2(exterior, interior)
            for exterior, interior in zip(points1, points2)]
