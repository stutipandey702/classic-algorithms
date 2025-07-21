#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: depth-first traversal
Author: Stuti Pandey

"""


# import statements
import sys
from collections import deque


def main():
    numInstances = int(input())
    outputs = []
    for i in range(numInstances):
    	outputs.append(" ".join(dfs_helper()))
    	
    #print()
    for i in range(len(outputs)):
    	print(outputs[i])

def dfs_helper():
	numNodes = int(input())
	adjacencyList = [None for x in range(numNodes)]
	for i in range(numNodes):
		nodes = input().split()
		if (i == 0):
			s = nodes[0]
		adjacencyList[i] = nodes


	visited = []
	output = ""
	dfs(adjacencyList, s, numNodes, visited, output)
	for i in range(1, numNodes):
		node = adjacencyList[i][0]
		if node not in visited:
			dfs(adjacencyList, node, numNodes, visited, output)

	return visited

			
	


def dfs(adj, s, num, visited, output):
	# print("Reached DFS for start node ", s)

	stack = []
	stack.append(s)

	while (stack):
		q = stack.pop()
		if q in visited:
			continue
		else:
			output += q + " "
			visited.append(q)
			for nodelist in adj:
				if nodelist[0] == q:
					for i in range(1,len(nodelist)):
						stack.append(nodelist[len(nodelist)-i])
		# print("   current stack ", stack)
	




if __name__ == "__main__":
    main()






