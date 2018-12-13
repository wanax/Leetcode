'''
Xiaochi Ma
2018-12-11
'''

class Solution(object):
    
    def countDigitOne(self, n):
        
        if n <= 0:
            return 0
        if n <= 9:
            return 1
        num = pow(10, len(str(n))-1)
        
        if n >= 2*num:
            return num + self.countDigitOne(n%num) + n//num*self.countDigitOne(num-1)
        return n%num + 1 + self.countDigitOne(n%num) + self.countDigitOne(num-1);
        
    
    def addBoldTag1(self, s, dict):
        
        inters = []
        for key in dict:
            n = len(key)
            for i in range(len(s)-n+1):
                if key == s[i:i+n]:
                    inters.append([i, i+n-1])
                    
        inters.sort(key=lambda x:x[0])            
        if len(inters) == 0:
            return s
        
        merge = []
        for inter in inters:
            if len(merge) == 0 or merge[-1][1] < inter[0] - 1:
                merge.append(inter)
            else:
                merge[-1][1] = max(inter[1], merge[-1][1])
        
        count = 0
        for r in merge:
            s = s[:r[0]+count] + '<b>' + s[r[0]+count:]
            count += 3
            s = s[:r[1]+count+1] + '</b>' + s[r[1]+count+1:]
            count += 4
            
        return s
    
    def addBoldTag(self, s, dict):
        status = [False]*len(s)
        final = ""
        for word in dict:
            start = s.find(word)
            last = len(word)
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word,start+1)
        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.countDigitOne(13))
    print(solution.addBoldTag("aaabbcc", ["aaa","aab","bc"]))
#    print(solution.addBoldTag("xhhjzbkvpmasiypsqqjobufcqmlhdjffrdohsxgksftaekzhwzydhbfdiylihnvjlvpoptnqigszckimljbepgisnmyszfsxkxyfdfqngytfuihepohapvhbyhqydvroflfnsyjmygtykdejfudrhxxawcewgiguiwsvqrgbxrbdnrvguzjftqcsjbvjlbxfsvzpdpmtlzobwnxrtgisbcqmhugncjwgatfctydryakvbnmlbiftndfefylsmlebzdumefuflwhtwijtrhhhmknklalgqjaoicmnywtvzldbeftkydjsdkkonayhdxhrjazosqloilagcwzeezavnsqelxqhtlzymedxmkrovxhkrgfenyhxgdroeejedbwpnkqbqknalwgxoxweyxngorvrpnfkvagdqkbtuayaihyhwcsdtjzzvxfavrhzgf", ["xh","hj","zb","kv","pm","as","iy","ps","qq","jo","bu","fc","qm","lh","dj","ff","rd","oh","sx","gk","sf","ta","ek","zh","wz","yd","hb","fd","li","hn","vj","lv","po","pt","nq","ig","sz","ck","im","lj","be","pg","is","nm","ys","zf","kx"]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    