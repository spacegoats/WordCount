# Count word frequency

import collections

print "\n\n###### Word Frequency Counter v1 ######"
print "######### by: Reese Gallagher #########"
print "# Make sure you change source file in source code! #"

with open('tweetsretweets.txt',"r") as word_list:
	words = word_list.read().split()

words = words.replace(',','')

stopWords = open('stopWords.txt','r').read().split()

countedWords=collections.Counter(words)


for x in countedWords.most_common():
	if x[0] in stopWords: 	
		continue
	else:
		print("%5s %8s %7s %s" % ('Word:',x[0], 'Count:', x[1]))

# Hopes and Dreams
# - further word filtering (i.e. months, URLs, dates)
## -- more elif: statements with comparing word to list of common words etc.
# - could even resort dates and months for time frequency
# - user input filename for more customization
# - embed into webpage for public use 

