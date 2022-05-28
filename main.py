# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open("story.txt", "r") as file:
        words = file.read()
        #print(words)
    
    return words

print(read_file_content("story.txt"))
def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    first = text.split()
    x={}
    for i in first:
        x[i] =len(i)
    return x

    #return {"as": 10, "would": 20}
print(count_words())