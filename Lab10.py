#!/usr/bin/env python
# coding: utf-8

# In[48]:


my_file_name = input('Enter a filename that you want to open: ')   # Prompts user to enter a file name for the file they wish to analyze 


# In[49]:


print(type(my_file_name))                           # To show user type of file selected it prints the type of file
my_file_name


# In[50]:


print(my_file_name, '\n')                           # This Prints the selevted files name 
temp_file = open(my_file_name, "r")                 # Opens the selected file for the program to read

for line_str in temp_file:                          # Observes the text in the file and for each line of text 
    print(line_str, end='')                         # it uses a new line

temp_file.close()                                   # This closes the file 


# In[51]:


temp_file = open(my_file_name, "r")                 # Opens original file to read
type(temp_file)                                     # Creates a temporary file with the same contents


# In[52]:


print(temp_file)


# In[53]:


temp_file.close()                                   # Exits the open file


# In[54]:


my_new_file_name = my_file_name + 'Backwards'       # Creates a new file to store edited text in

fout = open(my_new_file_name, "w")                  # Opens new file in a mode capable of writing/editing
fout.close()

longline = ''                                       # Gets data for new file from the old file
fin = open(my_file_name, "r")

for line in fin:                                    # Reads over each line of the text
    longline = longline + line                      # Adds lines read to longline variable

fin.close()


# In[55]:


longline                                            # The file is printed as an unbroken string


# In[56]:


print(longline)                                     # The file has different lines of text


# In[5]:


def reverse_string(input_string):                   # This part of the code creates the function to rewrite text backwards
    output_string = ""                              # It defines reverse string as well as its input the initializes the output as empty
    for char in input_string:                       # Reads through one character at a time and adds it to the output string
        output_string = char + output_string
    return output_string

print(reverse_string('step on no pet'))             # Input function to be printed backwards


# In[ ]:




