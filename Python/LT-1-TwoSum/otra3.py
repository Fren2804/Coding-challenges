#Es igual que la 2, pero más rápida y se salta el paso de guardar todo en un diccionario
#Complejidad O(n), pero espacio adicional O(n)
#Obtenemos el complemento -> (target - num) y comprobamos que exista, si no guardamos el valor y el indice

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i in range(len(nums)):
            complemento = target - nums[i]
            if complemento in indices:
                return [i, indices[complemento]]
            indices[nums[i]] = i
        
        return []

solucion = Solution()
print(solucion.twoSum([1,11,2,7], 9))