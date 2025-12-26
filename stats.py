def count_words(text): # need to pass text as an argument to avoid circular import issues
   # from main import get_book_text #nesting the import in the function to avoid circular import issues
    words = text.split() #I'm splitting the get_book_text() as it is retunrning the full text of the book; calling file_contents doesn't work.
    num_words = len(words)
    return num_words

def char_count(text):
   # from main import get_book_text # BTW: this is a no no, best practice is to build functions here and call them and use them in functions in main.py
    txt = text.lower()
    num_chars = {}
    for ch in txt:
        if ch in num_chars:
            num_chars[ch] += 1
        else:
            num_chars[ch] = 1
    return num_chars

def sort_this_list_of_char_count(char_count):
    def sort_this(item):
        return item["num"]
        
    # def get_key_val_pairs(char_count):
    #     num_tupes = []
    #     for v in char_count().items():
    #         num_tupes.append(v)
    #     return num_tupes
    sorted_chars = []
    for k, v in char_count.items():
        sorted_chars.append({"character": k, "num": v })
    sorted_chars.sort(reverse=True, key=sort_this) #nesting this in the loop creates unecessary resource use; better to build the list first then sort it after.
      #  sorted_chars.sort(reverse=True, key=lambda x: x["num"]) #lambda: doing an inline function that I am supposed to build separately on my own for this assignment
    return sorted_chars