-- MariaDB dump 10.19  Distrib 10.6.10-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: auth_register
-- ------------------------------------------------------
-- Server version	10.6.10-MariaDB-1:10.6.10+maria~ubu2004

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_key_server`
--

DROP TABLE IF EXISTS `admin_key_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_key_server` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `server_id` varchar(1000) DEFAULT NULL,
  `pub_key` varchar(1000) DEFAULT NULL,
  `priv_key` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_key_server`
--

LOCK TABLES `admin_key_server` WRITE;
/*!40000 ALTER TABLE `admin_key_server` DISABLE KEYS */;
INSERT INTO `admin_key_server` VALUES (1,'default','0x6c034ca62605648a47d09e01095a76af7f791087d713772b7b16ea3f19506f74fa0207dac0dbefeec3c6998095d1b6ff2fc971db91a79efc8b868347b70eea77','0xb40e2a72f5e3342c6f2174cbd6451e8d9e573606af9d901fc2ae597e4e62a6e3');
/*!40000 ALTER TABLE `admin_key_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directory_server3`
--

DROP TABLE IF EXISTS `directory_server3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `directory_server3` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `personal_ID` varchar(1000) DEFAULT NULL,
  `priv_key` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directory_server3`
--

LOCK TABLES `directory_server3` WRITE;
/*!40000 ALTER TABLE `directory_server3` DISABLE KEYS */;
INSERT INTO `directory_server3` VALUES (1,'$argon2i$v=19$m=32768,t=16,p=2$MTIzNDU2MTIzNDU2$/xQgkcHKNRtaa4Kh3JTA7T0U77fMNq3C4yJMJZmOwR4','BOqEkFnDJYZfgG4cbtd2F1eipMBSnxASYvsbHwFdvD2eAYUMUklUP5UUpBlOLYRm+uJycnVDtoWC3i73N3ZYxQlWwnxzt7Joyj6xpkQcQ/hZs5CMEn8zW5m754GimjH4KHdnwVt+Bb80UFvy05bKTnQXoCWOFQgLGcx1wFikGynyyVoWpcNfq29jaLFxwloifEeO7ae136O4q7JPFweZU85rIQ==');
/*!40000 ALTER TABLE `directory_server3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `server_name` varchar(1000) DEFAULT NULL,
  `server_ip` varchar(100) DEFAULT NULL,
  `server_port` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,'Loerrach','127.0.0.1','45677'),(2,'Freiburg','127.0.0.1','45678'),(3,'Hamburg','127.0.0.1','45679');
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voters`
--

DROP TABLE IF EXISTS `voters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `voters` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `PERSON_ID` varchar(100) NOT NULL,
  `HAS_VOTED` tinyint(1) DEFAULT NULL,
  `AUTH_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voters`
--

LOCK TABLES `voters` WRITE;
/*!40000 ALTER TABLE `voters` DISABLE KEYS */;
INSERT INTO `voters` VALUES (1,'T220101295',1,347540),(2,'E530904263',0,956856),(3,'U850101222',0,192493),(4,'V220403293',0,234843);
/*!40000 ALTER TABLE `voters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-14 21:50:24
