from node import Node


class Stack:
    """Simple stack implemented with linked Nodes (LIFO)."""

    def __init__(self):
        self.top = None

    def push(self, value):
        """Push a new value onto the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Pop the top value from the stack and return it."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        node = self.top
        self.top = node.next
        node.next = None
        return node.value

    def peek(self):
        """Return the top value without removing it, or None if empty."""
        return None if self.is_empty() else self.top.value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def clear(self):
        """Clear the stack."""
        self.top = None

    def print_stack(self):
        """Print the contents of the stack (top to bottom)."""
        values = []
        node = self.top
        while node:
            values.append(repr(node.value))
            node = node.next
        print("Top -> " + " -> ".join(values) if values else "<empty>")


def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ").strip()
            undo_stack.push(action)
            redo_stack.clear()  # Clear redo stack instead of re-creating it
            print(f"Action performed: {action}")

        elif choice == "2":
            if undo_stack.is_empty():
                print("Nothing to undo.")
            else:
                action = undo_stack.pop()
                redo_stack.push(action)
                print(f"Undid: {action}")

        elif choice == "3":
            if redo_stack.is_empty():
                print("Nothing to redo.")
            else:
                action = redo_stack.pop()
                undo_stack.push(action)
                print(f"Redid: {action}")

        elif choice == "4":
            print("\nUndo Stack (most recent on top):")
            undo_stack.print_stack()

        elif choice == "5":
            print("\nRedo Stack (most recent on top):")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break

        else:
            print("Invalid option. Please choose 1–6.")


if __name__ == "__main__":
    run_undo_redo()
from node import Node
from undo_redo_system import Stack
