"""
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном
порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Через рекурсию необходимо делать

Input: 2 -> 3 4
Output: 4 3
"""

from input import num, row
from recursion import revers_row
from signature import MySignature


number, new_row = num(), ''


print(revers_row(number, row(number), new_row))
MySignature()
