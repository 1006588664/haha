import csv

with open(r"C:\Users\Administrator\Desktop\Record.csv",'r' ) as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    row = []
    #print(rows)
    s = rows
    for i in s[1:-1]:
        # print(i[4])
        seconds = float(i[4])
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        # print("%d:%02d:%02d" % (h, m, s))
        wj = ("%d:%02d:%02d" % (h, m, s))
        a = i
        a[4] = wj
        row.append(wj)
print(row)
fileOb = open('baidu1.csv', 'w', encoding='utf-8')  # 打开一个文件，没有就新建一个
fileOb.write(str(row))
fileOb.close()


