# vocabulary_analyser.py


import re


sample_text = """
Python was conceived in the late 1980s[42] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands.[43] It was designed as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Python implementation began in December 1989.[43] Van Rossum first released it in 1991 as Python 0.9.0.[43] Van Rossum assumed sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from responsibilities as Python's "benevolent dictator for life" (BDFL); this title was bestowed on him by the Python community to reflect his long-term commitment as the project's chief decision-maker.[45] (He has since come out of retirement and is self-titled "BDFL-emeritus".) In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[46][47]
The name Python derives from the British comedy series Monty Python's Flying Circus.[48] (See § Naming.)
Python 2.0 was released on 16 October 2000, featuring many new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 2.7's end-of-life was initially set for 2015, and then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[50][51] It no longer receives security patches or updates.[52][53] While Python 2.7 and older versions are officially unsupported, a different unofficial Python implementation, PyPy, continues to support Python 2, i.e., "2.7.18+" (plus 3.10), with the plus signifying (at least some) "backported security updates".[54]
Python 3.0 was released on 3 December 2008, and was a major revision and not completely backward-compatible with earlier versions, with some new semantics and changed syntax. Python 2.7.18, released in 2020, was the last release of Python 2.[55] Several releases in the Python 3.x series have added new syntax to the language, and made a few (considered very minor) backward-incompatible changes.
Since 7 October 2025, Python 3.14.0 is the latest stable release, and Python 3.13.9 released a week later all older 3.x versions also had a security update down to Python 3.9.24, the last in 3.9 series. Python 3.10 is the oldest supported branch.[56] Releases receive two years of full support followed by three years of security support.
"""

# remove the [] references
sample_text = re.sub("\[[0-9]+\]", "", sample_text)
print (sample_text)

words = sample_text.split()

print (words)

# references_removed = [word for word in words if words.index("[")]

unique_words = set(words)

print(unique_words)

print (len(words))
print (len(unique_words))


# how many of each word are there

#dict = {
#    "Python": 27, 
#    "Programming": 15, 
#}

word_counts = {}

for word in words:

    if word in word_counts:
        # increment the count for existing words
        word_counts[word] += 1
    else:
        # first time encountering this word - count = 1
        word_counts[word] = 1

print (word_counts)





