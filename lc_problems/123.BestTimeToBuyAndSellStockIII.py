class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        the variables are numTransaction, hold a stock or no stock
        '''
        profit_T1_H0 = profit_T2_H0 = 0
        profit_T1_H1 = profit_T2_H1 = float('-inf')
        for p in prices:
            # at the end of current day,

            # if you used 2 transaction and hold 0 stock
            # you might hold 0 stock yesterday
            # or hold 1 stock yesterday and sold it today
            # we recorded all different choices yesterday
            # and we will choose the max profit for this 
            # posibility today
            profit_T2_H0 = max(profit_T2_H0, profit_T2_H1 + p)
            
            # if you used 2 transaction and hold 1 stock
            # you might hold 1 stock yesterday
            # or hold 0 stock yesterday and bought one today
            profit_T2_H1 = max(profit_T1_H0 - p, profit_T2_H1)

            # if you used 1 transaction and hold 0 stock
            # you might hold 0 stock yesterday
            # or hold 1 stock yesterday and sold one today
            profit_T1_H0 = max(profit_T1_H0, profit_T1_H1 + p)

            # if you used 1 transaction and hold 1 stock
            # you might hold 1 stock yesterday
            # or hold 0 stock yesterday and bought one today
            profit_T1_H1 = max(-p, profit_T1_H1)

        # the max profit should be used two transaction and 
        # hold 0 stock
        return profit_T2_H0
