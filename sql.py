import string
import time
import traceback
from multiprocessing.dummy import Pool
import pymysql
import requests
import re
from lxml import etree
import random
from bs4 import BeautifulSoup
from flask import json
from functools import partial


# def big_loop(num,url_bean,headers):
#     a=0
#     while a<=10:
#         num_str='%d'%num
#         num=num+20
#         a=a+1;
#         # 获取豆瓣页面电影数据
#         r = requests.get(url_bean + num_str, headers=headers)
#         print(num_str)
#         res_bean = json.loads(r.text);
#         data_bean = res_bean["data"]
#         print(f"{time.asctime()}开始插入数据")
#         insert_data(data_bean,headers)

# 测试函数
def update_time_num():
    cursor = None
    conn = None
    conn, cursor = get_conn()
    i = 5904;
    while i <=5906:
        print(i)
        i_str = '%s' % i
        i = i + 1
        # sql = "select meet from paper_data where id=" + i_str
        # cursor.execute(sql)
        # res = cursor.fetchall()
        # if(res!=()):
        # title_update=replace(res[0][0])
        try:
            sql_0="select scorenum from moviebean where id ="+i_str
            cursor.execute(sql_0)
            res = cursor.fetchall()
            print(res)
            print(res[0][0][1:len(res[0][0])])
            sql = "update  moviebean set scorenum = %s where id=" + i_str
            cursor.execute(sql, [res[0][0][1:len(res[0][0])]])
        except:
            traceback.print_exc()
            print("无此id", i)
    conn.commit()
def test():
    date="\n123456人评价"
    print(date[1:len(date)-3])
# 测试函数
# 获取连接
def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                    user="root",
                    password="000429",
                    db="movierankings",
                    charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor
def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
# 连接--关闭

# 爬取函数
def insert_data(data_beans,headers,cursor,conn):
    try:
        #外层循环（五十个拥有20个电影数据的数组）
        for data_bean in data_beans:
            #20个电影数据
            for i in data_bean:
                # 分配数据
                score = i["rate"].replace(" ", "")
                director = i["directors"]  # []
                director_str = ""
                for j in director:
                    director_str = director_str + " " + j
                name = i["title"].replace(" ", "")
                img = i["cover"].replace(" ", "")
                star = i["casts"]  # []
                star_str = ""
                for j in star:
                    star_str = star_str + " " + j
                # 分配数据

                # 获取电影详细数据的网址
                url_details = i["url"].replace(" ", "")
                print(url_details)
                r = requests.get(url_details, headers=headers)
                soup_bean = BeautifulSoup(r.text, "lxml")
                # 获取详细数据
                span = soup_bean.find_all("span", {"property": "v:genre"})
                type = ""
                for i in span:
                    type = type + " " + i.text
                span = soup_bean.find_all("span", {"property": "v:runtime"})
                timelen = span[0].text.replace(" ", "")
                span = soup_bean.find_all("span", {"property": "v:initialReleaseDate"})
                date_str= span[0].text.replace(" ", "")
                if(date_str.find('(')==-1):
                    date=date_str
                else:
                    date=date_str[0:date_str.find('(')]
                span = soup_bean.find("a", {"class", "rating_people"})
                scorenum_str = span.text.replace(" ", "")
                scorenum=scorenum_str[1:len(scorenum_str)-4]
                span = soup_bean.find("span", {"property": "v:summary"})
                summary = span.text.replace(" ", "")  # 将空格去掉
                ex = ' <span class="pl">制片国家/地区:</span> (.*?)<br/>'
                test = re.findall(ex, r.text, re.S)
                area = test[0].replace(" ", "")
                ex2 = '<span class="pl">语言:</span> (.*?)<br/>'
                test = re.findall(ex2, r.text, re.S)
                language = test[0].replace(" / ", " ")
                # 获取详细数据
                sql = "insert into moviebean (title,star,director,type_movie,area,date_time,summary,score,language_movie,img,scorenum,timelen) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,
                               [name, star_str, director_str, type, area, date, summary, score, language, img, scorenum,
                                timelen])
        conn.commit()  # 提交事务 update delete insert操作 //*[@id="info"]/text()[2]
        print(f"{time.asctime()}插入数据完毕")
    except:
        traceback.print_exc()
def get_bean_data():
    #豆瓣的网址
    url_bean = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }
    # num=[0,1020,2020,3020,4020,5020,6020,7020,8020,9020]
    # partial_big_loop =partial(big_loop,url_bean=url_bean,headers=headers)
    # #大循环在10个线程中进行
    # pool=Pool(10)
    # pool.map(partial_big_loop,num)
    # pool.close()
    # pool.join()
    cursor = None
    conn = None
    conn, cursor = get_conn()
    data_beans=[]
    num=2940#1820/1960/800/2320/2760
    b=0;
    while b<=500:
        a = 1
        b=b+1
        while a <= 1:
            num_str = '%d' % num
            num = num + 20
            a = a + 1;
            # 获取豆瓣页面电影数据
            r = requests.get(url_bean + num_str, headers=headers)
            print(num_str)
            res_bean = json.loads(r.text);
            print(url_bean+num_str)
            data_beans.append(res_bean["data"])
            print(f"{time.asctime()}开始插入数据")
        insert_data(data_beans, headers,cursor,conn)
        data_beans=[]
    print(f"{time.asctime()}所有数据插入完毕")
    close_conn(conn, cursor)
# 爬取函数

# 查询函数
def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询结果以((),(),)形式
    """
    conn,cursor = get_conn();
    cursor.execute(sql)
    res=cursor.fetchall()
    close_conn(conn,cursor)
    return res
#分类排序查询
def find_class_order(str):
    sql="select title,star,director,score,date_time,area,type_movie,scorenum,img from moviebean where 1=1 " \
        "and (type_movie like "+"'%"+str[0]+"%'"+") and (date_time like "+"'%"+str[1]+"%'"+") and(area like "+"'%"+str[2]+"%'"+") "
    if(str[3]=="star_1" or str[3]=="评分最高"):
        sql=sql+" order by score desc "
    if(str[3]=="star_0"):
        sql=sql+" order by score "
    if(str[3]=="hot_1" or str[3]=="最热门"):
        sql=sql+" order by scorenum desc "
    if(str[3]=="hot_0"):
        sql=sql+" order by scorenum "
    if(str[3]=="time_1" or str[3]=="最近更新"):
        sql=sql+" order by date_time desc "
    if(str[3]=="time_0"):
        sql=sql+" order by date_time "
    sql=sql+"limit "+str[4]+",20 "
    res = query(sql)
    print("分类查询")
    print(sql)
    print(res)
    return res
#详情页面查询
def find_by_title_and_scorenum(title,scorenum):
    sql = "select title,star,director,type_movie,area,date_time," \
          "summary,score,language_movie,img,scorenum,timelen from moviebean " \
          "where title="+"'"+title+"' and scorenum="+scorenum
    res=query(sql)
    print("详情页面")
    print(sql)
    print(res[0])
    return res[0]
#搜索查询
def find_by_qury_top(str):
    sql = "select title,star,director,score,date_time,area," \
          "type_movie,scorenum,img from moviebean " \
          "where (title like"+" '%"+str+"%') or (star like"+" '%"+str+"%' )"
    res = query(sql)
    print("Top-Query")
    print(sql)
    print(res)
    return res
# 查询函数 第二个页面moviepager.html
def find_all_movies(title):
    """
    SELECT
      A.`title`
    FROM
      moviebean A,
      movieimdb B,
      movieiqy C,
      moviesohu D,
      movieten E,
      movie1905 F
    WHERE A.`title` = B.`name`
      AND A.`title` = C.`name`
      AND A.`title` = D.`name`
      AND A.`title` = E.`name`
      AND A.`title` = F.`name`;

    :param title:
    :return:
    """
    dataRes=[]
    sqlten=" select name,score,path,state from movieten where name='"+title+"'"
    sqliqy=" select name,score,path,state from movieiqy where name='"+title+"'"
    sqlimdb=" select name,score from movieimdb where name='"+title+"'"
    sql1905 = " select name,score,path,state from movie1905 where name='"+title+"'"
    sqlsohu = " select name,score,path,state from moviesohu where name='" + title + "'"
    tencData=query(sqlten)
    iqyData=query(sqliqy)
    imdbData=query(sqlimdb)
    _1905Data=query(sql1905)
    sohuData=query(sqlsohu)
    try:
        dataRes.append(tencData[0])  # 腾讯
        # print(tencData[0])
    except:
        dataRes.append("")
    try:
        dataRes.append(iqyData[0])      #爱奇艺
    except:
        dataRes.append("")
    try:
        dataRes.append(imdbData[0])    #IMDB
    except:
        dataRes.append("")
    try:
        dataRes.append(_1905Data[0])  # 1905
    except:
        dataRes.append("")
        # print(_1905Data)
    try:
        dataRes.append(sohuData[0])  # 搜狐
    except:
        dataRes.append("")
    print(dataRes)
    # print(tencData[0])
    return dataRes
#查询函数   top榜滚动条
def get_top():
    dataRes=[]
    sql='select * from moviebean limit 100;'
    dataRes=query(sql)
    # print(len(dataRes))
    return dataRes
#搜索查询
def find_by_qury_head(str):
    sql = "select title,star,director,score,date_time,area," \
          "type_movie,scorenum,img from moviebean " \
          "where (title like"+" '%"+str+"%') or (star like"+" '%"+str+"%' )"
    res = query(sql)
    print("顶部搜索查询")
    print(sql)
    print(res)
    return res
# 查询函数

#用户部分
#用户（app）注册
def android_register(name,phone,password):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql="insert into userdata (userphone,userpass,useremail,username,userimg) values(%s,%s,%s,%s)"
    cursor.execute(sql,[phone,password,"",name,"../static/userimg/0000.jpg"])
    conn.commit()
    close_conn(conn,cursor)
    print("注册成功（APP）")
# 用户（web）注册
def web_register(phone, password, email , name):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql = "insert into userdata (userphone,userpass,useremail,username,userimg) values(%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, [phone, password, email, name, "../static/userimg/0000.jpg"])
        conn.commit()
    except(pymysql.err.IntegrityError):
        print("用户名已存在，注册失败")
        return False
    close_conn(conn, cursor)
    print("注册成功（WEB）")
# 用户（web）登录验证
def web_login(userphone, password):
    cursor = None
    conn = None
    res=[]
    if(userphone==None or password==None):
        return False
    conn, cursor = get_conn()
    sql = "select userphone,userpass from userdata where '"+userphone+"'=userphone and '"+password+"'=userpass "
    res=query(sql)
    conn.commit()
    if(len(res)==0):
        print("登陆失败（WEB）")
        close_conn(conn, cursor)
        return False
    else:
        close_conn(conn, cursor)
        print("登陆成功（WEB）")
        return True
#用户（app）查询
def android_query(phone):
    sql="select userphone,userpass,useremail,username,userimg from userdata where userphone="+phone
    res = query(sql)
    print("用户（app）查询")
    print(sql)
    res_2=("","","","","")
    try:
        print(res[0])
    except:
        print(res_2)
        return res_2
    return res[0]
#用户（app）收藏
def android_like(userphone,usermovie,usertyppe,scorenum,url,score):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    if (android_like_query_one(userphone, "", usermovie, scorenum)):
        try:
            sql = "delete from userlike where (userphone='" + userphone + "') and (usermovie='" + usermovie + \
              "')  and (scorenum=" + scorenum + ") "
            cursor.execute(sql)
            conn.commit()
        except:
            traceback.print_exc()
            return 0
    try:
        sql = "insert into userlike(userphone,usermovie,usertype,scorenum,url,score) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, [userphone, usermovie, usertyppe, scorenum, url, score])
        conn.commit()
        close_conn(conn, cursor)
    except:
        traceback.print_exc()
        return 0
    print("收藏（app）成功")
    return 1
#用户（app）收藏查询
def android_like_query(userphone,usertype):
    sql="select userphone,usermovie,usertype,scorenum,url,score from userlike where userphone='"+userphone+"' and usertype='"+usertype+"'"
    res = query(sql)
    print("用户（app）收藏查询")
    print(sql)
    print(res)
    return res
#用户（app）收藏删除
def android_delete(userphone,usertype,usermovie,scorenum):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql="delete from userlike where (userphone='"+userphone+"') and (usermovie='"+usermovie+\
        "') and (usertype='"+usertype+"') and (scorenum="+scorenum+") "
    try:
        print("用户（app）收藏删除")
        print(sql)
        cursor.execute(sql)
        conn.commit()
        close_conn(conn,cursor)
        return 1
    except:
        traceback.print_exc()
        return 0
#用户（app）收藏查询单个
def android_like_query_one(userphone,usertype,usermovie,scorenum):
    sql="select * from userlike where (userphone='"+userphone+"') and (usermovie='"+usermovie+\
        "') and (usertype like '%"+usertype+"%') and (scorenum="+scorenum+") "
    res = query(sql)
    print("用户（app）收藏查询单个")
    print(sql)
    try:
        print(res[0])
    except:
        traceback.print_exc()
        return 0
    return 1
#用户（app）收藏转移
def android_user_like_trans(userphone,usertype,usermovie,scorenum,usertype_new):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    if(android_like_query_one(userphone,usertype_new,usermovie,scorenum)):
        return -1;
    sql="update userlike set usertype='"+usertype_new+"' where (userphone='"+userphone+"') and (usermovie='"+usermovie+\
        "') and (usertype='"+usertype+"') and (scorenum="+scorenum+") "
    try:
        cursor.execute(sql)
        conn.commit()
        close_conn(conn, cursor)
        print("用户（app）收藏转移")
        print(sql)
        return 1
    except:
        traceback.print_exc()
        return 0
#用户上传头像
def user_img_input(userimg,userphone):
    cursor = None
    conn = None
    conn, cursor = get_conn()
    sql = "update userdata set userimg="+"'"+userimg+"' where userphone="+userphone
    try:
        cursor.execute(sql)
        conn.commit()
        close_conn(conn, cursor)
        print("上传成功")
        print(userimg+""+userphone)
        return 1
    except:
        traceback.print_exc()
        return 0
#用户部分

#-------------------------------------------#
#重置密码
def reset_pass(phone,password):
    conn,cursor=get_conn()
    sql="update userdata set userpass='"+password+"' where userphone='"+phone+"'"
    try:
        print("正在修改密码...")
        resetflag=cursor.execute(sql)
        conn.commit()
        close_conn(conn,cursor)
        if(resetflag==1):
            print("修改成功")
            return 1
        else:
            print("修改失败！")
            return 0
    except:
        print("系统错误...修改密码失败！")
        return 0

if __name__ == "__main__":
    # find_class_order(["喜剧","2020","中国","star_1","20"])
    # get_bean_data()
    reset_pass("15284206891","success02")
    # get_top()
    # update_time_num()
    # test()
    # find_by_title_and_scorenum("洛杉矶之战","100074")
    # find_by_qury_top("大圣")
    # res=find_all_movies("肖申克的救赎")
    # print(res)
    # find_all_movies("危险关系")
    # find_by_title_and_scorenum("危险关系", "80248")
