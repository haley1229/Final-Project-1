#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import heapq
import numpy as np


# create a dictionary, with the keys indicating the charge rate, the values indicating
# the percentage of students who are willing to take the bicycle.
# We set the charge rate to range from 0.01 to 0.06, and the percentage of students to range
# from 0.001 to 0.005, accordingly.
maps = {0.01: 0.0010,
        0.02: 0.0009,
        0.03: 0.0008,
        0.04: 0.0007,
        0.05: 0.0006,
        0.06: 0.0005
        }


class Bicycle(object):
    """
    class to simulate the usage of shared bicycles
    it contains four functions:  simulate(), sample_student(), sample_duration(),
    and sample_bicycle().
    """
    def __init__(self, num_bike, rate, seed=None):
        """
        :param num_bike: number of bikes to be deployed
        :param rate: charge rate for bike usage ($ per minute)
        :param seed: random seed
        """

        random.seed(seed)  # set random seed
        np.random.seed(seed)  # set random seed
        self.num_bike = num_bike  # total number of bikes
        self.rate = rate  # charge rate for bike usage ($ per minute)
        self.free_student = 50000  # total number of students
        self.free_bike = num_bike  # available number of bikes
        self.percent = maps[rate]  # percentage of students who are willing to take bikes
        self.cost = 2.0 * self.num_bike  # fixed cost for all bikes per day
        self.bike_usage_prob = 0.5  # by average, probability of the bikes to be actually used
        self.usage_duration = 0  # total duration of the bike usage


    def simulate(self):
        """
        We use the time range from 9:00 am to 6:00 pm, with intervals of 5 minutes,
        so there will be total of 540 minutes that we track.
        """

        # set a priority queue to store the number of free students and free bicycles.
        pq = []
        for t in range(0, 540, 5):
            while len(pq) and pq[0] <= t:
                heapq.heappop(pq)
                self.free_student += 1
                self.free_bike += 1

            # excepted number of students to ride a bicycle.
            mean = self.free_student * self.percent

            # to identify the real numbers of students that can take the bicycle, choose from the
            # minimum of excepted students and number of free bicycles.
            willing_student = min(self.sample_student(mean), self.free_bike)
            usage_student = self.sample_bicycle(willing_student)

            # when a student rides a bicycle, the total number of free students declilnes.
            self.free_student -= usage_student

            # when a student rides a bicycle, the total number of free bicycles declilnes.
            self.free_bike -= usage_student
            usage_time = self.sample_duration(usage_student)
            self.usage_duration += np.sum(usage_time)

            # push the total usage time of this student into the list of usage time.
            for tmp_t in usage_time:
                heapq.heappush(pq, tmp_t + t)

        # to calculate the profit, product the usage time and charge rate and deduct the cost.
        return self.usage_duration * self.rate - self.cost
            

    def sample_student(self, mean):
        """
        This function samples the number of students who are willing to take the bike,
        assuming it follows poisson distribution.

        :param mean: mean value for Poisson distribution
        """
        res = np.random.poisson(mean)

        return res


    def sample_duration(self, size):
        """
        This function samples the duration of trips , we set the usage time from 5 to 30 minmutes,
        with 5 minutes as an interval, and set probability of this duration as
        [0.3, 0.3, 0.2, 0.1, 0.05, 0.05] accordingly.

        :param size: number of data to be samples
        """
        times = [5, 10, 15, 20, 25, 30]
        prob = [0.3, 0.3, 0.2, 0.1, 0.05, 0.05]
        res = np.random.choice(times, size=size, replace=True, p=prob)
        
        return res


    def sample_bicycle(self, n):
        """
        This function samples the actually used bicycles with binomial distribution

        :param n: total number of bikes to be used
        """
        res = np.random.binomial(n, p=self.bike_usage_prob)

        return res
