import parameter
from shape import Shape


class Chair(Shape):
    def __init__(self):
        super(Chair, self).__init__()

    def setup_parameter_vector(self):
        """
        Define the parameter vector in this function
        Use the following format when adding element to the parameter vector
        self.add_parameter_vector_element
            (name_of_parameter,             # String, specifying name of the parameter
            type_of_parameter,              # 's', 'i' or 'b', for scalar, integer or binary respectively
            minimum_allowable_value,        # Ignore if binary parameter
            maximum_allowable_value)        # Ignore if binary parameter
        """
        self.add_parameter_vector_element('height', 's', 0.293, 0.43)   
        self.add_parameter_vector_element('leg_height', 's', 0.14, 0.5)    # Element at index 1
        self.add_parameter_vector_element('leg_width', 's', 0.01, 0.5)     # Element at index 2
        self.add_parameter_vector_element('seat_height', 's', 0.01, 0.5) 
        self.add_parameter_vector_element('seat_width', 's', 0.2, 0.9)
        self.add_parameter_vector_element('arc_radius', 's', 0.01, 0.5)

    def procedure(self, param_vector: parameter.ParameterVector):
        # Implement your procedure for the chair class in this function
        # Retrieve the parameter values
        height = param_vector.get_parameter('height')
        leg_height = param_vector.get_parameter('leg_height')
        leg_width = param_vector.get_parameter('leg_width')
        seat_height = param_vector.get_parameter('seat_height')
        seat_width = param_vector.get_parameter('seat_width')
        arc_radius = param_vector.get_parameter('arc_radius')

        # draw the legs
        xy = (0.01, 0.75 - height / 2, 0.01 + leg_width, 0.75 + height / 2)
        self.rectangle(xy)
        xy = (seat_width - leg_width, 0.75 - height / 2, seat_width, 0.75 + height / 2)
        self.rectangle(xy)

        # draw the seat
        seat_location = 0.5 - height / 2 + (height - leg_height)
        xy = (0.01, seat_location - seat_height / 2, seat_width, seat_location + seat_height / 2)
        self.rectangle(xy)

        ## draw curve top
        ## TODO: fix this..
        xy = (0.01, leg_height+seat_height, seat_width, leg_height+seat_height+arc_radius)
        self.chord(xy, 180, 360)
        return

    def specify_parameter_vectors(self):
        """
        Specify the parameter vectors in this function
        Use the following format when specifying a parameter vector
        self.assign_parameter_vector_to_shape
            (index,                         # Integer, specifying the index of the shape
            parameter_vector)               # List of elements, representing the parameter vector
        """
        self.assign_parameter_vector_to_shape(3, [0.43, 0.35, 0.045, 0.4, 0.4, 0.5])
        self.assign_parameter_vector_to_shape(4, [0.43, 0.3, 0.15, 0.4, 0.7, 0.5])
        return
