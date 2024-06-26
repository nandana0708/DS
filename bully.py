class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.leader = None

    def __str__(self):
        return f"Node {self.node_id}"

    def start_election(self, nodes):
        print(f"{self} initiates an election.")
        higher_nodes = [node for node in nodes if node.node_id > self.node_id]
        for higher_node in higher_nodes:
            higher_node.receive_election(self)

    def receive_election(self, initiating_node):
        print(f"{self} receives an election message from {initiating_node}.")
        if self.leader is None or self.node_id > self.leader.node_id:
            print(f"{self} sends an OK message to {initiating_node}.")
            initiating_node.receive_ok(self)
        else:
            print(f"{self} ignores the election message from {initiating_node}.")

    def receive_ok(self, responding_node):
        print(f"{self} receives an OK message from {responding_node}.")
        self.leader = responding_node
        print(f"{self} acknowledges {responding_node} as the leader.")

if __name__ == "__main__":
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)]
    for node in nodes:
        node.start_election(nodes)

    elected_leader = max(nodes, key=lambda node: node.node_id)
    print(f"\n{elected_leader} is elected as the leader.")
