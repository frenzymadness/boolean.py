"""
Boolean Algebra.

This module defines a Boolean Algebra over the set {TRUE, FALSE} with boolean
variables and the boolean functions AND, OR, NOT. For extensive documentation
look either into the docs directory or view it online, at
https://booleanpy.readthedocs.org/en/latest/.

Copyright (c) 2009-2010 Sebastian Kraemer, basti.kr@gmail.com
Released under revised BSD license.
"""

from __future__ import absolute_import

from boolean.boolean import Algebra
from boolean.boolean import BooleanAlgebra
from boolean.boolean import BooleanDomain
from boolean.boolean import BooleanOperations
from boolean.boolean import Expression
from boolean.boolean import BaseElement
from boolean.boolean import Symbol
from boolean.boolean import Function
from boolean.boolean import DualBase

from boolean.boolean import FALSE
from boolean.boolean import TRUE
from boolean.boolean import AND
from boolean.boolean import NOT
from boolean.boolean import OR

from boolean.boolean import normalize
from boolean.boolean import symbols
from boolean.boolean import parse
