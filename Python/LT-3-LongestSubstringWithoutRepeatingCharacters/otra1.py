class Solution:
    def lengthOfLongestSubstring(self, s):
        strings = {}
        longitud_maxima = 0
        inicio = 0

        for index, caracter in enumerate(s):
            print("In: ", index, " car:", caracter, " ", strings, " inicio: ", inicio)
            if caracter in strings:
                inicio = max(inicio, strings[caracter] + 1)

            strings[caracter] = index
            longitud_maxima = max(longitud_maxima, index - inicio + 1)

        return longitud_maxima


solucion = Solution()

print(solucion.lengthOfLongestSubstring("abcabcbb"))  # Esperado: 3
print(solucion.lengthOfLongestSubstring("bbbbb"))     # Esperado: 1
print(solucion.lengthOfLongestSubstring("pwwkew"))    # Esperado: 3
print(solucion.lengthOfLongestSubstring(""))          # Esperado: 0
print(solucion.lengthOfLongestSubstring("eea"))       # Esperado: 2
print(solucion.lengthOfLongestSubstring("1R1T7"))     # Esperado: 4
print(solucion.lengthOfLongestSubstring("cdcda"))     # Esperado: 3