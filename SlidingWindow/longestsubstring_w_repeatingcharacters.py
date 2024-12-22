def lengthOfLongestSubstring(s: str) -> int:
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res,r-l + 1)
        return res


if __name__ == "__main__":
     input = 'abcabcbb'
     output = lengthOfLongestSubstring(input)
     print("this is output",output)

     '''
     r = 0 {a} res = max(0,0-0+1) = 1
     r = 1 {a,b} res = max(1, 1-0+1)=2
    r = 2 {a,b,c} res = (2, 2-0+1 ) = 3
    r = 3 {b,c} remove first in the set or the leftmost which is 'a' then add s[r] which is 'a' index 3 and increment left which now makes leftmost 'b' index 1.
            {b,c,a} res = (3, 3 - 1 +1) = 3 so still res is 3 because leftmost incremented to 1
     '''