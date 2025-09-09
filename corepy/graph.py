from collections.abc import Callable
from queue import Queue
from typing import Any


class MutableGraph[Node, Edge]:
    directed: bool
    nodes: dict[Node, set[Node]]
    edges: set[Edge]

    edge_nodes: Callable[[Edge], tuple[Node, Node]]
    edge_reverse: Callable[[Edge], Edge]

    def __init__(
        self,
        edge_nodes: Callable[[Edge], tuple[Node, Node]],
        edge_reverse: Callable[[Edge], Edge],
        directed: bool = True,
    ) -> None:
        self.directed = directed
        self.nodes = {}
        self.edges = set()

        self.edge_nodes = edge_nodes
        self.edge_reverse = edge_reverse

    def add_node(self, node: Node) -> bool:
        if node in self.nodes:
            return False
        self.nodes.update({node: set()})
        return True

    def add_edge(self, edge: Edge) -> bool:
        modified = False

        from_node, to_node = self.edge_nodes(edge)
        modified |= self.add_node(from_node)
        modified |= self.add_node(to_node)
        modified |= _add_if_absent(self.nodes.get(from_node), to_node)

        modified |= _add_if_absent(self.edges, edge)

        if self.directed:
            return modified

        modified |= _add_if_absent(self.nodes.get(to_node), from_node)

        edge_reverse = self.edge_reverse(edge)
        modified |= _add_if_absent(self.edges, edge_reverse)
        return modified

    def remove_node(self, node: Node) -> bool:
        modified = False
        # fromNode -> toNode
        if node in self.nodes:
            self.nodes.pop(node)
            modified = True
        # fromNode <- toNode
        for to_nodes in self.nodes.values():
            modified |= _remove_if_absent(to_nodes, node)

        edge_to_remove = set()
        for edge in self.edges:
            from_node, to_node = self.edge_nodes(edge)
            if from_node == node or to_node == node:
                edge_to_remove.add(edge)
        if edge_to_remove:
            self.edges -= edge_to_remove
            modified = True
        return modified

    def remove_edge(self, edge: Edge) -> bool:
        modified = False
        from_node, to_node = self.edge_nodes(edge)

        edge_to_remove = set()
        for i in self.edges:
            from_node_i, to_node_i = self.edge_nodes(i)
            # fromNode -> toNode
            if from_node == from_node_i and to_node == to_node_i:
                edge_to_remove.add(i)
            # fromNode <- toNode
            if not self.directed:
                if to_node == from_node_i and from_node == to_node_i:
                    edge_to_remove.add(self.edge_reverse(i))

        if edge_to_remove:
            self.edges -= edge_to_remove
            modified = True

        # fromNode -> toNode
        to_nodes = self.nodes.get(from_node)
        modified |= _remove_if_absent(to_nodes, to_node)
        # fromNode <- toNode
        if not self.directed:
            from_nodes = self.nodes.get(to_node)
            modified |= _remove_if_absent(from_nodes, from_node)
        return modified

    def in_degree(self, node: Node) -> int:
        if not self.directed:
            return self.out_degree(node)

        in_degree = 0
        for to_nodes in self.nodes.values():
            if node in to_nodes:
                in_degree += 1
        return in_degree

    def in_degrees(self) -> dict[Node, int]:
        if not self.directed:
            return self.out_degrees()

        in_degrees = dict.fromkeys(self.nodes.keys(), 0)
        for nodes in self.nodes.values():
            for node in nodes:
                in_degrees[node] += 1
        return in_degrees

    def out_degree(self, node: Node) -> int:
        return len(self.nodes.get(node, set()))

    def out_degrees(self) -> dict[Node, int]:
        return {node: len(nodes) for node, nodes in self.nodes.items()}

    def successors(self, node: Node) -> set[Node]:
        return self.nodes.get(node, set())

    def predecessors(self, node: Node) -> set[Node]:
        if not self.directed:
            return self.successors(node)

        predecessors = set()
        for from_node, to_nodes in self.nodes.items():
            if node in to_nodes:
                predecessors.add(from_node)
        return predecessors

    def adjacent_nodes(self, node: Node) -> set[Node]:
        if self.directed:
            self.successors(node) | self.predecessors(node)
            return self.successors(node).union(self.predecessors(node))
        else:
            return self.successors(node)

    def root_nodes(self) -> set[Node]:
        in_degrees = self.in_degrees()
        return set([node for node, d in in_degrees.items() if d == 0])

    def topological_sort(self) -> list[Node]:
        if not self.directed:
            raise Exception("Not Supported for Undirected Graph")

        # in_degree
        in_degrees = self.in_degrees()

        # init queue
        remaining_nodes: Queue[Node] = Queue()
        for node in self.nodes.keys():
            if in_degrees[node] == 0:
                remaining_nodes.put(node)

        # topological sort
        nodes = []
        while not remaining_nodes.empty():
            node = remaining_nodes.get()
            successors = self.successors(node)
            for successor in successors:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    nodes.append(successor)

                    remaining_nodes.put(successor)

        return nodes

    def has_self_loops(self) -> bool:
        if not self.directed:
            raise Exception("Not Supported for Undirected Graph")
        raise Exception("Not implemented")

    def to_digraph(
        self,
        node_label: Callable[[Node], Any],
        edge_label: Callable[[Edge], Any] | None = None,
        node_id: Callable[[Node], Any] = lambda n: n,
    ) -> str:
        s = ["digraph G {\n"]
        for node in self.nodes.keys():
            s.append(f"  n{node_id(node)} [")
            is_root = self.in_degree(node) == 0
            if is_root:
                s.append("style=filled,shape=Msquare,")
            else:
                s.append("shape=box,")
            s.append(f'label="{node_label(node)}"]\n')

        for edge in self.edges:
            from_node, to_node = self.edge_nodes(edge)
            s.append(f"  n{node_id(from_node)} -> n{node_id(to_node)}")
            if edge_label:
                s.append(f' [label="{edge_label(edge)}"]')
            s.append("\n")

        s.append("\n}")
        return "".join(s)


def _add_if_absent(s, elem) -> bool:  # type: ignore[no-untyped-def]
    if elem not in s:
        s.add(elem)
        return True
    return False


def _remove_if_absent(s, elem) -> bool:  # type: ignore[no-untyped-def]
    if elem not in s:
        return False
    s.remove(elem)
    return True
