s1 = "ab"
s2 = "eidbaooo"

l = 0
r = len(s1)

def count(str):
    count = {}
    for i in range(len(str)):
        count[str[i]] = count.get(str[i],0) + 1
    return count

need = count(s1)
window = count(s2[:len(s1)])
if need == window:
        print(True)

while r < len(s2):
    window[s2[l]] -= 1
    if window[s2[l]] == 0:
        del window[s2[l]]
    window[s2[r]] = window.get(s2[r],0) + 1
    l += 1
    r += 1
    if need == window:
        print(True)
        break

