# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        in:
            - n : upper range to search (1 .. n)
        out:
            - The correct number based on Guess API results
                - 0 => correct
                - -1 => guess > number
                - 1 => guess < number
        """
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)

            if res == 1:
                low = mid + 1
            elif res == -1:
                high = mid - 1
            else:
                return mid

        return 0


# time complexity: O(log n)
# space complexity: O(1)
