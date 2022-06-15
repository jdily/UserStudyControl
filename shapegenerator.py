import rules
from importlib import reload


class ShapeGenerator:
    def __init__(self):
        reload(rules)
        self.rules = rules.Rules()
        self.params = dict()
        self.params['bench'] = [None]*50
        self.params['chair'] = [None]*50

        # As example, parameter vectors for the bench class are specified between here
        self.params['bench'][1] = [0.375, 0.19, 0.045, 0.04, 5, 0]
        self.params['bench'][38] = [0.3, 0.145, 0.02, 0.025, 4, 0]
        self.params['bench'][44] = [0.4, 0.22, 0.02, 0.03, 12, 1]
        # and here

        # Specify your own parameter vectors for the chair class between here
        # and here

    def get_image(self, shape_name: str, index: int):
        '''
        :param shape_name: shape category
        :param index: shape index
        :return: A 512X512 PIL image
        '''
        param_vector = self.params[shape_name][index]
        image = self.rules.make_shape(shape_name, param_vector)
        return image
