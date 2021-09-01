import re
text = 'Allowed Hello Hloolw'
found = re.finditer('l', text)
#for m in found:
#    print(m.span())

occ = []
for m in found:
    print(m.start())
    occ += [m.start()]

print(occ)

occ_queue = []
for idx,t in enumerate(text):
    try:
        if t == 'l':
            occ_queue += [idx]
            start = idx
    except Exception as err:
        print(err)
        pass
    finally:
        if len(occ_queue) == 3:
            del occ_queue[0]

print(occ_queue)