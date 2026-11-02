class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len_x = len(nums1)
        len_y = len(nums2)
        position_median = (len_x + len_y) / 2
        minimun_numbers = [0] * int((position_median) + 1)
        print(position_median)
        print(minimun_numbers)
        x = 0
        y = 0
        for i in range(int(position_median) + 1):
            if x < len_x:
                if y < len_y:
                    if nums1[x] < nums2[y]:
                        minimun_numbers[i] = nums1[x]
                        x += 1
                    else:
                        minimun_numbers[i] = nums2[y]
                        y += 1
                else:
                    minimun_numbers[i] = nums1[x]
                    x += 1
            else:
                minimun_numbers[i] = nums2[y]
                y += 1
        print(position_median)
        print(minimun_numbers)
        if position_median.is_integer():
            return ((minimun_numbers[int(position_median)] + minimun_numbers[int(position_median) - 1]) / 2)
        else:
            return (minimun_numbers[int(position_median)])


if __name__ == "__main__":
    solucion = Solution()

    casos = [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([1, 2, 3], [10, 20], 3),
        ([1], [2, 3, 4, 5, 6], 3.5),
        ([2, 2], [2, 2, 9], 2),
        ([-5, -1], [-3, 4], -2),
        ([], [4, 8, 12], 8),
        ([4, 8], [], 6),
        ([1, 7, 9], [2, 3], 3),
    ]

    for nums1, nums2, esperado in casos:
        resultado = solucion.findMedianSortedArrays(nums1, nums2)

        print("nums1:", nums1)
        print("nums2:", nums2)
        print("Resultado:", resultado)
        print("Esperado:", esperado)
        print("OK" if resultado == esperado else "ERROR")
        print()