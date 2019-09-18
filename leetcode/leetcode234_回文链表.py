# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #我的方法，时间超出限制，但是自我感觉可以
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
    
        count = 1
        head.pre = None
        nn = head
        while nn.next:
            nn.next.pre = nn
            nn = nn.next
            count += 1
        print(count)
        
        if count == 2:
            if head.val == head.next.val:
                return True
            else:
                return False
        
        if count == 3:
            if head.val == head.next.next.val:
                return True
            else:
                return False
            
        if count%2 == 0:
            tmp = head 
            for i in range(int(count/2)-1):
                tmp = tmp.next
            while tmp.pre:
                if tmp.val == tmp.next.val:
                    tmp.pre.next = tmp.next.next
                else:
                    return False
            if tmp.val == tmp.next.val:
                return True
            else:
                return False
        else:
            tmp = head 
            for i in range(count//2):
                tmp = tmp.next
            tmp.pre.next = tmp.next
            while tmp.pre:
                if tmp.val == tmp.next.val:
                    tmp.pre.next = tmp.next.next
                else:
                    return False
            else:
                if tmp.val == tmp.next.val:
                    return True
                else:
                    return False
                
    #作弊方法：转为列表判断
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        while(head):
            res.append(head.val)
            head = head.next

        if len(res) <= 1: # ps: 空链表和单个结点的链表都是回文链表
            return True
        else:
            n = len(res)
            for i in range(n//2):
                if res[i] != res[n-1-i]:
                    return False
            return True
        #注，还有更直接的代码：return res==res[::-1]
        
    #正规题解
    def isPalindrome3(self, head: ListNode) -> bool:
        if not head or not head.next:return True
        # 取中位数的上边界，比如[1, 2, 2, 3] 取到是第二个2
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 奇数时候，中点位置下一个，（这样翻转才一样）
        if fast:
            slow = slow.next
        # 翻转操作
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 对比
        p1 = head
        p2 = prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


        
    