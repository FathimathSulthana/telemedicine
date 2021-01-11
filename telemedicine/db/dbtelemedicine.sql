/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.5.8-log : Database - dbtelemedicine
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbtelemedicine` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dbtelemedicine`;

/*Table structure for table `tblallocation` */

DROP TABLE IF EXISTS `tblallocation`;

CREATE TABLE `tblallocation` (
  `allocId` int(11) NOT NULL AUTO_INCREMENT,
  `reqId` int(11) NOT NULL,
  `dEmail` varchar(50) NOT NULL,
  PRIMARY KEY (`allocId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `tblallocation` */

insert  into `tblallocation`(`allocId`,`reqId`,`dEmail`) values (1,1,'susheep@gmail.com'),(2,3,'manjula@gmail.com'),(3,4,'manjula@gmail.com'),(4,2,'anirudh@gmail.com'),(5,5,'sangeeth@gmail.com'),(6,6,'sangeeth@gmail.com'),(7,7,'sangeeth@gmail.com'),(8,8,'susheep@gmail.com');

/*Table structure for table `tblconsultationfee` */

DROP TABLE IF EXISTS `tblconsultationfee`;

CREATE TABLE `tblconsultationfee` (
  `feeId` int(11) NOT NULL AUTO_INCREMENT,
  `prescId` int(11) NOT NULL,
  `fees` int(11) NOT NULL,
  PRIMARY KEY (`feeId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tblconsultationfee` */

insert  into `tblconsultationfee`(`feeId`,`prescId`,`fees`) values (1,1,1200),(3,3,500),(4,4,500),(5,5,300),(6,6,400),(7,9,300);

/*Table structure for table `tblcourier` */

DROP TABLE IF EXISTS `tblcourier`;

CREATE TABLE `tblcourier` (
  `cId` int(20) NOT NULL AUTO_INCREMENT,
  `cName` varchar(50) NOT NULL,
  `cAddress` varchar(100) NOT NULL,
  `cContact` varchar(10) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `cDistrict` varchar(50) NOT NULL,
  `cLicence` varchar(50) NOT NULL,
  PRIMARY KEY (`cEmail`,`cId`),
  KEY `cId` (`cId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tblcourier` */

insert  into `tblcourier`(`cId`,`cName`,`cAddress`,`cContact`,`cEmail`,`cDistrict`,`cLicence`) values (2,'DTDC Angamalyy','Angamaly','9874561230','dtdcangamaly1@gmail.com','Eranakulam',''),(5,'Fastcourier','Ernakulam Aluva','8756778767','fastcourier@gmail.com','Eranakulam','768798'),(1,'Fasttrack','Kaloor Ernakulam','9876567656','fasttrack@gmail.com','Eranakulam',''),(4,'sfhugi','ehfiu','9867857584','uhfiuoew@gmail.com','Pathanamthitta','7537849'),(3,'Zoom','Ernakulam Aluva','9876859847','zoom@gmail.com','Eranakulam','');

/*Table structure for table `tblcourierorder` */

DROP TABLE IF EXISTS `tblcourierorder`;

CREATE TABLE `tblcourierorder` (
  `oId` int(11) NOT NULL AUTO_INCREMENT,
  `cEmail` varchar(50) NOT NULL,
  `prescId` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tblcourierorder` */

insert  into `tblcourierorder`(`oId`,`cEmail`,`prescId`,`status`) values (2,'dtdcangamaly1@gmail.com',4,'delivered'),(3,'zoom@gmail.com',5,'delivered'),(4,'zoom@gmail.com',6,'delivered'),(5,'zoom@gmail.com',9,'ordered');

/*Table structure for table `tbldepartment` */

DROP TABLE IF EXISTS `tbldepartment`;

CREATE TABLE `tbldepartment` (
  `deptId` int(11) NOT NULL AUTO_INCREMENT,
  `deptName` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`deptId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tbldepartment` */

insert  into `tbldepartment`(`deptId`,`deptName`,`status`) values (1,'Oncology','1'),(2,'Dentist','1'),(3,'Cardiology','1');

/*Table structure for table `tbldoctor` */

DROP TABLE IF EXISTS `tbldoctor`;

CREATE TABLE `tbldoctor` (
  `dId` int(11) NOT NULL AUTO_INCREMENT,
  `dName` varchar(50) NOT NULL,
  `dAddress` varchar(100) NOT NULL,
  `dContact` varchar(50) NOT NULL,
  `dEmail` varchar(50) NOT NULL,
  `depId` int(11) NOT NULL,
  `dImg` varchar(100) NOT NULL,
  `dQualification` varchar(50) NOT NULL,
  `dExperience` int(11) NOT NULL,
  `dDistrict` varchar(50) NOT NULL,
  `dlic` varchar(50) NOT NULL,
  PRIMARY KEY (`dEmail`,`dId`),
  KEY `dId` (`dId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `tbldoctor` */

insert  into `tbldoctor`(`dId`,`dName`,`dAddress`,`dContact`,`dEmail`,`depId`,`dImg`,`dQualification`,`dExperience`,`dDistrict`,`dlic`) values (8,'Aneesh','Ernakulam,Kaloor','9867678767','aneesh@gmail.com',2,'/media/t3_mzAm6WS.jpg','BDS',9,'Eranakulam','7685756'),(2,'Anirudh','Kottayam Kaduthuruthy','9789678894','anirudh@gmail.com',2,'/media/ab.jpg','BDS',9,'Kottayam',''),(4,'xxbfbgdf','hbdhdhd','9878567687','fgedf@gmail.com',1,'/media/g2.jpg','BDS',9,'Alappuzha',''),(5,'gegte','egrg','8978678567','fghrtfhr@gmail.com',2,'/media/banner4.jpg','jhkiy',9,'Kozhikode','567567'),(6,'Manjula','Aluva','9568741230','manjula@gmail.com',1,'/media/t2.jpg','MBBS FRCS MD',7,'Eranakulam','545'),(3,'dferfhty','dfghrtgreghh','8768567474','rewtwtg@fgfgsdg.com',2,'/media/c2.jpg','fdgjnero',21,'Kozhikode',''),(7,'Sangeeth','Ernakulam Aluva','9878678756','sangeeth@gmail.com',3,'/media/t3_TXlGo3J.jpg','MBBS MD',7,'Eranakulam','756775'),(1,'DrSudheep','Elamakkara','9876567656','susheep@gmail.com',1,'/media/t3.jpg','MBBS MD',7,'Eranakulam','');

/*Table structure for table `tblfeedback` */

DROP TABLE IF EXISTS `tblfeedback`;

CREATE TABLE `tblfeedback` (
  `fId` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `feeback` varchar(500) NOT NULL,
  `fDate` datetime NOT NULL,
  PRIMARY KEY (`fId`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tblfeedback` */

insert  into `tblfeedback`(`fId`,`pEmail`,`feeback`,`fDate`) values (1,'sindhu@gmail.com','good','2020-12-30 16:23:50'),(2,'shilpa@gmail.com','Good','2020-12-31 16:34:43');

/*Table structure for table `tbllogin` */

DROP TABLE IF EXISTS `tbllogin`;

CREATE TABLE `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `tbllogin` */

insert  into `tbllogin`(`username`,`password`,`utype`,`status`,`id`) values ('admin@gmail.com','admin123','admin','1',1),('susheep@gmail.com','sudheep123','doctor','1',2),('diya@gmail.com','diya123','pharmacy','1',3),('fasttrack@gmail.com','fasttrack','courier','1',4),('sindhu@gmail.com','sindhu123','patient','1',5),('anirudh@gmail.com','anirudh123','doctor','1',6),('manjula@gmail.com','manjula','doctor','1',10),('jeevanam@gmail.com','jeevanam','pharmacy','1',11),('dtdcangamaly1@gmail.com','dtdcangamaly','courier','1',12),('shilpa@gmail.com','shilpa','patient','1',13),('sangeeth@gmail.com','sangeeth123','doctor','1',14),('medon@gmail.com','medon123','pharmacy','1',15),('zoom@gmail.com','zoom123','courier','1',16),('ameen@gmail.com','ameen123','patient','1',17),('uhfiuoew@gmail.com','fiehiruerfh','courier','1',18),('sarath@gmail.com','sarath123','patient','1',22),('ghanshyam@gmail.com','ghanshyam123','patient','1',23);

/*Table structure for table `tblmedicine` */

DROP TABLE IF EXISTS `tblmedicine`;

CREATE TABLE `tblmedicine` (
  `medId` int(11) NOT NULL AUTO_INCREMENT,
  `medName` varchar(50) NOT NULL,
  `medDesc` varchar(100) NOT NULL,
  `medContent` varchar(100) NOT NULL,
  `medCompany` varchar(50) NOT NULL,
  `medRate` varchar(50) NOT NULL,
  `medStatus` int(11) NOT NULL,
  PRIMARY KEY (`medId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tblmedicine` */

insert  into `tblmedicine`(`medId`,`medName`,`medDesc`,`medContent`,`medCompany`,`medRate`,`medStatus`) values (1,'Diclovine','Body pain','Diclovine tablets','Paracetamole','300',1),(2,'Gelucine','Gas trouble','One pack of tablet','Star mount','450',1),(3,'Dolo','Paracetamol','Paracetamol','Cipla','2',1);

/*Table structure for table `tblmedicineorder` */

DROP TABLE IF EXISTS `tblmedicineorder`;

CREATE TABLE `tblmedicineorder` (
  `moId` int(11) NOT NULL AUTO_INCREMENT,
  `phEmail` varchar(50) NOT NULL,
  `prescId` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`moId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tblmedicineorder` */

insert  into `tblmedicineorder`(`moId`,`phEmail`,`prescId`,`status`) values (1,'6787654567',1,'ordered'),(3,'jeevanam@gmail.com',3,'passed to courier'),(4,'jeevanam@gmail.com',4,'delivered'),(5,'medon@gmail.com',5,'delivered'),(6,'medon@gmail.com',6,'delivered'),(7,'medon@gmail.com',9,'passed to courier');

/*Table structure for table `tblmedicinestock` */

DROP TABLE IF EXISTS `tblmedicinestock`;

CREATE TABLE `tblmedicinestock` (
  `stockId` int(11) NOT NULL AUTO_INCREMENT,
  `phEmail` varchar(50) NOT NULL,
  `medId` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`stockId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `tblmedicinestock` */

insert  into `tblmedicinestock`(`stockId`,`phEmail`,`medId`,`stock`) values (1,'diya@gmail.com',2,45),(2,'diya@gmail.com',1,46),(3,'jeevanam@gmail.com',1,25),(4,'jeevanam@gmail.com',2,25),(5,'jeevanam@gmail.com',3,50),(6,'medon@gmail.com',3,70),(7,'medon@gmail.com',1,52),(8,'medon@gmail.com',2,90);

/*Table structure for table `tblpatient` */

DROP TABLE IF EXISTS `tblpatient`;

CREATE TABLE `tblpatient` (
  `pId` int(11) NOT NULL AUTO_INCREMENT,
  `pName` varchar(50) NOT NULL,
  `pAddress` varchar(100) NOT NULL,
  `pPincode` varchar(6) NOT NULL,
  `pContact` varchar(10) NOT NULL,
  `pEmail` varchar(50) NOT NULL,
  `allergy` varchar(100) NOT NULL,
  `heriditary` varchar(100) NOT NULL,
  `surgery` varchar(100) NOT NULL,
  `admit` varchar(100) NOT NULL,
  `history` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `validid` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  PRIMARY KEY (`pEmail`,`pId`),
  KEY `pId` (`pId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tblpatient` */

insert  into `tblpatient`(`pId`,`pName`,`pAddress`,`pPincode`,`pContact`,`pEmail`,`allergy`,`heriditary`,`surgery`,`admit`,`history`,`dob`,`validid`,`gender`) values (3,'Ameen','Ernakulam Palarivattom','678987','8769475847','ameen@gmail.com','yes','no','no','no','no','08-13-1995','8758738',''),(5,'Ghanshyam','Ernakulam','678906','9769589585','ghanshyam@gmail.com','yes','no','no','no','no','1996-06-13','567678658','male'),(4,'Sarath','Ernakulam Kakkanad','678906','7689876756','sarath@gmail.com','yes','no','no','no','no','08-13-1995','8758738',''),(2,'Shilpa','Palarivattam','683548','9854710263','shilpa@gmail.com','shilpa@gmail.com','No','No','No','No','24-11-1997','kjn54',''),(1,'Sindhu','Palarivattom','678679','9878987654','sindhu@gmail.com','sindhu@gmail.com','sindhu@gmail.com','no','yes','no','','','');

/*Table structure for table `tblpayment` */

DROP TABLE IF EXISTS `tblpayment`;

CREATE TABLE `tblpayment` (
  `payid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `amount` varchar(40) DEFAULT NULL,
  `cardno` varchar(40) DEFAULT NULL,
  `month` varchar(40) DEFAULT NULL,
  `year` varchar(40) DEFAULT NULL,
  `cvv` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`payid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tblpayment` */

insert  into `tblpayment`(`payid`,`username`,`amount`,`cardno`,`month`,`year`,`cvv`) values (1,'sindhu@gmail.com','1000','567867987979','09','18','567'),(2,'shilpa@gmail.com','1000','985471263025','01','17','123'),(3,'ameen@gmail.com','1000','378657485972','06','18','356'),(4,'sarath@gmail.com','1000','546767979768','09','18','534'),(5,'ghanshyam@gmail.com','1000','498738472987','03','18','857');

/*Table structure for table `tblpharmacy` */

DROP TABLE IF EXISTS `tblpharmacy`;

CREATE TABLE `tblpharmacy` (
  `phId` int(11) NOT NULL AUTO_INCREMENT,
  `phName` varchar(50) NOT NULL,
  `phAddress` varchar(100) NOT NULL,
  `phContact` varchar(10) NOT NULL,
  `phEmail` varchar(50) NOT NULL,
  `phLicense` varchar(50) NOT NULL,
  `phDistrict` varchar(50) NOT NULL,
  PRIMARY KEY (`phEmail`,`phId`),
  KEY `phId` (`phId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tblpharmacy` */

insert  into `tblpharmacy`(`phId`,`phName`,`phAddress`,`phContact`,`phEmail`,`phLicense`,`phDistrict`) values (1,'Diya','Marine Drive','6787654567','diya@gmail.com','5467875','Eranakulam'),(4,'Imed','Ernakulam','8978675678','imed@gmail.com','678899','Eranakulam'),(2,'Jeevanam','Aluva','9632587410','jeevanam@gmail.com','hj57','Eranakulam'),(3,'Medon','kaloor Ernakulam','8795686758','medon@gmail.com','485965','Eranakulam');

/*Table structure for table `tblprescmedicine` */

DROP TABLE IF EXISTS `tblprescmedicine`;

CREATE TABLE `tblprescmedicine` (
  `prescmedId` int(11) NOT NULL AUTO_INCREMENT,
  `presId` int(11) NOT NULL,
  `medId` int(11) NOT NULL,
  `course` varchar(50) NOT NULL,
  `days` varchar(50) NOT NULL,
  `total` int(11) NOT NULL,
  PRIMARY KEY (`prescmedId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `tblprescmedicine` */

insert  into `tblprescmedicine`(`prescmedId`,`presId`,`medId`,`course`,`days`,`total`) values (1,1,1,'3-6','12',3600),(2,2,1,'twice daily','10',3000),(3,2,3,'twice daily','10',20),(4,3,1,'twice daily','10',3000),(5,3,3,'twice daily','15',30),(6,4,1,'twice daily','25',7500),(7,5,3,'3-6','5',10),(8,6,1,'3-6','10',3000),(9,6,2,'2-3','10',4500),(10,9,3,'3-6','10',20);

/*Table structure for table `tblprescription` */

DROP TABLE IF EXISTS `tblprescription`;

CREATE TABLE `tblprescription` (
  `presId` int(11) NOT NULL AUTO_INCREMENT,
  `allocId` int(11) NOT NULL,
  `diagnosis` varchar(100) NOT NULL,
  `prescription` varchar(100) NOT NULL,
  PRIMARY KEY (`presId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `tblprescription` */

insert  into `tblprescription`(`presId`,`allocId`,`diagnosis`,`prescription`) values (1,1,'dfsdfg','sgfsr'),(3,2,'jiniuhbn','ukhbubyu'),(4,3,'iojuinhji','iunhjini'),(5,5,'gedge','tryrty'),(6,6,'hgfhfgh','trhrtgh'),(7,7,'rfgehe','sdrte'),(8,8,'iouyiktyj','fgjtur'),(9,8,'iouyiktyj','fgjtur');

/*Table structure for table `tblrequest` */

DROP TABLE IF EXISTS `tblrequest`;

CREATE TABLE `tblrequest` (
  `reqId` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `depId` int(11) NOT NULL,
  `disease` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `district` varchar(50) NOT NULL,
  `reqDate` date NOT NULL,
  `reqStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`reqId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `tblrequest` */

insert  into `tblrequest`(`reqId`,`pEmail`,`depId`,`disease`,`description`,`district`,`reqDate`,`reqStatus`) values (1,'sindhu@gmail.com',1,'rfgerg','regtegy','Eranakulam','2020-12-23','doctor allocated'),(2,'sindhu@gmail.com',2,'rfgerg','edwfrwefg','Kottayam','2020-12-30','doctor allocated'),(3,'shilpa@gmail.com',1,'jhbjub','kjnjh','Eranakulam','2020-12-31','doctor allocated'),(4,'shilpa@gmail.com',1,'difun','inhujhbhj','Eranakulam','2020-12-31','doctor allocated'),(5,'ameen@gmail.com',3,'hrhhrtyh','tyretyrety','Eranakulam','2021-01-02','doctor allocated'),(6,'ghanshyam@gmail.com',3,'fgreger','rgertg','Eranakulam','2021-01-02','doctor allocated'),(7,'ghanshyam@gmail.com',3,'hrhhrtyh','gfjhfyg','Eranakulam','2021-01-02','doctor allocated'),(8,'ghanshyam@gmail.com',1,'fgreger','iuohiohgo','Eranakulam','2021-01-02','doctor allocated');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
