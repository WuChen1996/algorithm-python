class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    #方法一，看起来好高级，还是看不懂
    def largestNumber(self, nums):
        print(sorted(map(str, nums), key=LargerNumKey))
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        print(largest_num)
        return '0' if largest_num[0] == '0' else largest_num


    #方法二，好像冒泡牌排序，推荐
    def largestNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                print(i,j,nums)
        s = ''
        if nums[0] == 0:
            return('0')
        for i in nums:
            s = s + str(i)
        return s
    
lst = [3,30,97,8,979,976,34,5,9]    
s = Solution()
print(s.largestNumber2(lst))

#关于map
a = [1,2,3,4,5]
def mul(num):
    return num**2
print(list(map(mul,a)))

#关于reduce
def mul2(x,y):
    return x+y
import functools
print(functools.reduce(mul2,a))

#关于高级排序
import random
a = 'asdfghjkl'
lst1 = list(a)
lst2 = list(range(9))
random.shuffle(lst2)
dic = dict(zip(lst1,lst2))
lst = list(zip(lst1,lst2))
print(dic)
print(lst)
#按照key排序
d = sorted(lst,key = lambda k:k[0])
print(d)
#按照values排序
e = sorted(lst,key = lambda k:k[1])
print(e)