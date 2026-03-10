# problem 1

'''Question:- There are n houses build in a line, each of which contains some value in it.

A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two
neighbours left and right side.

What is the maximum stolen value?'''

#Sample Input: val[] = {6, 7, 1, 3, 8, 2, 5}

#Sample Output: 20

'''
n = list(map(int, input().split()))
even = 0         # even and odd usage because we can calculate adjacent houses like 1=3,2=4....
odd = 0                
for i in range(0, len(n), 2): # start,stop,step

    odd+=n[i]   # for adding values of odd index

for i in range(1, len(n), 2): # start,stop,step

    even+=n[i]   #  for adding values of even index

print(max(even,odd)) # to max value of even or odd'''



#problem 2

'''Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’
to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0  '''


#Input 1:
# [###***]   -> Value of S
#Output :

#0 → number of [* and #] are equal 



'''s=input()
a=0  # a means star 
b=0  # b means hash

# for loop is used for check each char one by ine

for i in s:
    if i=='*':  #char is * increase the count
        a+=1
    elif i=='#':  #char is # increase the count
        b+=1
print(a-b)'''


#problem 3
'''
Problem Statement – Ritik wants a magic board, which displays a character for a corresponding number for his science project. Help him to develop such an application.
For example when the digits 65,66,67,68 are entered, the alphabet ABCD are to be displayed.
[Assume the number of inputs should be always 4 ]
'''

#sample input and output

'''
Sample Input 1:

Enter the digits:
65
66
67
68
Sample Output 1:

65-A
66-B
67-C
68-D

Sample Input 2:

Enter the digits:
115
116
101
112
Sample Output 2:

115-s
116-t
101-e
112-p'''

#code

a=int(input())
b=int(input())
c=int(input())
d=int(input())

print(str(a)+"-"+chr(a))

print(str(b)+"-"+chr(b))

print(str(c)+"-"+chr(c))

print(str(d)+"-"+chr(d))






















