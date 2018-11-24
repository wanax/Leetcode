'''
Xiaochi Ma
2018-11-18
'''

class Solution:
    
    def helper(self, ip, idx, cur, res, count):
        
        if count > 4:
            return
        if count == 4 and idx == len(ip):
            res.append(cur[:])
            
        for i in range(1, 4):
            if idx + i > len(ip):
                break
            s = ip[idx:idx+i]
            if (s[0] == '0' and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue
            suf = "" if count == 3 else "."
            self.helper(ip, idx+i, cur+s+suf, res, count+1)
    
    def restoreIpAddresses(self, s):
        
        res = []
        self.helper(s, 0, "", res, 0)
        
        return res
    
if __name__ == '__main__':

    solution = Solution()
    print(solution.restoreIpAddresses("25525511135"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    