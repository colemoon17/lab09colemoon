# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   loop through twice and compare sum to target sum
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i < j:
                return [i,j]


def max_profit(prices):
    # Outline:
    #   go through each day and record the highest profit if sold on another day

    highestProfit = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[j] - prices[i] > highestProfit and j > i:
                highestProfit = prices[j] - prices[i]

    return highestProfit


def max_subarray(nums):
    # Outline:
    #   go through each value and record the highest value given by adding contiguous values
    maxVal = nums[0]
    for i in range(len(nums)):
        currentTotal = 0
        for j in range(len(nums)):
            if j >= i:
                currentTotal += nums[j]

                if currentTotal > maxVal:
                    maxVal = currentTotal


    return maxVal
            


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pairs = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    tempStack = []

    for i in range(len(s)):
        if s[i] in pairs:
            tempStack.append(s[i])

        else:
            if len(tempStack) == 0:
                return False
            elif not pairs[tempStack.pop()] == s[i]:
                return False

    if len(tempStack) > 0:
        return False
    return True



def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(is_balanced('(]'))
    pass


if __name__ == "__main__":
    main()
