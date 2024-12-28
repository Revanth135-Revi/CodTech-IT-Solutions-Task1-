/*Password Strength Checker*/
import string

password = input("Enter the Password Here: ")

lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_char = any([1 if c in string.punctuation else 0 for c in password])
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [lower_case, upper_case, special_char,digits]

length = len(password)

score = 0
with open ('password-list.txt', 'r') as f:
  common = f.read().splitlines()

if password in common:
  print("Password was found in a common list. Score: 0 / 5")
  exit()

if length > 4:
  score += 1
if length > 8:
  score += 1
if length > 12:
  score += 1
if length > 16:
  score += 1
if length > 20:
  score += 1



if sum (characters) > 1:
  score += 1
if sum (characters) > 2:
  score +=1
if sum (characters) > 3:
  score +=1
if sum (characters) > 4:
  score +=1

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")

if score < 4:
  print(f"The password is quite weak! Score: {str(score)} / 7")
elif score == 4:
  print(f"The password is ok! Score: {str(score)} / 7")
elif score > 4 and score < 6:
  print(f"The password is more good! Score: {str(score)} / 7")
elif score > 6:
  print(f"THe Password is strong! Score: {str(score)} / 7")
