#!/usr/bin/env python3

class Coffee:
  def __init__(self, size, price):
    self.size = size
    self.price = price

  def tip(self):
    self.price += 1
    print("This coffee is great, here’s a tip!")
  
  @property
  def size(self):
    return self._size
  
  @size.setter
  def size(self, value):
    if value not in ["Small", "Medium", "Large"]:
      print("size must be Small, Medium, or Large")
    else:
      self._size = value