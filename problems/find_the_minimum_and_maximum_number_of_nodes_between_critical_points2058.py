# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def islocalmaxima(self,prev, curr, next):
        return prev < curr > next
    def islocalminima(self, prev,curr,next):
        return prev > curr < next
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        i = 0
        first_critical = -1
        last_critical = -1
        prev = -1
        maxdistance = -1
        mindistance = -1
        while head and head.next:
            if i > 0:
                if self.islocalmaxima(prev, head.val, head.next.val):
                    if last_critical != -1:
                        if mindistance == -1:
                            mindistance = i - last_critical
                        mindistance = min(mindistance, i - last_critical)
                    if first_critical == -1:
                        first_critical = i
                    last_critical = i
                if self.islocalminima(prev, head.val, head.next.val):
                    if last_critical != -1:
                        if mindistance == -1:
                            mindistance = i - last_critical
                        mindistance = min(mindistance, i - last_critical)
                    if first_critical == -1:
                        first_critical = i
                    last_critical = i
            prev = head.val
            i += 1
            head = head.next
        if first_critical == -1 or first_critical == last_critical:
            return [-1, -1]
        maxdistance = last_critical - first_critical
        return [mindistance, maxdistance]

                
                    



        
        