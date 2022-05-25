import rules
from importlib import reload


class ShapeGenerator:
    def __init__(self):
        reload(rules)
        self.rules = rules.Rules()
        self.params = dict()
        self.params['bench'] = [None]*50
        self.params['chair'] = [None]*50
        self.params['sofa'] = [None]*50
        self.params['table'] = [None]*50

        self.params['bench'][1] = [193, 0.5, 24, 22, 5, 0]
        self.params['bench'][38] = [155, 0.5, 10, 14, 4, 0]
        self.params['bench'][44] = [205, 0.55, 10, 14, 13, 1]

    def get_image(self, shape_name: str, index: int):
        '''
        :param shape_name: shape category
        :param index: shape index
        :return: A 512X512 PIL image
        '''
        param_vector = self.params[shape_name][index]
        image = self.rules.make_shape(shape_name, param_vector)
        return image
