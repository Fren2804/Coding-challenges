class Solution:
    def lengthOfLongestSubstring(self, s):
        sequence = ''
        max_length = 0
        for i in s:
            print("i :", i, "se: ", sequence)
            if i in sequence:
                sequence = sequence[sequence.index(i)+1:]
            sequence += i
            print("i :", i, "se: ", sequence)
            if max_length < len(sequence):
                max_length = len(sequence)
        return max_length


solucion = Solution()

print(solucion.lengthOfLongestSubstring("abcabcbb"))  # Esperado: 3
print(solucion.lengthOfLongestSubstring("bbbbb"))     # Esperado: 1
print(solucion.lengthOfLongestSubstring("pwwkew"))    # Esperado: 3
print(solucion.lengthOfLongestSubstring(""))          # Esperado: 0
print(solucion.lengthOfLongestSubstring("eea"))       # Esperado: 2
print(solucion.lengthOfLongestSubstring("1R1T7"))     # Esperado: 4
print(solucion.lengthOfLongestSubstring("cdcda"))     # Esperado: 3