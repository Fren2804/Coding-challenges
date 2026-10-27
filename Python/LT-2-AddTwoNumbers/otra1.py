#O(max(n, m)), siendo n y m las longitudes de las dos listas.
#Es la misma, lo unico sin la flag primero y devolviendo el next nodo. Lo que pasa que uso un nodo extra de memoria
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        primero = ListNode()
        ultimo = primero
        extra = 0
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            suma = l1_val + l2_val + extra
            if (suma > 9):
                extra = 1
            else:
                extra = 0
            ultimo.next = ListNode(suma % 10)
            ultimo = ultimo.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if extra:
            ultimo.next = ListNode(1)
            ultimo = ultimo.next
        return primero.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(6)))

solucion = Solution()
resultado = solucion.addTwoNumbers(l1, l2)

valores = []
while resultado is not None:
    valores.append(resultado.val)
    resultado = resultado.next

print(valores)  # Esperado: [7, 0, 8]