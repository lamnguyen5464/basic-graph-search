EDGES = [
	('A','B', 50),
	('A','D', 80),
	('B','C', 40),
	('B','E', 60),
	('D','E', 80),
	('C','E', 90),
	('C','F', 30),
	('F','M', 40),
	('M','S', 25),
	('D','G', 50),
	('G','N', 60),
	('N','P', 45),
	('P','H', 40),
	('G','H', 65),
]

HEURISTIC = {
	'A': (0, 0),
	'B': (30, 0),
	'C': (70, 10),
	'D': (10, 40),
	'E': (40, 50),
	'F': (80, 40),
	'G': (20, 50),
	'H': (50, 70),
	'M': (90, 70),
	'N': (20, 90),
	'P': (50, 90),
	'S': (100, 100),
}