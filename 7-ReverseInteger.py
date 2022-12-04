class Solution:
    def reverse(self, x):
        if x <= 0:
            is_positive = False
            x *= -1
        else:
            is_positive = True

        x_list = []
        x_str = str(x)
        for char in x_str:
            x_list.append(char)

        multiplier = 1
        result = 0
        for i in range(len(x_list)):
            result = result + (int(x_list[i]) * multiplier)
            multiplier *= 10

        if result >= 2147483647:
            result = 0
        if is_positive:
            return result
        else:
            return result * -1





solution = Solution()
print(solution.reverse(600))
print(solution.reverse(0))
print(solution.reverse(-100))
print(solution.reverse(356))
print(solution.reverse(17))