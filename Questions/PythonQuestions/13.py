# Roman to Integer
def romanToInt(s: str) -> int:
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    ans = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    
    return ans

# Testing the romanToInt function

print(romanToInt("III"))  # Output: 3
print(romanToInt("IV"))  # Output: 4
print(romanToInt("IX"))  # Output: 9
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994