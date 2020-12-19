#Project 2: The change of species richness in forest under fire disturbance
#import all libraries I need
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Use pandas to import .csv file and make it into dataframe
df = pd.read_csv("species_richness.csv")
# Create two list
before_burn = df['before_burn'].values.tolist()
after_burn = df['after_burn'].values.tolist()
# Define Function that make bar graph to see data difference
def graph(before_burn,after_burn):
    divisions = [i for i in range(1,len(before_burn)+1)] # Make divsions and index that will change with length of inputdata and default width
    index = np.arange(len(before_burn))
    width = 0.30
# The characters of bar graph
    plt.bar(index, before_burn, width, color = 'blue', label = 'before burn')
    plt.bar(index+width, after_burn, width, color = 'green', label = 'after burn')
    plt.ylabel("species_richness")
    plt.xlabel("plot_number")
    plt.xticks(index+ width/2, divisions)
    plt.legend(loc='best')
    return(plt.show())

graph(before_burn,after_burn)

# pair t-test for species richness in unburn and burn forest
def ttest(before_burn,after_burn):
    import scipy.stats as stats
    t,p = stats.ttest_rel(before_burn, after_burn)
    return (t,p)
# the T-test result and conclusion
T_test_result = ttest(before_burn,after_burn)
print ("statistic and pvalue:",T_test_result)
pvalue = (T_test_result[1])
if pvalue <= 0.05:
    print ("Null hypothesis is rejected. Species richness between burn and unburn forest is significantly different")
else:
    print ("Null hypothesis is accepted. Species richness between burn and unburn forest is not significantly different")
