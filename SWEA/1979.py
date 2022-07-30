T = int(input())

for test_case in range(1, T + 1):
	answer = 0
	puzzle = []
	n, k = map(int, input().split())
	for _ in range(n):
		puzzle.append(list(map(int, input().split())))
		blank = 0
		for col in puzzle[-1]:
			if col == 1: 
				blank += 1
			else: 
				blank = 0
			if blank == k:
				answer += 1
			elif blank == k+1:
				answer -= 1

	for col in range(n):
		blank = 0
		for row in range(n):
			if puzzle[row][col] == 1:
				blank += 1
			else: 
				blank = 0
			if blank == k:
				answer += 1
			elif blank == k+1:
				answer -= 1
			
	print("#%d %d" %(test_case, answer))

	