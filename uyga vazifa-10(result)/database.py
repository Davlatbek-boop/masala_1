import pymysql


def datayoz(ism, sharif, yosh, jins, viloyat, raqam, fakultet, kurs):
    try:
        conn=pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
        )
        cursor=conn.cursor()  
        cursor.execute('create database if not exists malumot')
        cursor.execute('use malumot')
        cursor.execute('''create table if not exists students (
                        id int auto_increment primary key, 
                        first_name varchar(32), 
                        last_name varchar(32),
                        age int,
                        gender varchar(16),
                        region varchar(32),
                        phone varchar(15),
                        faculty varchar (32),
                        course varchar (8))''')
    
        cursor.execute(f''' insert into students 
                        (first_name, last_name, age, gender, region, phone, faculty, course)
                        values
                        ("{ism}","{sharif}",{yosh},"{jins}","{viloyat}","{raqam}","{fakultet}","{kurs}")
    ''')
        conn.commit()
        return True
    except:
        return False


# def datayoz(ism, sharif, yosh, jins, viloyat, raqam, fakultet, kurs):
#     try:

#         cursor.execute(f''' 
# insert into students (first_name, last_name, age, gender, region, phone, faculty, course)
#                     values
#                     ({ism},{sharif},{yosh},{jins},{viloyat},{raqam},{fakultet},{kurs})
# ''')
#     except:
#         print('datalar yozilmadi')