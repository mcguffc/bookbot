from stats import count_words, char_count, sort_this_list_of_char_count
import sys

if len(sys.argv) < 2:
    sys.argv = print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(sys.argv[1]) as file:
        file_contents = file.read()
        text = file_contents
    return file_contents #read the instructions again, removing print statement and returning just file_contents was the solution.

def main():  
   text = get_book_text()
   word_count = count_words(text)
   ch_count = char_count(text)
   sorted_list = sort_this_list_of_char_count(ch_count)
   
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {sys.argv[1]}...")
   print("----------- Word Count ----------")
   print(f"Found {word_count} total words")
   print("--------- Character Count -------")
   for item in sorted_list:
       ch = item["character"] # naming of things in stats matters; sorted_chars.append({"character": k, "num": v }) in stats.py sets ["character"] -- ["char"] didn't work.
       if ch.isalpha():
           print(f"{ch}: {item['num']}")
   print("============= END ===============")
  
main()
