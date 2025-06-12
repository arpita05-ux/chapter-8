def goodday(name):     # ← 'name' is the **parameter**
    print("Good day," + name)

goodday("Arpita")     # ← "Arpita" is the **argument**
goodday("ram")
goodday("krish") 

# So in short:
# In the definition: it's a parameter
# When calling the function: it's an argument
# But many people casually call both "arguments" in conversation — and that’s okay!

def goodday(name, ending):
    print("Good day," + name)
    print(ending)

goodday("Arpita", "Thank you")     
goodday("krish", "Thank you") 


