# File Analyzer

A simple Python utility to analyze user feedback files and generate summary insights in JSON format.

---

## Task Overview

You work for a data company that receives multiple `.txt` files daily containing user feedback. This tool processes a feedback file and generates insights to help your business understand trends and frequent topics.

---

## Features

- Reads a text file named `feedback.txt` (case-insensitive analysis)
- Counts total words, unique words, and sentences
- Finds and prints the top 5 most frequent words (ignoring case, punctuation, and stop words)
- Saves the output as a structured JSON report (`report.json`)

---

## Requirements

- Python 3.6 or above
- Only uses built-in modules: `json` and `collections.Counter`

---

## Usage

1. Place `feedback.txt` in the project directory.  
2. Save the following script as `file_analyzer.py` in the same directory.  
3. Run the script:  
   ```bash
   python file_analyzer.py
   ```  
4. After execution, open `report.json` for the analysis results.

---

## Example Output (`report.json`)

```json
{
  "total_words": 1250,
  "unique_words": 430,
  "sentences": 55,
  "top_words": ["good", "service", "fast", "recommend", "price"]
}
```

---

## Python Solution

```python
import json
from collections import Counter

def file_analyzer(filename, jsonfilename='report.json'):
    f = open(filename, "r")
    file_text = f.read().lower()
    f.close()

    # Count total words
    splitted_text = file_text.split()
    word_count = len(splitted_text)

    # Count unique words
    unique_word = set(splitted_text)

    # Count total sentences
    numfs = file_text.count('.')
    numem = file_text.count('!')
    numqm = file_text.count('?')
    total_sentence = numfs + numem + numqm

    # Remove punctuation for frequency analysis
    punc = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    empty_str = ""
    for i in file_text:
        if i not in punc:
            empty_str += i

    string_list = empty_str.split()
    # Define stop words
    stop_words = {"is", "am", "the", "a", "an", "to", "with", "are", "be", "here", "and", "or", "not", 'i', 'my', 'was','your', 'from', 'at'}

    # Filter and count top words
    filtered_words = [word for word in string_list if word.lower() not in stop_words]
    frequent_words_counter = Counter(filtered_words)
    frequent_list = Counter(frequent_words_counter).most_common(5)
    frequent_word = [item[0] for item in frequent_list]

    final_feedback = {
        "total_words": word_count,
        "unique_words": len(unique_word),
        "sentences": total_sentence,
        "top_words": frequent_word
    }

    with open(jsonfilename, 'w') as fp:
        json.dump(final_feedback, fp, indent=4)
        print(f'Successfully data saved at {jsonfilename}')

    return final_feedback

file_path = "feedback.txt"
final_response = file_analyzer(file_path, jsonfilename='report.json')
print(final_response)
```

---

## How the Code Works

- The script reads the entire feedback file and converts it to lowercase.  
- It splits the text into words to count total and unique occurrences.  
- It counts sentences by counting periods, exclamation points, and question marks.  
- It removes punctuation from the text for a clean word frequency analysis.  
- It filters out common stop words to focus on meaningful frequent words.  
- It uses `Counter` from Python's `collections` to identify the top 5 most frequent words.  
- Results are stored as a dictionary and saved to `report.json`.  
- The top frequent words list, total and unique word counts, and sentence count are printed and saved.

---

## Customization

- Modify the stop words list to adapt to your context or language needs.  
- Adjust input/output filenames within the script.  
- Extend frequency or sentence detection logic as needed.

---

## License

MIT License

---

For questions or contributions, please open an issue or submit a pull request.
