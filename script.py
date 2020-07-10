dic = open("dictionary.txt", "r")

out = open("input.txt", "r")

wordlist = dic.read().split('\n')
dic.close()

outputText = out.read()
out.close

for i in wordlist:
    outputText = outputText.replace(
            " " + i + " ", " " + i.capitalize() + " ")

out = open("output.txt", "w")
out.write(outputText)
out.close()
