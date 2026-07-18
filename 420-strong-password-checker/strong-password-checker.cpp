class Solution {
public:
    int strongPasswordChecker(string password) {
        int n = password.size();
        bool hasLower = false, hasUpper = false, hasDigit = false;
        for (char c : password) {
            if (islower(c)) hasLower = true;
            if (isupper(c)) hasUpper = true;
            if (isdigit(c)) hasDigit = true;
        }
        int missing = (!hasLower) + (!hasUpper) + (!hasDigit);
        
        int change = 0, one = 0, two = 0;
        int p = 2;
        while (p < n) {
            if (password[p] == password[p-1] && password[p-1] == password[p-2]) {
                int length = 2;
                while (p < n && password[p] == password[p-1]) {
                    length++;
                    p++;
                }
                change += length / 3;
                if (length % 3 == 0) one++;
                else if (length % 3 == 1) two++;
            } else {
                p++;
            }
        }
        
        if (n < 6) {
            return max(missing, 6 - n);
        } else if (n <= 20) {
            return max(missing, change);
        } else {
            int del = n - 20;
            change -= min(del, one);
            change -= min(max(del - one, 0), two * 2) / 2;
            change -= max(del - one - 2 * two, 0) / 3;
            return del + max(missing, change);
        }
    }
};