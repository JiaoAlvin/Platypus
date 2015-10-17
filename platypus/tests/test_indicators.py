# Copyright 2015 David Hadka
#
# This file is part of Platypus.
#
# Platypus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Platypus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Platypus.  If not, see <http://www.gnu.org/licenses/>.
import math
import unittest
from .test_core import createSolution
from ..indicators import generational_distance, inverted_generational_distance
from ..core import POSITIVE_INFINITY

class TestGenerationalDistance(unittest.TestCase):
    
    def test_dist(self):
        reference_set = [createSolution(0, 1), createSolution(1, 0)]
        gd = generational_distance(reference_set)
        
        set = []
        self.assertEqual(POSITIVE_INFINITY, gd(set))
        
        set = [createSolution(0.0, 1.0)]
        self.assertEqual(0.0, gd(set))
        
        set = [createSolution(0.0, 1.0), createSolution(1.0, 0.0)]
        self.assertEqual(0.0, gd(set))
        
        set = [createSolution(2.0, 2.0)]
        self.assertEqual(math.sqrt(5.0), gd(set))
        
        set = [createSolution(0.5, 0.0), createSolution(0.0, 0.5)]
        self.assertEqual(math.sqrt(0.5)/2.0, gd(set))

class TestInvertedGenerationalDistance(unittest.TestCase):
    
    def test_dist(self):
        reference_set = [createSolution(0, 1), createSolution(1, 0)]
        igd = inverted_generational_distance(reference_set)
        
        set = []
        self.assertEqual(POSITIVE_INFINITY, igd(set))
        
        set = [createSolution(0.0, 1.0)]
        self.assertEqual(math.sqrt(2.0)/2.0, igd(set))
        
        set = [createSolution(0.0, 1.0), createSolution(1.0, 0.0)]
        self.assertEqual(0.0, igd(set))
        
        set = [createSolution(2.0, 2.0)]
        self.assertEqual(math.sqrt(10.0)/2.0, igd(set))

        