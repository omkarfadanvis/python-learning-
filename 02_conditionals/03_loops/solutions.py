# number= [1,2,3,4,5,6,7,8,9, 10]
# positive_count=0
# negative_count=0

# for n in number:
#     print(n)
#     if n >0:
#         positive_count += 1
#     elif n < 0:
#         negative_count += 1

# print("Positive count is:", positive_count)
# print("Negative count is:", negative_count)

# number= [1,2,3,4,5,6,7,8,9, 10]
# even_sum=0
# odd_sum=0
# for n in number:
#     if n % 2 == 0:
#         even_sum = even_sum + n 
#     else:
#         odd_sum = odd_sum + n

# print("even number sum is:", even_sum)
# print("odd number sum is:", odd_sum)

# next question 

# n = int(input("Enter a number "))
# even_sum=0
# odd_sum=0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i

# print("even number sum is:", even_sum)
# print("odd number sum is:", odd_sum)

# number = 3

# for i in range (1, 11):
#     if i == 5:
#         continue
#     print(number *i)

# input_str =  "ommmakkaar"

# for char in input_str:                
#     print(char)                       i want to know can i display the output of the repeated letters only once 
#     if input_str.count(char) > 1:
#         print(f"{char} is a duplicate character")
#         break

# i =input("Enter a number: ")
# i = int(i)
# count = 1
# while i > 0:
#     count = count * i
#     i = i -1 

# print("Factorial is:", count)

# while True:
#     n = int(input("Enter a number: "))
#     if 1 <= n <= 10:
#         print ("Valid input")
#     else:
#         print ("Invalid input")

num = int(input("Enter a number: "))
for  i in range(2,num):
    if (num % i) == 0:
        print(f'{num} is not a prime number')
        break
else:
     print(f"{num} is a prime number")