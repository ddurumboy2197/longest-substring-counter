from collections import Counter

def longest_unique_substring(s):
    max_length = 0
    max_substring = ""
    char_index = {}

    left = 0
    for right in range(len(s)):
        char = s[right]
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_substring = s[left:right + 1]

    return max_substring

print(longest_unique_substring("abcabcbb"))  # "abc"
print(longest_unique_substring("bbbbb"))  # "b"
print(longest_unique_substring("pwwkew"))  # "wke"
