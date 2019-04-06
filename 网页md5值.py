import requests
import threading
import xlrd                 #输出文件
from xlwt import *          #输入文件
import hashlib

book = xlrd.open_workbook(r"C:\Users\阿苗\Desktop\报告\网站状态码.xls")   #打开本地目录
sheet = book.sheet_by_name(u'Sheet1')               #列表
biao = [sheet.col_values(1)][0]
ming = [sheet.col_values(0)][0]
book_n = Workbook(encoding='utf-8')             #打开一个新文件，以中文写入
sheet_n = book_n.add_sheet('Sheet1')            #创建一个新表格

def duo(s):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    for i in range(s*19,(s+1)*19):
        try:
            response = requests.get(biao[i],headers=header,timeout=20)
            zhuangtai = response.status_code
            a = ''
            print(zhuangtai)
            if zhuangtai != 404 and zhuangtai != 403:
                response.encoding = 'utf-8'
                response = response.text
                # 加密
                md = hashlib.md5()  # 构造一个MD5
                md.update(response.encode())
                a = md.hexdigest()
                print(a)
        #按位置写入
            for r in range(0, 4):
                if r == 0:
                    sheet_n.write(i, r, ming[i])
                elif r == 1:
                    sheet_n.write(i, r, biao[i])
                elif r == 2:
                    sheet_n.write(i, r, str(zhuangtai))
                elif r == 3:
                    sheet_n.write(i, r, str(a))
            book_n.save('C:\python\d\md.xls')                   #保存地址

        except requests.exceptions.ConnectionError as j:
            print('Error',j.args)



def main():
    for s in range(6):  # 6个线程
        t = threading.Thread(target=duo, args=(s,))
        t.start()


main()