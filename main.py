from stats import count_words, char_count, sorting_char_count

def main():  
    get_book_text()
    count_words()
    char_count()
    sorting_char_count(char_count)
    
def get_book_text():
    with open("/home/landstander/Documents/coding/Boot-dev/bookbot/books/frankenstein.txt") as file:
        file_contents = file.read()
        text = file_contents
    return file_contents #read the instructions again, removing print statement and returning just file_contents was the solution.
  
main()
