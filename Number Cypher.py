#CONSTANTS
WORD_SEP = " "
KEY_SEP = ":"
TABLE = ["WORD_SEP", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
BASE = len(TABLE)

WELCOME = "Welcome to the Cullen and Mader Number Cypher. Use this program to send and receive secret messages."
HELP = "AVAILABLE COMMANDS:\n\'quit\': quit this program\n\'help\': display this help message\n\'cypher\': open cyphering program\n\'decypher\': open deyphering program\n\nACCEPTED FORMS:\nwithout key: \'<word> <word>\'\nwith key: \'<keyword>:<word> <word>\'"
FAREWELL = "Thank you for using the Cullen and Mader Number Cypher."

COM_ERROR = "Command not recognised."
FORM_ERROR = "Form not recognised."

COM_PROMPT = "Which command do you wish to execute? "
CYPH_PROMPT = "What do you wish to cypher? "
DECYPH_PROMPT = "What do you wish to decypher? "

#FUNCTIONS
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

#String List[Integer(>0, <BASE+2)] -> String
def cypherWord(word,keylist=[]):
	global TABLE, BASE
	num = 0
	charlist = explode(word).reverse()
	i = 0
    j = 0
	while i < len(charlist):
		n = TABLE.find(charlist[i])
      if len(keylist) > 0:
        n += keylist[j]
        n = n % BASE
        j += 1
        j = j % len(keylist)
		num += n * BASE ** i
		i += 1
	return str(num)
assert cypherWord("RHYS") == str(17 * BASE ** 3 + 7 * BASE ** 2 + 24 * BASE + 18)
assert cypherWord("MADER") == str(12 * BASE ** 4 + 3 * BASE ** 2 + 4 * BASE + 17)
assert cypherWord("DAVID", [2, 1]) == str((4 + 2) * BASE ** 4 + (1 + 1) * BASE ** 3 + (22 + 2) * BASE ** 2 + (9 + 1) * BASE + 4 + 2)
assert cypherWord("CULLEN", [23, 18, 5, 9]) == str((3 + 23) * BASE ** 5 + (20 + 18 - BASE) * BASE ** 4 + (12 + 5) * BASE ** 3 + (12 + 9) * BASE ** 2 + (5 + 23 - BASE) * BASE + 14 + 18 - BASE)

#String -> String
def cypher(str0):
	global WORD_SEP, KEY_SEP
  key = str0.rpartition(KEY_SEP)[2]
  if len(key) > 0:
    keylist = explode(key)
    i = 0
    while i < len(keylist):
      keylist[i] = TABLE.find(keylist[i])
      i += 1
  mes = str0.rpartition(KEY_SEP)[0]
  words = mes.split(WORD_SEP)
  i = 0
  str1 = ""
  while i < len(words):
    if len(keylist) > 0:
      str1 += cypherWord(words[i], keylist)
    else:
      str1 += cypherWord(words[i])
    str1 += cypherWord(WORD_SEP)
    i += 1
	end = len(str1) - len(cypherWord(WORD_SEP))
  str1 = str1[0:end]
  return str1
assert cypher("RHYS" + WORD_SEP + "MADER") == str(cypherWord("RHYS") + WORD_SEP + cypherWord("MADER"))
assert cypher("DAVID" + WORD_SEP + "CULLEN") == str(cypherWord("DAVID") + WORD_SEP + cypherWord("CULLEN"))
assert cypher("KEY" + KEY_SEP + "NUMBER" + WORD_SEP + "CYPHER") == str("KEY" + KEY_SEP + cypherWord("NUMBER", [11, 5, 25]) + WORD_SEP + cypherWord("CYPHER", [11, 5, 25]))

#String -> String
def validateCypher(str0):
	global FORM_ERROR, WORD_SEP
	if len(str0) <= 0:
		return FORM_ERROR
	wordlist = str0.split(WORD_SEP)
	if wordlist.count("") > 0:
		return FORM_ERROR
	charlist = explode(str0)
	i = 0
	while i < len(charlist):
		if TABLE.count(charlist[i]) > 0:
			i += 1
		else:
			return FORM_ERROR
	return cypher(str0)
assert validateCypher("") == FORM_ERROR
assert validateCypher(WORD_SEP) == FORM_ERROR
assert validateCypher("RHYS") == cypher("RHYS")
assert validateCypher("RHYS" + WORD_SEP + WORD_SEP + "MADER") == FORM_ERROR
assert validateCypher("RHYS" + WORD_SEP + "MADER") == cypher("RHYS" + WORD_SEP + "MADER")
assert validateCypher(WORD_SEP + "RHYS") == FORM_ERROR
assert validateCypher("RHYS" + WORD_SEP) == FORM_ERROR

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

#String -> String
def decypher(str0):
	global WORD_SEP
	wordlist = str0.split(cypher(WORD_SEP))
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
def validateDecypher(str0):
	global FORM_ERROR, WORD_SEP
	if len(str0) <= 0:
		return FORM_ERROR
	wordlist = str0.split(WORD_SEP)
	if wordlist.count("") > 0:
		return FORM_ERROR
	charlist = explode(str0)
	i = 0
	while i < len(charlist):
		if charlist[i] == WORD_SEP:
			i += 1
		elif charlist[i].isdigit():
			i += 1
		else:
			return FORM_ERROR
	return decypher(str0)
assert validateDecypher("") == FORM_ERROR
assert validateDecypher(WORD_SEP) == FORM_ERROR
assert validateDecypher("1234556") == decypher("123456")
assert validateDecypher("123" + WORD_SEP + "456") == decypher("123" + WORD_SEP + "456")
assert validateDecypher(WORD_SEP + "123456") == FORM_ERROR
assert validateDecypher("123456" + WORD_SEP) == FORM_ERROR
assert validateDecypher("123" + WORD_SEP + WORD_SEP + "456") == FORM_ERROR

#MAIN
print(WELCOME)
print(HELP)
while True:
	com = raw_input(COM_PROMPT)
	if str0 == "quit":
		break
	elif str0 == "help":
		print(HELP)
	elif str0 == "cypher":
		com = raw_input(CYPH_PROMPT)
		print(cypher(com))
	elif str0 == "decypher":
		com = raw_input(DECYPH_PROMPT)
		print(decypher(com))
	else:
		print(COM_ERROR)
print(FAREWELL)
raise SystemExit
