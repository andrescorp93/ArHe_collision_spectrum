import numpy as np
import re

so_file = open("DM.out", "r")
m = [line.strip() for line in so_file.readlines()]
so_file.close()
parsed_dx = []
parsed_dy = []
parsed_dz = []
for j in range(len(m)):
    if re.search("DMX", m[j]) is not None:
        t1 = [s for s in m[j + 6: j + 1052] if s != '']
        t = [s.split() for s in t1 if re.search("Nr", s) is None]
        for k in range(len(t)):
            if k % 2 == 0:
                t[k] = t[k][2:]
        parsed_dx.append(t)
    if re.search("DMY", m[j]) is not None:
        t1 = [s for s in m[j + 6: j + 1052] if s != '']
        t = [s.split() for s in t1 if re.search("Nr", s) is None]
        for k in range(len(t)):
            if k % 2 == 0:
                t[k] = t[k][2:]
        parsed_dy.append(t)
    if re.search("DMZ", m[j]) is not None:
        t1 = [s for s in m[j + 6: j + 1052] if s != '']
        t = [s.split() for s in t1 if re.search("Nr", s) is None]
        for k in range(len(t)):
            if k % 2 == 0:
                t[k] = t[k][2:]
        parsed_dz.append(t)

dx = []
dy = []
dz = []
for j in range(len(parsed_dx)):
    preout = []
    out = []
    for k in range(len(parsed_dx[j])):
        if k % 2 == 0:
            r = np.array([float(s) for s in parsed_dx[j][k]])
            i = np.array([float(s) for s in parsed_dx[j][k + 1]])
            row = r + 1j * i
            preout.append(row)
    for i in range(49):
        t1 = np.array(preout[i])
        t2 = np.array(preout[i + 49])
        t3 = np.array(preout[i + 98])
        t4 = np.array(preout[i + 147])
        t5 = np.array(preout[i + 196])
        t6 = np.array(preout[i + 245])
        t7 = np.array(preout[i + 294])
        out.append(np.hstack((t1, t2, t3, t4, t5, t6, t7)))
    dx.append(np.array(out))

for j in range(len(parsed_dy)):
    preout = []
    out = []
    for k in range(len(parsed_dy[j])):
        if k % 2 == 0:
            r = np.array([float(s) for s in parsed_dy[j][k]])
            i = np.array([float(s) for s in parsed_dy[j][k + 1]])
            row = r + 1j * i
            preout.append(row)
    for i in range(49):
        t1 = np.array(preout[i])
        t2 = np.array(preout[i + 49])
        t3 = np.array(preout[i + 98])
        t4 = np.array(preout[i + 147])
        t5 = np.array(preout[i + 196])
        t6 = np.array(preout[i + 245])
        t7 = np.array(preout[i + 294])
        out.append(np.hstack((t1, t2, t3, t4, t5, t6, t7)))
    dy.append(np.array(out))

for j in range(len(parsed_dz)):
    preout = []
    out = []
    for k in range(len(parsed_dz[j])):
        if k % 2 == 0:
            r = np.array([float(s) for s in parsed_dz[j][k]])
            i = np.array([float(s) for s in parsed_dz[j][k + 1]])
            row = r + 1j * i
            preout.append(row)
    for i in range(49):
        t1 = np.array(preout[i])
        t2 = np.array(preout[i + 49])
        t3 = np.array(preout[i + 98])
        t4 = np.array(preout[i + 147])
        t5 = np.array(preout[i + 196])
        t6 = np.array(preout[i + 245])
        t7 = np.array(preout[i + 294])
        out.append(np.hstack((t1, t2, t3, t4, t5, t6, t7)))
    dz.append(np.array(out))

dx = np.array(dx)
dy = np.array(dy)
dz = np.array(dz)

intens = np.absolute(dx) ** 2 + np.absolute(dy) ** 2 + np.absolute(dz) ** 2

print(intens[0, 1])
print(intens[0, 13])
print(intens[0, 25])
print(intens[0, 37])
print(intens[0, 38])

