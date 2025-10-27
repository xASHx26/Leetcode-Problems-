'''
class Solution(object):
    def maxProfit(self, prices):
        max_value=0
        min_value=float("inf")
        if len(prices)<=1:
            return 0
        for i in prices:
            if i<min_value:
                min_value=i
            profit=i-min_value

            if profit>max_value:
                max_value=profit
        return max_value



min profit is infiity 
if one of the price is bigger then min then min = price
and profit will be price - min profit

if profit > max profit

then return the max profit
'''




class Solution(object):
    def maxProfit(self, prices):
        cur=prices[0]
        max_price=0
        max_profit=0

        for i in prices:
            if i<cur:
                cur=i
                max_price=i
            if max_price<i:
                max_price=i
                max_profit=max(max_profit,max_price-cur)
        return max_profit


'''

cur price is the first price

check if cur price is bigger then the price if it then the less price is the curr and max price price

if max price is less the price then bigger price is the max price then just return the maxprofit which is maxprice -cur
'''