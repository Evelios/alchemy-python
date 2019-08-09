''' This is the abstract base code for alchemy transmutation code '''

from abc import ABC, abstractmethod

class TransmutationTree(ABC):
    '''
    This is an abstract tree structure which contains the code to generate
    a tree of TransmutationNodes.
    '''

    def __init__(self, parent):
        pass

    def generate(self):
        pass

class TransmutationNode(ABC):
    ''' This is an abstract transmutation geometry node base class. '''
    def __init__(self, parent, polygon):
        self.parent = parent
        self.polygon = polygon
        self.children = []

        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def get_forking_polygons(self):
        ''' Get all the forking nodes that exist off this current node. '''
        return []

    def get_interior_polygon(self):
        ''' Get the interior continuation object for this node. '''
        return None

    @abstractmethod
    def get_rendering_geometry(self):
        ''' Get the rendering geometry for this node. '''
        pass

    def get_clipping_geometry(self):
        ''' Get the clipping geometry for this node. '''
        return self.polygon
