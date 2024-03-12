import collections  # Importing the collections module for deque

class RecentCounter:
    def __init__(self):
        self.queue = collections.deque()  # Initialize an empty deque to store ping requests

    def ping(self, t: int) -> int:
        self.queue.append(t)  # Add the current ping request to the deque
        
        # Remove ping requests that are older than 3000 milliseconds (5 minutes)
        while self.queue and t - 3000 > self.queue[0]:
            self.queue.popleft()
        
        return len(self.queue)  # Return the number of ping requests within the last 3000 milliseconds


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
