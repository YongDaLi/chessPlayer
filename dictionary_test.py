#dictonary test

def convert(num):
	switch = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine"
	}

	return switch[num]

def main():
	num = 3;
	print("num:", num)
	print("convert:", convert(num))

main()