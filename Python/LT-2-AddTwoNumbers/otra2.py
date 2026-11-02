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
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            #Aqui me he equivocado, si tengo esto para que arriba suma = carry
            suma = l1_val + l2_val + carry
            carry = suma // 10
            ultimo.next = ListNode(suma % 10)
            ultimo = ultimo.next
        return primero.next


""" La mejor solucion 1ms
class Solution:
    def addTwoNumbers(self, l1, l2):
        primero = ListNode(0)
        ultimo = primero
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            suma = val1 + val2 + carry
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