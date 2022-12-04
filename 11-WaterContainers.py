class Solution:
    def maxArea(self, height: list[int]) -> int:
        start_index = 0
        end_index = len(height) - 1
        max_water = 0
        # On each iteration area is narrowed on side with lower wall and max value is taken until two walls meet
        while start_index < end_index:
            if self.water_held(height, start_index, end_index) >= max_water:
                max_water = self.water_held(height, start_index, end_index)
            start_index, end_index = self.change_index(height, start_index, end_index)
        return max_water

    # Moves index on one side where height is lower, higher wall remains unchanged. Next index is a higher wall.
    def change_index(self, obj_list, left_index, right_index):
        if obj_list[left_index] >= obj_list[right_index]:
            next_index = right_index - 1
            while obj_list[right_index] > obj_list[next_index] and right_index > left_index:
                next_index -= 1
            right_index = next_index
        else:
            next_index = left_index + 1
            while obj_list[left_index] > obj_list[next_index] and right_index > left_index:
                next_index += 1
            left_index = next_index
        return left_index, right_index

    # calculates water held between start and end index
    def water_held(self, obj_list, start_index, end_index):
        if obj_list[start_index] <= obj_list[end_index]:
            max_height = obj_list[start_index]
        else:
            max_height = obj_list[end_index]
        return (end_index - start_index) * max_height

# Runtime: 642 ms, faster than 99.50% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.6 MB, less than 11.59% of Python3 online submissions for Container With Most Water.

list1 = [1,8,6,2,5,4,8,3,7]
list2 = [1, 1]

solution = Solution()
print(solution.maxArea(list1))
print(solution.maxArea(list2))