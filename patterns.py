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


# print triangle of asterisks with specified length
# first get function to solve to know spaces we are dealing with
def know_space(num):
    count = 1
    if (num == 1): return 1
    for i in range(num - 1):
        count += 2
    return count
# function to print actual triangle
def print_triangle(num):
    base = know_space(num)
    for i in range(1, num + 1):
        printed = know_space(i)
        space = (base - printed) // 2
        print(' ' * space , '*' * printed, ' ' * space)

# print_triangle(5)  # Test


# function to print inverted triangle
# we make use of know_space function earlier defined 
def print_inverted_triangle(num):
    base = know_space(num)
    for i in range(num, 0, -1):
        printed = know_space(i)
        space = (base - printed) // 2
        print(' ' * space , '*' * printed, ' ' * space)

# print_inverted_triangle(7) # test


# function to print diamond
# here we also make use of know_space function defined earlier
def print_diamond(num):
    base = know_space(num)
    for i in range(1, num + 1):
        printed = know_space(i)
        space = (base - printed) // 2
        print(' ' * space , '*' * printed, ' ' * space)
    for j in range(num, 0, -1):
        printed = know_space(j)
        space = (base - printed) // 2
        print(' ' * space , '*' * printed, ' ' * space)

print_diamond(6)