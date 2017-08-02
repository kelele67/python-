import math
def isPlayRight(nums):
    x = [n for n in range(10)]
    chunks = []
    result = []
    for i in range(9):
        if abs(nums[i+1] - nums[i]) == 1:
            chunks.append(nums[i:i+2])
        else:
            if abs(nums[i+2] - nums[i+1]) == 1:
                continue
            else:
                chunks.append([nums[i+1]])

    for chunk in sorted(chunks):
        chunk = sorted(chunk)
        result += chunk
    if result == x:
        return True
        
    return False

while True:
    nums = map(int, list(raw_input()))
    if isPlayRight(nums):
        print "yes"
    else:
        print "no"
