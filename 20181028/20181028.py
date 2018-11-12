askRedditComment = "I was probably 13 and home on a Saturday night. My parents had been drinking and listening to loud music in the living room so I was in my bedroom. Around 10pm I no longer heard music or talking so I decided to go watch tv in the living room... walked in on my parents doing it with all the lights on. They didn't see me and I immediately turned around and went back the way I came, mortified. Unfortunately we lived in an older house so they heard the floors creaking as I rushed back to my bedroom. A few minutes later I heard my parents drunkenly stumbling down the hall so I turned off my bedroom light and jumped in to bed, pretending to be asleep. I heard them knock on my brother's bedroom door next to mine (he was 10). Since he was still awake and playing video games in his bedroom, my parents assumed he had been the one who walked in on them. My dad, who was pretty drunk at the time, launched in to an hour long awkward talk about 'the birds and the bees' while my brother sat completely confused as to what the fuck was going on."
askRedditCommentlower = askRedditComment.lower()

charCounter = {}
for char in askRedditComment:
  if char not in charCounter:
    charCounter[char] = 0
  charCounter[char] += 1

print(charCounter)

lst = [10, 3, 3, 6, 4, 21, 1]

def insertSort(lst):
  sLst = []
  while len(lst) > 0:
    mElem = min(lst)
    sLst.append(mElem)
    lst.remove(mElem)
  return sLst

a = insertSort(lst)
print(a)

# def bubbleSort(lst):
  