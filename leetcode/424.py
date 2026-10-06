s = "AABABBA"
k = 1

l = r = 0
max_freq = 0
freq = {}
max_len = 0

while r < len(s):

    freq[s[r]] = freq.get(s[r],0) + 1

    max_freq = max(max_freq, freq[s[r]])

    while (r - l + 1) - max_freq > k:
        freq[s[l]] -= 1
        l += 1

    max_len = max(max_len, r - l + 1)
    r += 1

print(max_len)