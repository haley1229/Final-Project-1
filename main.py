#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bicycle import Bicycle

if __name__ == '__main__':
    num_bike = 100
    rate = 0.02
    seed = 42
    model = Bicycle(num_bike, rate, seed)
    model.simulate()