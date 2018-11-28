code = {
	0:" ",
	1:"█"
}

letters = {
	"A":"00100 01010 01110 10001 10001",
	"B":"11110 10001 11110 10001 11110",
	"C":"00111 01100 11000 01100 00111",
	"D":"11100 10010 10001 10010 11100",
	"E":"11111 10000 11100 10000 11111",
	"F":"11111 10000 11110 10000 10000",
	"G":"00111 01000 10011 01001 00110",
	"H":"10001 10001 11111 10001 10001",
	"I":"01110 00100 00100 00100 01110",
	"J":"00111 00001 00001 10001 01110",
	"K":"10001 10010 11100 10010 10001",
	"L":"10000 10000 10000 10000 11111",
	"M":"10001 11011 10101 10001 10001",
	"N":"10001 11001 10101 10011 10001",
	"O":"00100 01010 10001 01010 00100",
	"P":"11110 10001 11110 10000 10000",
	"Q":"00100 01010 10001 01010 00101",
	"R":"11110 10001 11110 10100 10010",
	"S":"01111 10000 01110 00001 11110",
	"T":"11111 00100 00100 00100 00100",
	"U":"10001 10001 10001 10001 01110",
	"V":"10001 10001 10001 01010 00100",
	"W":"10001 10001 10001 10101 01010",
	"X":"10001 01010 00100 01010 10001",
	"Y":"10001 01010 00100 00100 00100",
	"Z":"11111 00010 00100 01000 11111"
}



def convert_to_list(text):
	res = []
	for line in text.split(" "):
		newl = []
		for block in line:
			if not block in ["1","0"]:
				raise Exception("Input blocks can only be 1s or 0s")
			newl.append(int(block))
		res.append(newl)
	return res

def convert_to_blocks(lst):
	res = []
	for row in lst:
		newl = []
		for num in row:
			newl.append(code[num])
		res.append(newl)
	return res

def build(chunk):
	res = ''
	for line in chunk:
		if not res == '':
			res += "\n"
		res += ''.join(line)
	return res

def main(text):
	print(build(convert_to_blocks(convert_to_list(text))))

if __name__ == "__main__":
	main(input("Data: "))
