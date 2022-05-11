/*
SQLyog Ultimate v10.00 Beta1
MySQL - 5.5.15 : Database - movierankings
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`movierankings` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `movierankings`;

/*Table structure for table `userdata` */

DROP TABLE IF EXISTS `userdata`;

CREATE TABLE `userdata` (
  `userphone` varchar(20) COLLATE utf8_bin NOT NULL,
  `userpass` varchar(45) COLLATE utf8_bin NOT NULL,
  `useremail` varchar(100) COLLATE utf8_bin NOT NULL,
  `username` varchar(45) COLLATE utf8_bin NOT NULL,
  `userimg` text COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`userphone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `userdata` */

insert  into `userdata`(`userphone`,`userpass`,`useremail`,`username`,`userimg`) values ('15284206891','a1234567','1770996260@qq.com','昵称_0','../static/userimg/203858e3f3be888c.jpg'),('15711111111','123456','','风吹过半夏','../static/userimg/7f63594fdac4246926b76285a4d22de2.jpg'),('15722222222','1234567','','测试1','../static/userimg/0000.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
