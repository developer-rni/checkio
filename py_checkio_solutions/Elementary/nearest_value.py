#!/home/nikita/github/checkio/venv/bin/checkio --domain=py run nearest-value

# Find the nearest value to the given one.
# 
# You are given a list of values as set form and a value for which you need to find the nearest one.
# 
# For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.
# 
# A few clarifications:
# 
# If 2 numbers are at the same distance, you need to choose the smallest one;The set of numbers is always non-empty, i.e. the size is >=1;The given value can be in this set, which means that it’s the answer;The set can contain both positive and negative numbers, but they are always integers;The set isn’t sorted and consists of unique numbers.Input:Two arguments. A list of values in the set form. The sought value is an int.
# 
# Output:Int.
# 
# 
# END_DESC

def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    if len(values) == 1:
        return values.pop()
    values.add(one)
    new_values = sorted(list(values))
    index_one = new_values.index(one)
    if index_one + 1 == len(new_values):
        return new_values[-2]
    elif index_one == 0:
        return new_values[1]
    prev_numb = new_values[index_one - 1]
    next_numb = new_values[index_one + 1]
    dif_prev_numb = one - prev_numb
    dif_next_numb = next_numb - one
    if dif_prev_numb > dif_next_numb:
        return next_numb
    else:
        return prev_numb


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")