arr= [1, 2, 3, 10, 11, 16, 18, 4, 43, 2, 2, 4]

threshold1 = 2
threshold2 = 4

two_four_exists_in_array = False

for element in arr:
    print("Loop Starting")
    if element == threshold1 and threshold2:
        two_four_exists_in_array = True
        break
print(two_four_exists_in_array)

        
