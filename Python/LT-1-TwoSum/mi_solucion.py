#Complejidad O(n^2)
#La primera solución que me salió sin mirar nada
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []

solucion = Solution()
print(solucion.twoSum([1,11,2,7], 9))