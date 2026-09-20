
# 1.
'''que 3. Remove Duplicate Elements Without Using set)
You are given a list containing duplicate values.
Create a new list containing each value only once, while maintaining the original order.
You are not allowed to use set () .
Example:
Input:
[10, 20, 10, 30, 20, 40, 30]
Output:
[10, 20, 30, 40]


answer ----->

'''

def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

lst = [10, 20, 10, 30, 20, 40, 30]
print(remove_duplicates(lst))



#2.
'''
question 4. Student Marks Analysis
You are given the marks of students in a list.
marks = [78, 45, 90, 32, 67, 89,50, 92]
Write a program to:
1. Find the highest marks.
2. Find the lowest marks.
3. Calculate the average marks.
4. Count the number of students who passed.
5. Count the number of students who failed.
A student is considered passed if marks >= 40.
Expected Output:
Highest: 92
Lowest: 32
Average: 

------------------
solution
--------------

'''



marks = [78, 45, 90, 32, 67, 89, 50, 92]


highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

passed_count = sum(1 for score in marks if score >= 40)

failed_count = sum(1 for score in marks if score < 40)

print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average}")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {failed_count}")


'''
#3.
question 5. Find the Missing Number
You are given a list containing numbers from 1 to n, but exactly one number is missing.
Find the missing number.


'''


def find_missingnumber(nums):
    n = len(nums) + 1
    org_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return org_sum - actual_sum

numbers = [1, 2, 4, 5, 6] 
print(f"Missing Number is: {find_missingnumber(numbers)}")


'''
#4.
question 6. Compress Consecutive Duplicate Characters
You are given a string where some characters occur consecutively.
Create a new string by keeping only one character from each consecutive group.
Example 1:
Input:
"aaabbeccodaa"
Output:
"abcda"

'''
def compress_consecutive(text):
    if not text:
        return ""
    
    result = [text[0]]
    
    
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
            
    return "".join(result)

print(compress_consecutive("aaabbeccodaa")) 




'''
#5.

question 8. A shopping cart contains product names and their prices.
cart =
"
"Laptop": 55000,
"Mouse": 800, "Keyboard": 1500,
"Headphones": 2000
Write a program to:
1. Calculate the total bill.
2. Apply a discount:
• If total >=50,000 ￫ 10% discount
• If total >=20,000 ￫ 5% discount
• Otherwise ￫ no discount
3. Print the final amount.
'''



cart = {
    "Laptop": 55000, 
    "Mouse": 800, 
    "Keyboard": 1500, 
    "Headphones": 2000
}


total_bill = sum(cart.values())

if total_bill >= 50000:
    discount_per = 10
elif total_bill >= 20000:
    discount_per = 5
else:
    discount_per = 0

discount_amount = (discount_per / 100) * total_bill
final_amount = total_bill - discount_amount

print(f"Total bill: {total_bill}")
print(f"Discount values: {discount_per}% (-{discount_amount})")
print(f"Final Amount: {final_amount}")

#6.

'''
question 9. 
The function receives a list of marks for different subjects.
Calculate the average and assign a grade according to these rules:
90 or above ￫ A
75-89 ￫ B
60-74 ￫ C
40-59 ￫ D
Below 40 ￫ F
Additional Rule: If the student scores below 40 in any subject, the final result must be Example 1:
Input :
[85, 90, 78, 92, 88]
Output :
Average: 86.6
Grade: B
Result: Pass
Example 2:
Input:
"Fail" regardless of the average.
'''

def calculate_grade(marks):
    if not marks:
        return "No marks provided"
    
    failed_subject = any(mark < 40 for mark in marks)
    average = sum(marks) / len(marks)
    

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'


    result = "Fail" if failed_subject else "Pass"

    return (f"Average: {average:} Grade: {grade} Result: {result}")


print(calculate_grade([85, 90, 78, 92, 88]))  
