def find_nb(m):
	if 1 ** 3 == m:
		return 1
	else: 
		n = 2
		volume = 1
		while volume < m:
			volume = volume + n ** 3
			if volume == m:
				return n
			else:
				n = n + 1
				continue
		return -1
