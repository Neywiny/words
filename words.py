import time
alphabet = 'abcdefghijklmnopqrstuvwxyz'
with open("wordsUnfiltered.txt") as f:
    buff = list(set(f.readlines()))
#center = str(raw_input("Center: "))
center = 'f'
#letters = str(raw_input("Surrounding: "))
letters = 'racnle'
t1 = time.time()
buff = list(filter(lambda x: center in x,buff))
buff = list(sorted(map(lambda x: x.replace("\n",''),buff)))
alphabet = list(filter(lambda x: (x in letters) or (x in center), alphabet))
res = list()
full = list()
print('starting')
last = None
for word in buff:
    if word[0] not in alphabet:
        continue
    if last != word[0] or word[0]=='z':
        last = word[0]
    for letter in word:
        if letter not in alphabet:
            break
    else:
        res.append(word)
for word in res:
    if len(set(word)) == 7:
        full.append(word)
        res.remove(word)
res.sort()
full.sort()
print('done',len(res)+len(full))
print(res)
print(full)
print('score: ',str(len(res)+(3*len(full))))
print(time.time()-t1)
#input()
###########GENERATE WORDS LIST#####################
##words = set()
##t1 = time.time()
##for i in xrange(1,4):
##    with open("words"+str(i)+'.txt') as f:
##        buff = f.readlines()
##    buff = map(lambda x: x.lower(),buff)
##    buff = filter(lambda x: len(x)>=6 and ('-' not in x) and ("'" not in x) and ("." not in x),buff)
##    words.update(buff)
##words = sorted(list(words))
##with open("wordsUnfiltered.txt","w") as f:
##    f.writelines(words)
##print time.time()-t1
