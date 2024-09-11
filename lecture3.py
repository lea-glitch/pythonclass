###Lecture 3: Iteration 

##Example 1: while Loops (remember this is case-sensitive)

where=input("You're in the Lost Forest. Go left or right? ")
while where=="right":
    where=input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")

##Example 2: while Loops

n=int(input("Enter a non-negative integer: "))
while n>0:
    print('x')
    n=n-1
##Note that without this last line above (15), the program goes on forever

###Exercise 1 building off of Example 1: expanding the Lost Forest code
## to show a sad face when the user entered the while loop more than 2
#times; use a variable as a counter

n=0
where=input("Go left or right? ")
while where=="right":
    n=n+1
    if n>2:
        print(":(")
    where=input("Go left or right? ")
print("You got out!")

###Above, creating variable n allows us to keep track of how many times 
## we have gone through the loop

###Example 3: Iterate through numbers in a sequence
n=0
while n<5:
    n=n+1

###Example 4: a common pattern

x=4
i=1
factorial=1
while i<=x:
    factorial*=i
    i+=1
print(f'{x} factorial is {factorial}')

### range practice

for i in range(1, 4, 1):
    print(i)
for j in range(1, 4, 2):
    print(j*2)
for me in range(4, 0, -1):
    print("$"*me)

### mysum Example (make the print value 12 by adding +1 to end;
## rather than the original print value being 7)

mysum=0
start=3
end=5
for i in range(start, end+1):
    mysum += i
print(mysum)
