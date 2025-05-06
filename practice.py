"""
This is a simple Python script that applies PEP 8 style guide recommendations to a given Python file.
Also, it works as a practice for using git command line and GitHub.
"""
#----------------------------------------------------------

# Identation = 4 spaces per level

#----------------------------------------------------------

# Incorrect indentation:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)