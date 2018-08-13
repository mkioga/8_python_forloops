
# =================
# 8_forloops.py
# =================

# for loops are used to repeat an operation multiple times.
# for loop takes a range of values and assigns them one by
# one to a variable and then executes a block of code for
# each value.

# In this example, we will print numbers range one to 19
# in this case, the for loop takes first number, then prints it
# then takes second, third etc and prints it until it reaches
# the end of the range:
# Note that in range, the last number specified is not included.
# So in this case, 20 is not included


for i in range(1,20):
    print("i is now {}".format(i))


# There is no change if we put 0 in {0}
# This is because for every loop, the number is in position 0

for i in range(1,20):
    print("i is now {0}".format(i))


# Using Function "len" which stands for length
# so len(number) is the integer length of the string number
# NOTE that the length of this string including commas is 10
# NOTE that we use print(number[i]) to print the character in
# position i only. Otherwise if you say print(number) it will print
# the whole number ten times

number = "1,23,456,7"
for i in range(0, len(number)):
    print(number[i])

# Now lets say we only want to print the numbers without commas.
# we can add a test using function "in" and print those that pass
# The "for" loop picks first letter in number, i.e. position 0 = 1 and
# checks if it is in range 0 to 9 (i.e. 10 positions starting from 0)
# second line: if number[i], (character in position 0)  which in this
# case is 1 is in string "0123456789", then it is printed by line 3

number = "1,23,456,7"
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i])

# HOW TO MAKE ABOVE RESULT PRINT IN A SINGLE LINE
# if you put a comma after print(number[i],), it will tell you that
# the default is new line (end: str='\n') which means default is
# end='\n' i.e. to print to new line.
# we can override the default by using end='' and the numbers will
# all print in one row

number = "1,23,456,7"
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i],end='')

# CONVERTING ABOVE OUTPUT TO INTEGER
# Above output is a string. We want to convert it to integer
# First we are going to create new variable named cleanednumber
# and give it null value ''
# Then after the for loop runs and produces number[i], we concatenate
#  that character in number[i] with cleanednumber which is initially
# null. Note that [i] is the index i.e. character in that position.
# Then we convert string cleanednumber and assign it to newnumber
# NOTE the indentation of newnumber is at the beginning.
# This enables the for loop to run to completion, then assign the
# complete cleanednumber into newnumber.
# if newnumber was in same indentation as line 80, it would produce
# same result, but assignment would just run 10
# This would cause delays if range is really big


number = "1,23,456,7"
print("The length of the number is: {}". format(len(number)))
cleanednumber = '' # This is initially set to null
for i in range(0, len(number)):
    if number[i] in "0123456789": # We use the index [i] to denote number in position
        cleanednumber = cleanednumber + number[i] # concatenate string

newnumber = int(cleanednumber) # convert string to int
print("The number in int format is: {}". format(newnumber))
print()

# ====================================================================

# using "in" in for loops
# We are going to do same code above but us the "in"

number = "1,23,456,78,9"
print("The length of the second number is: {}". format(len(number)))
cleanednumber = '' # This is initially set to null

for char in number:  # Extracts the character for each position in number string
    if char in '0123456789':
        cleanednumber = cleanednumber + char # Adds to cleaned number and iterates to completion.

newnumber = int(cleanednumber) # Converts string to int
print("The new number in int format is: {}".format(newnumber))
print()

# ====================================================================

# lists: This is a sequence of things that we can use a for loop to iterate.
# Because its a list of strings, we can concatenate to text "This parrot is" using + sign.
# So every time it goes through the loop, it adds each of the list of strings one at a time.

for mood in ["Happy", "Very Happy", "Angry", "Very Angry"]: # A list of strings separated by commas
    print("This parrot is "+mood) # Concatenate lists of strings above to this text
print()

# We can also use normal print format
for mood in ["Sad", "Very Sad", "Excited", "Very Excited"]: # A list of strings separated by commas
    print("This parrot is {}". format(mood)) # We can use normal print format
print()


# Range: using range in for loops
# (0, 25, 5) 0 is first , 25 is last and 5 is interval
# So this will print from 0 to 20
# Note that results end in value of 20 because we are not going to take the last number
# If you use 26 instead of 25, then it will show 25 as the last number in the result

print("using range")
for i in range(0, 25, 5):
    print("i is {}".format(i))


# Nested for loop with range

print()
print("Multiplication table")
for i in range(1,5):  # When i is 1
    for j in range(1,5): # j loops four times
        print("{0} x {1} = {2}".format(i, j, i*j)) # does multiplication until 2nd loop completes
    print("============")  # Change indent level on this print to see different formats


# Results for above code are from up to down
# This is because end of line is usually newline \n
# To put results from left to right, we can add end='\t' to make it a tab instead of newline

print()
print("Results with tab instead of default newline")
print("Multiplication table")
for i in range(1,5):  # When i is 1
    for j in range(1,5): # j loops four times
        print("{0} x {1} = {2}".format(i, j, i*j), end='\t') # add tab instead of default newline
    print("============")




