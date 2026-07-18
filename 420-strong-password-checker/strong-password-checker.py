class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing = (not has_lower) + (not has_upper) + (not has_digit)
        
        change = 0
        one = 0
        two = 0
        p = 2
        while p < n:
            if password[p] == password[p - 1] == password[p - 2]:
                length = 2
                while p < n and password[p] == password[p - 1]:
                    length += 1
                    p += 1
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                p += 1
        
        if n < 6:
            return max(missing, 6 - n)
        elif n <= 20:
            return max(missing, change)
        else:
            delete = n - 20
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing, change)