class TimeMap:

    def __init__(self):
        self.key_time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store the key with value at the given timestamp
        """
        if key not in self.key_time:
            self.key_time[key] = []
        
        if timestamp not in self.key_time[key]:
            self.key_time[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        """
        Return a value s.t.
            - set was called previously w/timestamp_prev <= timestamp
        
        If there are multiple timestamps, return the most recent one
        """
        if key not in self.key_time:
            return ""

        left, right = 0, len(self.key_time[key]) - 1
        most_recent = (-1, "")

        while left <= right:
            mid = (left + right) // 2

            if timestamp < self.key_time[key][mid][0]:
                right = mid - 1
            elif self.key_time[key][mid][0] < timestamp:
                if most_recent[0] < self.key_time[key][mid][0] < timestamp:
                    most_recent = (self.key_time[key][mid][0], self.key_time[key][mid][1])
                left = mid + 1
            else:
                return self.key_time[key][mid][1]
        
        return most_recent[1]
