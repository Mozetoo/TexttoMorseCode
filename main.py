morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
    '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', " ": " "
}

user_input = input("Change your text to morse Code: ").upper()
output = ""
recovery = []
for letter in user_input:
    if letter in morse_code_dict:
        output += morse_code_dict[letter]
        recovery.append(morse_code_dict[letter])
    elif letter == " ":
        output += " "

print(f"Your Morse Code: {output}")

choice = True
rec_text = ""
while choice:
    dec = input("\nEnter Yes to Decipher and No to Leave It:  ").lower()
    if dec != "yes" and dec != "no":
        print("Wrong Input Try Again")
        continue
    elif dec == "yes":
        for data in recovery:
            for key, value in morse_code_dict.items():
                if value == data:
                    rec_text += key
        print(f"Your Original Text: {rec_text.title()}")
        choice = False
    else:
        print(f"Your Morse Code: {output}")
        choice = False

