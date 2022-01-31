# def wall_paint_cal(height, weight, coverage):
#     cal = round((height * weight) / coverage)
#     print(f"the total cands to buy is {cal}")

# h = int(input("please enter the height of the wall => ")) 
# w = int(input("please enter the widhth of the wall => ")) 
# c = int(input("please enter the coverage of the wall => ")) 


# wall_paint_cal(h, w, c)
# def prim_checker(nume):
#   if nume /  == 0:
#     print(f"{nume} is not a prime number ")
#   else:
#     print(f"{nume} is a prime number")

# check = int(input("enster an number"))

# prim_checker(check)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)