class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strings = {}
        lenghtLongest = 0
        index = 0
        for i in s:
            if i not in strings:
                strings[i] = index
                index += 1
            else:
                length = len(strings)
                if (length > lenghtLongest):
                    lenghtLongest = length
                index_to_clean = strings[i]
                primer_indice = next(iter(strings.values()))
                cantidad = index_to_clean - primer_indice + 1
                for clave in list(strings)[:cantidad]:
                    del strings[clave]
                strings[i] = index
                index += 1
        length = len (strings)
        if (length > lenghtLongest):
            lenghtLongest = length
        return (lenghtLongest)


solucion = Solution()

print(solucion.lengthOfLongestSubstring("abcabcbb"))  # Esperado: 3
print(solucion.lengthOfLongestSubstring("bbbbb"))     # Esperado: 1
print(solucion.lengthOfLongestSubstring("pwwkew"))    # Esperado: 3
print(solucion.lengthOfLongestSubstring(""))          # Esperado: 0
print(solucion.lengthOfLongestSubstring("eea"))       # Esperado: 2
print(solucion.lengthOfLongestSubstring("1R1T7"))     # Esperado: 4
print(solucion.lengthOfLongestSubstring("cdcda"))     # Esperado: 3