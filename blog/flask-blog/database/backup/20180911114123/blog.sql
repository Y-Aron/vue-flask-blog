-- MySQL dump 10.13  Distrib 5.6.39, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: blog
-- ------------------------------------------------------
-- Server version	5.6.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_auth_rule`
--

DROP TABLE IF EXISTS `tb_auth_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_auth_rule` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '节点ID',
  `root_id` int(11) DEFAULT '0' COMMENT '根节点',
  `pid` int(11) DEFAULT '0' COMMENT '父节点ID',
  `type` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-项目;2-模块;3-操作',
  `name` varchar(80) DEFAULT NULL COMMENT '节点名称',
  `method` varchar(30) DEFAULT NULL,
  `route` varchar(200) NOT NULL COMMENT '节点路由',
  `status` tinyint(4) DEFAULT '1' COMMENT '1-正常;0-禁用',
  `sorts` int(11) DEFAULT '1' COMMENT '列表升序显示',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_auth_rule`
--

LOCK TABLES `tb_auth_rule` WRITE;
/*!40000 ALTER TABLE `tb_auth_rule` DISABLE KEYS */;
INSERT INTO `tb_auth_rule` VALUES (1,0,0,1,'后台首页','GET','/api/admin',1,1000,1536605600,1536607095),(2,0,0,1,'文章管理','MENU','/api/arcitle/manage',1,1100,1536606174,1536607001),(3,2,2,2,'文章分类','GET','/api/arctype/index',1,1,1536606254,1536607030),(4,2,3,3,'新增分类','POST','/api/arctype',1,1,1536606317,1536607044),(5,2,3,3,'编辑分类','PUT','/api/arctype',1,2,1536606341,1536607054),(6,2,3,3,'删除分类','DELETE','/api/arctype/index',1,3,1536606366,1536607551),(7,2,2,2,'文章列表','GET','/api/archive/index',1,2,1536606515,1536607462),(8,2,7,3,'新增文章','POST','/api/archive',1,1,1536606537,1536607564),(9,2,7,3,'编辑文章','PUT','/api/archive',1,2,1536606567,1536607575),(10,2,7,3,'删除文章','DELETE','/api/archive/index',1,3,1536606590,1536607583),(11,2,2,2,'文章模型管理','GET','/api/arctype/model/index',1,3,1536606636,1536607531),(12,2,11,3,'删除模型','DELETE','/api/arctype/model/index',1,3,1536606668,1536606811),(13,2,11,3,'新增模型','POST','/api/arctype/model',1,1,1536606769,1536607593),(14,2,11,3,'编辑模型','PUT','/api/arctype/model',1,2,1536606795,1536607602),(15,0,0,1,'用户管理','MENU','/api/user/manage',1,1200,1536607645,1536635321),(16,15,15,2,'用户列表','GET','/api/user/index',1,1,1536607720,1536607720),(17,15,15,2,'角色管理','GET','/api/user/group/index',1,2,1536607792,1536607792),(18,15,15,2,'角色节点列表','GET','/api/user/group/rule/index',1,3,1536607844,1536607844),(19,15,16,3,'新增用户','POST','/api/user',1,1,1536607890,1536607890),(20,15,16,3,'编辑用户','PUT','/api/user',1,2,1536607922,1536607922),(21,15,16,3,'删除用户','DELETE','/api/user/index',1,3,1536607952,1536607952),(22,15,16,3,'授权角色','POST','/api/user/auth',1,4,1536608111,1536608111),(23,15,17,3,'新增角色','POST','/api/user/group',1,1,1536634120,1536634120),(24,15,17,3,'编辑角色','PUT','/api/user/group',1,2,1536634141,1536634141),(25,15,17,3,'删除角色','DELETE','/api/user/group/index',1,3,1536634169,1536634169),(26,15,18,3,'新增节点','POST','/api/user/group/rule',1,1,1536634222,1536634222),(27,15,18,3,'编辑节点','PUT','/api/user/group/rule',1,2,1536634248,1536634248),(29,15,18,3,'删除节点','DELETE','/api/user/group/rule/index',1,3,1536634828,1536634828),(30,0,0,1,'消息管理','MENU','/api/comment',1,1300,1536634899,1536634899),(31,30,30,2,'留言列表','GET','/api/comment/guestBook/index',1,1,1536634954,1536634954),(32,30,30,2,'文章评论列表','GET','/api/comment/archive/index',1,2,1536634983,1536634983),(33,30,31,3,'编辑留言','POST','/api/comment',1,1,1536635062,1536635062),(34,30,31,3,'删除留言','DELETE','/api/comment/guestBook/index',1,2,1536635093,1536635093),(35,30,32,3,'编辑评论','POST','/api/comment',1,1,1536635121,1536635121),(36,30,32,3,'删除评论','DELETE','/api/comment/archive/index',1,2,1536635150,1536635150),(37,0,0,1,'系统管理','MENU','/api/config/manage',1,1400,1536635217,1536635298),(38,0,0,1,'站长工具','MENU','/api/port/manage',1,1500,1536635274,1536635536),(39,0,0,1,'数据库管理','MENU','/api/database/manage',1,1600,1536635360,1536635360),(40,37,37,2,'系统配置字段','GET','/api/config/index',1,1,1536635414,1536635414),(41,37,40,3,'新增字段','POST','/api/config',1,1,1536635448,1536635498),(42,37,40,3,'编辑字段','PUT','/api/config',1,2,1536635461,1536635507),(43,37,40,3,'删除字段','DELETE','/api/config/index',1,3,1536635477,1536635528),(44,38,38,2,'登录日志','GET','/api/login_log/index',1,1,1536635710,1536635710),(45,38,44,3,'删除日志','DELETE','/api/login_log/index',1,1,1536635747,1536635747),(46,39,39,2,'数据库列表','GET','/api/database/index',1,1,1536635787,1536635870),(47,39,39,2,'还原数据库','GET','/api/database/backup',1,2,1536635808,1536636032),(48,39,46,3,'备份数据库','POST','/api/database/backup',1,1,1536636016,1536636016),(49,39,47,3,'还原','PUT','/api/database/backup/recovery',1,1,1536636181,1536636181),(50,39,47,3,'下载','GET','/api/database/backup/download',1,2,1536636228,1536636228),(51,39,47,3,'删除','DELETE','/api/database/backup',1,3,1536636267,1536636267);
/*!40000 ALTER TABLE `tb_auth_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_auth_group_rule`
--

DROP TABLE IF EXISTS `tb_auth_group_rule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_auth_group_rule` (
  `rule_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`rule_id`,`group_id`),
  KEY `FK_group_id` (`group_id`),
  CONSTRAINT `FK_group_id` FOREIGN KEY (`group_id`) REFERENCES `tb_auth_group` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_rule_id` FOREIGN KEY (`rule_id`) REFERENCES `tb_auth_rule` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_auth_group_rule`
--

LOCK TABLES `tb_auth_group_rule` WRITE;
/*!40000 ALTER TABLE `tb_auth_group_rule` DISABLE KEYS */;
INSERT INTO `tb_auth_group_rule` VALUES (1,1,1536637148,1536637148),(2,1,1536637148,1536637148),(3,1,1536637148,1536637148),(4,1,1536637148,1536637148),(5,1,1536637148,1536637148),(6,1,1536637148,1536637148),(7,1,1536637148,1536637148),(8,1,1536637148,1536637148),(9,1,1536637148,1536637148),(10,1,1536637148,1536637148),(11,1,1536637148,1536637148),(12,1,1536637148,1536637148),(13,1,1536637148,1536637148),(14,1,1536637148,1536637148),(15,1,1536637148,1536637148),(16,1,1536637148,1536637148),(17,1,1536637148,1536637148),(18,1,1536637148,1536637148),(19,1,1536637148,1536637148),(20,1,1536637148,1536637148),(22,1,1536637148,1536637148),(23,1,1536637148,1536637148),(24,1,1536637148,1536637148),(26,1,1536637148,1536637148),(27,1,1536637148,1536637148),(30,1,1536637148,1536637148),(31,1,1536637148,1536637148),(32,1,1536637148,1536637148),(33,1,1536637148,1536637148),(34,1,1536637148,1536637148),(35,1,1536637148,1536637148),(36,1,1536637148,1536637148),(37,1,1536637148,1536637148),(38,1,1536637148,1536637148),(39,1,1536637148,1536637148),(40,1,1536637148,1536637148),(41,1,1536637148,1536637148),(42,1,1536637148,1536637148),(43,1,1536637148,1536637148),(44,1,1536637148,1536637148),(45,1,1536637148,1536637148),(46,1,1536637148,1536637148),(47,1,1536637148,1536637148),(48,1,1536637148,1536637148),(49,1,1536637148,1536637148),(50,1,1536637148,1536637148),(51,1,1536637148,1536637148);
/*!40000 ALTER TABLE `tb_auth_group_rule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_login_log`
--

DROP TABLE IF EXISTS `tb_login_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_login_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `ip` varchar(100) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `province` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '1',
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_loginLog_user_r` (`uid`),
  CONSTRAINT `FK_loginLog_user_r` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_login_log`
--

LOCK TABLES `tb_login_log` WRITE;
/*!40000 ALTER TABLE `tb_login_log` DISABLE KEYS */;
INSERT INTO `tb_login_log` VALUES (2,1,'127.0.0.1','中国','','','',1,1536605008,1536605008),(3,1,'127.0.0.1','中国','','','',1,1536605047,1536605047),(4,1,'127.0.0.1','中国','','','',1,1536606932,1536606932),(5,1,'127.0.0.1','中国','','','',1,1536634041,1536634041),(6,1,'127.0.0.1','中国','','','',1,1536634064,1536634064),(7,1,'127.0.0.1','中国','','','',1,1536635884,1536635884);
/*!40000 ALTER TABLE `tb_login_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_config`
--

DROP TABLE IF EXISTS `tb_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_config` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `key` varchar(30) NOT NULL,
  `value` varchar(200) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `type` enum('web','sys') DEFAULT 'sys',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_config`
--

LOCK TABLES `tb_config` WRITE;
/*!40000 ALTER TABLE `tb_config` DISABLE KEYS */;
INSERT INTO `tb_config` VALUES (1,'web_author','Y-先生','前端作者显示~','web'),(2,'git_fork_url','https://gitee.com/suxiaoxin/Tp5-TuFanInc-Admin/members','github_fork链接','web'),(3,'web_title','天行健，君子以自强不息！地势坤，君子以厚德载物！','网站页面警句','web'),(4,'web_footer','Copyright © 2017-2018 Y-先生','网站页脚','web'),(5,'web_talk','杨文杰个人博客，是一个记录自己生活点滴、互联网技术的原创独立博客。','','web');
/*!40000 ALTER TABLE `tb_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user_info`
--

DROP TABLE IF EXISTS `tb_user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user_info` (
  `id` int(11) NOT NULL,
  `avatar` varchar(200) DEFAULT '',
  `sex` tinyint(4) DEFAULT '0',
  `qq` varchar(100) DEFAULT NULL,
  `birthday` varchar(100) DEFAULT NULL,
  `info` text,
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_user_userInfo_r` FOREIGN KEY (`id`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user_info`
--

LOCK TABLES `tb_user_info` WRITE;
/*!40000 ALTER TABLE `tb_user_info` DISABLE KEYS */;
INSERT INTO `tb_user_info` VALUES (1,'64c802693adb72e8f2147b780d93e7459ccd60a6.jpg',0,'1249205951','1997-02-17','> 这个人特别懒 \n\n****\n### 佛性更新\n',NULL,NULL);
/*!40000 ALTER TABLE `tb_user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_auth_user_group`
--

DROP TABLE IF EXISTS `tb_auth_user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_auth_user_group` (
  `uid` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`uid`,`group_id`),
  KEY `FK_group_userGroup_r` (`group_id`),
  CONSTRAINT `FK_group_userGroup_r` FOREIGN KEY (`group_id`) REFERENCES `tb_auth_group` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_user_userGroup_r` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_auth_user_group`
--

LOCK TABLES `tb_auth_user_group` WRITE;
/*!40000 ALTER TABLE `tb_auth_user_group` DISABLE KEYS */;
INSERT INTO `tb_auth_user_group` VALUES (1,1,1536637222,1536637222);
/*!40000 ALTER TABLE `tb_auth_user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(32) NOT NULL,
  `nickname` varchar(100) DEFAULT '',
  `email` varchar(100) DEFAULT '',
  `mobile` varchar(50) DEFAULT '',
  `logins` int(11) DEFAULT '0',
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  `register_ip` varchar(100) DEFAULT '',
  `last_time` int(11) DEFAULT NULL,
  `last_ip` varchar(100) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `AK_unique_key` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES (1,'admin','21232f297a57a5a743894a0e4a801fc3','Y-先生','1249205951@qq.com','15280553351',7,NULL,NULL,'',NULL,NULL,1);
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_auth_group`
--

DROP TABLE IF EXISTS `tb_auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module` varchar(200) NOT NULL DEFAULT '' COMMENT '所属模块名',
  `name` varchar(200) NOT NULL,
  `level` int(11) DEFAULT '0' COMMENT '0-系统浏览；1024-超级管理员',
  `status` tinyint(4) DEFAULT '1' COMMENT '1-正常;0-禁用',
  `description` varchar(100) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_auth_group`
--

LOCK TABLES `tb_auth_group` WRITE;
/*!40000 ALTER TABLE `tb_auth_group` DISABLE KEYS */;
INSERT INTO `tb_auth_group` VALUES (1,'管理员','超级管理员',9999,1,'权限大佬！！',1536637148,1536637148);
/*!40000 ALTER TABLE `tb_auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_comment`
--

DROP TABLE IF EXISTS `tb_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_comment` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `isAdmin` tinyint(4) DEFAULT '0',
  `pid` int(11) DEFAULT '0',
  `type` int(11) DEFAULT NULL COMMENT 'NULL——留言板评论 \r\n            其他——文章id',
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '-1',
  PRIMARY KEY (`id`),
  KEY `FK_comment_archive_r` (`type`),
  KEY `FK_comment_user_r` (`username`),
  CONSTRAINT `FK_comment_archive_r` FOREIGN KEY (`type`) REFERENCES `tb_archive` (`id`) ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_comment`
--

LOCK TABLES `tb_comment` WRITE;
/*!40000 ALTER TABLE `tb_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_arctype_mod`
--

DROP TABLE IF EXISTS `tb_arctype_mod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_arctype_mod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `operation` varchar(100) NOT NULL,
  `sorts` int(11) DEFAULT '50',
  `status` tinyint(4) DEFAULT '1' COMMENT '1-正常;0-禁用',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_unique_key` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_arctype_mod`
--

LOCK TABLES `tb_arctype_mod` WRITE;
/*!40000 ALTER TABLE `tb_arctype_mod` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_arctype_mod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_arctype`
--

DROP TABLE IF EXISTS `tb_arctype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_arctype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_id` int(11) DEFAULT NULL COMMENT '0-文章模型;1-单页模型;2-外部链接',
  `pid` int(11) NOT NULL DEFAULT '0' COMMENT '所属的分类ID',
  `typename` varchar(100) NOT NULL COMMENT '分类名称',
  `jumplink` varchar(200) NOT NULL COMMENT '跳转链接',
  `dirs` varchar(50) NOT NULL COMMENT '前台分类地址/ 必需 建议value为小写',
  `icon` varchar(50) DEFAULT '',
  `litpic` varchar(200) DEFAULT NULL COMMENT '分类图标',
  `description` text COMMENT '分类描述',
  `sorts` int(11) DEFAULT '0' COMMENT '分类排序',
  `status` tinyint(4) DEFAULT '1' COMMENT '1-正常;0-禁用',
  `keywords` text COMMENT '关键字: [文档,前端,后台]',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `edit_time` int(11) NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  KEY `FK_arctype_arctypeMod` (`model_id`),
  CONSTRAINT `FK_arctype_arctypeMod` FOREIGN KEY (`model_id`) REFERENCES `tb_arctype_mod` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_arctype`
--

LOCK TABLES `tb_arctype` WRITE;
/*!40000 ALTER TABLE `tb_arctype` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_arctype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_archive`
--

DROP TABLE IF EXISTS `tb_archive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_archive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT '0',
  `uid` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `flag` set('p','c','a','h') DEFAULT 'p' COMMENT 'h-头条；a-特荐；c-推荐；p-图片',
  `litpic` varchar(200) DEFAULT NULL,
  `jumplink` varchar(200) DEFAULT '',
  `keywords` varchar(200) DEFAULT '',
  `content` longtext,
  `description` text NOT NULL,
  `views` bigint(255) DEFAULT '0',
  `click` int(11) DEFAULT '0',
  `status` tinyint(4) DEFAULT '1',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_arctype_archive` (`type_id`),
  KEY `FK_user_archive` (`uid`),
  CONSTRAINT `FK_arctype_archive` FOREIGN KEY (`type_id`) REFERENCES `tb_arctype` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `FK_user_archive` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_archive`
--

LOCK TABLES `tb_archive` WRITE;
/*!40000 ALTER TABLE `tb_archive` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_archive` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-11 11:41:23
