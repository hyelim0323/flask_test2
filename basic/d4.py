'''
    데이터 베이스 접속후 쿼리 수행 + 파라미터 전달
'''
import pymysql as my

def select_login(uid, upw):
    connection = None
    row = None  
    try:    
        connection = my.connect(host        ='localhost',
                                #port        = 3306,     
                                user        ='root',     
                                password    ='2658374', 
                                database    ='ml_db',    
                                # 조회 결과는 [ {}, {}, {},...  ] 이런 형태로 추출된다                            
                                cursorclass =my.cursors.DictCursor
                                )
        with connection.cursor() as cursor: # cursor는 with문을 벗어나면 자동으로 닫힘
                # 파라미터는 %s 표시로 순서대로 세팅된다 '값' => ''는 자동으로 세팅된다
            sql = '''
                SELECT 
                    `name`, uid, regdate 
                FROM 
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
            '''
            cursor.execute( sql, (uid, upw) )
            row = cursor.fetchone()
            # 5. 결과확인 -> 딕셔너리 -> 이름만 추출하시오 -> '게스트'
            print( row )
            print( row['name'] )
            pass
    except Exception as e:
        print('접속 오류', e)
    else:
        print('접속시 문제 없었음')
    finally:    
        if connection:
            connection.close()   


if __name__ == "__main__":
    # d4 개발자의 테스트 코드
    # f5 개발자가 사용할 때는 작동안함
    select_login('guest', '1234')