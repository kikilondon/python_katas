# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.def report_long_words(words):
  #FILTER
  #set a variable [] to store selected words longer then 10 char 
  #set a length variable to store the length of the words 
  #iterate through the list "words"
  #if the len is >10 
  #append the word to the list 
print("")
print("Function: report_long_words")



def report_long_words(words):
  long_words = extract_long_words(words)
  #remove or filter out those containing hypens 
  without_hypens = remove_hypens(long_words)
  #Map words >15  chars then shorten them to 15 char and add ellipsis ...
  #append the word to words list too
  shortened_words = shortened_long_words(without_hypens)
  # summarise to a string report of the words 
  return format_long_words_report(shortened_words)


def extract_long_words(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words

print(extract_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]))

def remove_hypens(words):
  without_hypens = []
  for word in words:
    if "-" not in word:
      without_hypens.append(word)
  return without_hypens


print(remove_hypens([
  'hello',
  'nonbiological',
  'Kay',
  'this-is-a-long-word',
  'antidisestablishmentarianism'
]))


def shortened_long_words(words):
  shortened_words = []
  for word in words:
    if len(word)  > 15:
      word = word[0:15] + "..."
      shortened_words.append(word)
    else:
      shortened_words.append(word)
                             
  return shortened_words


print(shortened_long_words([
  'hello',
  'nonbiological',
  'Kay',
  'this-is-a-long-word',
  'antidisestablishmentarianism'
]))

def format_long_words_report(shortened_words):
  report = "These words are quite long: "
  if len(shortened_words) == 0:
    return report
  for word in shortened_words:
     report = report + word + ", "
  return report [0:-2]
    