from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  encrypted = ''
  for char in text:
    if char.isalpha():
      if char.isupper():
        char = char.lower()
        rotated_index = alphabet.index(char) + rot
        if rotated_index < 26:
          encrypted = encrypted + (alphabet[rotated_index]).upper()
        else:
          encrypted = encrypted + (alphabet[rotated_index % 26]).upper()
      else:
        rotated_index = alphabet.index(char) + rot
        if rotated_index < 26:
          encrypted = encrypted + alphabet[rotated_index]
        else:
          encrypted = encrypted + alphabet[rotated_index % 26]
    else:
      encrypted = encrypted + char
  return encrypted

def main():
  text = str(input("What string would you like to encrypt? "))
  rot = int(input("How many rotations? "))
  print(encrypt(text, rot))




if __name__ == "__main__":
  main()



  
  
  











