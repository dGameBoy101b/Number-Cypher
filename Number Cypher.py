#CONSTANTS
WORD_SEP = " "
TABLE = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
BASE = len(TABLE)

#FUNCTIONS
#String -> String
def cypher(str0):
	global WORD_SEP
  words = str0.split(WORD_SEP)
  i = 0
  str1 = ""
  while i < len(words):
    str1 += cypherWord(words[i])
    str1 += WORD_SEP
    i += 1
	end = len(str1) - len(WORD_SEP)
  str1 = str1[0:end]
  return str1
assert cypher("RHYS" + WORD_SEP + "MADER") == str(cypherWord("RHYS") + WORD_SEP + cypherWord("MADER"))
assert cypher("DAVID" + WORD_SEP + "CULLEN") == str(cypherWord("DAVID") + WORD_SEP + cypherWord("CULLEN"))

#String -> String
def cypherWord(word):
	global TABLE, BASE
	num = 0
	charlist = explode(word).reverse()
	i = 0
	while i < len(charlist):
		n = TABLE.find(charlist[i])
		num += n * BASE ** i
		i += 1
	return str(num)
assert cypherWord("RHYS") == str(17 * BASE ** 3 + 7 * BASE ** 2 + 24 * BASE + 18)
assert cypherWord("MADER") == str(12 * BASE ** 4 + 3 * BASE ** 2 + 4 * BASE + 17)

#String -> List
def explode(str0):
	list1 = []
	i = 0
	while i < len(str0):
		list1.append(str0[i])
		i += 1
	return list1
assert explode("RHYS") == ["R", "H", "Y", "S"]
assert explode("MADER") == ["M", "A", "D", "E", "R"]
assert explode("") == []

#String -> String
def decypher(str0):
	global WORD_SEP
	wordlist = str0.split(" ")
	i = 0
	str1 = ""
	while i < len(wordlist):
		str1 += decypherWord(wordlist[i])
		str1 += WORD_SEP
		i += 1
	end = len(str1) - len(WORD_SEP)
	str1 = str1[0:end]
	return str1
assert decypher(cypher("RHYS MADER")) == "RHYS MADER"
assert decypher(cypher("DAVID CULLEN")) == "DAVID CULLEN"

#String -> String
def decypherWord(str0):
	global BASE, TABLE
	num = int(str0)
	power = 0
	while num > BASE:
		num /= BASE
		power += 1
	num = int(str0)
	charlist = []
	while power >= 0:
		n = num // BASE ** power
		charlist.append(n)
		num -= n * BASE ** power
		power -= 1
	i = 0
	while i < len(charlist):
		charlist[i] = TABLE[charlist[i]]
		i += 1
	str1 = implode(charlist)
	return str1
assert decypherWord(cypherWord("RHYS")) == "RHYS"
assert decypherWord(cypherWord("MADER")) == "MADER"

#List -> String
def impolde(list0):
	i = 0
	str1 = ""
	while i < len(list0):
		str1 += list0[i]
		i += 1
	return str1
assert implode(["R", "H", "Y", "S"]) == "RHYS"
assert implode(["M", "A", "D", "E", "R"]) == "MADER"
assert implode([]) == ""
