"""
Insertion sort works the way many people sort a hand of
playing cards. We start with an empty left hand and the cards face down on the
table. We then remove one card at a time from the table and insert it into the
correct position in the left hand. To find the correct position for a card, we compare
it with each of the cards already in the hand, from right to left

"""

import random


def insertion_sort(arr):
	n = len(arr)
	for i in range(1, n):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr
	

if __name__ == '__main__':
	temp = [random.randint(0, 100) for _ in range(20)]
	print("Unsorted Array:", temp)
	print("Sorted Array:", insertion_sort(temp))
