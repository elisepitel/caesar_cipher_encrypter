alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, amount_shift, cipher_direction):
  caesar_text = ""

  if cipher_direction == "decode":
    amount_shift *= -1
  if amount_shift >= 25:
    amount_shift %= 25
  for char in start_text: 
    if char in alphabet: 
      position = alphabet.index(char)
      new_position = position + amount_shift
      caesar_text += alphabet[new_position]
    else:
      caesar_text += char
  
  print(f"The {cipher_direction}d is {caesar_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, amount_shift=shift, cipher_direction=direction)

  replay = input("Type 'yes' if you would like to encode a new message. Otherwise type 'no'.")
  if replay == "no":
    print("Have a nice day!")
    should_continue = False
