#Python program to find second largest number in a list


#Method 1: Sorting is an easier but less optimal method. Given below is an O(n) algorithm to do the same.

list1 = [10, 20, 4, 45, 99] 
  
mx=max(list1[0],list1[1])  
secondmax=min(list1[0],list1[1])  
n =len(list1) 
for i in range(2,n):  
    if list1[i]>mx:  
        secondmax=mx 
        mx=list1[i]  
    elif list1[i]>secondmax and mx != list1[i]:  
        secondmax=list1[i] 
    else: 
        if secondmax == mx: 
            secondmax = list1[i] 
  
print("Second highest number is : ",str(secondmax))

#Method 2 : Sort the list in ascending order and print the second last element in the list.

# Python program to find largest 
# number in a list 
  
# list of numbers 
list1 = [10, 20, 4, 45, 99] 
  
# sorting the list 
list1.sort() 
  
# printing the second last element 
print("Second largest element is:", list1[-2]) 

#Method 3 : By removing the max element from list


# Python program to find second largest 
# number in a list 

# list of numbers 
list1 = [10, 20, 4, 45, 99] 

# new_list is a set of list1 
new_list = set(list1) 

# removing the largest element from temp list 
new_list.remove(max(new_list)) 

# elements in original list are not changed 
# print(list1) 

print(max(new_list)) 




#anjay had m rupees and cost of each chocolate was c rupees. Shopkeeper gave away one chocolate for three wrappers. In this problem lets generalise the question saying, Sanjay has m rupees, each chocolate costs c rupees, shopkeeper will give away k chocolates for w wrappers. Can you find now how many chocolates Sanjay will be able to eat?

Input: 4 integers separated by space in order m, c, w, k
 
#Sample input:
#15, 2, 3, 1
 
#Sample output:
#10

#method 1:
n = input()
i = n.split(',')
m, c, w, k = [int(x) for x in i]

total_eaten = 0
current_money = m

# buy as many as we can
buy = current_money // c

# reduce money, increase eaten
current_money -= buy * c
total_eaten += buy

# then start trading wrappers

wrappers = total_eaten

while True:
  # we get extra chocolate for wrappers back
  extra_choc = (wrappers // w)

  # remove the wrappers
  wrappers -= extra_choc * w

  if extra_choc == 0:
     # no more extra chocolate :(
    break

  # eat the extra chocolate
  total_eaten += extra_choc * k

  # and also increase how many wrappers we have
  wrappers += extra_choc * k

print(total_eaten)



#method 2:
#Input: 4 integers separated by space in order m, c, w, k
 
#Sample input:
#15, 2, 3, 1

number = input()
myList = number.split(',')
m = int(myList[0])
c = int(myList[1])
k= int(myList[3])
w = m//c
chocolate = m//c
#start writing your code here
while w//3 !=0 :
    wrapper = (w//3)*k
    chocolate = chocolate + wrapper
    w= wrapper +w%3
print(chocolate)



letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def convert_str(string, step):
    converted = ""
    for char in string:
        if char != "Z":
            converted += letters[letters.index(char) + step]
        else:
            converted += letters[step-1]
    return converted

in_str = "banana"
print(convert_str(in_str, 7))















a=[1,2,3]
b=[4,5]
d=list(map(lambda i:list(i),map(lambda i:map(lambda j:i+j,b),a)))
c=[]
for i in d:
    for j in i:
        c.append(j)
print(c)
#added one more map to breakdown, and then doing flatten list
#there is a way to flatten list is sum(listoflists,[])


x = [["a","b"], ["c"]]

result = sum(x, [])



#1st input
=========
orders = [ ["34587", "Medicines", 4, 40.95],
           ["98762", "Books", 5, 56.80],
           ["77226", "Items", 3,32.95],
           ["88112", "Groceries", 3, 24.99]]
		   
		   
		   
for each row, two values  ordernumber and (quantity*price per item) , if (quantity*price per item) < 100 then add 20



orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
                  map(lambda x: (x[0],x[2] * x[3]), orders)))

print(invoice_totals)
