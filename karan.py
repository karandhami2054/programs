nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
find = 36
while i < len(nums):
    if nums[i] == find:
        print(f"found at index {i}")
        
    else:
        print("not found")
    
    i += 1

