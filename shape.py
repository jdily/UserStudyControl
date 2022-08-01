from drawer import Drawer
from PIL import Image, ImageOps
import parameter
from importlib import reload


class Shape:
    def __init__(self):
        reload(parameter)
        self.param_vector_info = parameter.ParameterVectorInfo()
        self.param_vectors = [None]*50
        self.drawer = None
        self.images = []
        self.setup_parameter_vector()
        self.specify_parameter_vectors()
        self.__make_shapes()

    def add_parameter_vector_element(self, param_name: str, param_type: str, min_value=None, max_value=None):
        self.param_vector_info.add_element(param_name, param_type, min_value, max_value)

    def assign_parameter_vector_to_shape(self, index: int, param_vector: list):
        self.param_vectors[index] = parameter.ParameterVector(self.param_vector_info, param_vector)

    def __make_shapes(self):
        for i in range(len(self.param_vectors)):
            image = Image.new('L', (512, 512))
            if isinstance(self.param_vectors[i], parameter.ParameterVector) and self.param_vectors[i].is_valid():
                self.drawer = Drawer(image)
                self.procedure(self.param_vectors[i])
                image = ImageOps.invert(image)
            else:
                image = ImageOps.invert(image)
            self.images.append(image)

    def arc(self, xy, start, end):
        self.drawer.arc(xy, start, end)

    def chord(self, xy, start, end):
        self.drawer.chord(xy, start, end)

    def ellipse(self, xy):
        self.drawer.ellipse(xy)

    def line(self, xy):
        self.drawer.line(xy)

    def pieslice(self, xy, start, end):
        self.drawer.pieslice(xy, start, end)

    def point(self, xy):
        self.drawer.point(xy)

    def regular_polygon(self, bounding_circle, n_sides, rotation=0):
        self.drawer.regular_polygon(bounding_circle, n_sides, rotation=rotation)

    def rectangle(self, xy):
        self.drawer.rectangle(xy)

    def rounded_rectangle(self, xy, radius=0):
        self.drawer.rounded_rectangle(xy, radius=radius)

    def get_image(self, index: int):
        return self.images[index]

    def setup_parameter_vector(self):
        raise NotImplementedError()

    def procedure(self, param_vector: parameter.ParameterVector):
        raise NotImplementedError()

    def specify_parameter_vectors(self):
        raise NotImplementedError()
