#O(max(n, m)), siendo n y m las longitudes de las dos listas.
#Sigue siendo mia, pero con mas lógica y mejor estructura
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        primero = ListNode()
        ultimo = primero
        carry = 0
        while l1 or l2 or carry:
            suma = carry
            if l1:
                suma += l1.val
                l1 = l1.next
            if l2:
                suma += l2.val
                l2 = l2.next
            carry = suma // 10
            ultimo.next = ListNode(suma % 10)
            ultimo = ultimo.next
        return primero.next

""" La misma funcion pero haciendo mas simple la declaracion de la funcion y ademas dando el valor va mas rápido
class Solution:
    def addTwoNumbers(self, l1, l2):
        primero = ListNode(0)
        ultimo = primero
        carry = 0
        while l1 or l2 or carry:
            suma = carry
            if l1:
                suma += l1.val
                l1 = l1.next
            if l2:
                suma += l2.val
                l2 = l2.next
            carry = suma // 10
            ultimo.next = ListNode(suma % 10)
            ultimo = ultimo.next
        return primero.next
"""

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solucion = Solution()
resultado = solucion.addTwoNumbers(l1, l2)

valores = []
while resultado is not None:
    valores.append(resultado.val)
    resultado = resultado.next

print(valores)  # Esperado: [7, 0, 8]