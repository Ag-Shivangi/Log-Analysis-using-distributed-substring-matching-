#!/usr/bin/env python

import sys
import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

def build_trie(keywords):
    root = TrieNode()
    for keyword in keywords:
        node = root
        for char in keyword:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append(keyword)
    return root

def build_fail_transitions(root):
    queue = []
    for node in root.children.values():
        queue.append(node)
        node.fail = root

    while queue:
        current_node = queue.pop(0)
        for char, child in current_node.children.items():
            queue.append(child)
            fail_node = current_node.fail
            while fail_node and char not in fail_node.children:
                fail_node = fail_node.fail
            child.fail = fail_node.children[char] if fail_node else root
            child.output += child.fail.output

def process_input(text, keywords, lineid):
    matches = []
    root = build_trie(keywords)
    build_fail_transitions(root)

    current_node = root
    for i, char in enumerate(text):
        while current_node and char not in current_node.children:
            current_node = current_node.fail
        if not current_node:
            current_node = root
            continue
        current_node = current_node.children[char]
        for match in current_node.output:
            matches.append((i - len(match) + 1, lineid))
    return matches

def main():
    pattern = os.environ['PATTERN']
    keywords = [pattern]  # Define your keywords here
    lineid = 0
    for line in sys.stdin:
        lineid += 1
        text = line.strip()
        matches = process_input(text, keywords, lineid)
        for match in matches:
            print(f"{match[0]}\t{match[1]}")
    
if __name__ == "__main__":
    main()