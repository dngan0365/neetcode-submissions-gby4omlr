class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        if len(s_clean) == 0:
            return True
        s_clean_list = list(s_clean)
        # print(s_clean_list)
        s_reverse = s_clean_list[::-1]
        # print(s_reverse)
        return s_reverse == s_clean_list
        