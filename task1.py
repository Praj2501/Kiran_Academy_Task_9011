# Task 1
name=input("Enter the name:")
print("Hello World", name)

# Task 2
cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))
Profit_loss=selling_price-cost_price
if Profit_loss>0:
    print("Profit", Profit_loss)
else:
    print("Loss", Profit_loss)

# Task 3:
num1=int(input("Enter the number:"))
if num1%2==0:
    print(num1, "is a Even number")
else:
    print(num1, "is a Odd number")

# Task 4:
age=int(input("Enter the age:"))
if age>=18 and age <= 100:
    print("Eligible Voter")
elif age<=0 or age>100:
    print("Invalid age")
else:
    print("Not an Eligible Voter")

# Task 5:
word1=input("Enter word 1:")
word2=input("Enter word 2:")
if sorted(word1)==sorted(word2):
    print("The words are Anagram")
else:
    print("The words are not Anagram")

