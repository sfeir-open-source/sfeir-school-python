# -*- coding: utf-8 -*-

"""
To-Do application
"""

class MyContextManager(object):
  def __enter__(self):
    print("Before")

  def __exit__(
    self,
    type,
    value,
    traceback
  ):
    print("After")

with MyContextManager():
  print("func")


