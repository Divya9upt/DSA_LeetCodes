class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                digit2 = int(num2[j])
                mul = digit1 * digit2
                
                p1, p2 = i + j, i + j + 1
                total = mul + result[p2]
                
                result[p2] = total % 10
                result[p1] += total // 10
        
        idx = 0
        while idx < len(result) - 1 and result[idx] == 0:
            idx += 1
        
        return ''.join(map(str, result[idx:]))