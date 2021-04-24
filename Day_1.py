#1.Condition Inside the print Function

print("Odd" if int(input("Enter a num: "))%2 else "even")

#2.Conditional List — All (The all method can be used to match all the conditions or work in place of the and condition.)

salary = 35000
bonusTimes=2
incrementPerYear=1500

listCond = [salary>3000,
            bonusTimes>1,
            incrementPerYear>1000
            ]

if(all(listCond)):
    print("I will do the Job")
else:
    print("Sorry I have to look for another job")

#3.Conditional List — Any (We can use the same conditional list with the any method in Python to check whether anyone’s condition satisfies it.)

salary = 35000
bonusTimes=2
incrementPerYear=1500

listCond = [salary>3000,
            bonusTimes>3,
            incrementPerYear>500
            ]

if(any(listCond)):
    print("I will do the Job")
else:
    print("Sorry I have to look for another job")

#4. Swapping in easy way 
salary=85000
exp=3
salary,exp=exp,salary
print(exp)  

#6. Take out the Duplicate Data

li = [1,5,6,8,5,9,5,9,6,5,4,8,5]
print(list(set(li)))

#7. Most Repeated Object

li=[1,5,8,6,5,9,6,9,5,6,9,6,5,4,"a","a","b","b","a","a","a"]
print(max(set(li), key=li.count))

#8. Reverse 

name = "Jahid Hasan Shawon"
print(name[::-1])