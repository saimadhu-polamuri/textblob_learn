from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from nltk.corpus import wordnet


# Function for Dictinary
def word_dictinary(word):
	synsets = wordnet.synsets(word)
	print synsets
	for synset in synsets:
		print '-' * 10
		#print synset.name()
		print "Name:", synset.name()
		print "Lexical Type:", synset.lexname()
		print "Lemmas:", synset.lemma_names()
		print "Definition:", synset.definition()
		for example in synset.examples():
			print "Example:", example

# Create a TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print wiki

# Part-of-speech Tagging
print wiki.tags

# Noun Phrase Extraction
print wiki.noun_phrases

# Sentiment Analysis
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print testimonial
print testimonial.sentiment
print testimonial.sentiment.polarity
print testimonial.sentiment.subjectivity

# Tokenization (Breaking Textblob to words or senctences)
zen = TextBlob("Beautiful is better than ugly. " "Explicit is better than implicit. " "Simple is better than complex.")
print zen
print zen.words
print zen.sentences
for sentence in zen.sentences:
	print sentence.sentiment

# Words Inflection and Lemmatization
sentence = TextBlob('Use 4 spaces per indentation level.')
print sentence.words
print sentence.words[2].singularize()
print sentence.words[-1].pluralize()

# Words can be lemmatized by calling the lemmatize method.
w = Word("octopi")
print w.lemmatize()
w = Word("completed") 	# Pass in part of speech (verb)
print w.lemmatize("v")

# WordNet Integration
# You can access the synsets for a Word via the synsets property or the get_synsets method, optionally passing in a part of speech.
word = Word("good")
print word.synsets
print Word("hack").get_synsets(pos=VERB)
print Word("octopus").definitions[1]
print Word("octopus").synsets

#word_dictinary('project')

# WordLists (A WordList is just a Python list with additional methods.)
animals = TextBlob("cat dog octopus")
print animals.words
print animals.words.pluralize()
# Spelling Correction (Use the correct() method to attempt spelling correction.)
b = TextBlob("I havv goood speling!")
print(b.correct())
w = Word('falibility')
print w.spellcheck()

# Get Word and Noun Phrase Frequencies
monty = TextBlob("We are no longer the Knights who say Ni. " "We are now the Knights who say Ekki ekki ekki PTANG.")
print monty.word_counts['ekki']
# The second way is to use the count() method.
print monty.words.count('ekki')
print monty.words.count('Ekki', case_sensitive=True)

# TextBlobs Are Like Python Strings
print zen.upper()

# You can make comparisons between TextBlobs and strings.
apple_blob = TextBlob('apples')
banana_blob = TextBlob('bananas')
print apple_blob < banana_blob
# You can concatenate and interpolate TextBlobs and strings.
print apple_blob + ' and ' + banana_blob
print "{0} and {1}".format(apple_blob, banana_blob)
# n-grams ( The TextBlob.ngrams() method returns a list of tuples of n successive words. )
blob = TextBlob("Now is better than never.")
print blob.ngrams(n=3)