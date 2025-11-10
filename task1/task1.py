import json
from collections import Counter


def file_analyzer(filename, jsonfilename='report.json'):
  
  
  f= open(filename, "r")
  
  file_text = f.read().lower()
  f.close()
  
  
  #for word count, counted words
  splitted_text = file_text.split()
  word_count = len(splitted_text)
  # print(word_count)
  
  #for unique words , unique words
  unique_word = set(splitted_text)
  # print(unique_word)
  
  #for total number of sentences
  numfs = 0
  numem = 0
  numqm = 0
  
  numfs = file_text.count('.')
  numem = file_text.count('!')
  numqm = file_text.count('?')
  
  total_sentence = numfs + numem + numqm
  
  # print(total_sentence)
  
  #for top 5 most frequent words
  punc = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

  
  empty_str = ""
  for i in file_text:
    if i not in punc:
      empty_str += i
      
      
  # print(empty_str)
  
  string_list = empty_str.split()
  
  # Define your stop words
  stop_words = {"is", "am", "the", "a", "an", "to", "with", "are", "be", "here", "and", "or", "not", 'i', 'my', 'was','is', 'am', 'your', 'from', 'at'}

  # Filter words and count frequencies
  filtered_words = [word for word in string_list if word.lower() not in stop_words]
  frequent_words_counter = Counter(filtered_words)

  frequent_list = Counter(frequent_words_counter).most_common(5)
  frequent_word = [item[0] for item in frequent_list]
  # print(frequent_word)
  
  
  final_feedback = {
      "total_words": word_count,
      "unique_words": len(unique_word),
      "sentences": total_sentence,
      "top_words": frequent_word
  }
  
  with open(jsonfilename, 'w') as fp:
    json.dump(final_feedback, fp,indent=4)
    print(f'Successfully data saved at {jsonfilename}')
  
  
  return final_feedback

file_path = "feedback.txt"

final_response = file_analyzer(file_path, jsonfilename='report.json')

print(final_response)