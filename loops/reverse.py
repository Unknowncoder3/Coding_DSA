#Reverse a number using loop
num=int(input("Enter a number to reverse: "))
reversed_num=0
while(num>0):
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("Reversed Number: ",reversed_num)

#Reverse a string using loop
string=input("Enter a string to reverse: ")
reversed_string=""
for i in range(len(string)-1,-1,-1):
    reversed_string+=string[i]
print("Reversed String: ",reversed_string)


