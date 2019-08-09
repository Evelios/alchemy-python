''' External Fork Module '''

import math
import atum.geometry as geo
from . import TransmutationNode

class ExternalFork(TransmutationNode):
    ''' Creating a forking continuation inside the current geometry '''
    def __init__(self, parent, polygon):
        super().__init__(parent, polygon)

        self.inset_radius = self.polygon.radius / self.polygon.n
        self.outer_circle = geo.Circle(self.polygon.center,
                                       self.polygon.radius)

    def get_forking_polygons(self):
        rotation = lambda i: self.polygon.rotation + i * 2*math.pi / self.polygon.n
        gen_polygon = lambda i, point: geo.RegularPolygon(
            point, self.inset_radius, rotation(i), self.polygon.n)
        return [gen_polygon(i, point)
                for i, point in enumerate(self.polygon.points)]

    def get_interior_polygon(self):
        interior_polygon = self.polygon.copy()
        interior_polygon.radius = self.polygon.radius - self.inset_radius
        return interior_polygon

    def get_rendering_geometry(self):
        forking_circles = [geo.Circle(center, self.inset_radius)
                           for center in self.polygon.points]
        return forking_circles + [self.outer_circle]

    def get_clipping_geometry(self):
        return self.polygon
