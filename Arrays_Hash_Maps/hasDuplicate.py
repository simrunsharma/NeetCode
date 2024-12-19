def hasDuplicate(nums):
    for i in range(len(nums)):
        temp = nums[i]
        for j in range(i+1,len(nums)):
            if temp == nums[j]:
                return True
    return False # make sure it runs through every iteration

'''essentially I compare i = 0 which is 1 with every number (2,3,3)
and then I check to see if i = 1 which is 2 is equivalent to 3, 3.
You might say why do we only check till the len(nums) in j? Its because 
1 and 2 were compared in i =0 so in i = 1 we don't need to compare 2 with 1.'''

def alternate(nums):
    dicts = {}

    for i in nums:
        dicts[i] = dicts.get(i,0) + 1
        if dicts[i] > 1:  
            return True
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 3]
    output = hasDuplicate(nums)
    print(output)

    output2 = alternate(nums)
    print("this is the alternate solution", output2)

    #Output: true because three is there twice
