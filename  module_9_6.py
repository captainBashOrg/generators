print("Генераторы")

def all_variants(text):
    x = 0
    y = 0
#    for x in range(len(text)):
#        for y in range(x + 1, len(text) + 1):
#            #print(text[x:y])
#            yield text[x:y]

    for length in range(len(text)):
        for l in range(len(text)-length):
            yield text[l:l+length+1]

a = all_variants("abcdef")
for i in a:
    print(i)
