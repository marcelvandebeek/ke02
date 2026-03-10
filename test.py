filename = 'C:\\Users\\beekmhwa\\OneDrive - Zuyd Hogeschool\\_Zuyd\\_OE\\_summerschool\\2023\\vissenradio.txt'
lijst = []
dictionary = {}

# lees bestand
f = open(filename, 'r')
for line in f.readlines():
    lijst.append(line.strip())
f.close()

regel = (lijst[0])
lijst.clear()
rmax = len(regel)
pleft = 0
pright = regel.find(' ', pleft + 1, rmax)

while pright != -1:
    print(regel[pleft:pright])
    lijst.append(regel[pleft:pright])
    pleft = pright + 1
    pright = regel.find(' ', pleft, rmax)
    regel.find(' ', pright, rmax) + 1

print(lijst)
lijst.sort
print(lijst)
