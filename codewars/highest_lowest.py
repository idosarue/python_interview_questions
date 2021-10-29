# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

# one solution
def first_high_and_low(numbers):
    new_li = numbers.split()
    li = []
    for num in new_li:
        li.append(int(num))
    list().sort()
    return str(sorted(li)[-1]) + ' ' + str(sorted(li)[0])
print(first_high_and_low("1 2 -3 4 5"))

#second solution

def second_high_and_low(numbers):
    li = [int(num) for num in sorted(numbers.split())]
    return f'{li[-1]} {li[0]}'
    
    #second solution

print(second_high_and_low("1 2 -3 4 5"))


def my_sort(arr):
    li = []
    for i in arr:
        li.append(arr.pop(min(arr)))
        print(li)
    print(li)
    # for i in arr:
    #     print(min(arr), 'min')
    #     x = arr.pop(arr.index(min(arr)))
    #     li.append(x)
    #     print(arr)
        
    # print(li)
my_sort([1,2,-3,4,5])