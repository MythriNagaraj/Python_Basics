'''List-Based Questions
Find the Maximum and Minimum in a List
→ Ask the user to enter numbers into a list and print the max and min values.'''

list = input("enter the number is the list: ")
number_list = [int(num) for num in list.split()]
print(max(number_list))



