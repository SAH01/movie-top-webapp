# MovieTop11
电影网站项目使用Python爬虫技术，综合各大网站的电影信息进行数据分析，分列出同一部电影在不同电影网站的评分信息并且可以在同一个页面获取这部电影的可观看片源链接，同时可以显示片源的观看限制信息（免费，付费，独播等等）。


树懒电影系统
V1.0






使
用
手
册

 

目录

1	概述	2

1.1	系统简介	2

1.2	系统访问	2

1.2.1	环境要求	2

1.2.2	访问入口	3

2	网站功能详细操作	4

2.1	用户注册	4

2.2	用户登录以及忘记密码	5

2.3	分类筛选电影及搜索	7

2.4	查看电影详情以及电影收藏等	8

2.5	个人中心及切换头像	13

2.6退出登录	16

3	附：MySQL数据库设计	17

3.1	1905电影表（movie1905）	17

3.2	豆瓣电影表（moviebean）	17

3.3	IMDB（movieimdb）	18

3.4	爱奇艺电影（movieiqy）	19

3.5	搜狐电影表（moviesohu）	19

3.6	腾讯电影表（movieten）	20

3.7	用户信息表（userdata）	20

3.8	用户收藏表（userlike）	21


1	概述

1.1	系统简介

背景：
现如今人们的文娱生活越来越丰富，大多数人在闲暇的时候会选择观看一部电影。但是电影的水平参差不齐，人们的喜好各有不同。所以找电影，尤其是找一部好电影或是自己满意的电影就成了一件令人头疼的事情。而且同一部电影在各大网站的播放权限状况以及每部电影的评分等各有不同，迅速地掌握这些信息将对用户快速定位自己想要的影片提供极大的方便。

特点：
网站的集成了各大知名影视网站（豆瓣电影、腾讯视频、爱奇艺视频、搜狐视频、IMDB‘ 互联网电影资料库’Internet Movie Database、1905电影网）的影片信息，在同一个网站用户可以快速找到可以看的片源，同一部电影会给用户推荐可观看的所有片源，并显示这部电影在各个网站的评分信息。综合了这部电影在不同网站的观看权限，比如同一部电影在爱奇艺是收费的，但是可能在腾讯视频就是免费的，这有助于用户快速找到可观看的片源。同时我们把同一部电影在各个影视网站的评分等信息做了加权分析，给出一个综合评分，综合评分更加客观真实，更加有助于用户选择电影进行观看。
1.2	系统访问

1.2.1	环境要求

序号	版本	设备	硬件配置	支撑软件
1	V1.0	PC端	CPU：i5-9300H 2.40GHz
内存：8G
硬盘：500G	Windows 10
Google Chrome 版本 99.0.4844.74（正式版本）
表1：	环境配置要求

1.2.2	访问入口

在PC浏览器，输入网址：
http://127.0.0.1:5000/（目前网站未发布，只能本机运行。）

 ![image](https://user-images.githubusercontent.com/72775628/160059887-d5ae8f8f-9605-4d68-a01a-1258c7fef14c.png)

登陆页

 ![image](https://user-images.githubusercontent.com/72775628/160059902-2a9a9ee7-eb72-4aaf-9f82-267dc0b3d7f9.png)

网站首页

2	网站功能详细操作

2.1	用户注册

1.	进入网站首页点击注册按钮
 ![image](https://user-images.githubusercontent.com/72775628/160059912-abebe030-7201-44d2-99d3-4a87fcf6b1f9.png)

2.	2. 点击注册按钮后进入用户注册界面，阅读用户协议后，点击下一步；

 ![image](https://user-images.githubusercontent.com/72775628/160059921-e4c73628-5c00-4cb0-ae13-06dcd9a4d334.png)



3. 依次输入用户注册信息后点击完成按钮，即可无需登录直接进入网站首页。（网站会自动记住用户登录状态（15天），下次进入网站无须输入登录信息即可直接进入网站首页！）
 
![image](https://user-images.githubusercontent.com/72775628/160059933-e8df987d-86b9-411d-8a70-3943e44f9e32.png)
![image](https://user-images.githubusercontent.com/72775628/160059946-601b5760-59bc-42ce-b018-503b85558559.png)

 
2.2	用户登录以及忘记密码

输入用户名密码后点击登录按钮进入网站首页。
 ![image](https://user-images.githubusercontent.com/72775628/160059981-0d1e0d89-85cb-45bf-85d4-8282eec80354.png)


点击忘记密码可以修改密码。

 ![image](https://user-images.githubusercontent.com/72775628/160059999-99f59513-0cac-4b94-923d-fce9eb8d827e.png)
![image](https://user-images.githubusercontent.com/72775628/160060019-c811749d-077c-408a-8dba-0b5623e4fed6.png)

 
2.3	分类筛选电影及搜索

进入首页后，点击选择类型、年份、地区和排序顺序之后就会看到相关的电影排名展示情况。
![image](https://user-images.githubusercontent.com/72775628/160060029-67b5340a-053e-4a61-9455-fc91e5713fe0.png)

 

通过搜索框输入片名或者导演（支持模糊查找）可以搜索想要的电影。
![image](https://user-images.githubusercontent.com/72775628/160060036-4377a796-d789-4afe-8561-2f7fc8e18e46.png)

 
2.4	查看电影详情以及电影收藏等

1、查看电影详情
分类筛选或查找之后，点击想要查看详情的电影名称即可进入电影详情界面。

 ![image](https://user-images.githubusercontent.com/72775628/160060051-a74c7d95-632e-4b48-9a01-363108e97d53.png)

	  
 
2、观看电影

在右边的片源部分，点击片源名称后即可跳转链接观看电影。
![image](https://user-images.githubusercontent.com/72775628/160060060-87c5d444-36a6-4563-8af5-13b4a9b7c716.png)
![image](https://user-images.githubusercontent.com/72775628/160060069-c3bc57b8-86da-490a-a735-1c9a1a06723e.png)

 
 
3.收藏电影

收藏电影分为“想看”、“在看”和“看过”三类，点击对应按钮即可将电源收藏到对应分类中，可在个人中心查看。

 ![image](https://user-images.githubusercontent.com/72775628/160060081-feb77047-c38f-4a3d-97da-bc3f493f4114.png)


在个人中心查看已收藏的电影。

 ![image](https://user-images.githubusercontent.com/72775628/160060100-c876664f-2ec2-40af-9574-23d1a8b015f8.png)

 ![image](https://user-images.githubusercontent.com/72775628/160060111-e4d360b5-c169-46f3-9f3e-7eb2d141b1d2.png)
 ![image](https://user-images.githubusercontent.com/72775628/160060174-ead8b65b-1ba3-47a2-be17-e40fd41ea346.png)

 

 
2.5	个人中心及切换头像

1、进入个人中心
在网站首页，点击用户头像进入个人中心。
 
![image](https://user-images.githubusercontent.com/72775628/160060182-76061988-24de-480e-b375-8ad884608195.png)
![image](https://user-images.githubusercontent.com/72775628/160060188-df0661d1-7cb9-4a12-9ee1-50c2b4bea7b3.png)


 
2、查看以及修改个人收藏的电影

点击电影名称即可查看对应收藏的电影的详情。
 ![image](https://user-images.githubusercontent.com/72775628/160060196-ce0c4a61-fba4-4ec1-b1f4-704382ef7af1.png)


电影下方的移动按钮可以实现电影所属的“想看、在看、看过”类别转移。
![image](https://user-images.githubusercontent.com/72775628/160060203-635177c9-6ad0-4bce-86d7-e905786fd32e.png)

 
3、修改个人资料
点击修改资料，进入修改资料界面，输入想要修改的信息后点击提交完成资料修改操作。

 ![image](https://user-images.githubusercontent.com/72775628/160060210-01f39396-dd2a-4a73-ab5c-92b2c8ff8ed0.png)

4、修改头像
在个人中心界面，点击左上角的“选择文件”来选择头像，选择完成后，点击上传头像，完成头像修改。

 ![image](https://user-images.githubusercontent.com/72775628/160060217-7ef3f011-1744-464d-a3a4-4e24fc9397ac.png)

2.6退出登录 

在个人中心界面点击右上角的“退出”即可退出登录（退出后下次登录需要验证用户的登录信息！）
![image](https://user-images.githubusercontent.com/72775628/160060220-adebef2d-0147-4a4c-93ec-6c8e971c9c82.png)

 

勾选记住密码之后会再次记住登录状态（15天）
![image](https://user-images.githubusercontent.com/72775628/160060228-0a3732e9-a848-4c4c-b480-ecd217c3c0f0.png)

 


3	附：MySQL数据库设计

3.1	1905电影表（movie1905）

1 CREATE DATABASE /*!32312 IF NOT EXISTS*/`movierankings` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
 2 
 3 USE `movierankings`;
 4 
 5 /*Table structure for table `movie1905` */
 6 
 7 DROP TABLE IF EXISTS `movie1905`;
 8 
 9 CREATE TABLE `movie1905` (
10   `id` INT(11) NOT NULL AUTO_INCREMENT,
11   `name` VARCHAR(100) COLLATE utf8_bin NOT NULL,
12   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
13   `path` VARCHAR(100) COLLATE utf8_bin NOT NULL,
14   `state` VARCHAR(30) COLLATE utf8_bin NOT NULL,
15   PRIMARY KEY (`name`),
16   KEY `id` (`id`)
17 ) ENGINE=INNODB AUTO_INCREMENT=13530 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

3.2	豆瓣电影表（moviebean）

1 DROP TABLE IF EXISTS `moviebean`;
 2 
 3 CREATE TABLE `moviebean` (
 4   `id` INT(11) NOT NULL AUTO_INCREMENT,
 5   `title` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 6   `star` TEXT COLLATE utf8_bin NOT NULL,
 7   `director` TEXT COLLATE utf8_bin NOT NULL,
 8   `type_movie` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 9   `area` VARCHAR(45) COLLATE utf8_bin NOT NULL,
10   `date_time` VARCHAR(45) COLLATE utf8_bin NOT NULL,
11   `summary` TEXT COLLATE utf8_bin NOT NULL,
12   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
13   `language_movie` VARCHAR(45) COLLATE utf8_bin NOT NULL,
14   `img` TEXT COLLATE utf8_bin NOT NULL,
15   `scorenum` INT(11) NOT NULL,
16   `timelen` VARCHAR(45) COLLATE utf8_bin NOT NULL,
17   PRIMARY KEY (`id`,`title`,`scorenum`)
18 ) ENGINE=INNODB AUTO_INCREMENT=3157 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

3.3	IMDB（movieimdb）

1 DROP TABLE IF EXISTS `movieimdb`;
2 
3 CREATE TABLE `movieimdb` (
4   `id` INT(11) NOT NULL AUTO_INCREMENT,
5   `name` VARCHAR(100) COLLATE utf8_bin NOT NULL,
6   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
7   PRIMARY KEY (`name`),
8   KEY `id` (`id`)
9 ) ENGINE=INNODB AUTO_INCREMENT=12483 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

3.4	爱奇艺电影（movieiqy）

1 DROP TABLE IF EXISTS `movieiqy`;
 2 
 3 CREATE TABLE `movieiqy` (
 4   `id` INT(11) NOT NULL AUTO_INCREMENT,
 5   `name` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 6   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 7   `path` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 8   `state` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 9   PRIMARY KEY (`name`),
10   KEY `id` (`id`)
11 ) ENGINE=INNODB AUTO_INCREMENT=14350 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

3.5	 搜狐电影表（moviesohu）

1 DROP TABLE IF EXISTS `moviesohu`;
 2 
 3 CREATE TABLE `moviesohu` (
 4   `id` INT(11) NOT NULL AUTO_INCREMENT,
 5   `name` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 6   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 7   `path` VARCHAR(100) COLLATE utf8_bin NOT NULL,
 8   `state` VARCHAR(10) COLLATE utf8_bin NOT NULL,
 9   PRIMARY KEY (`name`),
10   KEY `id` (`id`)
11 ) ENGINE=INNODB AUTO_INCREMENT=3654 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


3.6	 腾讯电影表（movieten）

1 DROP TABLE IF EXISTS `movieten`;
 2 
 3 CREATE TABLE `movieten` (
 4   `id` INT(11) NOT NULL AUTO_INCREMENT,
 5   `name` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 6   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 7   `path` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 8   `state` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 9   PRIMARY KEY (`name`),
10   KEY `id` (`id`)
11 ) ENGINE=INNODB AUTO_INCREMENT=20037 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

3.7	用户信息表（userdata）

1 DROP TABLE IF EXISTS `userdata`;
2 
3 CREATE TABLE `userdata` (
4   `userphone` VARCHAR(20) COLLATE utf8_bin NOT NULL,
5   `userpass` VARCHAR(45) COLLATE utf8_bin NOT NULL,
6   `useremail` VARCHAR(100) COLLATE utf8_bin NOT NULL,
7   `username` VARCHAR(45) COLLATE utf8_bin NOT NULL,
8   PRIMARY KEY (`userphone`)
9 ) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

3.8	 用户收藏表（userlike）

1 DROP TABLE IF EXISTS `userlike`;
 2 
 3 CREATE TABLE `userlike` (
 4   `id` INT(11) NOT NULL AUTO_INCREMENT,
 5   `userphone` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 6   `usermovie` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 7   `usertype` VARCHAR(45) COLLATE utf8_bin NOT NULL,
 8   `scorenum` INT(11) NOT NULL,
 9   `url` TEXT COLLATE utf8_bin NOT NULL,
10   `score` VARCHAR(45) COLLATE utf8_bin NOT NULL,
11   PRIMARY KEY (`id`,`userphone`,`usermovie`,`usertype`,`scorenum`)
12 ) ENGINE=INNODB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

