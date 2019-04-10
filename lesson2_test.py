#!/usr/local/bin/python
from vector import Vector

def run():
  test_vector_init()
  test_vector_plus()
  test_vector_minus()
  test_vector_scalar_multiply()
  test_magnitude()
  test_normalize()
  test_dot_product()
  test_angle()
  test_parallel_or_orthognal()
  test_component_parallel_to()
  test_component_orthogonal_to()
  test_component_parallel_and_orthogonal_to()
  test_cross_product()
  test_area()
  test_triangle()

def test_vector_init():
  vector = Vector([1, 2])
  print("Vector initialized: %s" % (vector))

def test_vector_plus():
  vector1 = Vector([8.218, -9.341])
  vector2 = Vector([-1.129, 2.111])
  result_vector = vector1.plus(vector2)
  print("%s + %s = %s" % (vector1, vector2, result_vector))

def test_vector_minus():
  vector1 = Vector([7.119, 8.215])
  vector2 = Vector([-8.223, 0.878])
  result_vector = vector1.minus(vector2)
  print("%s - %s = %s" % (vector1, vector2, result_vector))

def test_vector_scalar_multiply():
  vector = Vector([1.671, -1.012, -0.318])
  scalar = 7.41
  result_vector = vector.scalar_multiply(scalar)
  print("%s * %s = %s" % (vector, scalar, result_vector))

def test_magnitude():
  vector1 = Vector([-0.221, 7.437])
  print("Magnitude of %s = %s") % (vector1, round(vector1.magnitude(), 3))
  vector2 = Vector([8.813, -1.331, -6.247])
  print("Magnitude of %s = %s") % (vector2, round(vector2.magnitude(), 3))

def test_normalize():
  vector1 = Vector([5.581, -2.136])
  print("%s normalized = %s") % (vector1, vector1.normalize())
  vector2 = Vector([1.996, 3.108, -4.554])
  print("%s normalized = %s") % (vector2, vector2.normalize())

def test_dot_product():
  vector1 = Vector([1, 2, -1])
  vector2 = Vector([3, 1, 0])
  result = vector1.dot_product(vector2)
  print("%s dot %s = %s" % (vector1, vector2, result))
  vector3 = Vector([7.887, 4.138])
  vector4 = Vector([-8.802, 6.776])
  result = vector3.dot_product(vector4)
  print("%s dot %s = %s" % (vector3, vector4, round(result, 3)))
  vector5 = Vector([-5.955, -4.904, -1.874])
  vector6 = Vector([-4.496, -8.755, 7.103])
  result = vector5.dot_product(vector6)
  print("%s dot %s = %s" % (vector5, vector6, round(result, 3)))

def test_angle():
  vector1 = Vector([1, 2, -1])
  vector2 = Vector([3, 1, 0])
  result = vector1.angle_radians(vector2)
  print("%s angle to %s = %s radians" % (vector1, vector2, round(result, 3)))
  vector3 = Vector([3.183, -7.627])
  vector4 = Vector([-2.668, 5.319])
  result = vector3.angle_radians(vector4)
  print("%s angle to %s = %s radians" % (vector3, vector4, round(result, 3)))
  vector5 = Vector([7.35, 0.221, 5.188])
  vector6 = Vector([2.751, 8.259, 3.985])
  result = vector5.angle_degrees(vector6)
  print("%s angle to %s = %s degrees" % (vector5, vector5, round(result, 3)))

def test_parallel_or_orthognal():
  vector_pairs = [
    [Vector([-7.579, -7.88]), Vector([22.737, 23.64])],
    [Vector([-2.029, 9.97, 4.172]), Vector([-9.231, -6.639, -7.245])],
    [Vector([-2.328, -7.284, -1.214]), Vector([-1.821, 1.072, -2.94])],
    [Vector([2.118, 4.827]), Vector([0, 0])]
  ]
  for vector1, vector2 in vector_pairs:
    is_parallel = vector1.is_parallel(vector2)
    is_orthogonal = vector1.is_orthogonal(vector2)
    print("%s and %s: Parallel: %s. Orthogonal: %s" % (vector1, vector2, is_parallel, is_orthogonal))

def test_component_parallel_to():
  vector1 = Vector([3.039, 1.879])
  vector2 = Vector([0.825, 2.036])
  result = vector1.component_parallel_to(vector2)
  print("%s projected onto %s = %s" % (vector1, vector2, result))

def test_component_orthogonal_to():
  vector1 = Vector([-9.88, -3.264, -8.159])
  vector2 = Vector([-2.155, -9.353, -9.473])
  result = vector1.component_orthogonal_to(vector2)
  print("%s orthogonal to %s = %s" % (vector1, vector2, result))

def test_component_parallel_and_orthogonal_to():
  vector1 = Vector([3.009, -6.172, 3.692, -2.51])
  vector2 = Vector([6.404, -9.144, 2.759, 8.718])
  parallel = vector1.component_parallel_to(vector2)
  orthogonal = vector1.component_orthogonal_to(vector2)
  print("%s projected onto %s = %s" % (vector1, vector2, parallel))
  print("%s orthogonal to %s = %s" % (vector1, vector2, orthogonal))

def test_cross_product():
  vector1 = Vector([8.462, 7.893, -8.187])
  vector2 = Vector([6.984, -5.975, 4.778])
  result = vector1.cross_product(vector2)
  print("%s x %s = %s" % (vector1, vector2, result))

def test_area():
  vector1 = Vector([-8.987, -9.838, 5.031])
  vector2 = Vector([-4.268, -1.861, -8.866])
  result = vector1.area(vector2)
  print("Area of %s and %s = %s" % (vector1, vector2, round(result, 3)))

def test_triangle():
  vector1 = Vector([1.5, 9.547, 3.691])
  vector2 = Vector([-6.007, 0.124, 5.772])
  result = vector1.triangle(vector2)
  print("Triangle of %s and %s = %s" % (vector1, vector2, round(result, 3)))

run()
