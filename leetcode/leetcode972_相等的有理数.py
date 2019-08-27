class Solution:
    #把末尾的循环的0都去掉
    def ling(self,x):
        if "(0)" == x[-3:]:
            x = x[:-3]
        elif "(00)" == x[-4:]:
            x = x[:-4]
        elif "(000)" == x[-5:]:
            x = x[:-5]
        elif "(0000)" == x[-6:]:
            x = x[:-6]
        return x
    #把末尾的循环的9都去掉，并且进一
    def jiu(self,x):
        newx = 'j'
        if "(9)" == x[-3:]:
            x = x[:-3]
            for k in range(len(x)):
                if x[k] == '.':
                    break
            newx=x[:k]+x[k+1:]
            count = 0
            for t in range(len(newx)):
                if newx[t] == '0':
                    count+=1
                else:
                    break
            newx=str(int(newx)+1)         
            if newx[-1] == '0':
                count = count-1
            for o in range(count):
                newx = '0'+newx
            newx=newx[:k]+'.'+newx[k:]

        elif "(99)" == x[-4:]:
            x = x[:-4]
            for k in range(len(x)):
                if x[k] == '.':
                    break
            newx=x[:k]+x[k+1:]
            count = 0
            for t in range(len(newx)):
                if newx[t] == '0':
                    count+=1
                else:
                    break
            newx=str(int(newx)+1)
            if newx[-1] == '0':
                count = count-1
            for o in range(count):
                newx = '0'+newx
            newx=newx[:k]+'.'+newx[k:]
            
        elif "(999)" == x[-5:]:
            x = x[:-5]
            for k in range(len(x)):
                if x[k] == '.':
                    break
            newx=x[:k]+x[k+1:]
            count = 0
            for t in range(len(newx)):
                if newx[t] == '0':
                    count+=1
                else:
                    break
            newx=str(int(newx)+1)
            if newx[-1] == '0':
                count = count-1
            for o in range(count):
                newx = '0'+newx
            newx=newx[:k]+'.'+newx[k:]
            
        elif "(9999)" == x[-6:]:
            x = x[:-6]
            for k in range(len(x)):
                if x[k] == '.':
                    break
            newx=x[:k]+x[k+1:]
            count = 0
            for t in range(len(newx)):
                if newx[t] == '0':
                    count+=1
                else:
                    break
            newx=str(int(newx)+1)
            if newx[-1] == '0':
                count = count-1
            for o in range(count):
                newx = '0'+newx
            newx=newx[:k]+'.'+newx[k:]
        
        if newx != 'j':
            return newx
        else:
            return x
    def isRationalEqual(self, s: str, t: str) -> bool:
        if '0.' != s[:2]:
            s = s.lstrip('0')
        if '0.' != t[:2]:   
            t = t.lstrip('0')
        if "." in s:
            s = s.rstrip('0')
        if "." in t:
            t = t.rstrip('0')
        s = self.ling(s)
        t = self.ling(t)
        s = s.rstrip('.')
        t = t.rstrip('.')
        if s == '':
            s = '0'
        if t == '':
            t = '0'
        s = self.jiu(s)
        t = self.jiu(t)
        if "." in s:
            s = s.rstrip('0')
        if "." in t:
            t = t.rstrip('0')
        s = s.rstrip('.')
        t = t.rstrip('.')

                
        #针对N.0(0)=N的情况
        #如果s是整数
        if '.' not in s and '.' in t:
            if int(s) == int(t.split('.')[0]):
                if set(t)=={'(', ')', '.', '0'}:
                    return True
        #如果t是整数
        if '.' not in t and '.' in s:
            if int(t) == int(s.split('.')[0]):
                if set(s)=={'(', ')', '.', '0'}:
                    return True

        
        #一般情况
        #如果没有重复位
        if "(" not in s:
            if s == t:
                return True
            else:
                return False
        #如果有重复位
        else:
            if ")" not in t:
                return False
            #对s
            #提取括号里的内容
            for i in range(len(s)):
                if s[i]=="(":
                    break
            repeat = s[i+1:-1]
            news = s[:i]+repeat
            while True:
                news = news+repeat
                if len(news)>13:
                    break
            news = news[:13]
            
            #对t
            for i in range(len(t)):
                if t[i]=="(":
                    break
            repeat = t[i+1:-1]
            newt = t[:i]+repeat
            while True:
                newt = newt+repeat
                if len(newt)>13:
                    break
            newt = newt[:13]
            
            if news == newt:
                return True
            else:
                return False
s = "0.08(9)"
t = "0.09"
q =Solution()
print(q.isRationalEqual(s,t))

#一个投机取巧的方法
class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = self.handle(S)
        t = self.handle(T)
        return abs(float(s)-float(t))<0.00000001
    def handle(self,s):
        p = s.find('(')
        if p!=-1:
            cycle = s[p+1:-1]
            s = s[:p]+cycle*15
        return s