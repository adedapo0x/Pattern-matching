# print increasing number of asterisks
def asc_order(number):
    for i in range(1, number + 1):
        print('*' * i)

# asc_order(5)  # Test


# print ascending increasing numbers
def asc_numbers(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end = '')
        print()

# asc_numbers(5) # Test


# print ascending numbers same number of times
def repeat_numbers(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(i, end='')
        print()
    
# repeat_numbers(5) # Test


# print decreasing number of asterisks
def decrease_star(num):
    for i in range(num, 0, -1):
        print('*' * i)

# decrease_star(5) # Test


# print descending numbers in decreasing order
def decrease_number(num):
    count = num
    for i in range(num, 0, -1):
        for j in range(1, count + 1):
            print(j, end='')
        count -= 1
        print()

# decrease_number(5) # Test

