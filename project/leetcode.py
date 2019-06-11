class Solution:
    def twoSum(self, array, target):
        """find the list indices that sum to a target"""
        results = {}
        for index, val in enumerate(array):
            complement = target - val
            if complement in results:
                return [results[complement], index]
            else:
                results[val] = index
        return []

    def reverse(self, x) -> int:
        """reverse the (base 10) digits of an integer
        # a pairwise swap might take n//2 steps and works in place
        # NOTE: blah blah 32 bit if > 2**31 return 0"""
        result = 0
        is_negative = (x != abs(x))
        if is_negative:
            x = abs(x)
            max_value = 2**31
        else:
            max_value = 2**31-1
        array = list(str(x))
        power = len(array)-1
        for index in range(0, power+1):
            result += (10**(index)*int(array[index]))
            if result > max_value:
                return 0
        if is_negative:
            result = - result
        return result

    def simple_reverse(self, x) -> int:
        """TODO try using extended slice to reverse the string, 
        i.e. foo = x[::-1]. Note that we're using str(x) anyway"""
        result = 0
        is_negative = (x != abs(x))
        if is_negative:
            x = abs(x)
            max_value = 2**31
        else:
            max_value = 2**31-1
        power = len(str(x))-1
        while x > 0:
            result += x % 10 * 10**power
            if result > max_value:
                return 0
            x = x // 10
            power-=1
        if is_negative:
            result = - result
        return result

    # these are really bad variable names
    def isPalindrome(self, x: int) -> bool:
        """without converting to string. TODO: try successively divide by 10 
        to get the length instead of using a list"""
        assert type(x) == int
        if x < 0: return False
        print(x)
        loop = 0
        digits = []
        while x > 0:
            digit = (x // 10**loop) % 10
            digits.append(digit)
            x = x - digit * 10**loop
            print(digit, loop, x, digits)
            loop += 1
        length = len(digits)
        for index in range(0, length//2):
            if digits[index] != digits[length-1-index]:
                return False
        return True
    
    def romanToInt(self, s: str) -> int:
        # MCMLXIII
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        numerals = [1, 5, 10, 50, 100, 500, 1000]
        roman_numerals = dict(zip(roman, numerals))
        result = 0
        characters = len(s)
        skip_next = False
        for index, letter in enumerate(list(s)):
            if not skip_next:
                value = roman_numerals[letter]
                if index + 1  <= characters-1:
                    if roman_numerals[s[index+1]] > roman_numerals[s[index]]:
                        value = roman_numerals[s[index+1]] - value
                        skip_next = True
                result += value
            else:
                skip_next = False
        return result
            


# nums = [11, 2, 7, 15]
# target = 9
# result = Solution().twoSum(nums, target)
# print(result)

# print(Solution().simple_reverse(321))
# print(Solution().simple_reverse(-321))
# # -1534236469
# # -2147483412
# assert Solution().reverse(-1534236469) == 0
# assert Solution().reverse(-2147483412) == -2143847412

# print(Solution().isPalindrome(121))

print(Solution().romanToInt('MCMLXIII')) # 1963