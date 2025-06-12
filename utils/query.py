import pymysql

def querys(sql, params, type='no_select'):
    try:
        # 创建数据库连接
        conn = pymysql.connect(host='localhost', user='root', password='root', database='doubanmovie', port=3306)
        cursor = conn.cursor()
        params = tuple(params)

        cursor.execute(sql, params)

        if type != 'no_select':
            data_list = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return data_list
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return '数据库操作成功'
    except pymysql.MySQLError as e:
        print(f"数据库错误: {e}")
        return None
    except Exception as e:
        print(f"其他错误: {e}")
        return None
