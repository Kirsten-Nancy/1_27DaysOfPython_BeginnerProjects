#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

print('Welcome to the Creative Space where Everything is Possible!')

city = input('Which city did you grow up in?\n')
print("How wonderful!" + " Heard the landscape there is amazing")

response = input('Did you have a pet growing up?\n')

if response.capitalize() == 'No':
    print("That is unfortunate.")
    alt = input("So what do you like?\n")
    print('Your band name could be '+ city + ' ' + alt)
else:
    petName = input("What was the name of your pet?\n")
    print('Your band name could be '+ city + ' ' + petName)

print('I know, i know, not very creative but we will get there.')

