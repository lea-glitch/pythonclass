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

### F-Strings

num=3000
fraction= 1/3
print(num*fraction, 'is', fraction*100, '% of', num)
print(num*fraction, 'is', str(fraction*100)+'% of', num)
print(f'{num*fraction} is {fraction*100}% of {num}')

###Conditions for Branching -> Logical Operators
##Remember that for this to work, both objects must be same Type
#here we had to change the int 4 to a str

secret = '4'
guess=input("Guess the secret number between 1-10: ")
if guess==secret :
    print('Correct')
else :print('Wrong')

###Branching Example 1

pset_time=12
sleep_time=2
if (pset_time+sleep_time)>24:
    print('impossible!')
elif(pset_time+sleep_time)>=24:
    print('full schedule!')
else:
    leftover=abs(24-pset_time-sleep_time)
    print(leftover,'h of free time!')
print('end of day')

##Branching Example 2

snumber=6

mguess=int(input("Guess a number: "))
if mguess<snumber:
    print('Too low')
elif mguess>snumber:
    print('Too high')
elif mguess==snumber:
    print("That's exactly it")


