def maxProfit(self, prices: List[int]) -> int:
    # have l and r pointer
    # profit tracker

    # loop through will R is less than len
    # if l < r
    # calculate profit of this
    # store new max profit of this versus current profit
    # else
    # if l > r
    # meaning we move left = right (buy is more than sell)

    # add one to our sell price or the right

    l = 0
    r = 1
    maxProf = 0

    while r < len(prices):

        if prices[l] < prices[r]:
            curProf = prices[r] - prices[l]
            maxProf = max(maxProf, curProf)
        else:
            l = r

        r += 1

    return maxProf
