# alphabet list will be referenced to replace letters during encryption and decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#ask user for all required inputs for caesar cipher program
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

#one function to rule them all
#caesar decides to decode or encode based on direction input, then performs that function
def caesar(plain_text, shift_amount, encrypt_or_decrypt):
  cipher_text = ""
  #outside "if" statement takes care of bad "decrypt" inputs
  if encrypt_or_decrypt == "encode" or encrypt_or_decrypt =="decode":
    for letter in plain_text:
      position = alphabet.index(letter)
      if encrypt_or_decrypt == "encode":
        new_position = position + shift_amount
      else:
        new_position = position - shift_amount
      cipher_text += alphabet[new_position]
    print(f"The {direction}d text is {cipher_text}")
  else:
    print("I can't figure out if you want to encode or decode. Try again")

#call caesar function
caesar(plain_text=text, shift_amount=shift, encrypt_or_decrypt = direction)





# # alphabet list will be referenced to replace letters during encryption and decryption
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# #ask user for all required inputs for caesar cipher program
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #caesar cipher encrypt function
# def encrypt(plain_text, shift_amount):
#   encrypted_ans = ""
#   # for loop goes 0, 1, 2... as many letters as exist in "text"
#   for letter in range(len(text)):
#     #
#     shift_index = (alphabet.index(text[letter]) + shift)
#     if shift_index > 25:
#       shift_index -= 26
#     encrypted_ans += alphabet[shift_index]
#   print(encrypted_ans)
#
# #caesar cipher decrypt function
# def decrypt(plain_text, shift_amount):
#   decrypted_text = ""
#   for letter in plain_text:
#     shift_index = alphabet.index(letter) - shift_amount
#     decrypted_text += alphabet[shift_index]
#   print(decrypted_text)
#
# #determine if user is trying to encode or decode and call appropriate function
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(plain_text=text, shift_amount=shift)
# else:
#   print("Couldn't figure out if you wanted to decode or encode")



# # prime number checker
# def prime_checker(number):
#   its_prime="bad"
#   # edge cases so we can do our "for" loop from 2-number later
#   if number == 1 or number == 2:
#     its_prime = True
#   elif number >= 2:
#     for numbers in range(2, number):
#       if number % numbers == 0:
#         its_prime = False
#   #edge case for number ==0
#   elif number == 0:
#     its_prime = False
#   # if number is negative we will end up here
#   else:
#     its_prime =="bad"
#
# #control the output based on its_prime variable
#   if its_prime == True:
#     print("It's a prime number.")
#   elif its_prime =="bad":
#     print("I don't understand the input")
#   else:
#     print("It's not a prime number.")
#
# #actually prompt user for number and throw it into prime_checker function
# n = int(input("Check this number: "))
# prime_checker(number=n)

# #basic function implementation
# import math
# def paint_calc(height, width, cover):
#   area = height * width
#   cans = math.ceil(area / cover)
#   print(f"You'll need {cans} cans of paint")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
