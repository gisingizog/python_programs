# Build a word count function which display the following through
# input provided by the user:
# i. Number of characters without spaces
# ii. Number of characters with spaces
# iii. Number of words

sentence = input('Enter text: ');

def wordCount(userInput):
    print(len(userInput));
    wordCount = 0;
    withoutSpaces = 0;
    withSpaces = 0;
    i = 0;
    while i < len(userInput):
        wordCount = len(userInput.split(' '));
        withSpaces = len(userInput);
        if userInput[i] != ' ':
            withoutSpaces += 1;
            i += 1;
        else : 
            i += 1;
    
    textInfo = [wordCount, withoutSpaces, withSpaces];
    return textInfo;

sentenceInfo = wordCount(sentence);

print(f'Sentence info for {sentence}: \n Number of characters without spaces: {sentenceInfo[1]}\n Number of characters with spaces: {sentenceInfo[2]}\n Number of words: {sentenceInfo[0]}');
