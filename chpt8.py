
# 1. Call a different function from the stastics module

import statistics as stat

nums = [10, 3, 4, 8,8,  99, 112, 35, 60, 30, 77, 25]
print(stat.mode(nums))

# module named subed, w/ function that takes number as param, returns number cubed. import call func from another module

#cubed module 
#def f(num):
    #num = num**3
    #return num


import cubed

cubed.f(2)
print(cubed.f(5))
