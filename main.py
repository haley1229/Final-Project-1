#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bicycle import Bicycle


if __name__ == '__main__':
    num_bike_lists = [200, 300, 400, 500, 600, 700, 800]
    charge_rates = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
    profit_mean = []
    profit_std = []
    bike_list = []
    rate_list = []
    duration_mean = []
    duration_std = []

    # conduct simulation
    for num_bike in num_bike_lists:
        for rate in charge_rates:
            tmp_profit = []
            tmp_duration = []
            for i in range(1000):
                bike = Bicycle(num_bike=num_bike, rate=rate, seed=None)
                tmp_profit.append(bike.simulate())
                tmp_duration.append(bike.usage_duration)

            bike_list.append(num_bike)
            rate_list.append(rate)
            profit_mean.append(np.mean(tmp_profit))
            profit_std.append(np.std(tmp_profit))
            duration_mean.append(np.mean(tmp_duration))
            duration_std.append(np.std(tmp_duration))

    # create csv file
    maps = {'num_bike': bike_list,
            'rate': rate_list,
            'revenue': profit_mean,
            'revenue_std': profit_std,
            'duration': duration_mean,
            'duration_std': duration_std}
    columns = ['num_bike', 'rate', 'revenue', 'revenue_std', 'duration', 'duration_std']
    df = pd.DataFrame(maps, columns=columns)
    df.to_csv('./result.csv')

    # visualize revenue heatmap
    pivot = pd.pivot_table(df, values='revenue', index='num_bike', columns='rate')

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(pivot, ax=ax, cbar_kws={'label': 'Revenue'})
    ax.set_xlabel('Charge rate ($/minute)', fontsize=14)
    ax.set_ylabel('Number of bikes', fontsize=14)
    ax.figure.axes[-1].yaxis.label.set_size(14)
    fig.savefig('./revenue_heatmap.png', dpi=300)
    plt.show()

    # visualize bike usage heatmap
    df['mean_duration'] = df['duration'] / df['num_bike']
    pivot = pd.pivot_table(df, values='mean_duration', index='num_bike', columns='rate')

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(pivot, ax=ax, cbar_kws={'label': 'Usage rate (minutes/bike)'})
    ax.set_xlabel('Charge rate ($/minute)', fontsize=14)
    ax.set_ylabel('Number of bikes', fontsize=14)
    ax.figure.axes[-1].yaxis.label.set_size(14)
    fig.savefig('./duration_heatmap.png', dpi=300)
    plt.show()
