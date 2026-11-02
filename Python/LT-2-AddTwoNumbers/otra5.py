#O(max(n, m)), siendo n y m las longitudes de las dos listas.
#Si no dejamos el por defecto, y le damos un valor (aunque sea el por defecto) y ademas la declaracion de la funcion arriba es mas simple, aumenta la velocidad
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        d = ListNode(0)
        p = d
        c = 0
        while l1 or l2 or c:
            s = c
            if l1: s += l1.val; l1 = l1.next
            if l2: s += l2.val; l2 = l2.next
            #Esto hace que vaya mas lento
            c, v = divmod(s, 10)
            p.next = ListNode(v)
            p = p.next
        return d.next
    
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solucion = Solution()
resultado = solucion.addTwoNumbers(l1, l2)

valores = []
while resultado is not None:
    valores.append(resultado.val)
    resultado = resultado.next

print(valores)  # Esperado: [7, 0, 8]