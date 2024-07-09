from typing import List


def averageWaitingTime(customers: List[List[int]]) -> float:
        avaliable = 0
        totalWait = 0
        for customer, time in customers:
            avaliable = max(avaliable, customer) + time
            totalWait += avaliable - customer

        return totalWait / len(customers)