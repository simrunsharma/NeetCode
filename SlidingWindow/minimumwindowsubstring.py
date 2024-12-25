def minWindow(s: str, t: str) -> str:

        #exception with the no string given in problem
        if t == "":
            return ""
        
       
        
        #creating two dictionaries: window and count of t
        window, countT = {}, {}

        #initialize t substring in CountT: 'A': 1, 'B':1, 'C':1
        for char in t:
            countT[char] = countT.get(char,0) + 1
        #print(countT)

        #we want substring in s to be = to length of substring of t
        have, need = 0, len(countT) #len of dictionary for unique words length only
        #current minimal length of 's' substring and indexes
        #infinity because we are trying to see minimum length
        res, reslen = [-1,-1], float('infinity')
        l = 0

        for r in range(len(s)): #index of substring s
            c = s[r] #represents the characters in the s substring
            window[c] = window.get(c,0) + 1
        

            if c in countT and window[c]==countT[c]:
                have +=1
            while have == need:
                if (r-l+1) < reslen:
                #this means we found substring t in s
                    res = [l,r] #current pointers is the string we need to store
                    reslen = (r -l +1) #window size is min substring length
                #shrink window to try and find a smaller substring in s
                window[s[l]] -=1 #popping out the left pointer from window count, so we pop out A from beginning of 's' substring

                #once we pop out left we need to see if current left is in countT and if the value of s[l] in window is less than count[s[l]] 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                
                #now we increment left pointer. so we move from A to D
                l += 1

        # record final l,s for final window size to return
        l,r = res

        # plus one because indexing is exclusive
        return s[l:r+1] if reslen != float('infinity') else ""


if __name__ == "__main__":
     
     s = "ADOBECODEBANC"

     t = "ABC"

     #output = "BANC"

     output = minWindow(s,t)
     print("this is the smallest window t in s",output)

        
        