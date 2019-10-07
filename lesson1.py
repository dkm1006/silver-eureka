# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # Variables and Types
# 
# ## Assignment
# In Python you assign a value to a *variable* name with **=** like this. Case is important, i.e. the name Mimi is not the same as mimi

#%%
x = 5

#%% [markdown]
# There are several built-in datatypes:
# 
# ## Strings
# *Strings* are sequences of characters, enclosed by **" "** or **' '**. Values can be printed out with the *print* function.

#%%
name = 'Mimi'
print(name)
other_name = "Nenad"
print(other_name)

#%% [markdown]
# ## Numbers
# There are *int*egers like 4 and *float*ing point numbers like 4.1

#%%
integer = 28
floating_point = 3.2
print(integer)
print(floating_point)

#%% [markdown]
# We can add, subtract, multiply, divide, etc. numbers

#%%
print(integer + floating_point)
print(integer - floating_point)
print(integer * floating_point)
print(integer / floating_point)
# This is a comment: 2**4 is equivalent to 2*2*2*2
print(integer ** 2)
# // returns the integer that results from the division
print(integer // floating_point)
# % returns the remainder of a division
print(integer % 3)

#%% [markdown]
# We can also *compare* values:
# == *(equal)*, != *(unequal)*, < *(smaller than)*, > *(greater than)*, <= *(smaller or equal)*, >= *(greater or equal)*

#%%
print(2**4 == 2*2*2*2)
print(2**4 != 5)
print(4.1 < 4)
print(4.1 > 4)
print(4.1 <= 4)
print(4.1 >= 4.1)

#%% [markdown]
# If we compare values that cannot be compared because they are of a different type we may run into a **TypeError**

#%%
print(2 == 'a')
print(2 < 'a')

#%% [markdown]
# ## Lists
# Lists are sequences of objects, enclosed by [ ] and separated by ,

#%%
list_of_values = ['Djordje', integer, floating_point]
print(list_of_values)

#%% [markdown]
# We can add values to a list by calling the **append** method, which adds the new item to the end of the list, or the **insert** method to place it at an index that we specify. 

#%%
list_of_values.append(other_name)
print(list_of_values)
list_of_values.insert(0, 'At beginning')
print(list_of_values)

#%% [markdown]
# We can retrieve and remove an item by calling **pop**

#%%
retrieved_value = list_of_values.pop()
print('Retrieved ' + str(retrieved_value) + ' from list')  # The function str converts a value to a String
print(list_of_values)
retrieved_value = list_of_values.pop(2)
print('Retrieved ' + str(retrieved_value) + ' from list')
print(list_of_values)

#%% [markdown]
# ## Dictionaries
# Dictionaries are collections of key: value pairs enclosed by { }

#%%
mimi = {
    'firstname': 'Jasmin',
    'lastname': 'Benn',
    'nickname': name,
    'age': 28
}
print(mimi)

#%% [markdown]
# ## Accessing items
# We can access single items from lists and dictionaries (and other sequences) with **name\[index/key\]**.
# Careful, the indices start with 0!

#%%
print(mimi['lastname'])
print(list_of_values[1])

#%% [markdown]
# We can also change the value at a particular index or key in a similar way.

#%%
mimi['lastname'] = 'Benn-Maksimović'
list_of_values[1] = 28
print(mimi['lastname'])
print(list_of_values[1])

#%% [markdown]
# ## Loops
# We can access all items in a list in turn by *looping* through it.
# 
# ### for-loop

#%%
print('Looping through a list:')
for value in list_of_values:
    print(value)
    
print('Looping through a dictionary:')
for characteristic in mimi:
    print(characteristic)

#%% [markdown]
# As you can see, we only got the keys of the dictionary, not the values. 
# To access the values we can either use dictionary_name.items() or we simply access the values by the key

#%%
print('Looping through the items of a dictionary:')
for key, value in mimi.items():
    print(key + ': ' + str(value))

print('Looping again:')
for key in mimi:
    print(str(mimi[key]) + ' is the value of the key ' + key)


#%% [markdown]
# ## Exercise
# Create a dictionary for Djordje, loop through its items and compare them to Mimi's values


