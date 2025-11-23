class Node:
    def __init__(self, product):
        self.product = product  # product is a dictionary or an object with product details
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_product(self, product):
        # Add a product to the end of the linked list.
        new_node = Node(product)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        # Traverse the linked list and return a list of product details.
        products = []
        current = self.head
        while current:
            products.append(current.product)
            current = current.next
        return products
