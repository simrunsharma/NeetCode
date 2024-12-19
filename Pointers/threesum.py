def threeSum(nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: #b/c if positive number then sum already > 0
                break

            if i > 0 and a == nums[i - 1]: #first iteration can be unique but next iteration i = 1 we see if the current and previous value are duplicates if so go to next iteration (continue) loop
                continue

            l, r = i + 1, len(nums) - 1 # b/c 3sum = i(current) + l(i+1)+r(last) = 0
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #then decrease positive numbers
                    r -= 1
                elif threeSum < 0: #then increase negative numbers
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 # this is because if triplet = -1,-1,2 we can have another triplet that starts with -1 but l and r could be 3 and 2
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: #we don't want to have same triplet duplicates so we check if first and 2nd of triplet are duplicates
                        l += 1
                        
        return res


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    output = threeSum(nums)
    print(output)
# expepcected answer: Output: [[-1,-1,2],[-1,0,1]]
