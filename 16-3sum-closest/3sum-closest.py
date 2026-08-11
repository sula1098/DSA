class Solution(object):
    def threeSumClosest(self, nums, target):

        # Step 1: Sort the array
        nums.sort()

        # Step 2: Take first possible sum as closest
        closest = nums[0] + nums[1] + nums[2]

        # Step 3: Choose the first number
        for i in range(len(nums) - 2):

            # Step 4: Two pointers
            left = i + 1
            right = len(nums) - 1

            # Step 5: Search for the other two numbers
            while left < right:

                # Step 6: Calculate 3 numbers' sum
                total = nums[i] + nums[left] + nums[right]

                # Step 7: Check if this sum is closer
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Step 8: Exact answer
                if total == target:
                    return total

                # Step 9: Sum is too small
                elif total < target:
                    left += 1

                # Step 10: Sum is too large
                else:
                    right -= 1

        return closest