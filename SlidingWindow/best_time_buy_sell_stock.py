def maxProfit(prices) -> int:
        profit = 0
        min = prices[0]
        r = 1
        while r < len(prices):
            # print(f"this is min {min} and r {r}")
            new_profit = prices[r] - min
            # print("this is profit",new_profit)
            if new_profit > profit:
                profit = new_profit
                
            if min > prices[r]:
                min = prices[r]
                # print(f'new min {min}')
            
            
            
            r +=1
           
        return profit

def alternate(prices1):
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell  = prices[j]
            res = max(res, sell - buy)
    return res    

if __name__ == "__main__":
        prices = [10,1,5,6,7,1]
        
        output = maxProfit(prices)
        print("This is the output",output)

        prices1 =  [10,8,7,5,2]
        alternate(prices1)
        output2 = maxProfit(prices1)
        print("alternate output from neetcode", output2)

        #Output: 6 is this because you buy 10 dollars for the first min
        #price and then go to next price and see if its a smaller minimum buying price. 
        #Then we sell for the next price and see if the profit is high and positive and return that profit
