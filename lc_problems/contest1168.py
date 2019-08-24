class Node:
def __init__(self, val, neighbors):
    self.val = val
    self.neighbors = neighbors  # node: distance

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        nodes = self.build_graph(wells, pipes) 
        # assume all houses are connected
        # dfs: base case, myself is cheaper than everyone else
        costs = {}
        def min_cost(curr_house):
            cost = curr_house.val
            for neigh, distance in curr_house.neighbors:
                if neigh not in costs:
                    min_cost(neigh)
                cost = min(cost, distance + costs[neigh])
            costs[curr_house] = cost

        for house in nodes:
            min_cost(house)
            if len(costs) == len(nodes):
                break
        return sum(costs.values())

    def build_graph(wells, pipes):
        nodes = [Node(val, {}) for val in wells]
        for i, pipe in enumerate(pipes):
            nodes[pipe[0]].neighbors[pipe[1]] = pipe[2]
            nodes[pipe[1]].neighbors[pipe[0]] = pipe[2]
        return nodes

            

