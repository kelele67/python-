# give up the max distance point
# import math
# def minDistance(N, points):
#     mind = -100000000000000000000000000000000
#     distance = 0
#     tag = 0
#     # for point in points[1:-1]:
#     #     d = abs(point - points[-1]) + abs(point - points[0])
#     #     if d > maxd:
#     #         maxd = d
#     #         tag = point
#     for i in range(1, N-2):
#         # contibute
#         # d = (points[i] - points[i-1])/ ((points[i] - points[-1]) - (points[i-1] - points[-1]))
#         # d = float(abs(points[i] - points[i-1])) / abs(points[i]-points[-1])
#         # d = float(abs(points[i] - points[i-1])) / abs(points[i] - points[-1])
#         # d = abs(points[i]-points[0]) + abs(points[i]-points[-1])
#         dd =  abs(points[i] - points[i-1])
#         d0 =  abs(points[i-1] - points[-1])
#         d2 =  abs(points[i] - points[-1])
#         d = float(d2 - d0) / dd
#         print d
#         print "----------"
#         # print d
#         if d > mind:
#             mind = d
#             tag = i
#     print points[tag]
#     points.remove(points[i])
#     for i in range(0, N-2):
#         step = abs(points[i+1] - points[i])
#         distance += step
#     return distance

def minDistance(N,nums):
    distance = list()
    for i in range(1,N-1):
        nums1 = nums[0:i]+nums[i+1:N]
        sum = 0
        for j in range(0,N-2):
            sum += abs(nums1[j+1]-nums1[j])
        distance.append(sum)
    return min(distance)
    
N = int(raw_input())
points = map(int, raw_input().split())
print minDistance(N, points)