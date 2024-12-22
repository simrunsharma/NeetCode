def maxArea(heights):
        max_areas = []
        for i,a in enumerate(heights):
            l = i
            r = i + 1
            #print("this is FIRST left",l)
            #print("this is FIRST right",r)
            while r < len(heights):
                width = r - l
                #print("this is width",width)
                height = min(heights[l],heights[r])
                area = width * height
                max_areas.append(area)
                #print("this is area",area)
                r +=1
            #print("this is left",l)
            #print("this is right",r)
        return max(max_areas)

if __name__ == '__main__':
    Input1 = [1,7,2,5,4,7,3,6]
    Output1 = maxArea(Input1)
    print("This is the output1", Output1)
    #Output: 36

    Input2 = [2,2,2]
    Output2 = maxArea(Input2)
    print("This is the output2", Output2)
    #Output: 4

'''
I put the image here in the folder: but essentially we want take the width every index and then the minumum of the two numbers for heights.
Then find the max area.
'''