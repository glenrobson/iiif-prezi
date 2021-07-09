
from iiif_prezi.prezi3 import Manifest as ManifestSkeleton
from iiif_prezi.prezi3 import Canvas as CanvasSkeleton

# or monkey patch existing classes 

# Maybe add Skeleton or Properties to generated classes 

class Manifest(ManifestSkeleton):
    pass


class Canvas(CanvasSkeleton):
    def __init__(self, id=None, label=None):
        # if no id set use a default
        if not id:
            id = 'http://example.com/canvas/1'

        super().__init__(id=id,type="Canvas") 

        self.id = id
        if label:
            self.label = { 'en': label }
