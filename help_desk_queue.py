from node import Node


class Queue:
    """A simple queue implemented with linked Nodes (FIFO)."""

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        """Add a value to the back of the queue."""
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        """Remove and return the value from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # Queue is now empty
            self.rear = None
        return value

    def peek(self):
        """Return the value at the front of the queue without removing it."""
        return None if self.is_empty() else self.front.value

    def print_queue(self):
        """Print the current contents of the queue."""
        values = []
        node = self.front
        while node:
            values.append(repr(node.value))
            node = node.next
        print("Front -> " + " -> ".join(values) if values else "<empty>")


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter customer name: ").strip()
            if name:
                queue.enqueue(name)
                print(f"{name} added to the queue.")
            else:
                print("No name entered; nothing added.")

        elif choice == "2":
            if queue.is_empty():
                print("No customers in the queue.")
            else:
                helped_customer = queue.dequeue()
                print(f"Helped customer: {helped_customer}")

        elif choice == "3":
            next_customer = queue.peek()
            if next_customer:
                print("Next customer to be helped:", next_customer)
            else:
                print("No customers in the queue.")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid option. Please choose 1–5.")


if __name__ == "__main__":
    run_help_desk()
