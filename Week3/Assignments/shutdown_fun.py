"""
First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an
s equal to &quot;yes&quot;, it should return &quot;Shutting down&quot; Alternatively, elif s is equal to &quot;no&quot;, then the function
should return &quot;Shutdown aborted&quot;. Finally, if shut_down gets anything other than those inputs, the
function should return &quot;Sorry&quot;.
"""


def shut_down(s):
    if s == "yes":
        return "Shutting Down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"


command = input("Shutdown ?").lower()
print(command)
print(shut_down(command))