''' Inset Module '''

from . import TransmutationNode

class Inset(TransmutationNode):
    ''' Create an inset from another node. '''

    def __init__(self, parent, polygon, strength):
        assert 0 < strength < 1
        super().__init__(parent, polygon)
        self.strength = strength

    def get_interior_polygon(self):
        return self._inset()

    def get_clipping_geometry(self):
        return self._inset()

    def get_rendering_geometry(self):
        return [self._inset()]

    def _inset(self):
        inset_poly = self.parent.get_interior_polygon().copy()
        inset_poly.radius *= self.strength
        return inset_poly
