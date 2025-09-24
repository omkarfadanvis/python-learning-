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

number = 3

for i in range (1, 11):
    if i == 5:
        continue
    print(number *i)

