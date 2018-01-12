
'''
This is the encoding function responsible for encoding the text

@params 	text, the text provided by the user as a string
		alpha, the new alphabet for the encoding device as a string

@return 	newtext, the new encoded text as a string


'''

def encode(text, alpha):
	i=0
	k=0
	newalpha = alpha.lower()		
	length = len(list(text))		
	newtext=[]
	for i in range (length):
		for k in range(26):		
			if text[i] == chr(65+k):			
				newtext.append(newalpha[k])
		if text[i] < chr(65):
			newtext.append(text[i])	
		code = "".join(newtext).upper()	
	return code;
'''
This is the decoding function which take a illegible text and makes it legible

@params		code, A scambled string provided by the user.
		alpha, the alphabet that the orriginal text was scrambled with.

@return		newtext, A uppercase string which is legible text.

'''
def decode(code, alpha):	
	length = len(list(code))		
	newtext=[]
	for i in range (length):
		for k in range(26):		
			if code[i] == alpha[k]:			
				newtext.append(chr(97+k))	
		if code[i] < chr(65):
			newtext.append(code[i])		
	text = "".join(newtext)
	text = text.upper()	
	return text;

'''
This funtion will shift the alphabet over by said amount.

@params		x, A intiger that is between 0 and 26.

@return		alpha, The shifted alphabet in a uppercase string.
'''

def ceasar_cipher_alphabet(x):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cipher = []	
	i=0
	k=65	
	l=0	
	alpha = alpha.lower()	
	for i in range(26):
		j= alpha[i]		
		if (k+x) <= 90:
			cipher.append(chr(k+x))
			k=k+1		
		else:
			cipher.append(chr(65+l))
			l=l+1
		i=i+1
	alpha = join(cipher)
	return alpha.upper();

'''
This function turns a list into a ordered string

@params		a, The desired list to turn into a string.

@return		a, The string value of the list.
'''

def join(lis):
	a = ""	
	l = len(lis)
	i = 0	
	for i in range(l):
		b = lis.pop(0)
		a = a + b
	return a;
'''
This function checks if the inputed alphabet has 26 characters, and that they are all letters.

@params 	none

@return 	alpha, If no errors were made the desired uppercase alphabet as a string. 
		bet, If there was a mistake then the regular uppercase alphabet as a string
''' 

def cryptogram_alphabet():
	alpha = input("Type in a 26 letter code with no duplicating letters: ").upper()	
	i=0	
	bet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	if len(alpha) == 26 :
		for i in range(26):			
			for k in range(26):
				if alpha[i] == alpha[k] and (i != k):
					print("You had matching letters.")
					return bet;
				elif  65 > ord(alpha[i]) or ord(alpha[i]) > 90 :
					print("Not all of your characters were letters")
					return bet;
		return alpha;
	else: 
		print("You didnt have exactly 26 letters.")
		return bet;

'''
This function takes a keyword, and adds the it to the start of the alphabet. It also removes the letters in the keyword from the alphabet.

@params		word, The keyword as a string.

@returns	alpha, The new alphabet as a uppercase string if only letters were inputed.
		bet, The regular alphabet as a uppercase string. if other characters were used instead of letters.
'''


def keyword_cypher_alphabet(word):
	alpha = list(word.upper())	
	alpha = dif_letters(alpha)
	word = word.upper()	
	alpha = list(alpha)
	bet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	betl = list(bet)	
	l = len(alpha)
	


	for i in range(l):			
		if 65 > ord(word[i]) or ord(word[i]) > 90: 		
			print("Not all your charaters were letters. please try again.\n")
			return bet;		
		for k in range(26):
			if alpha[i] == bet[k]:
				betl.pop(26-(26-k))
				betl.insert(26 -(26-k),"")	
	for z in range(26):
		alpha.append(betl[z])	
	alpha = join(alpha)
	return alpha;

'''
This function checks if a word as duplicate letters in it. If the function does, it reoves the kater duplicate letter.

@params 	x,The word as a string

@return		x,The word without duplicate letters in a string
'''

def dif_letters(x):	
	l = len(x)	
	for i in range(l):
		for k in range(l):
			if x[i] == x[k] and k!=i:
				x.pop(l-(l-k))
				x.append("")
	x = join(x)
	return x;
'''
This function will load a text file. 

@params		file_name, the name of the file to be loaded
@return		file_data, an uppercase string containing the data read from the file
'''
def load_text(file_name):
	file_hndl = open(file_name, "r")
	file_data = file_hndl.read()
	file_hndl.close()
	return file_data.upper()
'''

This function will save data to a text file.

@params	file_name, The name of the file to be saved

@return 	file_data, the data to be written to the file

'''


def save_text(file_name, file_data):
	file_hndl = open(file_name, "w")
	file_hndl.write(file_data)
	file_hndl.close()


'''
This is the main function, respinsible for the user interface.

@params 		none
@return			none
'''
def main():			
	intext = ""
	modtext = ""
	alpha = ""	
	while True:		
	
	
		option = input("Welcome to the menu. What would you like to do? \nIf you would like to load a text file, type L. \nIf you would like to save the text file, type S. \nIf you would like to encode the current text, type E. \nIf you would like to Decode the current text, type D. \nIf you would like to create a alphabet using the ceaser cipher method, type C.\nIf you would like to create a alphabet using the cryptogram method, type CR.\nIf you would like to create a alphabet using the keyword cipher method, type K.\nIf you would like to quit, type Q:\t")
		if option.upper() == "L":
			text = input("What is the text file called? ")		
			intext = load_text(text)	
			modtext = ""
			alpha = ""		
		elif option.upper() == "S":
			if modtext == "":
				print("You havent modified any text. plese try again.\n")
			else:			
				newfile = input("\nWhat is the file you want to save it to: ")			 
				save_text(newfile,modtext)
		elif option.upper() == "E":
			if intext == "" or alpha == "":
				print("\nYou havent loaded a text or created a alphabet. Please try again.\n")			
			else:				
				modtext = encode(intext,alpha)				
		elif option.upper() == "D":
			if intext == "" or alpha == "":
				print("\nYou havent loaded a text or created a alphabet. Please try again.\n")			
			else:			
				modtext = decode(intext,alpha)
				print(modtext)	
		elif option.upper() == "C":
			x= int(input("\nHow many letter would you like to shift to the right? "))
			if 0 <= x < 27:			
				alpha = ceasar_cipher_alphabet(x)	
			else:
				print("\nYour value was not in betwenn 0 and 25.Please try again.\n")		
		elif option.upper() == "CR":		
			alpha = cryptogram_alphabet()
		elif option.upper() == "K":
			word = input("\nWhat is the keyword you would like to use? ")
			alpha = keyword_cypher_alphabet(word)		
		elif option.upper() == "Q":	
			print("\nHave a nice day.")
			break
		else:
			print("\nYou tpyed an incorect key. Please try again.")
		#Printing the texts
		print("\nIntial text:\t", intext,"\nCurrent text:\t",modtext, "\nAlphabet:\t", alpha,"\n\n")
main()