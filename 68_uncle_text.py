s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
words = s.split()
for x in words:
    start_m = x.startswith('м') or x.startswith('М')
    if start_m:
        words.remove(x)

new_s = ' '.join(words)
print(new_s)
