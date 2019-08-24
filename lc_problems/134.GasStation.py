class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        start = 0
        #  this is gaurenteed to return
        while True:
            remain = gas[start] - cost[start]
            while remain < 0:
                start += 1
                remain = gas[start] - cost[start]
            # now the diff is positive
            end = (start + 1) % len(gas) 
            while remain >= 0:
                remain += gas[end] - cost[end]
                end = (end + 1) % len(gas)
                if end == start:
                    return start
            start = end + 1



            
