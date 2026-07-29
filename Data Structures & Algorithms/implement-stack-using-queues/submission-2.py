from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Pushes element x to the top of the stack.

        Time complexity: O(1)
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.

        Time complexity: O(n)
        """
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        return self.q.popleft()

    def top(self) -> int:
        """
        Returns the element on the top of the stack.

        Time complexity: O(1)
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.

        Time complexity: O(1)
        """
        return len(self.q) <= 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()