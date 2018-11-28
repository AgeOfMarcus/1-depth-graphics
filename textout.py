from main import *

def m_main(text):
	res = []
	for char in text:
		res.append(letters[char.upper()])

if __name__ == "__main__":
	while True:
		try:
			a = print(main(letters[input("char: ").upper()]))
		except KeyboardInterrupt:
			break
