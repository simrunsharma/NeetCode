def isAnagram(s: str, t: str) -> bool:
        counts = {}
        countc = {}

        for char in s:
            counts[char] = counts.get(char,0) + 1 
        for c in t:
            countc[c] = countc.get(c,0) + 1
        print(counts)
        print(countc)
        return counts == countc

if __name__ == "__main__":
     
     s = "racecar"
     t = "carrace"

     output = isAnagram(s, t)
     print("this is if its made of the same letters each string - an anagram",output)