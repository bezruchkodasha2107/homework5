"""
Запросить у учителя оценки ученика до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

mark = int(input("Введите оценки ученика:"))
list_marks = []

while mark != 0:
    list_marks.append(mark)
    mark = int(input())

print(list_marks)
sr_arifm = sum(list_marks) / len(list_marks)
print(f"Средний балл={sr_arifm}")