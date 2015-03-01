def pythagorean_triple(nums):
    """Find three numbers a, b, and c in nums such that a^2 + b^2 = c^2."""
    nums.sort()

    for ci in reversed(xrange(2, len(nums))):
        ai = 0
        bi = ci - 1

        while ai < bi:
            pythagorean_sum = nums[ai] * nums[ai] + nums[bi] * nums[bi]
            c_squared = nums[ci] * nums[ci]

            if pythagorean_sum == c_squared:
                return nums[ai], nums[bi], nums[ci]
            elif pythagorean_sum < c_squared:
                ai += 1
            else:
                bi -= 1
