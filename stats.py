def get_num_words(text):
    words = text.split()
    return len(words)

def count(text):
    text = text.lower()
    dic = {}
    for key in text:
        if not key.isalpha():
            continue
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    return dict(sorted(dic.items()))

# A function that takes a dictionary and returns the value of the "num"
# key This is how the `.sort()` method knows how to sort the list of
# dictionaries
def sort_on(char_count):
    char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return char_count

# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
