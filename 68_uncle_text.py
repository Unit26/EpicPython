s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
s2 = list(s.split())
s3 = [s2.remove(s2[s2.index(x)]) for x in s2 if x.startswith('м') or x.startswith('М')]
s4 = ' '.join(s2)
print(s4)
