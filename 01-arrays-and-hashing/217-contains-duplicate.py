import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.performance import Performance
from utils.test_cases import large_array_with_duplicates

class BruteSolution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
    
class SortingSolution(object):
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False

class HashSetSolution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    
class HashSetLengthSolution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

array = large_array_with_duplicates

Performance.measure(BruteSolution().containsDuplicate, array, timeout=2)
Performance.measure(SortingSolution().containsDuplicate, array, timeout=2)
Performance.measure(HashSetSolution().containsDuplicate, array, timeout=2)
Performance.measure(HashSetLengthSolution().containsDuplicate, array, timeout=2)
