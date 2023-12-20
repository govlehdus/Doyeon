class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_level = [poured]
        for row in range(query_row):
            next_level = [0.0] * (row+2)

            for glass in range(len(current_level)):
                pouring = (current_level[glass]-1) /2
                if pouring > 0:
                    next_level[glass] +=pouring
                    next_level[glass+1] += pouring

            current_level = next_level
        
        return min(1.0, current_level[query_glass])
