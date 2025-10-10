# Goal: make a small function called whatever you want and then call(run) it.

def add_two_numb(a,b):
    this_will_happen=(a+b)
    return this_will_happen
print (add_two_numb (1,2))

# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"

# a to d
def count_above(seq,lim):
    count = 0
    for se in seq:
        if seq > lim:
            count + 1
            return
        

# e) Outside the function:
#    - Print the GLOBAL count.
print (count)
#    - Call count_above(nums, limit) and print the returned number.
#    - Print the GLOBAL count again (notice the global didn’t change).
print (count)


4.2
# Text summary  (uses text, summary)
# Goal: classify characters with an if/elif/else chain and return a clear result.
summary ={"digits" : 0, "letters" : 0, "other" : 0}
# a) Define a function named summarize_text that takes one argument: s.
def summarize_text (s):
    summary ={"digits" : 0, "letters" : 0, "other" : 0} # b)
    for suma in s:                               # c) Loop through each character in s:
        if suma.isdigit():
             summary ["digits"] += 1 #       - if the character is a digit, increase "digits"
        elif suma.isalpha():
            summary["letters"] += 1   #       - elif the character is a letter, increase "letters"
        else:
            summary ["other"]+= 1           #       - else increase "other"
    return summary                 # d) Return the summary dictionary.______

# e) Outside the function:
#    - Print the GLOBAL summary.
print (summary)
#    - Call summarize_text(text) and print the returned dictionary.
x= summarize_text("hi26??")
print (x)
#    - Print the GLOBAL summary again.
print (summary)




