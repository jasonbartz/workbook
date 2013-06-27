"""
A series of models that make up the basis for a configurable recipe

"""

class Model(object):
    """
    The base model for all of the data models.
    """

class Unit(Model):
    """
    A canonical unit
    """

class Ingredient(Model):
    """
    A canonical ingredient
    """

class Measurement(Model):
    """
    A combination of ingredients and units
    """

class Method(Model):
    """
    A pattern for doing something.
    """

class Direction(Model):
    """
    A combination of measurement and method
    """

class Recipe(Model):
    """
    A combination of Measurements and Directions.
    """