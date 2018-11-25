# 590PR Final_Project

# Title: Shared Bicycle Monte Carlo Simulation

## Team Member(s):
- Jifu Zhao (jzhao59)
- Yunya Gu (yunyagu2)
- Bo Zhao (boz5)

# Monte Carlo Simulation Scenario & Purpose:
- Scenario: UIUC recently has a new shared bicycles program with [VeoRide](https://www.veoride.com/).
- Purpose: To study the best number of bicycles and charge rate for shared bicycles

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?
- Number of students who are willing to take the ride: Poisson distribution with given expectation
    - the expectation should be inversely related to charge rate
- Duration of the trip
- Whether or not the willing students can get bicycles immediately

- Charge rate: $0.01/min, $0.02/min, $0.03/min, $0.04/min, $0.05/min
- Number of bicycles: 50, 100, 150, 200, 250, 300
- Percentage of students who are willing to take the bicycle: 1%, 0.9%, 0.8%, 0.7%, 0.6%
- Assume there are 20,000 students in total

## Hypothesis or hypotheses before running the simulation:
- We can find the best combination of number of bicycles and charge rate to maximize the profit
    - Cost for bicycles is fixed number per bicycle per day
    - Don't consider other uncertainties such as weather effects

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
