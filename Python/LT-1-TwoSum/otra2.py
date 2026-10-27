#Complejidad O(n), pero espacio adicional O(n)
#Guardamos cada número como clave y el indice como valor.
#Luego buscamos su complemento -> (target - num) y comprobamos que no tenga el mismo indice.
#O sea 
"""
indices = {
1:0
11:1
2:2
7:3
}
Para i = 0 | 9 - 1 = 8 -> 8 no esta en el diccionario
Para i = 1 | 9 - 11 = -2 -> -2 no esta en el diccionario
Para i = 2 | 9 - 2 = 7 -> 7 está en indices, y el indice es 3. 3 != i -> i = 2
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)):
            complemento = target - nums[i]
            if complemento in indices and indices[complemento] != i:
                return [i, indices[complemento]]
        
        return []

solucion = Solution()
print(solucion.twoSum([1,11,2,7], 9))