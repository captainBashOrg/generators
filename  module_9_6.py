print("Генераторы")

def all_variants(text):
    x = 0
    y = 0
    for x in range(len(text)):
        for y in range(x + 1, len(text) + 1):
            #print(text[x:y])
            yield text[x:y]

a = all_variants("abcdef")
for i in a:
    print(i)
