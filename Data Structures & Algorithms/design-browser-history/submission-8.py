class ListNode:
    """
    Helper class to manage Nodes in our DLL implementation
    """
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Initializes the object with the homepage of the browser.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = ListNode(url)
        prev = self.current

        prev.next = new_node
        new_node.prev = prev

        self.current = new_node

    def back(self, steps: int) -> str:
        """
        Move steps back in history. If you can only return x steps in the
        history and steps > x, you will return only x steps. Return the current
        url after moving back in history at most steps.

        Time Complexity: O(min(steps, n))
        Space Complexity: O(1)
        """
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.val

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. If you can only forward x steps in the
        history and steps > x, you will forward only x steps. Return the
        current url after forwarding in history at most steps.

        Time Complexity: O(min(steps, n))
        Space Complexity: O(1)
        """
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1

        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
