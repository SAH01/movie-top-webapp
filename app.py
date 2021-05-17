from flask import request, jsonify, render_template
from flask import redirect
from flask import Flask, url_for
import sql
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("login.html")
@app.route('/regis')
def regis():
    return render_template("regitser.html")
@app.route('/show')
def hello_world_show():
    return render_template("show.html")
#星级

@app.route('/movie_page')
def hello_world_movie_page():
    title=request.values.get("title")
    scorenum=request.values.get("scorenum")
    str_s=sql.find_by_title_and_scorenum(title,scorenum)
    #获取所有查询到的带星级电影库 腾讯、爱奇艺、IMDB、1905、搜狐
    str_three=sql.find_all_movies(title)

    return render_template("moviepager.html",title=str_s[0],star=str_s[1],
                           director=str_s[2],type_movie=str_s[3],area=str_s[4]
                           ,date_time=str_s[5],summary=str_s[6],score=str_s[7]
                           ,language_movie=str_s[8],img=str_s[9],scorenum=str_s[10]
                           ,timelen=str_s[11],str_one=str_three[0],str_two=str_three[1]
                           ,str_three=str_three[2],str_four=str_three[3],str_five=str_three[4])

@app.route('/android_query')
def android_query():
    title = request.values.get("title")
    scorenum = request.values.get("scorenum")
    str_s = []
    str_s = sql.find_by_title_and_scorenum(title, scorenum)
    return jsonify({"data": str_s})

@app.route('/query_tag')
def query_tag():
    str_s=[]
    str_s.append(request.values.get("type"))
    str_s.append(request.values.get("date"))
    str_s.append(request.values.get("area"))
    str_s.append(request.values.get("first"))
    str_s.append(request.values.get("num"))
    if (str_s[3] == "热门(正序)"):
        str_s[3]="hot_1"
    if (str_s[3] == "热门(倒序)"):
        str_s[3]="hot_0"
    if (str_s[3] == "评分(正序)"):
        str_s[3]="star_1"
    if (str_s[3] == "评分(倒序)"):
        str_s[3]="star_0"
    if (str_s[3] == "时间(正序)"):
        str_s[3]="time_1"
    if (str_s[3] == "时间(倒序)"):
        str_s[3]="time_0"
    if(str_s[0]=="全部"):
        str_s[0]=""
    if(str_s[1]=="全部"):
        str_s[1]=""
    if(str_s[2]=="全部"):
        str_s[2]=""
    if(str_s[0]==None):
        str_s[0]=""
    if(str_s[1]==None):
        str_s[1]=""
    if(str_s[2]==None):
        str_s[2]=""
    if(str_s[3]==None):
        str_s[3]=""
    print(str_s)
    data=[]
    for i in sql.find_class_order(str_s):
        data.append(i)
    return jsonify({"data": data})
#获取top
@app.route('/get_top')
def get_top():
    toplist=[]
    temptoplist=sql.get_top()
    dataRes=[]
    print("这里是路由get_top")
    for item in temptoplist:
        toplist.append(item[1])
        toplist.append(item[8])
        toplist.append(item[12])
        dataRes.append(toplist)
        toplist=[]
    return jsonify({"data": dataRes})
if __name__ == '__main__':
    host="127.0.0.1"
    port=5000
    app.run(host,port)
