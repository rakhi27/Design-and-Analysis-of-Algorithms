############
# Pecoraro Cyril
# Design and Analysis of Algorithms - Week 2
# Quicksort algorithm
# August 2016
############

from Week2.functions import quicksort
import numpy as np


#input
input_Array = np.loadtxt("quicksort.txt", dtype="int")

#QuickSort

output_Array, total_comparisons = quicksort(input_Array, len(input_Array), "first")
#output_Array, total_comparisons = quicksort(input_Array, len(input_Array), "last")
#output_Array, total_comparisons = quicksort(input_Array, len(input_Array), "medthree")
print (output_Array)
print ("Number of comparisons :" , total_comparisons)