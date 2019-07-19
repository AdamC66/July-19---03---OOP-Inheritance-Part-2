
# Getting started
# Fork this repository containing the Multilinguist class.
# Inside that repo, make a new virtual environment for this project: pyenv virtualenv multilinguist and then pyenv activate multilinguist.
# Install the requests library by running the following command: pip install requests
# Open the Multilinguist documentation and take a look around.
# At the bottom of multilinguist.py, try creating a Multilinguist instance and calling some of its methods 
# (printing the results to the terminal) to make sure you understand how it works.
# Math genius
# The multilinguist documentation tells us that this class represents a world-traveller who speaks many languages. 
# The first child class that we're going to define represents a world-travelling math genius who can speak many languages and mentally add up huge lists of numbers.

# Instances of this class should be able to accept a list of numbers and returtouchn a sentence stating the sum of the numbers. 
# Make use of the inherited Multilinguist methods to ensure this sentence will always be delivered in the local language.

# me = MathGenius()
# print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# me.travel_to("India")
# print(me.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# me.travel_to("Italy")
# print(me.report_total([324,245,6,343647,686545])) # È Il totale 1030767
# Quote collector
# The second child class we're going to define represents a person who loves to memorize quotes and then travel the world, 
# unleashing poor translations of them to unsuspecting passers-by.

# Each instance of this class should have its own ever-growing collection of favourite quotes. 
# It should have the ability to add a new quote to its collection as well as the ability to select a random quote to share in the local language.

# Stretch goals
# Improve the quote collector's conversational skills be allowing them to keep track of the topic of each quote (eg. "wisdom", "friendship") 
# and add the ability to share a quote according to a specific topic, in addition to being able to share a random one.
# Come up with a third child class that can make use of the multilinguist's abilities.
# Give the math genius additional math-related skills besides adding long lists of numbers. Check out Python's Math module for inspiration.