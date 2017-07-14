import pymysql.cursors
import random

connection = pymysql.connect(host='localhost',
														user='wonjin',
														password='1234',
														db='wonjindb',
														charset='utf8')

try:

	with connection.cursor() as cursor:
		sql = "drop table `ubt_vip`;"
		cursor.execute(sql)
	connection.commit()

	with connection.cursor() as cursor:
		sql = "CREATE TABLE IF NOT EXISTS `ubt_vip` (`id` int NOT NULL AUTO_INCREMENT, `cguid` bigint NOT NULL, \
									`gdlc_cd` bigint NOT NULL, \
									`brand_no` int NOT NULL, \
									`vip_cnt` int NOT NULL, \
									PRIMARY KEY (id));"
		cursor.execute(sql)
	connection.commit()
	
	data_lst = []
	cguid_lst = ['11111','22222','33333','44444','5555','66666',\
							'77777','88888','99999']
	gdlc_lst = ['10001', '10002']
	brand_lst = ['1','2','3','4','5']
	for cguid in cguid_lst:
		for gdlc in gdlc_lst:
			for brand in brand_lst:
				data_lst.append([cguid,gdlc,brand,random.randrange(1,99)])

	for data in data_lst:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `ubt_vip` (cguid, gdlc_cd, brand_no, vip_cnt) VALUES(%s,%s,%s,%s);;" % \
						(data[0], data[1], data[2], data[3])
			#sql = "drop table ubt_vip;"
			cursor.execute(sql)
		connection.commit()

	with connection.cursor() as cursor:
		sql = "SELECT * FROM ubt_vip;"
		cursor.execute(sql)
		result = cursor.fetchall()
		print(result)

finally:
	connection.close()