def mean(nums):
    bot = len(nums)
    it = 0
    top = 0
    print("Still Running at line 5")
    while it < len(nums):
        top += nums[it]
        print(top)
    return float(top) / float(bot)

if __name__ == '__main__':
    a_list = [1, 2, 3, 4, 5, 6, 10, "one hundred"]
    mean(a_list)
