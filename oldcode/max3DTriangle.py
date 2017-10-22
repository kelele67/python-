# def max3DTriangle(Rpoints, Gpoints, Bpoints):
# pointers = []
# def max3DTriangle(points):
    # for point in points:
    #     side[0] = sqrt(pow(point[1] - ))

# def countTriangleSide(a, b):
#     side = sqrt(pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2) + pow(a[3] - b[3]))
#     return side

# def countTriangleArea(A, B, C):
#     # sides = [countTriangleSide(A, B), countTriangleSide(A, C), countTriangleSide(B, C)]
#     sides = map(countTriangleSide, for (x, y) in [(A,B), (A,C), (B,C)])
#     # side[0] = sqrt(pow(A[1] - B[1], 2) + pow(A[2] - B[2], 2) + pow(A[3] - B[3]))
#     # side[1] = sqrt(pow(A[1] - C[1], 2) + pow(A[2] - C[2], 2) + pow(A[3] - C[3]))
#     # side[2] = sqrt(pow(C[1] - B[1], 2) + pow(C[2] - B[2], 2) + pow(C[3] - B[3
#     # side.append(countTriangleSide(A, B))
#     # side.append(countTriangleSide(A, C))
#     # side.append(countTriangleSide(B, C))
  
#     # if (side[0] + side[1] <= side[2] || side[0] + side[1] <= side[2] || side[1] + side[2] <= side[0])
#     p = sum(sides)
#     for side in sides:
#         if sum(sides) - side <= side:
#             return -1
#     area = sqrt(p*(p-side[0])*(p-side[1])*(p-side[2]))

#     return area

# def max3DTriangle(Rpoints, Gpoints, Bpoints):
#     maxSameArea = max(map(countSameColor, [Rpoints, Gpoints, Bpoints]))
#     maxDiffArea = countDiffColor(Rpoints, Gpoints, Bpoints)
#     if !maxSameArea and !maxDiffArea:
#         return -1
#     return max(maxSameArea, maxDiffArea)

# def countDiffColor(Rpoints, Gpoints, Bpoints):
#     if !Rpoints || !Gpoints || !Bpoints:
#         return -1
#     area = 0
#     maxArea = 0
#     for i in range(len(Rpoints)):
#         A = Rpoints[i]
#         for j in range(len(Gpoints)):
#             B = Gpoints[j]
#             for k in range(len(Bpoints)):
#                 C = Bpoints[k]
#                 area = countTriangleArea(A, B, C)
#                 if area > maxArea:
#                     maxArea = area
#     return maxArea

# def countSameColor(points)
#     area = 0
#     maxArea = 0
#     if len(points) >= 3:
#         for i in range(len(points)):
#             A = points[i]
#             for j in range(len(points)) and j != i:
#                 B = points[j]
#                 for k in range(len(points)) and k != j and k != i:
#                     C = pointers[k]
#                     area = countTriangleArea(A, B, C)
#                     if area > maxArea:
#                         maxArea = area 
#     return area
# from math import sqrt

# def countTriangleSide(a, b):
#     side = sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2))
#     return side

# def countTriangleArea(A, B, C):   
#     sides = [countTriangleSide(A, B), countTriangleSide(A, C), countTriangleSide(B, C)]
#     for side in sides:
#         if sum(sides) - side <= side:
#             return -1
#     p = sum(sides) / 2
#     area = sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

#     return area

# def countDiffColor(Rpoints, Gpoints, Bpoints):
#     if not Rpoints or not Gpoints or not Bpoints:
#         return -1
#     area = 0
#     maxArea = 0
#     # for i in range(len(Rpoints)):
#     #     A = Rpoints[i]
#     #     for j in range(len(Gpoints)):
#     #         B = Gpoints[j]
#     #         for k in range(len(Bpoints)):
#     #             C = Bpoints[k]
#     #             area = countTriangleArea(A, B, C)
#     #             if area > maxArea:
#     #                 maxArea = area
#     # return maxArea
#     for A in Rpoints:
#         for B in Gpoints:
#             for C in Bpoints:
#                 area = countTriangleArea(A, B, C)
#                 if area > maxArea:
#                     maxArea = area
#     return maxArea


# # def countSameColor(points):
# #     area = 0
# #     maxArea = 0
# #     if len(points) >= 3:
# #         for i in range(len(points)):
# #             A = points[i]
# #             for j in range(len(points)):
# #                 if j == i:
# #                     break
# #                 B = points[j]
# #                 for k in range(len(points)):
# #                     if k == j or k == i:
# #                         break
# #                     C = points[k]
# #                     area = countTriangleArea(A, B, C)
# #                     if area > maxArea:
# #                         maxArea = area 
# #     return area

# def countSameColor(points):
#     area = 0
#     maxArea = 0
#     if len(points) >= 3:
#         # for i in range(len(points)):
#         #     A = points[i]
#         #     for j in range(len(points)):
#         #         if j == i:
#         #             break
#         #         B = points[j]
#         #         for k in range(len(points)):
#         #             if k == j or k == i:
#         #                 break
#         #             C = points[k]
#         for A in points:
#             for B in points:
#                 if B == A:
#                     break
#                 for C in points:
#                     if C == A or C == B:
#                         break
#                     area = countTriangleArea(A, B, C)
#                     if area > maxArea:
#                         maxArea = area 
#     return area
# def max3DTriangle(Rpoints, Gpoints, Bpoints):
#     maxSameArea = max(map(countSameColor, [Rpoints, Gpoints, Bpoints]))
#     maxDiffArea = countDiffColor(Rpoints, Gpoints, Bpoints)
#     if not maxSameArea and not maxDiffArea:
#         return -1
#     return max(maxSameArea, maxDiffArea)

# N = int(raw_input())
# Rpoints = []
# Gpoints = []
# Bpoints = []
# for i in range(N):
#     row = raw_input().split()
#     if row[0] == 'R':
#         Rpoints.append(map(int, row[1:]))
#     elif row[0] == 'G':
#         Gpoints.append(map(int, row[1:]))
#     else:
#         Bpoints.append(map(int, row[1:]))
# print ("%.5f") %(max3DTriangle(Rpoints, Gpoints, Bpoints))

# from math import sqrt

# def countTriangleSide(a, b):
#     side = sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2))
#     return side

# def countTriangleArea(A, B, C):   
#     sides = [countTriangleSide(A, B), countTriangleSide(A, C), countTriangleSide(B, C)]
#     for side in sides:
#         if sum(sides) - side <= side:
#             return -1
#     p = sum(sides) / 2
#     area = sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

#     return area

# def countDiffColor(Rpoints, Gpoints, Bpoints):
#     if not Rpoints or not Gpoints or not Bpoints:
#         return -1
#     area = 0
#     maxArea = 0
#     for A in Rpoints:
#         for B in Gpoints:
#             for C in Bpoints:
#                 area = countTriangleArea(A, B, C)
#                 if area > maxArea:
#                     maxArea = area
#     return maxArea

# def countSameColor(points):
#     area = 0
#     maxArea = 0
#     if len(points) >= 3:
#         # for A in points:
#         #     for B in points:
#         #         if B == A:
#         #             break
#         #         for C in points:
#         #             if C == A or C == B:
#         #                 break
#         #             area = countTriangleArea(A, B, C)
#         #             if area > maxArea:
#         #                maxArea = area
#         tmp = points
#         for A in points:
#             tmp = points[:points.index(A)] + points[points.index(A):] 
#             for B in tmp:
#                 tmp = points[:points.index(B)] + points[points.index(B):]
#                 for C in tmp:
#                     area = countTriangleArea(A, B, C)
#                     if area > maxArea:
#                         maxArea = area
#     else:
#         return -1
#     return maxArea

# def max3DTriangle(Rpoints, Gpoints, Bpoints):
#     maxSameArea = max(map(countSameColor, [Rpoints, Gpoints, Bpoints]))
#     maxDiffArea = countDiffColor(Rpoints, Gpoints, Bpoints)
#     if not maxSameArea and not maxDiffArea:
#         return -1
#     return max(maxSameArea, maxDiffArea)

# N = int(raw_input())
# Rpoints = []
# Gpoints = []
# Bpoints = []
# for i in range(N):
#     row = raw_input().split()
#     if row[0] == 'R':
#         Rpoints.append(map(int, row[1:]))
#     elif row[0] == 'G':
#         Gpoints.append(map(int, row[1:]))
#     else:
#         Bpoints.append(map(int, row[1:]))
# print ("%.5f") %(max3DTriangle(Rpoints, Gpoints, Bpoints))

#AC
from math import sqrt

def countTriangleSide(a, b):
    side = sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2))
    return side

def countTriangleArea(A, B, C):   
    sides = [countTriangleSide(A, B), countTriangleSide(A, C), countTriangleSide(B, C)]
    for side in sides:
        if sum(sides) - side <= side:
            return -1
    p = sum(sides) / 2
    area = sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))

    return area

def countDiffColor(Rpoints, Gpoints, Bpoints):
    if not Rpoints or not Gpoints or not Bpoints:
        return -1
    area = 0
    maxArea = 0
    for A in Rpoints:
        for B in Gpoints:
            for C in Bpoints:
                area = countTriangleArea(A, B, C)
                if area > maxArea:
                    maxArea = area
    return maxArea

def countSameColor(points):
    area = 0
    maxArea = 0
    if len(points) >= 3:
        for A in points:
            for B in points:
                if B == A:
                    break
                for C in points:
                    if C == A or C == B:
                        break
                    area = countTriangleArea(A, B, C)
                    if area > maxArea:
                        maxArea = area 
    return maxArea

def max3DTriangle(Rpoints, Gpoints, Bpoints):
    maxSameArea = max(map(countSameColor, [Rpoints, Gpoints, Bpoints]))
    maxDiffArea = countDiffColor(Rpoints, Gpoints, Bpoints)
    if not maxSameArea and not maxDiffArea:
        return -1
    return max(maxSameArea, maxDiffArea)

N = int(raw_input())
Rpoints = []
Gpoints = []
Bpoints = []
for i in range(N):
    row = raw_input().split()
    if row[0] == 'R':
        Rpoints.append(map(int, row[1:]))
    elif row[0] == 'G':
        Gpoints.append(map(int, row[1:]))
    else:
        Bpoints.append(map(int, row[1:]))
print ("%.5f") %(max3DTriangle(Rpoints, Gpoints, Bpoints))