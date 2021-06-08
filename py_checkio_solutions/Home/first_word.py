#!/home/nikita/github/checkio/venv/bin/checkio --domain=py run first-word

# You are given a string where you have to find its first word.
# 
# When solving a task pay attention to the following points:
# 
# There can be dots and commas in a string.A string can start with a letter or, for example, a dot or space.A word
# can contain an apostrophe and it's a part of a word.The whole text can be represented with one word and that's
# it.Input:A string.
# 
# Output:A string.
# 
# Precondition:the text can contain a-z A-Z , . '
# 
# 
# END_DESC

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    index_word = 0
    chars = set("abcdefghijklmnopqrstuvwxyz\\'")
    for word in text.strip().split():
        if any((c in chars) for c in word.lower()):
            break
        else:
            index_word += 1
    text = text.strip().split()[index_word]
    if text.find('.'):
        text = text.split('.')[0]
    for i in range(0, -2, -1):
        for j in text[i]:
            if j == '.' or j == ',':
                if i == 0:
                    text = text[1:]
                else:
                    text = text[:-1]
    return text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")