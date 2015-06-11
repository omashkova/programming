import random
class Grid:
	def __init__(self, n = 3):
		self.n = n
		self.table = [[((i*n + i//n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]
	def show_grid(self):
		for i in range(self.n * self.n):
			print(*self.table[i])
	def swap_strings(self, line):
		if line % self.n == 2:
			b = [line - 1, line + 1]
			a = random.choice(b)
			self.table[line - 1], self.table[a - 1] = self.table[a - 1], self.table[line - 1]
		if line % self.n == 1:
			b = [line + 1, line + 2]
			a = random.choice(b)
			self.table[line - 1], self.table[a - 1] = self.table[a - 1], self.table[line - 1]
		if line % self.n == 0:
			b = [line - 1, line - 2]
			a = random.choice(b)
			self.table[line - 1], self.table[a - 1] = self.table[a - 1], self.table[line - 1]	
	def swap_columns(self, column):
		if column % self.n == 2:
			b = [column - 1, column + 1]
			a = random.choice(b)
			for i in range(self.n * self.n):
				self.table[i][column - 1], self.table[i][a - 1] = self.table[i][a - 1], self.table[i][column - 1]
		if column % self.n == 1:
			b = [column + 2, column + 1]
			a = random.choice(b)
			for i in range(self.n * self.n):
				self.table[i][column - 1], self.table[i][a - 1] = self.table[i][a - 1], self.table[i][column - 1]
		if column % self.n == 0:
			b = [column - 1, column - 2]
			a = random.choice(b)
			for i in range(self.n * self.n):
				self.table[i][column - 1], self.table[i][a - 1] = self.table[i][a - 1], self.table[i][column - 1]
	def swap_horizontal_stripes(self, stripe):
		pass
	def swap_vertical_stripes(self, stripe):
		pass	
	def random_generate_grid(self):
		for i in range(random.randint(0, 10)):
			self.swap_strings(random.randint(0, self.n * self.n))
		for j in range(random.randint(0, 10)):
			self.swap_columns(random.randint(0, self.n * self.n))
	def picture1(self):
		self.random_generate_grid()
		for i in range(1, 3):
			self.table[0][i] = '-'
			self.table[1][i] = '-'
			self.table[2][i] = '-'
			self.table[6][i] = '-'
		self.table[5][1] = '-'
		for i in range(1, 4):
			self.table[3][i] = '-'
			self.table[4][i] = '-'
			self.table[7][i] = '-'
		for i in range(6, 8):
			self.table[0][i] = '-'
			self.table[1][i] = '-'
			self.table[2][i] = '-'
			self.table[6][i] = '-'
		self.table[5][7] = '-'
		for i in range(5, 8):
			self.table[3][i] = '-'
			self.table[4][i] = '-'
			self.table[7][i] = '-'		 		
	



a = Grid()
a.show_grid()
print('----------------------')		
a.picture1()
a.show_grid()
