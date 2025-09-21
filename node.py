class Node:
    """A simple node for a linked data structure."""

    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node

    def __repr__(self):
        return f"Node({self.value!r})"

#A stack is the right choice for an undo/redo system because it works like a stack of papers on a desk—the last thing you put on top is the first thing you take off. This “last in, first out” pattern is exactly how undo and redo should work. When you undo something, you’re always undoing the most recent action. By using two stacks, one for undo and one for redo, we can move actions back and forth in a way that makes sense for the user.

# queue, on the other hand, is better for the help desk because it’s like a line of people waiting to be served. The first person in line should be the first one helped, which is called “first in, first out.” When a customer arrives, they are added to the end of the line, and when it’s their turn, they are taken from the front. This makes sure everyone is helped in the order they arrived, which is fair and practical.

#My versions of the stack and queue are different from Python’s built-in lists. With lists, you can jump around and grab items from anywhere, but that doesn’t match the real rules of a stack or queue. By building them from scratch, the rules are clearer: stacks only add and remove from the top, and queues only add at the back and remove from the front. This way, the structures act more like the real-world situations they are meant to model, such as undoing mistakes or waiting in line.
