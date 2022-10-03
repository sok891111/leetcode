class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = len(height) -1
        if L < 2 :
            return 0
        left , right, result = 0 , 1 , 0
        cur_sum = 0
        while True:
            
            if left >= L :
                break
                
            
            if right > L:
                tmp = left
                if cur_sum > 0 :
                    cur_sum = 0
                    while True:
                        if left >= right:
                            break
                        height[left] , height[right-1] = height[right-1] , height[left]
                        left +=1 
                        right -= 1
                    left = tmp
                    right = left +1
                else:
                    left += 1
                    right = left+1
                
                continue
            
            
            if height[left] <= height[right]:
                result += cur_sum
                cur_sum = 0
                left = right
                right = left +1
            else :
                cur = height[left] - height[right]
                cur_sum += cur
                right += 1
        return result
     
