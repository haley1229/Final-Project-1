#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import scipy as sp

maps = {0.02: 0.01,
        0.03: 0.008,
        0.04: 0.006
        }


class Bicycle(object):
    """ class to simulate the usage of shared bicycles """
    def __init__(self, num_bike, rate, seed=None):
        """
        :param num_bike:
        :param rate:
        :param seed:
        """
        random.seed(seed)
        np.random.seed(seed)
        self.num_bike = num_bike
        self.rate = rate
        self.free_student = 20000
        self.occupy_student = 0
        self.free_bike = num_bike
        self.occupy_bike = 0
        self.percent = maps[rate]
        self.cost = 1 * self.num_bike

    def simulate(self):
        pass

    def sample_student(self):
        pass

    def sample_duration(self):
        pass

    def sample_bicycle(self):
        pass


