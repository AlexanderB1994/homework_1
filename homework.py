my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list = sorted(my_list)
# my ascending list
print(my_list)
# my descending list
print(sorted(my_list, reverse=True))
# even numbers
print(my_list[1::2])
# odd numbers
print(my_list[::2])
# the multiples of 3
print(my_list[2::3])