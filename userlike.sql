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

/*Table structure for table `userlike` */

DROP TABLE IF EXISTS `userlike`;

CREATE TABLE `userlike` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userphone` varchar(45) COLLATE utf8_bin NOT NULL,
  `usermovie` varchar(45) COLLATE utf8_bin NOT NULL,
  `usertype` varchar(45) COLLATE utf8_bin NOT NULL,
  `scorenum` int(11) NOT NULL,
  `url` text COLLATE utf8_bin NOT NULL,
  `score` varchar(45) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`,`userphone`,`usermovie`,`usertype`,`scorenum`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `userlike` */

insert  into `userlike`(`id`,`userphone`,`usermovie`,`usertype`,`scorenum`,`url`,`score`) values (7,'15722222222','肖申克的救赎','想看',2349647,'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg','9.7'),(10,'15722222222','千与千寻','看过',1846885,'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.jpg','9.4'),(15,'15711111111','这个杀手不太冷','想看',1944418,'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p511118051.jpg','9.4'),(17,'15711111111','千与千寻','想看',1846885,'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.jpg','9.4'),(18,'15711111111','泰坦尼克号','在看',1731020,'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p457760035.jpg','9.4'),(22,'15711111111','阿甘正传','看过',1769622,'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2372307693.jpg','9.5'),(23,'15711111111','盗梦空间','看过',1708967,'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2616355133.jpg','9.3'),(24,'15711111111','疯狂动物城','看过',1526125,'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614500649.jpg','9.2'),(25,'15711111111','西虹市首富','在看',874934,'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529206747.jpg','6.6'),(27,'15711111111','哪吒之魔童降世','看过',1607534,'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2563780504.jpg','8.4'),(30,'15711111111','肖申克的救赎','看过',2349647,'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg','9.7'),(31,'15722222222','我不是药神','看过',1717723,'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2561305376.jpg','9.0'),(33,'15722222222','哪吒之魔童降世','在看',1607534,'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2563780504.jpg','8.4'),(34,'15284206891','千与千寻','看过',1846885,'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2557573348.jpg','9.4'),(35,'15284206891','星际穿越','想看',1381783,'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2614988097.jpg','9.3'),(36,'15284206891','阿凡达','在看',1154798,'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2634997853.jpg','8.8');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
