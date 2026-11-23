#!/usr/bin/env python3
"""One Letter: Coffee or Tea - entry A (coffee).

A for coffee: the builder's fuel. One letter, nothing else.
"""
import os

here = os.path.dirname(os.path.abspath(__file__))
print(open(os.path.join(here, "entry.txt")).read().strip())
