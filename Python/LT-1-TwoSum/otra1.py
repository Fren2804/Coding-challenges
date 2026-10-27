#Esta es relativamente mas rápida, al llamar a un método menos, "len"
#Complejidad O(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(0, i):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []

solucion = Solution()
print(solucion.twoSum([1,11,2,7], 9))