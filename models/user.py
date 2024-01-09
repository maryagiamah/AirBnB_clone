#!/usr/bin/python3
"""Contains User Model"""


from models.base_model import BaseModel


class User(BaseModel):
  """ User Model"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
