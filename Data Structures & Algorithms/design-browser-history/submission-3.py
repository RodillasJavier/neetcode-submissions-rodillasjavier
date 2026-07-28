class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage: str):
        """Initializes the object with the homepage of the browser."""
        self.currentNode = ListNode(homepage)

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        """
        newNode = ListNode(url)
        prev = self.currentNode

        prev.next = newNode
        newNode.prev = prev

        self.currentNode = newNode

    def back(self, steps: int) -> str:
        """
        Move steps back in history. If you can only return x steps in the
        history and steps > x, you will return only x steps. Return the current
        url after moving back in history at most steps.
        """
        currentNode = self.currentNode

        while currentNode.prev and steps > 0:
            currentNode = currentNode.prev
            steps -= 1

        self.currentNode = currentNode
        return self.currentNode.val

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. If you can only forward x steps in the
        history and steps > x, you will forward only x steps. Return the
        current url after forwarding in history at most steps.
        """
        currentNode = self.currentNode

        while currentNode.next and steps > 0:
            currentNode = currentNode.next
            steps -= 1

        self.currentNode = currentNode
        return self.currentNode.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
