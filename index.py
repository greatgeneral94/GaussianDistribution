import numpy
import math
import matplotlib.pyplot as plt
from random import randrange
# Algorithm:

# Construct a sum array S[] from the given probability array P[], where S[i] holds the sum of all P[j] for 0 <= j <= i.
# Generate a random integer from 1 to 100 and check where it lies in S[].
# Based on the comparison result, return the corresponding element from the input array.
def GaussianDistribution():
    size = 100000
    mean_str = input("Enter Mean: ")
    deviation_str = input("Enter Deviation: ")
    mean = float(mean_str)
    deviation = float(deviation_str)
    x = numpy.random.normal(mean, deviation, size) #generate random numbers based on Gaussian destribution
    p = [None] * size #create array. this array has all the same value.
    for i in range(size):
        p[i] = 100/size
    # construct a sum list from the given probabilities
    prob_sum = [None] * size
    # `prob_sum[i]` holds sum of all `p[j]` for `0 <= j <=i`
    prob_sum[0] = p[0]
    for i in range(1, size):
        prob_sum[i] = prob_sum[i-1]+p[i]
    # generate a random integer from 1 to 100
    # and check where it lies in `prob_sum`
    r = randrange(0, 100)
    result = 0
    # based on the comparison result, return the corresponding
    # element from the input list
    if r <= prob_sum[0]:
        result = x[0]
 
    for j in range(1, size):
        if prob_sum[j - 1] < r <= prob_sum[j]:
            result = x[j]
    print(result)
    if(result>mean):
        print(math.floor((result-mean)/deviation))
    else:
        print((math.ceil((result-mean)/deviation))*(-1))
    plt.hist(x, 100)
    plt.show()

GaussianDistribution()