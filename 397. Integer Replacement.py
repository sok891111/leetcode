class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.result = n
        mem = defaultdict(int)
        def backtracking(number):

            if number == 1:
                return 1
            
            if number in mem.keys():
                return mem[number] + 1

            if number % 2 == 0:
                step = backtracking(number // 2)
            else:
                step = backtracking(number + 1)
                step = min(backtracking(number - 1),step)

            mem[number] = step
            return step +1

        backtracking(n)
        return mem[n]
