def characterReplacement(s: str, k: int) -> int:
    #creating has map of counts of each letter in string
    count = {}
    l = 0 #beginning of string
    res = 0 #length of string

    for r in range(len(s)): # right pointer shifts to the right

        #getting counts of each letter in string so A's and B's
        count[s[r]] = 1 + count.get(s[r],0)

        if (r-l+1) - max(count.values()) > k:
            #we want to shrink the window size
            count[s[l]] -=1
            l+=1
        res = max(res,r-l+1) #we want the maximum string between shrinking size and res
    return res

if __name__ == "__main__":

    input ="ABABBA"
    k=2
    output = characterReplacement(input,k)
    print("this is the longest string with replacement",output)
