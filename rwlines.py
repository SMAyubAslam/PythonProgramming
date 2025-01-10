# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# f = open('myfile.txt', 'r')
# while True:
#     lines = f.readline()
#     # print(lines)
#     if not lines:
#         break
#     print(lines)

# The readlines() method reads all the lines of the file and returns them as a list of strings.

# f = open('myfile.txt','r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(',')[0])
#     m2 = int(line.split(',')[1])
#     m3 = int(line.split(',')[2])
#     print(f'Marks of student {i} in English is {m1*2}')
#     print(f"Marks of student {i} in Maths is {m2*2}")
#     print(f"Marks of student {i} in SST is {m3*2}")
    
#     print(line)

# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# Here's an example of how to use the writelines() method:

# f = open('myfile2.txt','w')
# lines = ('line1\n','line2\n','line3\n')
# f.writelines(lines)
# f.close()

# This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

f = open('myfile2.txt','w')
lines = ['Line1','Line2','Line3']
for line in lines:
    f.write(line + '\n')
# f.close()

