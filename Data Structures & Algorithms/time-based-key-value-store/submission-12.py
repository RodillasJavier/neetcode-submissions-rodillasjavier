class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key with value at the given timestamp
        """
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Return a value s.t.
            - set was called previously w/timestamp_prev <= timestamp

        If there are multiple timestamps, return the most recent one
        """
        res = ""

        if key not in self.store:
            return res

        entries = self.store[key]

        l, r = 0, len(entries) - 1
        while l <= r:
            m = (l + r) // 2

            if entries[m][0] < timestamp:
                res = entries[m][1]
                l = m + 1
            elif entries[m][0] == timestamp:
                return entries[m][1]
            else:
                r = m - 1

        return res


# time complexity: O(log v)
# space complexity: O(k * v)
