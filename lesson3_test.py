#!/usr/local/bin/python
from line import Line

def run():
  test_line_init()

def test_line_init():
  flat_line = Line()
  print("Flat line initialized: %s" % (flat_line))
  constant_line = Line(constant_term=2)
  print("Constant line initialized: %s" % (constant_line))
  complex_line = Line(normal_vector=[2, 3], constant_term=4)
  print("Complex line initialized: %s" % (complex_line))

run()
