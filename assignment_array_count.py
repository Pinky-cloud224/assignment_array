arr = [1, 2, 3, 10, 11, 16, 18, 4, 43, 2, 2, 4]

threshold1 = 2
threshold2 = 4

two_four_exists_in_array = False
count_two_in_array = 0

for element in arr:
    if element == threshold1:
        two_four_exists_in_array = True
        count_two_in_array +=1
print(count_two_in_array)

two_four_exists_in_array = False
count_four_in_array = 0

for element in arr:
    if element == threshold2:
        two_four_exists_in_array = True
        count_four_in_array +=1
print(count_four_in_array)

print("Two exists in:",count_two_in_array,"times")
print("Four exists in:",count_four_in_array,"times")






        
