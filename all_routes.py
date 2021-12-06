from collections import defaultdict
from sys import maxsize
from itertools import permutations
from link import Link
from router import Router

b = 8 # num of routers

# implementation of traveling Salesman Problem
def findAllViablePaths(graph, s):
    cost_constraint = 100 # temp
    quality_constraint = 100 # temp
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(b):
        if i != s:
            vertex.append(i)

    viable_path_sums = {}
    viable_paths = [] #3D matrix
    num_of_viable_paths = 0
    next_permutation=permutations(vertex) # all permutations of nodes
    for i in next_permutation:
        # print("path with permutation: ", i)
        path_arr = [[0 for _ in range(b)] for __ in range(b)]
        # store current Path weight(cost)
        curr_t = 0
        curr_q = 0 
        curr_c = 0

        # compute current path weight
        k = s
        for j in i:
            path_arr[k][j] = 1
            # print("iteration for element: ", j)
            # print("path in this iteration: ", path_arr)
            curr_t += graph[k][j].time
            curr_q += graph[k][j].quality
            curr_c += graph[k][j].cost
            k = j
        # connect to source node
        path_arr[k][s] = 1
        curr_t += graph[k][s].time
        curr_q += graph[k][s].quality
        curr_c += graph[k][s].cost
 
        # check if constraints are met 
        if curr_c <= cost_constraint and curr_q <= quality_constraint:
            # add to viable path
            viable_paths.append(path_arr)
            viable_path_sums[num_of_viable_paths] = [curr_t, round(curr_c, 2), curr_q]
            num_of_viable_paths += 1
            # viable_paths[round(curr_c, 2)] = i

    return viable_paths, viable_path_sums
 
 
# Driver Code
# matrix representation of graph

# ALL VALUES ARE REGENERATED EVERY TIME THIS FILE IS RUN
graph = [
    [Router(), Link(110), Link(190), Link(95), Link(310), Link(350), Link(320), Link(95)],
    [Link(110), Router(), Link(80), Link(80), Link(220), Link(270), Link(240), Link(80)],
    [Link(190), Link(80), Router(), Link(140), Link(175), Link(250), Link(205), Link(130)],
    [Link(95), Link(80), Link(140), Router(), Link(220), Link(240), Link(230), Link(135)], 
    [Link(310), Link(220), Link(175), Link(220), Router(), Link(110), Link(40), Link(295)],
    [Link(350), Link(270), Link(250), Link(240), Link(110), Router(), Link(70), Link(345)],
    [Link(320), Link(240), Link(205), Link(230), Link(40), Link(70), Router(), Link(315)],
    [Link(95), Link(80), Link(130), Link(135), Link(295), Link(345), Link(315), Router()]
    ]
s = 0

# print(graph[0][0].cost)
# print(graph[0][0].time)
# print(graph[0][0].quality)
# print(graph[0][1].cost)
# print(graph[0][1].time)
# print(graph[0][1].quality)

a, sums = findAllViablePaths(graph, s)
min_time = maxsize
min_path = []

# option 1: go through matrices and calculate times
print("OPTION 1")
for path in a:
    curr_time = 0 
    for m in range(0,b):
        for n in range(0,b):
            if path[m][n] == 1: 
                curr_time += graph[m][n].time
    if curr_time <= min_time: 
        min_time = curr_time
        min_path = path

print("best path: ", min_path)
print("with time: ", min_time)

# option 2: read costs from sums dictionary
print("OPTION 2")
min_t = maxsize
min_path_idx_t = maxsize
for idx, sum in enumerate(sums.values()):
    if sum[0] < min_t:
        min_t = sum[0]
        min_path_idx_t = idx
min_path_t = a[min_path_idx_t]
print("best (time-wise) path: ", a[min_path_idx_t], "with time: ", min_t)

# for analysis later on 

# # (1) Minimizing cost instead:

# min_c = maxsize
# min_path_idx = maxsize
# for idx, sum in enumerate(sums.values()):
#     if sum[1] < min_c:
#         min_c = sum[1]
#         min_path_idx = idx
# min_path_c = a[min_path_idx]
# print("best (cost-wise) path: ", min_path_c, "with cost: ", min_c)

# # (2) Maximizing quality instead:
# max_q = -maxsize
# max_path_idx_q = -maxsize
# for idx, sum in enumerate(sums.values()):
#     if sum[2] > max_q:
#         max_q = sum[2]
#         max_path_idx_q = idx
# max_path = a[max_path_idx_q]
# print("best (cost-wise) path: ", max_path, "with quality: ", max_q)