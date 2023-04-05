MORSE_CODE_DICT = { 'A':'Anna', 'B':'Boris',
                    'C':'tzapla(Цапля)', 'D':'Dmitry(Дмитрий)', 'E':'Elena(Елена)',
                    'F':'Fyodor(Фёдор)', 'G':'Grigory(Григорий)', 'H':'Hariton(Харитон)',
                    'I':'Ivan(Иван)', 'J':'Ivan kratkiy(Иван Краткий)', 'K':'Konstantin(Константин)',
                    'L':'Leonid(Леонид)', 'M':'Mihail(Михаил)', 'N':'Nikolay(Николай)',
                    'O':'Olga(Ольга)', 'P':'Pavel(Павел)', 'Q':'Shuka(щука)',
                    'R':'Roman(Роман)', 'S':'Simeon(Семён)', 'T':'Tatyana(Татьяна)',
                    'U':'Uliana(Ульяна)', 'V':'Zenia(Женя)', 'W':'Vasiliy(Василий)',
                    'X':'znak(Знак)', 'Y':'ery(Еры)', 'Z':'Zinaida(Зинаида)',
                    '1':'1', '2':'2', '3':'3',
                    '4':'4', '5':'5', '6':'6',
                    '7':'7', '8':'8', '9':'9.',
                    '0':'0', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
 
# Function to decrypt the string
# from morse to english
def decrypt(message):
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher
 
# Hard-coded driver function to run the program
def main():
    message = input("Input youre callsign> ")
    result = encrypt(message.upper())
    print ("Youre translated callsign> " + result)
 
    message = result
    result = decrypt(message)
    print ("Your message: " + result)
 
# Executes the main function
if __name__ == '__main__':
    main()