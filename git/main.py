import re
rusAlph = r"[А-Я]"
engAlph = r"[A-Z]"
language = input("Выберите язык: англ/рус\n")
if language.lower() == "англ":
    input_string = input("Введите строку: ")
    result = re.findall(engAlph, input_string)
    print("Прописные буквы:", result)
elif language.lower() == "рус":
    input_string = input("Введите строку: ")
    result = re.findall(rusAlph, input_string)
    print("Прописные буквы:", result)
else:
    print("Выберите один из двух предложенных языков!")

