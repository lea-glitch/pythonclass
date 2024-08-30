### Recap from Lec 1
pi=355/113
print(pi)

### Intro to Strings

b=":"
c=")"
s1=b+2*c
print(s1)
f="a"
g=" b"
h="3"
s2=(f+g)*int(h)
print(s2)

### len() is a function to retrieve length of string

s="abc"
print(len(s))

### Slicing to get a Substring

alphab= 'abcdefghijklmnopqrstuvwxyz'
print(alphab[3:6])
print(alphab[::-1])
print(alphab[4:1:-2])

s="ABC d3f ghi"
print(s[3:len(s)-1])
print(s[4:0:-1])
print(s[6:3])

### Printing multiple objects

print(pi, alphab)

###Input function to bind value to a variable

x=input()
print(x+'... something an idiot would say')

##Second example

verb=input("enter verb: ")
# Coe is commenting out your code so it doesn't run this whole thing twice. 
# print("I can",verb,"better than you!")
# print((verb+" ")*5)

## Or, by defining a function that performs the above script but only uses one line of code:

def butBetter():
    print("I can",verb,"better than you!")
    print((verb+" ")*5)

butBetter()