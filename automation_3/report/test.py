# coding=utf-8


a = [1, 3, 5, 10, 11, 12, 13, 53]
d_val = 0
around = []
for i in range(len(a)-1):
    d = abs(a[i] - a[i+1])
    if d > d_val:
        d_val = d
        around = [a[i], a[i+1]]

print(str(d_val) + str(around))


if __name__ == '__main__':
    pass
