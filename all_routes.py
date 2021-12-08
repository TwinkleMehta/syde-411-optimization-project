from collections import defaultdict
from sys import maxsize
from itertools import permutations
from link import Link
from router import Router

b = 8 # num of routers

def findAllViablePaths(graph, s):
    cost_constraint = 11.04 # based on averaged cost results
    quality_constraint = 45 # based on averaged quality results
    # cost_constraint = maxsize # unconstrained
    # quality_constraint = -maxsize # unconstrained
 
    # store all routers excluding source router
    vertex = []
    for i in range(b):
        if i != s:
            vertex.append(i)

    viable_path_sums = {}
    viable_paths = [] #3D matrix
    num_of_viable_paths = 0
    next_permutation=permutations(vertex) # all permutations of nodes
    for i in next_permutation:
        path_arr = [[0 for _ in range(b)] for __ in range(b)]
        # store current path weights
        curr_t = 0
        curr_q = 0 
        curr_c = 0

        # compute current path weights
        k = s
        for j in i:
            path_arr[k][j] = 1
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
        if curr_c <= cost_constraint and curr_q >= quality_constraint:
            # add to viable path
            viable_paths.append(path_arr)
            viable_path_sums[num_of_viable_paths] = [curr_t, round(curr_c, 2), curr_q]
            num_of_viable_paths += 1

    return viable_paths, viable_path_sums
 
 
# Driver Code

# links as per UW engineering building distance data
l1 = Link(110)
l2 = Link(190)
l3 = Link(95)
l4 = Link(310)
l5 = Link(350)
l6 = Link(320)
l7 = Link(80)
l8 = Link(80)
l9 = Link(220)
l10 = Link(270)
l11 = Link(240)
l12 = Link(80)
l13 = Link(140)
l14 = Link(175)
l15 = Link(250)
l16 = Link(205)
l17 = Link(130)
l18 = Link(220)
l19 = Link(240)
l20 = Link(230)
l21 = Link(135)
l22 = Link(110)
l23 = Link(40)
l24 = Link(295)
l25 = Link(70)
l26 = Link(345)
l27 = Link(315)

# matrix representation of network graph
graph = [
    [Router(), l1, l2, l3, l4, l5,l6, l3],
    [l1, Router(), l7, l8, l9, l10, l11, l12],
    [l2, l7, Router(), l13, l14, l15, l16, l17],
    [l3, l8, l13, Router(), l18, l19, l20, l21], 
    [l4, l9, l14, l18, Router(), l22, l23, l24],
    [l5, l10, l15, l19, l22, Router(), l25, l26],
    [l6, l11, l16, l20, l23, l25, Router(), l27],
    [l3, l12, l17, l21, l24, l26, l27, Router()]
    ]
s = 0

# print generated parameters for all links and routers
for idx, node in enumerate(graph):
    for i in node:
        obj_type = 'link'
        if isinstance(i,Router):
            obj_type = 'router'
    
        print('Node: ',idx+1, ' type: ', obj_type, ' cost: ', i.cost, ' quality: ', i.quality, ' time: ', i.time)

a, sums = findAllViablePaths(graph, s)
min_time = maxsize
min_path = []
print('number of viable paths found: ', len(a))

# 2 options to find minimized time value (included for testing purposes)

# option 1: go through matrices and calculate times
# print("OPTION 1")
# for path in a:
#     curr_time = 0 
#     for m in range(0,b):
#         for n in range(0,b):
#             if path[m][n] == 1: 
#                 curr_time += graph[m][n].time
#     if curr_time <= min_time: 
#         min_time = curr_time
#         min_path = path

# print("best path: ", min_path)
# print("with time: ", min_time)

# option 2: read costs from sums dictionary
# print("OPTION 2")
min_t = maxsize
min_path_idx_t = maxsize
for idx, sum in enumerate(sums.values()):
    if sum[0] < min_t:
        min_t = sum[0]
        min_path_idx_t = idx
min_path_t = a[min_path_idx_t]
o_cost = sums[min_path_idx_t][1]
o_quality = sums[min_path_idx_t][2]
print("best (time-wise) path: ", min_path_t, " with time: ", min_t, ' with cost: ', o_cost, ' with quality: ', o_quality)

# Finding max time for comparison purposes
max_t = -maxsize
max_path_idx_t = -maxsize
for idx, sum in enumerate(sums.values()):
    if sum[0] > max_t:
        max_t = sum[0]
        max_path_idx_t = idx
maxt_cost = sums[max_path_idx_t][1]
maxt_quality = sums[max_path_idx_t][2]
print("max time (time-wise) path: ", a[max_path_idx_t], " with max time: ", max_t, ' with cost: ', maxt_cost, ' with quality: ', maxt_quality)

# Minimizing cost instead:
min_c = maxsize
min_path_idx = maxsize
for idx, sum in enumerate(sums.values()):
    if sum[1] < min_c:
        min_c = sum[1]
        min_path_idx = idx
min_path_c = a[min_path_idx]
minc_time = sums[min_path_idx][0]
minc_quality = sums[min_path_idx][2]
print("best (cost-wise) path: ", min_path_c, " with cost: ", min_c, ' with time: ', minc_time, ' with quality: ', minc_quality)

# Maximizing quality instead:
max_q = -maxsize
max_path_idx_q = -maxsize
for idx, sum in enumerate(sums.values()):
    if sum[2] > max_q:
        max_q = sum[2]
        max_path_idx_q = idx
max_path_q = a[max_path_idx_q]
maxq_time = sums[max_path_idx_q][0]
maxq_cost = sums[max_path_idx_q][1]
print("best (quality-wise) path: ", max_path_q, "with quality: ", max_q, 'with cost: ', maxq_cost, ' with time: ', maxq_time)

#  Constraints were identified using the following: 
# temp_sums = []
# for i in sums:
#     temp_sums.append(sums[i][2])
# print('average quality sum: ', sum(temp_sums)/len(temp_sums))


# temp_c_sums = []
# for i in sums:
#     temp_c_sums.append(sums[i][1])
# print('average cost sum: ', sum(temp_c_sums)/len(temp_c_sums))
