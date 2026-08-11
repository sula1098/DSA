class Solution(object):
    def fourSum(self, nums, target):

        nums.sort()
        result = []

        # Choose first number
        for i in range(len(nums) - 3):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Choose second number
            for j in range(i + 1, len(nums) - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Two pointers for remaining two numbers
                left = j + 1
                right = len(nums) - 1

                while left < right:

                    # Calculate sum of 4 numbers
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # We found 4 numbers
                    if total == target:

                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate left values
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right values
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    # Sum is too small
                    elif total < target:
                        left += 1

                    # Sum is too large
                    else:
                        right -= 1

        return result