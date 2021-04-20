import re

#Регулярное выражение
pattern = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"

#Пример для теста (Важно, что перечислены русские буквы)
numbers = ["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12","О123ОО59","а123аа59"]
answer = list()
for i in numbers:
    if re.fullmatch(pattern, i):
        answer.append(i)
print(answer)
