class Solution(object):
    def combinationSum2(self, candidates, target):
        """https://github.com/sok891111/leetcode/tree/main
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        L = len(candidates)
        candidates.sort()

        combination = []
        def backtracking(nums, index,current):
            if current > target : 
                return

            if current == target:
                if nums in self.result :
                    return
                combination.append(set(nums))
                self.result.append(nums[:])
                return

            for i in range(index, L):

                if candidates[i] > target:
                    break
                if sum(candidates[i:]) + current < target : 
                    break
                if set(candidates[i:]) in combination:
                    continue

                nums.append(candidates[i])
                backtracking( nums , i +1, current+ candidates[i])
                nums.pop()


        backtracking([],0,0)
        return self.result
