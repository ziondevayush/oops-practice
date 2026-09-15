def Word_Count(sentence):
    words = sentence.split()
    return len(words)

sen = input("Enter Sentence: ")
result = Word_Count(sen)
print(result)

