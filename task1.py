def count_vsound(text):
    count = 0
    for letter in text:
        if letter in vsound:
            count +=1
    return count
vinnipuh = input("введите фразу: ")
vsound = ["а","е","ё","и","о","у","ы","э","ю","я"]
phrases = vinnipuh.split()
vcount = count_vsound(phrases[0])
phraseOK = True
for phrase in phrases:
    phraseOK &= count_vsound(phrase) == vcount
if phraseOK:
        print("Парам пам-пам")
else: print("Пам парам")


