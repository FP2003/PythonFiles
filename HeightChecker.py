from typing import List


def heightChecker(heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count