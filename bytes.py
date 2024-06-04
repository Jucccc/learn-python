# small integer ranging from 0 to 255

avengers = b'Tony, Steve, Bruce'
print(avengers)
print(type(avengers))

avengers2 = b'Gro\xddt'
#avengers2 = rb'Gro\xddt'
print(avengers[3])
print(int(0xdd))