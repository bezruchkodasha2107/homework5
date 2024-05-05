"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""
def text_info(text):
    num_chars = len(text)
    num_words = len(text.split())
    num_str = text.count('\n') + 1
    num_sentences = text.count('.') + text.count('!') + text.count('?')

    info = {
        'Characters': num_chars,
        'Words': num_words,
        'Lines': num_str,
        'Sentences': num_sentences
    }
    return info

def print_text_info(info):
    print("Text Info:")
    for key, value in info.items():
        print(f"{key}: {value}")

text = """
This is a sample text.
It has multiple lines.
It also contains multiple sentences! Right?
And a few characters too...
"""

info = text_info(text)
print_text_info(info)