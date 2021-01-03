class Solution:
    def maxArea(height) -> int:
        def calArea(height,i,j,a) -> int:
            if j-i >0:
                mh = min(height[i],height[j])
                area = (j-i) * mh
                if area > a:
                    a = area

                if height[i]<height[j]:
                    nexti = i
                    while nexti < j and height[nexti] <= height[i]:
                        nexti += 1
                    return max(a, calArea(height, nexti, j, a))
                else:
                    nextj = j
                    while nextj > i and height[nextj] <= height[j]:
                        nextj += -1
                    return max(a, calArea(height, i, nextj, a))
            else:
                return 0
        return calArea(height,0,len(height)-1,0)

aa= Solution

print(aa.maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146, \
                  58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]))