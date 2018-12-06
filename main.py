#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt
from bicycle import Bicycle

if __name__ == '__main__':
    num_bike = 100
    rate = 0.02
    seed = 42
    model = Bicycle(num_bike, rate, seed)
    model.simulate()

    # set charge rate as 0.01:
    profit = []
    for i in range(100):
        bike = Bicycle(num_bike=200, rate=0.01, seed=None)
        profit.append(bike.simulate())

    # visualization
    fig, ax = plt.subplots()
    sns.distplot(profit, ax=ax)
    plt.show()

    # set charge rate as 0.02:
    profit = []
    for i in range(100):
        bike = Bicycle(num_bike=200, rate=0.02, seed=None)
        profit.append(bike.simulate())

    # visualization
    fig, ax = plt.subplots()
    sns.distplot(profit, ax=ax)
    plt.show()

    # set charge rate as 0.03:
    profit = []
    for i in range(100):
        bike = Bicycle(num_bike=200, rate=0.03, seed=None)
        profit.append(bike.simulate())

    # visualization
    fig, ax = plt.subplots()
    sns.distplot(profit, ax=ax)
    plt.show()

    # set charge rate as 0.04:
    profit = []
    for i in range(100):
        bike = Bicycle(num_bike=200, rate=0.04, seed=None)
        profit.append(bike.simulate())

    # visualization
    fig, ax = plt.subplots()
    sns.distplot(profit, ax=ax)
    plt.show()

    # set charge rate as 0.05:
    profit = []
    for i in range(100):
        bike = Bicycle(num_bike=200, rate=0.05, seed=None)
        profit.append(bike.simulate())

    # visualization
    fig, ax = plt.subplots()
    sns.distplot(profit, ax=ax)
    plt.show()

    # set charge rate as 0.06:
    profit = []
    for i in range(100):
        bike = Bicycle(num_bike=200, rate=0.06, seed=None)
        profit.append(bike.simulate())

    # visualization
    fig, ax = plt.subplots()
    sns.distplot(profit, ax=ax)
    plt.show()



