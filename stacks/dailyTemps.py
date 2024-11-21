class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)  # Initialize all days with 0
        stack = []  # Stack to hold indices

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index  # Difference in days

            stack.append(i)  # Add current day index to the stack

        return result


solution = Solution()

print(
    "Answer: ",
    solution.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]),
    "\nExpected:",
    "[1, 4, 1, 2, 1, 0, 0]",
)
# expected => [1,4,1,2,1,0,0]
