//Write a program which does the following:
//printing al data from 1 to 15 but skipping 11 in python


#Update the '_' in the code below to solve the problem

c = 0

#Note that print(c) is coming after c = c + 1
#How does this change the condition of the while loop?
while c < 15:
  c = c + 1
  if c == 11 :
   continue
  print(c)

 