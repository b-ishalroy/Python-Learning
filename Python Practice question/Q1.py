# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2,7,4,15]
target = 6

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
             return [i,j]
            
result=two_sum(nums,target)
print("The sum of two array is =", result)            




#merge two sorted list

list1 = [1,2,4]
list2 = [1,3,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        curr=dummy=ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                curr.next=list2
                list2=list2.next

            else:
                curr.next=list1
                list1=list1.next

            curr=curr.next

        curr.next = list1 or list2

        return dummy.next 

Solution_1=Solution()
resultdummy=Solution_1.mergeTwoLists(list1,list2)



