from typing import List, Tuple
from collections import defaultdict

with open('input.txt') as f:
    data = [a.strip() for a in f.readlines()]
    all_parents = [a[:a.index('(')-1] for a in data]
    all_weights = [int(a[a.index('(') + 1:a.index(')')]) for a in data]
    all_children = [a[a.index(')')+5:].split(', ') for a in data]

# Part 1
def find_base(parents: List[str], children: List[List[str]]) -> str:
    names = defaultdict(int)
    for node in parents:
        names[node] += 1

    for node in children:
        for sub_node in node:
            names[sub_node] += 1
    
    for key,value in names.items():
        if value == 1:
            return key

base_name = find_base(all_parents, all_children)

print(f'Part 1 Answer: {base_name}')

# Part 2
class Node:
    def __init__(self, name: str, weight: int, children: List[str]) -> None:
        self.name = name
        self.weight = weight
        self.children = []
        
        if children != ['']:
            for child in children:
                idx = all_parents.index(child)
                self.children.append(Node(all_parents[idx], all_weights[idx], all_children[idx]))

    def get_child_weights(self) -> Tuple[int, List[int]]:
        child_weights = []
        for child in self.children:
            total_weight,_ = child.get_child_weights()
            child_weights.append(total_weight)
        return sum(child_weights) + self.weight, child_weights

base_idx = all_parents.index(base_name)
tree = Node(all_parents[base_idx], all_weights[base_idx], all_children[base_idx])

def find_imbalance(node: Node, ideal_weight = 0) -> int:
    _, weights = node.get_child_weights()
    if len(set(weights)) == 1:
        return ideal_weight - sum(weights)

    ideal_weight = max(weights, key=weights.count)
    broken_child = node.children[weights.index(min(weights, key=weights.count))]

    return find_imbalance(broken_child, ideal_weight)


print(f'Part 2 Answer: {find_imbalance(tree)}')
