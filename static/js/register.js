function next(i){
    if(i==1){
        $("#step-01").css("display","none");
        $("#step-02").css("display","block");
        $("#step-01-line").css("backgroundColor","#0C75BB");
        $("#step-2").css("backgroundColor","#0C75BB");
        $("#step-2-text").css("color","#0C75BB");
    }else if(i==2){
        $("#step-02").css("display","none");
        $("#step-03").css("display","block");
        $("#step-3").css("backgroundColor","#0C75BB");
        // $("#step-02-line").css("backgroundColor","#0C75BB");
        // $("#step-3-text").css("color","#0C75BB");
    // }else if(i==3){
    //     $("#step-03").css("display","none");
    //     $("#step-04").css("display","block");
    //     $("#step-4").css("backgroundColor","#0C75BB");
    //     $("#step-03-line").css("backgroundColor","#0C75BB");
    //     $("#step-4-text").css("color","#0C75BB");
    //     console.log($("#userobjectform").serialize());
    //     console.log($("#userinfoform").serialize());
    //     console.log($("#passwordform").serialize());
    //     //serializeObject()
    }
    else{
        console.log(225)
    }
}
var host="127.0.0.1"
var port=5000
function previous(i){
    if(i==2){
        $("#step-01").css("display","block");
        $("#step-02").css("display","none");
        $("#step-01-line").css("backgroundColor","#cccccc");
        $("#step-2").css("backgroundColor","#cccccc");
        $("#step-2-text").css("color","#cccccc");
    }
    // else if(i==3){
    //     $("#step-02").css("display","block");
    //     $("#step-03").css("display","none");
    //     $("#step-02-line").css("backgroundColor","#cccccc");
    //     $("#step-3").css("backgroundColor","#cccccc");
    //     $("#step-3-text").css("color","#cccccc");
    // }
}
//跳转功能

// function gologin(){
//     window.open("http://"+host+":"+port, "_self")
// }
// function goindex(){
//     // alert("请先登录！");
//     window.open("http://"+host+":"+port+"/show", "_self")
// }
//
function showTips(id,info){
    document.getElementById(id+"span").innerHTML="<font color='gray'>"+info+"</font>";
}

function check(id,info){
    var uValue = document.getElementById(id).value;
    if(uValue==""){
        document.getElementById(id+"span").innerHTML="<font color='red'>"+info+"</font>";
    }else{
        document.getElementById(id+"span").innerHTML="";
    }
}

function showTips_pass(id,info){
    document.getElementById(id+"span").innerHTML="<font color='gray'>"+info+"</font>";
}

function check_pass(id,info){
    var one_pass=document.getElementById("password").value
    var two_pass = document.getElementById(id).value;
    if(one_pass!=two_pass||(two_pass=="")){
        document.getElementById(id+"span").innerHTML="<font color='red'>"+info+"</font>";
    }else{
        document.getElementById(id+"span").innerHTML="";
    }
}
//检测第二步信息

//检测中文字符
function checkCN(str){
    if (escape(str).indexOf("%u")<0){       //indexOf()方法查找字符串是否包含"\u" 
        return true;    //没有
    } else {
        return false;       //有
    }
}
function check_name(){
    // alert("!")
    //检测昵称合法性 2-16个字符
    var username=document.getElementById("username").value
    part_name=username.split(" ")
    if(part_name.length!=1){
        alert("昵称不可以包含空格！")
        document.getElementById("username").focus();
        return false
    }
    // alert(username.length)
    if(! (username.length>=2) && (username.length<=16))
    {
        alert("昵称长度为2-16个字符！")
        document.getElementById("username").focus();
        return false
    }
    return true
}

// function check_id(){
//     var idcode= document.getElementById("IDNumber").value
//     // alert(idcode)
//     //检测身份证号码合法性---全部数字或数字+X/x 18位
//      // 加权因子
//      var weight_factor = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2];
//      // 校验码
//      var check_code = ['1', '0', 'X' , '9', '8', '7', '6', '5', '4', '3', '2'];
 
//      var code = idcode + "";
//      var last = idcode[17];//最后一位
 
//      var seventeen = code.substring(0,17);
 
//      // ISO 7064:1983.MOD 11-2
//      // 判断最后一位校验码是否正确
//      var arr = seventeen.split("");
//      var len = arr.length;
//      var num = 0;
//      for(var i = 0; i < len; i++){
//          num = num + arr[i] * weight_factor[i];
//      }
     
//      // 获取余数
//      var resisue = num%11;
//      var last_no = check_code[resisue];
 
//      // 格式的正则
//      // 正则思路
//      /*
//      第一位不可能是0
//      第二位到第六位可以是0-9
//      第七位到第十位是年份，所以七八位为19或者20
//      十一位和十二位是月份，这两位是01-12之间的数值
//      十三位和十四位是日期，是从01-31之间的数值
//      十五，十六，十七都是数字0-9
//      十八位可能是数字0-9，也可能是X
//      */
//      var idcard_patter = /^[1-9][0-9]{5}([1][9][0-9]{2}|[2][0][0|1][0-9])([0][1-9]|[1][0|1|2])([0][1-9]|[1|2][0-9]|[3][0|1])[0-9]{3}([0-9]|[X])$/;
 
//      // 判断格式是否正确
//      var format = idcard_patter.test(idcode);
//     //  alert(format)
//      // 返回验证结果，校验码和格式同时正确才算是合法的身份证号码
//     //  return last === last_no && format ? true : false;
//      if(!(format==true && (last_no===last))){
//          alert("身份证号码格式输入有误！")
//          document.getElementById("IDNumber").focus();
//      }
// }

function check_email(){
        /*     1.由大小写字母，数字，"_ - @" 组成；
        2.必须要有@，@两边都有内容，且两边的内容头尾均不为: " - _"
        3. " - _ ." 不允许连续使用
        4. 发现一般域名后缀 “.com”、".cn" 、".shop" ,新域名甚至会出现 “.cloud”、".fashion",至少2位 */

        //检测邮箱合法性
        var reg = new RegExp("^[a-zA-Z0-9]+([-_.][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([-_.][a-zA-Z0-9]+)*\.[a-z]{2,}$"); //正则表达式
        var obj = document.getElementById("email"); //要验证的对象
        if(obj.value === ""){ //输入不能为空
            // alert("邮箱不能为空!");
            return false;
        }else if(!reg.test(obj.value)){ //正则验证不通过，格式不对
            alert("您输入的邮箱格式不正确！");
            document.getElementById("email").focus();
            return false;
        }else{
            // alert("通过！");
            return true;
        }

}
function check_phone(){
    var phone = document.getElementById("phoneNumber").value
    if(phone.length!=11){
        alert("手机号码应为11位！")
        document.getElementById("phoneNumber").focus();
        return false;
    }
    var regu =  /^1[3456789]\d{9}$/
    if(!(regu.test(phone)) ){
        alert("手机号码格式有误！")
        document.getElementById("phoneNumber").focus();
        return false
    }
    return true
    //检测手机号码合法性 11位 全数字
}
//两次密码验证
function check_pass(){
    var first_pass=document.getElementById("password").value
    var second_pass=document.getElementById("confirmPassword").value
    var res = checkCN(first_pass)
    if(res== false){
        alert("密码不可以包含中文！")
        return false
    }
    //限制密码6-16位
    // alert(first_pass.length )
    if(!((first_pass.length>=6)&&first_pass.length<=18))
    {
        alert("密码长度应该为6-16位!")
        document.getElementById("password").focus();
        return false
    }
    var regex = new RegExp('(?=.*[0-9])(?=.*[a-zA-Z]).{6,18}');
    part_pass=first_pass.split(" ")
    if((!(regex.test(first_pass))) || part_pass.length!=1)
    {
        alert("密码为数字+英文字母 且不可以包含空格！")
        document.getElementById("password").focus();
        return false
    }
    return true
}
//第二步整体验证
function check_step2(){
    var userinfoform =document.getElementById('userinfoform')
    var password = document.getElementById('password')
    var confirmPassword = document.getElementById('confirmPassword')
    var name= document.getElementById("username").value
    // var id= document.getElementById("IDNumber").value
    var email= document.getElementById("email").value
    var phoneNumber= document.getElementById("phoneNumber").value
    if(name.length==0 || email.length==0 || phoneNumber.length==0 || password.length==0 || confirmPassword.length == 0)
    {
        alert("请把信息填写完整！")
        return false
    }
    else{
        flag1=check_name();
        flag2=check_pass();
        flag3=check_email();
        flag4=check_phone();
        if(flag1&&flag2&&flag3&&flag4){
            alert("注册成功！")
        }
        if(flag1&&flag2&&flag3&&flag4){
            userinfoform.submit()
            return true
        }
        else{
            alert("注册失败！")
            return false
        }
    }
}