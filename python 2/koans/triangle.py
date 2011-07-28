#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if _is_invalid_triangle(a,b,c):
        raise TriangleError
    
    if a == b == c:
        return 'equilateral'
    elif a == b or b == c or c==a:
        return 'isosceles'
    elif a != b and b != c and c != a:
        return 'scalene'

def _is_invalid_triangle(*values):
    values = list(values)
    values.sort()
    if values[0] + values[1] > values[2]:
        return False
    return True

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
