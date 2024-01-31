# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

import utils as u


# Example of how to specify a binary with the structure:
#
#         Root
#         /  \
#        /    \
#       A      B
#      / \    / \
#     C   D  E   F
#
root = u.BinaryTree("Root")
A = root.insert_left("Root rule left")
B = root.insert_right("Root root right")
C = A.insert_left("A rule left")
D = A.insert_right("B rule right")
E = B.insert_left("B rule left")

print("\nPrint Tree")
root.print_tree()
print()

""" 
Notes: 
"A rule left" would be the specific rule. For example, for a
a boolean variables, it would be "A = True" or "A = False". 
For a continuous variable: left corrresponds to x <= 53.7 (for example). 
The specifics are laid out in the problems below. 
"""


# ----------------------------------------------------------------------


def question1():
    answer = False
    answer = {}
    level1 = {}
    level2 = {}

    # Leave as None if it doesn't apply
    level1["smoking"] = 0.0
    level1["smoking_info_grain"] = 0.0
    level1["cough"] = 0.0
    level1["cough_info_gain"] = 0.0
    level1["radon"] = 0.0
    level1["radon_info_grain"] = 0.0
    level1["weight_loss"] = 0.0
    level1["weight_loss_info_gain"] = 0.0

    level2["smoking"] = 0.0
    level2["smoking_info_grain"] = 0.0
    level2["cough"] = 0.0
    level2["cough_info_gain"] = 0.0
    level2["radon"] = 0.0
    level2["radon_info_grain"] = 0.0
    level2["weight_loss"] = 0.0
    level2["weight_loss_info_gain"] = 0.0

    answer["level1"] = level1
    answer["level2"] = level2

    # change tree as needed
    tree = u.BinaryTree("Root")  
    answer["tree"] = tree
    answer["training_error"] = 0.

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.0
    answer["(b) x < 0.2"] = 0.0
    answer["(b) x < 0.7"] = 0.0
    answer["(b) y < 0.6"] = 0.0

    # choose one of 'x = 0.2', 'x = 0.7', or 'x = 0.6'
    answer["(c) attribute"] = 0.0

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    # Fill up the tree
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a)"] = 0.0

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.0
    answer["(d) Gini, Car type"] = 0.0

    # One of ['ID', 'Gender', 'Car type'] (string)
    answer["(e) attr with lowest Gini"] = ""

    # Attribute for splitting
    answer["(f) attr for splitting"] = ""

    # Explanatory text string
    answer["(f) explain choice"] = ""

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ""

    # Explain if there is more than one interpretation. Repeat for the other questions.
    answer["a, explain"] = ""

    answer["b"] = ""
    answer["b explain"] = ""

    answer["c"] = ""
    answer["c explain"] = ""

    answer["d"] = ""
    answer["d explain"] = ""

    answer["e"] = ""
    answer["e explain"] = ""

    answer["f"] = ""
    answer["f explain"] = ""

    answer["g"] = ""
    answer["g explain"] = ""

    answer["h"] = ""
    answer["h explain"] = ""

    answer["i"] = ""
    answer["i explain"] = ""

    answer["j"] = ""
    answer["j explain"] = ""

    answer["k"] = ""
    answer["k explain"] = ""

    answer["l"] = ""
    answer["l explain"] = ""

    answer["m"] = ""
    answer["m explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = ""
    explain["a explain"] = ""

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = ""
    explain["b explain"] = ""

    # string: one of 'Model 1' or 'Model 2'
    explain["c similarity"] = ""
    explain["c difference"] = ""

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}

    # answer is 'x <= c' or 'y <= c' where `c` is a float
    # Left: x < ..., Right: x > ...
    answer["a, level 1"] = ""
    answer["a, level 2, left"] = ""
    answer["a, level 2, right"] = ""
    answer["b, expected error"] = ""

    # Use u.BinaryTree to define the tree. Create your tree.
    answer["c, tree"] = u.BinaryTree("Root")

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}
    # answer is a float
    answer["a, info gain, ID"] = 0.0
    answer["b, info gain, Handedness"] = 0.0

    # string: one of 'ID' or 'Handedness' based in information gain
    answer["c, which attrib"] = ""

    # answer is a float
    answer["d, gain ratio, ID"] = 0.0
    answer["e, gain ratio, Handedness"] = 0.0

    # string: one of 'ID' or 'Handedness' based on gain ratio
    answer["f, which attrib"] = ""

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
