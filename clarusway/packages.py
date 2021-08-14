# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 00:00:52 2021

@author: admin
"""

#Packages
#In order to make the modules more systematically organized, we can use packages.
earth/                          # Top-level package
      __init__.py               # Initialize the earth package
      asia/                     # Subpackage for file asia
              __init__.py
              japan.py
              mongolia.py       # A module under a subpackage
              pakistan.py
              taiwan.py
              ...
      europe/                   # Subpackage for file europe
              __init__.py
              germany.py        # A module under a subpackage
              england.py
              turkey.py
              kosovo.py
              ...
      america/                  # Subpackage for file america
              __init__.py
              canada.py
              ustates.py
              mexico.py
              peru.py           # A module under a subpackage
 
import earth.europe.kosovo  # importing with naming package, subpackage and module

earth.europe.kosovo.a_function()  # we want to access a function defined in kosovo module
#or
from earth.europe import kosovo  # importing without naming package and subpackage

kosovo.a_function()  # we want to access a function defined in kosovo module
#or
from earth.europe.kosovo import a_function  # importing without any naming

a_function()  # we use directly the function's name

#When using the syntax: "from package import item ", the item can be either a submodule (or subpackage) of the package.

#In connection with this subject, we can say that there is another and practical way
# to import packages / subpackages / modules. Consider this method : from package.subpackage import * .
# This syntax allows us to import all modules that the subpackage has.
 

