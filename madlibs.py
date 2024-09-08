madlib_words = {
    "noun": "",
    "verb": "",
    "adjective": ""
    }

madlib_words["noun"] = input("Enter a noun: ")
madlib_words["verb"] = input("Enter a verb: ")
madlib_words["adjective"] = input("Enter an adjective: ")

print("The %s %s is %s" % (madlib_words["adjective"], madlib_words["noun"], madlib_words["verb"]))