#%% [markdown]
# ## Lesson 2
# # Ranges
# You can get sequences of numbers with the `range` function,
# that accepts a `start`, `stop` and `step` parameter. 
# `start` is inclusive, `stop` is exclusive.
#%%
print('Numbers from 0 to 4')
for number in range(5):
    print(number)

print('Numbers from 1 to 4')
for number in range(1, 5):
    print(number)

print('Numbers from 1 to 4, step 2')
for number in range(1, 5, 2):
    print(number)
#%% [markdown]
# # Slices
# This is very similar to the slice notation for sequences like lists or strings
#%% 
print('Numbers from 1 to 4, step 2')
numbers = [0, 1, 2, 3, 4, 5]
for integer in numbers[1:5:2]:
    print(integer)

print('Characters from a to l, step 2')
word = 'abcdefghijkl'
for character in word[::2]:
    print(character)
#%% [markdown]
# Leaving out a value means the slice continues until the end 
# or begins at the start of the sequence. 
# Negative values count backwards from the end. 

#%% 
print('Last character:', word[-1])
print('Word backwards:', word[::-1])
#%% [markdown]
# # Conditional logic
# The indented code following an `if`-statement is only executed if the expression is True. 
# Otherwise the program goes to the next non-indented line. 
# In particular, there may be an `elif` (else if) clause that is tested next. 
# If no `if` or `elif` clause evaluates to True, then the `else` clause will execute. 
#%% 
old = 80
young = 17
if young > old:
    print('Young is older than old')
elif young < old:
    print('Young is younger than old')
else:
    print('This will never be printed')

print('-> This is after the if block')
    
#%% [markdown]
# ## Task
# Given an integer n, 
# perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

#%%
n = 12
is_weird = False

# TODO: Add conditional logic here


print('Weird' if is_weird else 'Not weird')
#%% [markdown]
# # Leap Years
# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source
#%% [markdown]
# ## Task
# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.
# Your function must return a boolean value (True/False)
#%% 
def is_leap_year(year):
    is_leap = False
    # TODO: Add logic here

    return is_leap

current_year = 2019
next_year = 2020
print(current_year, 'is leap year:', is_leap_year(current_year))
print(next_year, 'is leap year:', is_leap_year(next_year))

#%%


