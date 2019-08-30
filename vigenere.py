from helpers import alphabet_position, rotate_character

def new_encrypt(text,rot):
  new_text = ''
  rot_letter = 0

  for char in text:
    start = rot[rot_letter]
    rotation_amount = alphabet_position(start)
    new_text += rotate_character(char,rotation_amount)
    if char.isalpha():
      rot_letter+= 1
    if rot_letter >= len(rot):
      rot_letter = 0
  return new_text
    

def main():
  message = str(input("What message would you like to encrypt? "))
  encryption_key = str(input("What is going to be your encryption key? "))
  print("This is the result of your encryption:")
  print(new_encrypt(message,encryption_key))

if __name__ == "__main__":
  main() 
      