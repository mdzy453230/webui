# # import pymysql
# # import xlwt
# #
# # connect = pymysql.connect(database='test_result', user='root', password='jc_test@1234', host='localhost', port=3306)
# # cur = connect.cursor()
# # cur.execute("SELECT * FROM `test_result`.`auto_result` LIMIT 0,1000")
# # fields = [field[0] for field in cur.description]  # 获取所有字段名
# # all_data = cur.fetchall()  # 所有数据
# # # 写入excel
# # book = xlwt.Workbook()
# # sheet = book.add_sheet('sheet1')
# # for col,field in enumerate(fields):
# #     sheet.write(0,col,field)
# # row = 1
# # for data in all_data:
# #     for col,field in enumerate(data):
# #             sheet.write(row,col,field)
# #     row += 1
# # book.save("%s.xls" % auto_result)
# #
#
# # --*-- coding:utf8 --*--
# import pymysql, xlwt
# def export_excel(table_name):
#     # 连接数据库，查询数据
#     conn = pymysql.connect(database='test_result', user='root', password='jc_test@1234', host='localhost', port=3306)
#     cur = conn.cursor()
#     sql = 'select * from %s' % table_name
#     cur.execute(sql)  # 返回受影响的行数
#     fields = [field[0] for field in cur.description]  # 获取所有字段名
#     all_data = cur.fetchall()  # 所有数据
#
#     # 写入excel
#     book = xlwt.Workbook()
#     sheet = book.add_sheet('sheet1')
#     for col,field in enumerate(fields):
#         sheet.write(0,col,field)
#     row = 1
#     for data in all_data:
#         for col,field in enumerate(data):
#             sheet.write(row,col,field)
#         row += 1
#     book.save("%s.xls" % table_name)
# if __name__ == '__main__':
#     export_excel('auto_result')
import xlsxwriter
import datetime
import pymysql

# 定义时间标志变量
sheet_time = datetime.datetime.now()
sheet_mark = sheet_time.strftime('%Y-%m-%d')
book_mark = sheet_time.strftime('%Y%m%d')

# 定义输出excel文件名
workbook = xlsxwriter.Workbook('result.xlsx')

# 定义sheet的名字
worksheet = workbook.add_worksheet(sheet_mark)

# 定义sheet中title的字体format
bold = workbook.add_format({'bold': True})

# 定义sql查询命令
cmd="SELECT * FROM `test_result`.`auto_result` LIMIT 0,1000;"
conn = pymysql.connect(database='test_result', user='root', password='jc_test@1234', host='localhost', port=3306)
cur = conn.cursor()
cur.execute(cmd)
result = cur.fetchall()
fields = cur.description # get column name

for field in range(0,len(fields)):
    worksheet.write(0,field,fields[field][0],bold)

#数据坐标0,0 ~ row,col   row取决于：result的行数；col取决于fields的总数
for row in range(1,len(result)+1):
    for col in range(0,len(fields)):
        worksheet.write(row,col,u'%s' % result[row-1][col])
cur.close()
conn.close()
workbook.close()