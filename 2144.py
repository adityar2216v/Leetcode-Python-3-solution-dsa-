class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate through the candies
        for i in range(len(cost)):
            # Every 3rd candy (index 2, 5, 8...) is free, so we skip it
            if (i + 1) % 3 == 0:
                continue
            total_cost += cost[i]
            
        return total_cost