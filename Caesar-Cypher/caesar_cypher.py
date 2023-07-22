from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(txt, n, choice):
    if choice == 'encode':
        encptn = []
        while n not in range(26):
            n = abs(n-26)
        for letter in txt:
            if letter not in alphabet:
                encptn.append(letter)
            else:
                encptn.append(alphabet[(alphabet.index(letter)+n)%26])
        print(f"Your encoded text is: {''.join(encptn)}")
        
    elif choice == 'decode':
        decptn = []
        while n not in range(26):
            n = abs(n-26)
        for letter in txt:
            if letter not in alphabet:
                decptn.append(letter)
            else:
                decptn.append(alphabet[(alphabet.index(letter)-n)%26])
        print(f"Your decoded text is: {''.join(decptn)}")
        
ch = True
while ch:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    caesar(text, shift, direction)
    
    ch = input("You want to continue yes/no?: ")
    if ch == 'no':
        ch = False