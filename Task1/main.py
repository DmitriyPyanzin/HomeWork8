"""
1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1
"""

from virus import hacker
from signature import MySignature
from register import create_register, read_register


create_register()
hacker()
read_register()
MySignature()
