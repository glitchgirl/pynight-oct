arr1 = [96, 15, 27, 75, 16, 1, 27, 26, 3, 25, 66, 52, 94, 78, 51, 7]
arr1.sort()
print(arr1)

def divide_chunks(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
# How many elements each 
# list should have 
n = 4
x = list(divide_chunks(arr1, n)) 
print (x) 