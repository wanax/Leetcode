'''
Xiaochi Ma
2018-10-31
'''

class Solution:
    
    def helper(self, num):
        
        belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]   
        
        result = ""
        if num < 10:
            result = belowTen[num]
        elif num < 20:
            result = belowTwenty[num-10]
        elif num < 100:
            result = belowHundred[num//10] + " " + self.helper(num%10)
        elif num < 1000:
            result = self.helper(num//100) + ' Hundred ' + self.helper(num%100)
        elif num < 1000000:
            result = self.helper(num//1000) + ' Thousand ' + self.helper(num%1000)
        elif num < 1000000000:
            result = self.helper(num//1000000) + ' Million ' + self.helper(num%1000000)
        else:
            result = self.helper(num//1000000000) + ' Billion ' + self.helper(num%1000000000)
            
        return result.strip()
    
    def numberToWords(self, num):
        
        if num == 0:
            return 'Zero'
        return self.helper(num)
    
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.numberToWords(1234567891))






























