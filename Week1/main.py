############
# Pecoraro Cyril
# Design and Analysis of Algorithms - Week 1
# Merge-sort algorithm
# August 2016
############

from Week1.functions import  merge_sort
import numpy as np

input_Array = np.loadtxt("test1.txt", dtype="int")
n = len(input_Array)

#Largest possible number of inversion
max_inversion = n*(n-1)/2

#Merge-sort
output_Array,total_inv = merge_sort(input_Array)
#print output_Array
print ("number of inversions :")
print (total_inv)


