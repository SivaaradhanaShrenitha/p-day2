name = "shrenitha"
name[0]="s"
name = "s"+"hrenitha"
print(name)

str1 = "All silver tea cups"
for i in range(len(str1)):
    if str1[i]==" "and str1[i+1]!=" ":
        str1 = str1[:i+1]+str1[i+1].upper()+str1[i+2:]
print(str1)#to print starting letter capital

print(input("enter").title())

list = "1 2 3 4"
list=list.split()
print(list)

a = "all silver tea cups"
b = a.split()
c= "_".join(b)
# print(c) #snake


a= "all silver tea cups"
b = a.split(" ")
c = "-".join(b)
print(c) 

a= "all silver tea cups".title()
b = a.split(" ")
c = "".join(b)
print(c)  #pascal


a= "all silver tea cups".title()
b = a.split(" ")
c = "".join(b)
c=c[0].lower()+c[1:]
print(c) #camel


n = input().lower()
c = 0 
for i in n:
    if i in "aeiou":
        c+=1
print(c) #for vowel count

n = input()
new_str =" "
for i in n:
    if i.isupper():
        new_str += i.lower()
    else:
        new_str += i.upper()
print(new_str) #coverts upper to lower and vice versa

l1 = input()
l2 = sorted(l1)
print(l2[len(l2)-1]) #to find largest num

l1 = input()
l2 = sorted(l1)
print(l2[len(l2)-2]) #second largest

list_1 = [3,5,6,7,8,9]
highest = list_1[0]
for i in range(len(list_1)):
    if list_1[i]>highest:
        highest = list_1[i]
print(highest)        


        

    
