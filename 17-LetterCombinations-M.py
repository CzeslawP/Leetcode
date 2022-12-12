# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]


class Solution:
    def letterCombinations(self, digits: str):
        final_list = []
        for digit_str in digits:
            final_list = self.append_combinations(final_list, digit_str)
        return final_list


    def append_combinations(self, input_list, digit):
        output_list = []
        number_values = {
            "1": [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": [""]
        }
        if input_list == []:
            input_list = [""]
        for digit_return in number_values[digit]:
                for list_object in input_list:
                    output_list.append(list_object + digit_return)
        return output_list


solution = Solution()
print(solution.append_combinations([], "5"))
print(solution.append_combinations(['j', 'k', 'l'], "2"))

print(solution.letterCombinations("52"))

