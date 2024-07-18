import sys

def read_file(file):
    """Open and read the file"""
    with open(file, 'r') as values:
        nums = [int(line.strip()) for line in values]
    return nums

def min_step_to_median(nums):
    """Finding the median and min steps to the median """
    nums.sort()
    median = nums[len(nums) // 2]
    steps = sum(abs(num - median) for num in nums)
    return steps


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("USE: python task4.py nums.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = read_file(input_file)
    min_step = min_step_to_median(nums)
    print(min_step)