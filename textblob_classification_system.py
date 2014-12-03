from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [('I love this sandwich.', 'pos'),
 		('this is an amazing place!', 'pos'),
 		('I feel very good about these beers.', 'pos'),
 		('this is my best work.', 'pos'),
 		('what an awesome view', 'pos'),
 		('I do not like this restaurant', 'neg'),
 		('I am tired of this stuff.', 'neg'),
 		("I can't deal with this", 'neg'),
 		('he is my sworn enemy!', 'neg'),
 		('my boss is horrible.', 'neg')]

test = [('the beer was good.', 'pos'),
		('I do not enjoy my job', 'neg'),
 		("I ain't feeling dandy today.", 'neg'),
 		('I feel amazing!', 'pos'),
 		('Gary is a friend of mine.', 'pos'),
 		("I can't believe I'm doing this.", 'neg')]

print test 		

print train 		
cl = NaiveBayesClassifier(train)	# Learning classifier with NaiveBayesClassifier

#	Classifying Text ( Call the classify(text) method to use the classifier.)
test_check = cl.classify("This is an amazing library!")
print test_check

#	You can get the label probability distribution with the prob_classify(text) method.

prob_dist = cl.prob_classify("This one's a doozy.")
print prob_dist.max()
print round(prob_dist.prob("pos"), 2)
print round(prob_dist.prob("neg"), 2)
print prob_dist.prob("pos")
print prob_dist.prob("neg")

blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
print blob.classify()


# Evaluating Classifiers (To compute the accuracy on our test set, use the accuracy(test_data) method.)
print cl.accuracy(test)

# Updating Classifiers with New Data (Use the update(new_data) method to update a classifier with new training data.)

new_data = [('She is my best friend.', 'pos'),
 			("I'm happy to have a new friend.", 'pos'),
 			('Stay thirsty, my friend.', 'pos'),
 			("He ain't from around here.", 'neg')]

#print new_data
print cl.update(new_data)
print cl.accuracy(test)