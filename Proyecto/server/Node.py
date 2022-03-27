class Node:
    def __init__(self, hashed_key):
        self.value = self.set_node(hashed_key)

    def set_node(self, hashed_key):

        if 0 <= hashed_key < 50:
            return "1"
        elif 50 <= hashed_key < 100:
            return "2"
        elif 100 <= hashed_key <= 150:
            return "3"
        else:
            return "0"
        