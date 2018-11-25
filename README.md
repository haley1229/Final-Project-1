# 590PR Final_Project
Fork from here to create your final project repository.

Two things are different than all the previous assignments in 590PR regarding the permissions settings:

1. Please KEEP the "All_Students" team to have Read access.  
2. Whenever you choose to, you are welcome to change your Final Project repository to public.  This will enable you to list it in your resume, website, or other portfolio.

DELETE these lines from TEMPLATE up.

TEMPLATE for your report to fill out:

# Title:

## Team Member(s):
- Jifu Zhao (jzhao59)
- Yunya Gu (yunyagu2)
- Bo Zhao (boz5)

# Monte Carlo Simulation Scenario & Purpose:
- Scenario: UIUC recently has a new shared bicycles program with VeoRide.
- Purpose: To study the best number of bicycles and charge rate for shared bicycles

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?
- Number of students who are willing to take the ride: Poisson distribution with given expectation
    - the expectation should be inversely related to charge rate
- Duration of the trip
- Whether or not the willing students can get bicycles immediately

## Hypothesis or hypotheses before running the simulation:
- We can find the best combination of number of bicycles and charge rate to maximize the profit
    - Cost for bicycles is fixed number per bicycle per day
    - Don't consider other uncertainties such as weather effects

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:
