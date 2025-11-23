class CategoryNode:
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes if attributes else {}
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_category(self, name):
        # Recursive search to find a category node by name.
        if self.name == name:
            return self
        for child in self.children:
            result = child.find_category(name)
            if result:
                return result
        return None

    def traverse(self, depth=0):
        # Traverse the category tree and print nodes.
        print('  ' * depth + self.name)
        for child in self.children:
            child.traverse(depth + 1)
