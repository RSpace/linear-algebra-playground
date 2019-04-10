#!/usr/local/bin/python
from vector import Vector
from line import Line, MyDecimal

def run():
  test_line_init()
  test_intersection_and_same()

def test_line_init():
  flat_line = Line()
  print("Flat line initialized: %s" % (flat_line))
  constant_line = Line(constant_term=2)
  print("Constant line initialized: %s" % (constant_line))
  complex_line = Line(normal_vector=Vector([2, 3]), constant_term=4)
  print("Complex line initialized: %s" % (complex_line))

def test_intersection_and_same():
  line_pairs = [
    [
      Line(normal_vector=Vector([4.046, 2.836]), constant_term=MyDecimal('1.21')),
      Line(normal_vector=Vector([10.115, 7.09]), constant_term=MyDecimal('3.025'))
    ],
    [
      Line(normal_vector=Vector([7.204, 3.182]), constant_term=MyDecimal('8.68')),
      Line(normal_vector=Vector([8.172, 4.114]), constant_term=MyDecimal('9.883'))
    ],
    [
      Line(normal_vector=Vector([1.182, 5.562]), constant_term=MyDecimal('6.744')),
      Line(normal_vector=Vector([1.773, 8.343]), constant_term=MyDecimal('9.525'))
    ]
  ]

  for line1, line2 in line_pairs:
    if line1 == line2:
      print("Lines %s and %s are the same" % (line1, line2))
    elif line1.is_parallel_to(line2):
      print("Lines %s and %s are parallel" % (line1, line2))
    else:
      intersection = line1.intersection_with(line2)
      print("Intersection between %s and %s are at (%s, %s)" % (line1, line2, round(intersection[0], 3), round(intersection[1], 3)))

run()
