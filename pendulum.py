# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:38:34 2020

@author: Carlesso
"""

from datetime import datetime
import pendulum

dt = datetime(2013, 3, 31, 2, 30)

t2 = pendulum.timezone('Europe/Paris')

t2.convert(dt)