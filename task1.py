def isanagram(word1,word2):
    #sorts words and compares them
    return sorted(word1) == sorted(word2)



while(1):
    word_input = input("Input:\n")

    #checking if the input is not in lowercase
    if not word_input.islower():
        print("Your words need to be lowercase!")
        continue
    #checking if the amount of words is different than two
    if len(word_input.split()) != 2:
        print("You need to write two words!")
        continue
    word1, word2 = word_input.split()
     
    if isanagram(word1,word2):
        print("Output:\nYES")
    else:
        print("Output:\nNO")
    break
