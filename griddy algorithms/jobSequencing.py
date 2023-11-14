#Job Sequencing
def printJobScheduling(arr, time):

	# length of array
	n = len(arr)

	# Sort all jobs according to
	# decreasing order of profit
	for i in range(n):
		for j in range(n - 1 - i):
			if int(arr[j][2]) < int(arr[j + 1][2]):
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	# To keep track of free time slots
	result = [False] * time

	# To store result (Sequence of jobs)
	job = ['-1'] * time

	# Iterate through all given jobs
	for i in range(len(arr)):

		# Find a free slot for this job
		# (Note that we start from the
		# last possible slot)
		for j in range(min(time - 1, int(arr[i][1]) - 1), -1, -1):

			# Free slot found
			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break

	# print the sequence
	print(job)

# Driver's Code
if __name__ == '__main__':
	# Job Array
	# arr = [['a', 2, 100], 
	# 		['b', 1, 19],
	# 		['c', 2, 27],
	# 		['d', 1, 25],
	# 		['e', 3, 15]]
	
	# print("Following is maximum profit sequence of jobs")

	# # Function Call
	# printJobScheduling(arr, 3)

	arr = []
	
	print("How many jobs are available?")

	numberOfJobs = int(input())

	for i in range(numberOfJobs):
		arr.append([])

	for i in range(len(arr)):
		userInput = str(input("List the jobs, their start time, and profit (e.g ['a',2,100]): "))
		userInput = userInput.split(',')

		arr[i] = userInput

	time = int(input("Deadline? "))
	print("Following is maximum profit sequence of jobs: ")
	printJobScheduling(arr,time)
	

	

