def count_words():
    from main import get_book_text #nesting the import in the function to avoid circular import issues
    words = get_book_text().split() #I'm splitting the get_book_text() as it is retunrning the full text of the book; calling file_contents doesn't work.
    num_words = len(words)
    return print(f"Found {num_words} total words.")

def char_count():
    from main import get_book_text
    text = get_book_text().lower()
    num_chars = {}
    for ch in text:
        if ch in num_chars:
            num_chars[ch] += 1
        else:
            num_chars[ch] = 1
    return num_chars
   
def get_nums():
    for v in char_count().items():
        print("num:",v)
    return v

def sorting_char_count(char_count):
    sorted_chars = [{}]
   # for ch in char_count():
    for v in get_nums():
        print("v:",v)
            # if v == ch[v]:
            #     char_sort = char_count(ch,v).sort(key = char_count, reverse = True)
            #     sorted_chars.append(char_sort(ch,v))
    return print("sorted char:",sorted_chars)