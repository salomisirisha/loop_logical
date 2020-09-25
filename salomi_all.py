# num = int(input("Enter  number"))  
# sum = 0  
# a=num  
# while a < 0:  
#    b = a % 10  
#    var= b ** 3 
#    sum=sum+var 
#    a //= 10  
# if a== sum:  
#    print("it is an Armstrong number")  
# else:  
#    print("it is not an Armstrong number")  


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# i=0
# while i<len(marks):
#     sum=0
#     j=0
#     while j<len(marks[i]):
#        a=marks[i][j]
#        sum=sum+a
#        j=j+1
#     avg=sum/len(marks[i])
       
#     print(avg)
#     i=i+1


# char_list= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# b_list=[]
# while i<len(char_list):
#      k=0
#      count=0
#      c_list=[]
#      while k<len(char_list):
#           if char_list[i]==char_list[k]:
#                count=count+1
#           k=k+1
#      c_list.append(char_list[i])
#      c_list.append(count)
#      if c_list not in b_list:
#           b_list.append(c_list)
#      i=i+1
# print(b_list)



# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# coredepathi_count=0
# lakhpathi_count=0
# dilwale_count=0
# while i<len(kitna_paisa_hai):
#     if kitna_paisa_hai[i]>=10000000: 
#         coredepathi_count=coredepathi_count+1   
#     if kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<10000000:
#         lakhpathi_count=lakhpathi_count+1
#     if kitna_paisa_hai[i]<100000:
#         dilwale_count=dilwale_count+1
#     i=i+1
# print(coredepathi_count,"coredepathi hai",lakhpathi_count,"lakhpathi hai",dilwale_count,"dilwale hai")



# i=20
# while i<=100:
#     if i%2==0:
#         print(i)
#     i=i+1



# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# a_list=[]
# while i<len(n):
#      if n[i] not in a_list:
#           a_list.append(n[i])
#      i=i+1
# print(a_list)


# guess=5
# i=1
# while i<=5:
#     num=int(input("enter your num"))
#     if num<guess:
#         print("your number is small!please try again")
#     elif num>guess:
#         print("your number is big!please try again")
#     elif num==guess:
#         print("congratulations!you have done it.")
#         break
#     i=i+1



# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# empty_list=0
# i=0
# while i < len(n):
#     if n[i] not in empty_list:
#         empty_list.append(n[i])
#     i=i+1
# print(empty_list)



# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# list3=[]
# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         list3.append(list1[i])
        
#     i=i+1
# print(list3)



# name=["n","a","y","a","n"]
# rev=name[::-1]
# print("reversed name:",rev)
# if name==rev:
#     print("it is palendrome")
# else:
#     print("it is not a palendrome")



# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# sum=0
# i=0
# while i<len(marks):
#    j=0 
#    while j<len(marks[i]):
#        a=marks[i][j]
#        sum=sum+a
#        j=j+1
#    i=i+1
# print(sum)



# i=2
# while i<=100:
#     j=2
#     while j<=100:
#         print("it is not a prime number")
#         break
#     j=j+1
#     i=i+1  
# else:
#     ("it is a prime number")


# i=1
# while i<=100:
#     if i%3==0 and i%7==0:
#         print(i,"navgurkul")
#     elif i%3==0:
#         print(i,"nav")
#     elif  i%7==0:
#         print(i,"gurukul")
#     i=i+1




# num=int(input("Enter number:"))
# a=num
# rev=0
# while num>0:
#     b=num%10
#     rev=rev*10+b
#     num=num//10
# if a==rev:
#     print("The number is a palindrome!")
# else:
#     print("The number is not a palindrome!")



# i=1
# while i<=5:
#     j=i
#     while j<=5:    
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1



# n = int(input("Enter any number: "))
# sum1 = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum1 = sum1 + i
# if (sum1 == n):
#     print("The number is a Perfect number!")
# else:
#     print("The number is not a Perfect number!")



# num=int(input("enter number"))
# i=2
# while i<num:
#     if num%i==0:
#         print("it is not a prime number")
#         break
#     i=i+1
# else:
#     print("it is a prime number")









