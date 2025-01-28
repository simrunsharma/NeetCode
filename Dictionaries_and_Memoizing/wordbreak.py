def wordBreak(s, wordDict) -> bool:
        
        #create base case
        if not s:
            return True
        
        #length of the word
        n = len(s)

        #find prefixes and check if in wordlist
        for i in range(1,n+1):

            pre = s[:i]

            #recrusive calls until the word is empty
            if pre in wordDict and wordBreak(s[i:],wordDict):
                return True
        
        #if not in the WordDict
        return False




if __name__ == "__main__":
    words = ["leet","code"]
    word = "leetcode"
    x = wordBreak(word,words)
    print(x)