class Sudoku:
	def __init__(self, world=None):
		if world is None:
			self.world = [[0] * 9 for _ in range(9)]
			self.empty = [(i, j) for i in range(9) for j in range(9)]
		else:
			self.world = world
			self.empty = []
			for i in range(9):
				for j in range(9):
					if self.world[i][j] == 0:
						self.empty.append((i, j))

	def solve(self, ind=0):
		if ind == len(self.empty):
			return True
		i, j = self.empty[ind]
		for k in range(1, 10):
			check = True
			for r in range(9):
				if self.world[r][j] == k or self.world[i][r] == k or self.world[i // 3 * 3 + r // 3][
					j // 3 * 3 + r % 3] == k:
					check = False
					break
			if not check:
				continue

			self.world[i][j] = k
			if self.solve(ind + 1):
				return True
			self.world[i][j] = 0
		return False

	def __str__(self):
		return "\n".join([" ".join(list(map(str, self.world[s]))) for s in range(9)])


task = [[0, 0, 0, 1, 2, 3, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 7, 0, 0],
		[0, 0, 8, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 7, 0, 5, 6, 0],
		[0, 6, 0, 0, 0, 0, 0, 4, 2],
		[0, 2, 0, 0, 0, 8, 0, 0, 0],
		[4, 3, 0, 0, 0, 0, 0, 0, 6],
		[0, 0, 6, 0, 9, 0, 8, 0, 0],
		[0, 0, 0, 0, 0, 5, 0, 0, 3]]

sud = Sudoku(world=task)
print(sud.solve())
print(sud)
