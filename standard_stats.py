
import math
from collections import defaultdict


f_coin_1 = 0.5*0.5*0.5
f_coin_2 = 0.1*0.9*0.9
def bays(p0,p1,p2):
	nom = p0 * p1
	denom = p0*(p1 + p2)
	return nom / denom
#print (bays(0.5,f_coin_1,f_coin_2))

final_prob = (0.608)**2 + (1-0.6080)**2

#print (4/5)

def maximum_likelihood(list_of_numbers):
	d = defaultdict(int)
	n = len(list_of_numbers) 
	for number in list_of_numbers:
		d[number] += 1
	return [[i, d[i] / n] for i in d]


def laplacian_estimator(list_of_numbers):
	d = defaultdict(int)
	n = len(list_of_numbers) 
	for number in list_of_numbers:
		d[number] += 1


	return [[i, (d[i] + 1) / (n + 6)] for i in d]
def mean(list_of_numbers):
	return sum(list_of_numbers) / len(list_of_numbers)


def variance(list_of_numbers):
	x = mean(list_of_numbers)
	normalized = [i - x for i in list_of_numbers]

	return sum([i**2 for i in normalized]) / len(list_of_numbers)

def standard_deviation(list_of_numbers):
	return variance(list_of_numbers)**(1/2)

numbers = [3.0, 4.0, 5.0, 7.0, 6.0]
y = [5]


def z_score(list_of_numbers, compute_z):
	meu = mean(list_of_numbers)
	print (meu)

	std = standard_deviation(list_of_numbers)
	print (std)
	return [[i, (i - meu) / std] for i in compute_z]

def median(list_of_numbers):

	list_of_numbers.sort()

	try:
		mid_num = (len(list_of_numbers) -1) / 2
		median = list_of_numbers[mid_num]
	except TypeError:
		ceil = int( math.ceil(mid_num))
		floor = int(math.floor(mid_num))
		median = (list_of_numbers[ceil] + list_of_numbers[floor]) / 2
	return median

def lower_quartile(list_of_numbers):
	list_of_numbers.sort()
	try:
		low_mid = (len(list_of_numbers) - 1) / 4
		lq = list_of_numbers[low_mid]
	except TypeError:
		ceil = int(math.ceil(low_mid))
		floor = int(math.floor(low_mid))
		lq = (list_of_numbers[ceil] + list_of_numbers[floor]) / 2
	return lq

def upper_quartile(list_of_numbers):
	list_of_numbers.sort()
	try:
		upper_mid = (len(list_of_numbers) - 1) * .75
		uq = list_of_numbers[upper_mid]
	except TypeError:
		ceil = int(math.ceil(upper_mid))
		floor = int(math.ceil(upper_mid))
		uq = (list_of_numbers[ ceil] + list_of_numbers[floor]) / 2
	return uq


def remove_outlires_quartile(list_of_numbers):
	mid = median(list_of_numbers)

	low = lower_quartile(list_of_numbers)
	high = upper_quartile(list_of_numbers)

	no_ol = [i for i in list_of_numbers if i >= low and i <= high]
	return no_ol




print (remove_outlires_quartile([-99, 33, 17, 13, 1489]))

