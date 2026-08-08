class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]

        for i in strs[1:]:
            while not i.startswith(pre):
                pre = pre[:-1]
                if pre == "":
                    return ""
        return pre
    
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna