import random
import itertools

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
		return self.table
			
	def picture_sudoku(self):
		table = self.random_generate_grid()
		#for i in range(1, 3):
			#self.table[0][i] = ' '
			#self.table[1][i] = ' '
			#self.table[2][i] = ' '
			#self.table[6][i] = ' '
		self.table[5][1] = ' '
		#for i in range(1, 4):
			#self.table[3][i] = ' '
			#self.table[4][i] = ' '
			#self.table[7][i] = ' '
		#for i in range(6, 8):
			#self.table[0][i] = ' '
			#self.table[1][i] = ' '
			#self.table[2][i] = ' '
			#self.table[6][i] = ' '
		self.table[5][7] = ' '
		#for i in range(5, 8):
			#self.table[3][i] = ' '
			#self.table[4][i] = ' '
			#self.table[7][i] = ' '
		#return table		

	def create_solving_state(self):
		solving_state = dict()
		for i in range(self.n * self.n):
			for j in range(self.n * self.n):
				if type(self.table[i][j]) == int:
					solving_state[(i, j)] = {self.table[i][j]}
				else:
					solving_state[(i, j)] = {k for k in range(1, 10)}

	#def sudoku_with_one_solution(self):
		#current_table = self.random_generate_grid()
		#solution = performFiltering(self.create_solving_state(), getStandardRestrictions())
		#self.show_grid()

#создаёт словарь, хранящий для каждой клетки (i, j) области, в которых её значение не должно повторяться (соответствующий квадрат 3х3, строка и столбец)
def get_standard_restrictions():
	restriction_sets = dict()
	for i in range(9):
		for j in range(9):
			restriction_sets[(i,j)] = list()
			i_anchor = i // 3 * 3
			j_anchor = j // 3 * 3
			restriction_sets[(i,j)].append(set((i1,j1) for i1 in range(i_anchor,i_anchor + 3) for j1 in range(j_anchor, j_anchor + 3)))
			restriction_sets[(i,j)].append(set((i1,j) for i1 in range(9)))
			restriction_sets[(i,j)].append(set((i,j1) for j1 in range(9)))           
	return restriction_sets
#функции передаётся набор из множеств S1, ... Sn, по которому определяется, можно ли составить из элементов этих 
#множеств систему различных представителей (system of different representatives),
#т.е. существует ли взаимо-однозначное отображение Si -> s(i), s(i) из Si, все s(i) различны
def has_sdr(set_system):
    	#"элемент", который по умолчанию присваивается всем наборам
	NULL = -1
	if any(len(s) == 0 for s in set_system):
		return False
    	#совокупность всех различных элементов, которым можно поставить в соответствие множества
	all_elements = set(itertools.chain.from_iterable(set_system))
    	#если всех различных элементов меньше, чем множеств, то системы различных представителей не существует, т.к. нет
    	#взаимо-однозначного отображения
	if len(all_elements) < len(set_system):
		return False
	#если вариантов расстановки чисел не очень много, то пробуем просто перебрать их все
	prod = 1
	stupid_limit = 100
	for s in set_system:
		prod *= len(s)
		if prod > stupid_limit:
			break
		else:
			for x in itertools.product(*(set_system)): #простой перебор декартовых произведений множеств
				if len(set(x)) == len(x):
					return True
		return False

	set_system = set_system.copy()
	for i,s in enumerate(set_system):
		set_system[i] = s.copy()
	for i,s in enumerate(set_system):
		if len(s) == 1:#если для данной клетки есть только одно число, которое может стоять в ней
			for j,t in enumerate(set_system):
				if i != j: #из всех остальных наборов
					t -= s #удаляем это число
					if len(t) == 0:#если в результате этого появилась клетка, в которую ничего нельзя поставить, то 
						return False #такой способ не работает

	sdp = [NULL] * len(set_system) #предварительно заполняем СРП
	for i,s in enumerate(set_system):
		if not s.issubset(sdp[:i]): #если все элементы множества s не содержатся уже в sdp
			sdp[i] = (s - set(sdp[:i])).pop() #записываем первый элемент s из тех, что ещё не записаны в sdp
	
	who_fixes_element = dict() #словарь, в котором элементу сопоставляется множество, переходящее в него
	for i,e in enumerate(sdp):
		if e != NULL:
			who_fixes_element[e] = i

	free_elements = all_elements - set(sdp) #не зафиксированные ни одним множеством элементы
	unsatisfied_set_indices = set(i for i, t in enumerate(sdp) if t == NULL) #номера множеств, которые не прикреплены ни к одному элементу
	for unsatisfied_set_index in unsatisfied_set_indices:
		has_free_elements = [len(s & free_elements) > 0 for s in set_system ] #массив, который хранит для данного множества True, если есть свободные элементы, куда оно может перейти, и False в другом случае
		reachable_set_indices = {unsatisfied_set_index} #номера множеств, до которых можно добраться обходом графа. Вначале это просто те множества, которые не прикреплены ни к одному элементу
		target_set_index = unsatisfied_set_index #номер множества, которое будет "перенаправлено"
		reached_from = [NULL] * len(set_system) #хранит для данного множества номер того множества, от которого мы попали в данное 
		set_indices_to_be_checked = {unsatisfied_set_index} #номера множеств, которые должны быть обработаны на данный момент
		while len(set_indices_to_be_checked) > 0:
			new_set_indices_to_be_checked = set()
			for si in set_indices_to_be_checked:
				if has_free_elements[si]: #если есть свободный элемент, в который можно перевести данное множество, то
					target_set_index = si
					new_set_indices_to_be_checked.clear() #не нужно обрабатывать никакие другие множества
					break
				else: #если нет свободных элементов, в которые можно было бы перевести данное множество
					for e in set_system[si]: #для каждого элемента этого множества
						if who_fixes_element[e] not in reachable_set_indices: #если множества, которое переводится в этот элемент, нет в reachable_set_indices 
							new_set_indices_to_be_checked.add(who_fixes_element[e]) #необходимо проверить это множество
							reached_from[who_fixes_element[e]] = si
			reachable_set_indices |= new_set_indices_to_be_checked #расширяем множество номеров множеств, до которых можем добраться
			set_indices_to_be_checked = new_set_indices_to_be_checked #модифицируем набор номеров множеств, которые нужно обработать
		if not has_free_elements[target_set_index]:
			return False

		sdp[target_set_index] = list(set_system[target_set_index] & free_elements)[0]
		new_fixed_element = sdp[target_set_index]
		who_fixes_element[new_fixed_element] = target_set_index
		free_elements.remove(sdp[target_set_index])
		target_set_index = reached_from[target_set_index]
		while target_set_index != NULL:
			new_temp_free_element = sdp[target_set_index]
			sdp[target_set_index] = new_fixed_element
			who_fixes_element[new_fixed_element] = target_set_index
			new_fixed_element = new_temp_free_element
			target_set_index = reached_from[target_set_index]
	return True	

def perform_filtering(solving_state, restriction_sets):
	removed_something = True
	while removed_something:
		removed_something = False
		for i in range(9):
			for j in range(9):
				for e in solving_state[(i,j)].copy():
					backup_set = solving_state[(i,j)]
					solving_state[(i,j)] = {e}
					if any(not has_sdr([solving_state[pair] for pair in restriction_set]) for restriction_set in restriction_sets[(i,j)]):
						backup_set.remove(e)
						if len(backup_set) == 0:
							print(i,j)
							for restriction_set in restriction_sets[(i,j)]:
								if not has_sdr([solving_state[pair] for pair in restriction_set]):
									print({pair : solving_state[pair] for pair in restriction_set})
							return False
						removed_something = True
					solving_state[(i,j)] = backup_set
	print(solving_state)

a = Grid()
a.picture_sudoku()
perform_filtering(a.create_solving_state(), get_standard_restrictions())
