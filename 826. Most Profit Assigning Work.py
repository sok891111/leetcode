class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        result = 0
        max_worker = max(worker)
        max_diff = max(difficulty)
        max_difficulty = max(max_worker , max_diff)+1
        job = [0]* max_difficulty
        
        for diff, pro in zip(difficulty, profit):
            job[diff] = max(job[diff] , pro)

        max_val = 0
        for index in range(max_difficulty):
            max_val = max(max_val , job[index])
            job[index] = max_val

        for w in worker:
            result += job[w]

        return result
