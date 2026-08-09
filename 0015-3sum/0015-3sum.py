class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        target = []
        n = len(nums)

        for a in range(n - 2):

            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b = a + 1
            c = n - 1

            while b < c:

                total = nums[a] + nums[b] + nums[c]

                if total == 0:
                    target.append([nums[a], nums[b], nums[c]])

                    while b < c and nums[b] == nums[b + 1]:
                        b += 1

                    while b < c and nums[c] == nums[c - 1]:
                        c -= 1

                    b += 1
                    c -= 1

                elif total < 0:
                    b += 1

                else:
                    c -= 1

        return target

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna