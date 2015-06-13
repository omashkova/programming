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
		elif line % self.n == 1:
			b = [line + 1, line + 2]
			a = random.choice(b)
			self.table[line - 1], self.table[a - 1] = self.table[a - 1], self.table[line - 1]
		else:
			b = [line - 1, line - 2]
			a = random.choice(b)
			self.table[line - 1], self.table[a - 1] = self.table[a - 1], self.table[line - 1]

	def swap_columns(self, column):
		if column % self.n == 2:
			b = [column - 1, column + 1]
			a = random.choice(b)
			for i in range(self.n * self.n):
				self.table[i][column - 1], self.table[i][a - 1] = self.table[i][a - 1], self.table[i][column - 1]
		elif column % self.n == 1:
			b = [column + 2, column + 1]
			a = random.choice(b)
			for i in range(self.n * self.n):
				self.table[i][column - 1], self.table[i][a - 1] = self.table[i][a - 1], self.table[i][column - 1]
		else:
			b = [column - 1, column - 2]
			a = random.choice(b)
			for i in range(self.n * self.n):
				self.table[i][column - 1], self.table[i][a - 1] = self.table[i][a - 1], self.table[i][column - 1]

	def swap_horizontal_stripes(self, stripe):
		if stripe % self.n == 2:
			b = [stripe - 1, stripe + 1]
			a = random.choice(b)
			for i in range(1, self.n + 1):
				if a == stripe - 1:
					self.table[stripe + i], self.table[stripe + i - self.n] = self.table[stripe + i - self.n], self.table[stripe + i]
				else:
					self.table[stripe + i], self.table[stripe + i + self.n] = self.table[stripe + i + self.n], self.table[stripe + i]
		elif stripe % self.n == 1:
			b = [stripe + 1, stripe + 2]
			a = random.choice(b)
			for i in range(-1, self.n - 1):
				if a == stripe + 1:
					self.table[stripe + i], self.table[stripe + i + self.n] = self.table[stripe + i + self.n], self.table[stripe + i]
				else:
					self.table[stripe + i], self.table[stripe + i + self.n * 2] = self.table[stripe + i + self.n * 2], self.table[stripe + i]
		else:
			b = [stripe - 1, stripe - 2]
			a = random.choice(b)
			for i in range(self.n, self.n * 2):
				if a == stripe - 1:
					self.table[stripe + i], self.table[stripe + i - self.n] = self.table[stripe + i - self.n], self.table[stripe + i]
				else:
					self.table[stripe + i], self.table[stripe + i - self.n * 2] = self.table[stripe + i - self.n * 2], self.table[stripe + i]								

	def swap_vertical_stripes(self, stripe):
		if stripe % self.n == 2:
			b = [stripe - 1, stripe + 1]
			a = random.choice(b)
			for j in range(self.n * self.n):
				for i in range(1, self.n + 1):
					if a == stripe - 1:
						self.table[j][stripe + i], self.table[j][stripe + i - self.n] = self.table[j][stripe + i - self.n], self.table[j][stripe + i]
					else:
						self.table[j][stripe + i], self.table[j][stripe + i + self.n] = self.table[j][stripe + i + self.n], self.table[j][stripe + i]
		elif stripe % self.n == 1:
			b = [stripe + 1, stripe + 2]
			a = random.choice(b)
			for j in range(self.n * self.n):
				for i in range(-1, self.n - 1):
					if a == stripe + 1:
						self.table[j][stripe + i], self.table[j][stripe + i + self.n] = self.table[j][stripe + i + self.n], self.table[j][stripe + i]
					else:
						self.table[j][stripe + i], self.table[j][stripe + i + self.n * 2] = self.table[j][stripe + i + self.n * 2], self.table[j][stripe + i]
		else:
			b = [stripe - 1, stripe - 2]
			a = random.choice(b)
			for j in range(self.n * self.n):
				for i in range(self.n, self.n * 2):
					if a == stripe - 1:
						self.table[j][stripe + i], self.table[j][stripe + i - self.n] = self.table[j][stripe + i - self.n], self.table[j][stripe + i]
					else:
						self.table[j][stripe + i], self.table[j][stripe + i - self.n * 2] = self.table[j][stripe + i - self.n * 2], self.table[j][stripe + i]

	def reflect_grid(self):
		for i in range(self.n * self.n):
			for j in range(i, self.n * self.n):
				self.table[i][j], self.table[j][i] = self.table[j][i], self.table[i][j]

	def random_generate_grid(self):
		for i in range(random.randint(0, 10)):
			self.swap_strings(random.randint(0, self.n * self.n))
		for j in range(random.randint(0, 10)):
			self.swap_columns(random.randint(0, self.n * self.n))
		b = [0, 1]
		a = random.choice(b)
		if a == 0:
			self.reflect_grid()	
		self.swap_horizontal_stripes(random.randint(0, self.n))
		self.swap_vertical_stripes(random.randint(0, self.n))
			
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
a.random_generate_grid()
a.show_grid()
