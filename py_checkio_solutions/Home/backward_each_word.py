#!/home/nikita/github/checkio/venv/bin/checkio --domain=py run backward-each-word

# In a given string you should reverse every word, but the words should stay in their places.
# 
# Input:A string.
# 
# Output:A string.
# 
# Precondition:The line consists only from alphabetical symbols and spaces.
# 
# 
# END_DESC

def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return ""
    list_words = text.split()
    index_words = []
    stop_index_words = []
    result = ""
    count_alpha = 0
    count_whitespace = 0
    for index, item in enumerate(text):
        if item.isalpha() and count_alpha == 0:
            index_words.append(index)
            count_whitespace = 0
            count_alpha += 1
        elif item.isalpha():
            count_alpha += 1
        elif item == ' ':
            count_whitespace += 1
            count_alpha = 0
    for index in range(len(list_words)):
        stop_index_words.append(index_words[index] + len(list_words[index]))
    count_iter = 1
    for index, stop_index, word in zip(index_words, stop_index_words, list_words):
        if count_iter == 1 and index > 0:
            result += ' ' * index
        if count_iter == 1:
            result += text[stop_index-1:-(len(text)+1):-1]
        elif count_iter == len(list_words):
            result += text[len(text)+1:index-1:-1]
        else:
            result += text[stop_index-1:index-1:-1]
        if count_iter != len(list_words):
            whitespace = index_words[count_iter] - stop_index
            result += ' ' * whitespace
        count_iter += 1
    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
