def alphabet_position(letter):
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  letter = letter.lower()
  letter_index = alphabet.index(letter)
  return letter_index

def rotate_character(char, rot):
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  final_rotated = ''
  if char.isalpha():
    for letter in alphabet:
      rotated_index = alphabet.index(char.lower()) + rot
      if rotated_index < 26:
        final_rotated = alphabet[rotated_index]
      else:
        final_rotated = alphabet[rotated_index % 26]
    
    if char.islower():
      return final_rotated.lower()
    else:
      return final_rotated.upper()

    if char != char.isalpha():
      return char
  else: 
    return char