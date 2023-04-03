#!/usr/bin/env python
# coding: utf-8

# In[23]:


name = input("Enter a name: "); print("The number of characters in the name is:", len(name))


# In[24]:


print(len(input("what is your name? ")))


# In[30]:


a = input("a:")
b = input("b:")



print("a=" + a)
print("b=" + b)


# In[31]:


a = input("a:")
b = input("b:")

print("Before swapping: a=" + a + " b=" + b)

# Swap the values of a and b using a temporary variable
temp = a
a = b
b = temp

print("After swapping: a=" + a + " b=" + b)


# In[36]:


def function1(x):
    print(x)
    print("sting")
    return 3*x

function1(4)


# In[35]:


print(a)


# In[42]:


name = input("What is your name? ")
length = len(name)
print(length)


# In[15]:


# Python Project

#1. Create a Greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see example at :  https://band-name-generator-end.appbrewery.repl.run/

#1. Create a Greeting for your program.
print('Welcome to the Band Name Generator.')

#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
#   band_name = "{} {}".format(city_name, pet_name)
#   print("Your band name could be {}".format(band_name))

print("Your band name could be " + city + "" + pet)


# In[14]:


print('Welcome to the Band Name Generator.')
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
band_name = "{} {}".format(city_name, pet_name)
print("Your band name could be {}".format(band_name))


# In[21]:


# How can we concatenate strings in Python?

# Using the format() function 
# Using the + operator 


# In[23]:


str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1 + str2
print("Concatenated two different strings:",str)


# In[ ]:




