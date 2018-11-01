#CONSTANTS
TABLE = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
BASE = len(TABLE)

#FUNCTIONS
#String -> String
def cypher(str0):
  words = str0.split(" ")
  i = 0
  str1 = ""
  while i < len(words):
    str1 += cypherWord(words[i])
    str1 += " "
    i ++
  str1 -= " "
  return str1
assert cypher("RHYS MADER") == str(cypherWord("RHYS") + cypherWord("MADER"))
assert cypher("DAVID CULLEN") == str(cypherWord("DAVID") + cypherWord("CULLEN"))

#String -> String
def cypherWord(word):
	global TABLE, BASE
	num = 0
	charlist = explode(word).reverse()
	i = 0
	while i < len(charlist):
		n = TABLE.find(charlist[i])
		num += n * BASE ** i
		i ++
	return str(num)
assert cypherWord("RHYS") == str(17 * BASE ** 3 + 7 * BASE ** 2 + 24 * BASE + 18)
assert cypherWord("MADER") == str(12 * BASE ** 4 + 3 * BASE ** 2 + 4 * BASE + 17)

#String -> List
def explode(str0):
	list1 = []
	i = 0
	while i < len(str0):
		list1.append(str0[i])
		i ++
	return list1
assert explode("RHYS") == ["R", "H", "Y", "S"]
assert explode("MADER") == ["M", "A", "D", "E", "R"]
