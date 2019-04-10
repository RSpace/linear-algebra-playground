import math
from decimal import Decimal, getcontext
import itertools

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

    def __iter__(self):
        return iter([x for x in self.coordinates])

    def __getitem__(self, index):
        return self.coordinates[index]

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

    def is_parallel(self, other_vector):
        if self.is_zero_vector() or other_vector.is_zero_vector():
            return True
        divided_coordinates = [round(x/y, 3) for x, y in zip(self.coordinates, other_vector.coordinates)]
        return all(x==divided_coordinates[0] for x in divided_coordinates)

    def is_orthogonal(self, other_vector):
        return round(self.dot_product(other_vector), 3) == 0

    def is_zero_vector(self):
        return all(x==0 for x in self.coordinates)

    def component_parallel_to(self, other_vector):
        unit_vector = other_vector.normalize()
        weight = self.dot_product(unit_vector)
        return unit_vector.scalar_multiply(weight)

    def component_orthogonal_to(self, other_vector):
        projection = self.component_parallel_to(other_vector)
        return self.minus(projection)

    def cross_product(self, other_vector):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other_vector.coordinates
        x = y1*z2 - y2*z1
        y = -(x1*z2 - x2*z1)
        z = x1*y2 - x2*y1
        return Vector([x, y, z])

    def area(self, other_vector):
        cross_vector = self.cross_product(other_vector)
        return cross_vector.magnitude()

    def triangle(self, other_vector):
        return self.area(other_vector) / Decimal("2.0")
