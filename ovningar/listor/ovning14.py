talföljd = [0, 1]

while (len(talföljd) < 100):
    talföljd.append((talföljd[-1] + talföljd[-2]))

print(talföljd)