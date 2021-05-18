//分类js
var oDivLength = [];
        var div = document.getElementsByTagName('div');
        var divSpan = document.getElementsByTagName('span');
        //判断有几个列表
        for (var i = 0; i < div.length; i++) {
            div[i].index = i;//给所有div标序号
        }
        for (var i = 0; i < divSpan.length; i++) {
            divSpan[i].onclick = function() {
                oDivLength[this.parentElement.index] = this.innerText//标签的文本;获取对应的文本，其中下标为对应div的序号，从5开始
                var oChild = this.parentElement.children;//获取div下的所有span标签
                for (var j = 0; j < oChild.length; j++) {
                    oChild[j].className = '';//将classname设为“”
                }
                this.className = 'mystyle'; //已选中的当前列的当前元素添加样式
                document.getElementById('yi').innerHTML = ''//标签的html文本;
                for (var m = 0; m < oDivLength.length; m++) { //放到已选择里面
                    if (oDivLength[m] == '' || oDivLength[m] !== undefined) {
                        var para = document.createElement("span");
                        var node = document.createTextNode(oDivLength[m]);
                        para.appendChild(node);
                        document.getElementById('yi').appendChild(para);
                    }
                }
                $.ajax({
                    url: "/query_tag",
                    data: {
                        type:oDivLength[7],date:oDivLength[9],area:oDivLength[11],
                        first:oDivLength[13],num:"0"
                    },
                    success: function (data) {
                        $(".ul_show").empty()
                        if(data.data==""){
                            alert("暂无数据！")
                        }else{
                            for (var i = 0; i < data.data.length; i++) {
                                a="/movie_page?"+"title="+data.data[i][0]+"&scorenum="+data.data[i][7];
                                appendUlBody ="<li> <p class='picture'>"
                                    +"<img src="+"'"+data.data[i][8]+"'"+" height='200px' width='140px' referrer='no-referrer'/></p>"
                                    +"<p class='instroction'>"
                                    +'<a href="'+a+'" style="text-decoration:none;" target="_blank" >'
                                    +data.data[i][0]+"</a><br><br>导演: "+leave_out(data.data[i][2])+"<br>主演: "+leave_out(data.data[i][1])+"<br>"
                                    +data.data[i][4]+"/"+data.data[i][5]+"<br>"+data.data[i][6]+"<br>"+data.data[i][3]+"分<br>"+data.data[i][7]+"人评价</p></li>"
                                $(".ul_show").append(appendUlBody);
                            }
                        }
                    },
                    error: function (xhr, type, errorThrown) {
                    }
                })
            }
        }
        //点击完毕后有数据的为下标5,6,7,8
        function leave_out(str){
            if(str.length>=20)
            {
                str=str.substring(0,20)+"..."
            }
            return str
        }

//加载更多js
var btn=document.getElementById("json_more");
        json_num=20;
        btn.onclick=function(){
            $.ajax({
                    url: "/query_tag",
                    data: {
                        type:oDivLength[7],date:oDivLength[9],area:oDivLength[11],
                        first:oDivLength[13],num:json_num
                    },
                    success: function (data) {
                        if(data.data==""){
                            alert("暂无数据！")
                        }else{
                            for (var i = 0; i < data.data.length; i++) {
                                a="/movie_page?"+"title="+data.data[i][0]+"&scorenum="+data.data[i][7];
                                appendUlBody ="<li> <p class='picture'>"
                                    +"<img src="+"'"+data.data[i][8]+"'"+" height='200px' width='140px' referrer='no-referrer'/></p>"
                                    +"<p class='instroction'>"
                                    +'<a href="'+a+'" style="text-decoration:none;" target="_blank" >'
                                    +data.data[i][0]+"</a><br><br>导演: "+leave_out(data.data[i][2])+"<br>主演: "+leave_out(data.data[i][1])+"<br>"
                                    +data.data[i][4]+"/"+data.data[i][5]+"<br>"+data.data[i][6]+"<br>"+data.data[i][3]+"分<br>"+data.data[i][7]+"人评价</p></li>"
                                $(".ul_show").append(appendUlBody);
                            }
                            json_num=json_num+20;
                        }
                    },
                    error: function (xhr, type, errorThrown) {
                    }
            })
        }
//top榜js
//获取数据
        var toplist=[]
        $.ajax({
            url: "/get_top",
            success: function (data) {
                toplist=data.data
                console.log(toplist[0].topname)
                console.log(toplist[0].topscore)
                console.log(toplist[0].toptime)
                console.log(toplist[0].toprank)
                var str = '';
            for (var i = 0; i < 20; i++) {
                var topname=toplist[i].topname
                var topscore=toplist[i].topscore
                var toptime=toplist[i].toptime
                var toprank=toplist[i].toprank
                str += '<tr>';
                str += '<td class="ellipsis">';
                str += '<span class="center" title="'+topname+'" style="margin-left: 5px;">'+topname+'</span>';
                str += '</td>';

                str += '<td class="ellipsis" title="'+topscore+'"><div class="d_score">'+topscore+'</div></td>';

                str += '<td class="ellipsis" title="'+toprank+'" id="toprank">'+toprank+'</td>';
                str += ' </tr>';
                }
            var box = document.getElementById("bm_content");
            var l1 = document.getElementById("tb1");
            var l2 = document.getElementById("tb2");
            var product = str;
            l1.innerHTML = product;
            if (l1.offsetHeight > box.offsetHeight) {
                l2.innerHTML = l1.innerHTML;//克隆list1的数据，使得list2和list1的数据一样
                scrollMove = setInterval(scrollup, 30);//数值越大，滚动速度越慢
                box.onmouseover = function () {
                    clearInterval(scrollMove)
                    }
                }
            function scrollup() {
            //滚动条距离顶部的值恰好等于list1的高度时，达到滚动临界点，此时将让scrollTop=0,让list1回到初始位置，实现无缝滚动
            if (box.scrollTop >= l1.offsetHeight) {
                box.scrollTop = 0;
                } else {
                box.scrollTop++;
                    }
                }
                //鼠标离开时，滚动继续
                box.onmouseout = function () {
                    scrollMove = setInterval(scrollup, 30);
                }
            }
        })