from datetime import datetime

now = datetime.now() # time object

print("now =", now)

file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
  
# Writing a string to file
file1.write(s)
  
# Writing multiple strings
# at a time
file1.writelines(L)
  
# Closing file
file1.close()

now2 = datetime.now() # time object

print("now2 =", now2)
print("difence", now2-now)