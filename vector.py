import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format([round(x, 3) for x in self.coordinates])


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, other_vector):
        result_coordinates = []
        for index, coordinate in enumerate(self.coordinates, start=0):
            result_coordinates.append(coordinate + other_vector.coordinates[index])
        return Vector(result_coordinates)

    def minus(self, other_vector):
        result_coordinates = []
        for index, coordinate in enumerate(self.coordinates, start=0):
            result_coordinates.append(coordinate - other_vector.coordinates[index])
        return Vector(result_coordinates)

    def scalar_multiply(self, scalar):
        result_coordinates = []
        for index, coordinate in enumerate(self.coordinates, start=0):
            result_coordinates.append(coordinate * Decimal(scalar))
        return Vector(result_coordinates)

    def magnitude(self):
        squared_coordinates = [x**2 for x in self.coordinates]
        summed_coordinates = sum(squared_coordinates)
        square_root = math.sqrt(summed_coordinates)
        return Decimal(square_root)

    def normalize(self):
        normalizer = Decimal('1.0')/self.magnitude()
        unit_vector = self.scalar_multiply(normalizer)
        return unit_vector

    def dot_product(self, other_vector):
        multiplied_coordinates = [x*y for x, y in zip(self.coordinates, other_vector.coordinates)]
        return sum(multiplied_coordinates)

    def angle_radians(self, other_vector):
        dp = self.dot_product(other_vector)
        step = dp/(self.magnitude() * other_vector.magnitude())
        return math.acos(step)

    def angle_degrees(self, other_vector):
        radians = self.angle_radians(other_vector)
        return radians * (180/math.pi)
