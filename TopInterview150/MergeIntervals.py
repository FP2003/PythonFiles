from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
        new_area = []
        
        intervals = sorted(intervals, key=lambda x: x[0])

        for interval in intervals:
            if not new_area or new_area[-1][1] < interval[0]:
                new_area.append(interval)
            else:
                new_area[-1][1] = max(new_area[-1][1], interval[1])
        
        return new_area