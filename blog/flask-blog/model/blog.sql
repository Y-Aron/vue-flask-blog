/*
Navicat MySQL Data Transfer

Source Server         : learn
Source Server Version : 50639
Source Host           : 127.0.0.1:3306
Source Database       : learn

Target Server Type    : MYSQL
Target Server Version : 50639
File Encoding         : 65001

Date: 2018-08-18 20:17:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_archive
-- ----------------------------
DROP TABLE IF EXISTS `tb_archive`;
CREATE TABLE `tb_archive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_id` int(11) DEFAULT '0',
  `uid` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `flag` set('h','a','c','p') DEFAULT NULL COMMENT 'h-头条；a-特荐；c-推荐；p-图片',
  `jumplink` varchar(200) DEFAULT NULL,
  `litpic` varchar(200) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `description` text,
  `click` int(11) NOT NULL DEFAULT '0',
  `status` tinyint(4) NOT NULL DEFAULT '1',
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_arctype_archive` (`type_id`),
  KEY `FK_user_archive` (`uid`),
  CONSTRAINT `FK_arctype_archive` FOREIGN KEY (`type_id`) REFERENCES `tb_arctype` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `FK_user_archive` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_arctype
-- ----------------------------
DROP TABLE IF EXISTS `tb_arctype`;
CREATE TABLE `tb_arctype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT '1' COMMENT '0-文章模型;1-单页模型;2-外部链接',
  `pid` int(11) NOT NULL DEFAULT '0' COMMENT '所属的分类ID',
  `typename` varchar(100) NOT NULL COMMENT '分类名称',
  `jumplink` varchar(200) NOT NULL COMMENT '跳转链接',
  `dirs` varchar(50) NOT NULL COMMENT '前台分类地址',
  `litpic` varchar(200) DEFAULT NULL COMMENT '分类图标',
  `description` text COMMENT '分类描述',
  `sorts` int(11) NOT NULL DEFAULT '0' COMMENT '分类排序',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-正常;0-禁用',
  `keywords` text COMMENT '关键字: [文档,前端,后台]',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `edit_time` int(11) NOT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  KEY `FK_arctype_arctypeMod` (`mid`),
  CONSTRAINT `FK_arctype_arctypeMod` FOREIGN KEY (`mid`) REFERENCES `tb_arctype_mod` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_arctype_mod
-- ----------------------------
DROP TABLE IF EXISTS `tb_arctype_mod`;
CREATE TABLE `tb_arctype_mod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `operation` varchar(100) DEFAULT NULL,
  `sorts` int(11) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-正常;0-禁用',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_auth_group
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_group`;
CREATE TABLE `tb_auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) DEFAULT '0' COMMENT '0-系统浏览；1024-超级管理员',
  `title` varchar(200) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-正常;0-禁用',
  `description` varchar(100) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `edit_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_auth_group_rule
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_group_rule`;
CREATE TABLE `tb_auth_group_rule` (
  `rule_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`rule_id`,`group_id`),
  KEY `FK_group_groupRule_r` (`group_id`),
  CONSTRAINT `FK_group_groupRule_r` FOREIGN KEY (`group_id`) REFERENCES `tb_auth_group` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_rule_groupRule_r` FOREIGN KEY (`rule_id`) REFERENCES `tb_auth_rule` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_auth_rule
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_rule`;
CREATE TABLE `tb_auth_rule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL DEFAULT '0',
  `level` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-项目;2-模块;3-操作',
  `name` varchar(80) DEFAULT NULL,
  `title` varchar(30) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1-正常;0-禁用',
  `ismenu` tinyint(4) NOT NULL DEFAULT '0' COMMENT '1-导航;0-非导航',
  `icon` varchar(50) DEFAULT NULL,
  `sorts` int(11) DEFAULT '1' COMMENT '列表升序显示',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_auth_user_group
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_user_group`;
CREATE TABLE `tb_auth_user_group` (
  `uid` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`uid`,`group_id`),
  KEY `FK_group_userGroup_r` (`group_id`),
  CONSTRAINT `FK_group_userGroup_r` FOREIGN KEY (`group_id`) REFERENCES `tb_auth_group` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_user_userGroup_r` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_comment
-- ----------------------------
DROP TABLE IF EXISTS `tb_comment`;
CREATE TABLE `tb_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL DEFAULT '0',
  `type` int(11) DEFAULT NULL COMMENT 'NULL——留言板评论 \r\n            其他——文章id',
  `uid` int(11) NOT NULL,
  `content` text,
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `FK_comment_archive_r` (`type`),
  KEY `FK_comment_user_r` (`uid`),
  CONSTRAINT `FK_comment_archive_r` FOREIGN KEY (`type`) REFERENCES `tb_archive` (`id`) ON UPDATE SET NULL,
  CONSTRAINT `FK_comment_user_r` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_login_log
-- ----------------------------
DROP TABLE IF EXISTS `tb_login_log`;
CREATE TABLE `tb_login_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `ip` varchar(100) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `province` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '1',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_loginLog_user_r` (`uid`),
  CONSTRAINT `FK_loginLog_user_r` FOREIGN KEY (`uid`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(32) NOT NULL,
  `nickname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(50) DEFAULT NULL,
  `sex` tinyint(4) DEFAULT '0',
  `logins` int(11) DEFAULT '0',
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  `register_ip` varchar(100) DEFAULT NULL,
  `last_time` int(11) DEFAULT NULL,
  `last_ip` varchar(100) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `AK_unique_key` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tb_user_info
-- ----------------------------
DROP TABLE IF EXISTS `tb_user_info`;
CREATE TABLE `tb_user_info` (
  `id` int(11) NOT NULL,
  `avatar` varchar(200) DEFAULT NULL,
  `qq` varchar(100) DEFAULT NULL,
  `birthday` varchar(100) DEFAULT NULL,
  `info` text,
  `create_time` int(11) NOT NULL,
  `edit_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_user_userInfo_r` FOREIGN KEY (`id`) REFERENCES `tb_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Procedure structure for edit_arctype
-- ----------------------------
DROP PROCEDURE IF EXISTS `edit_arctype`;
DELIMITER ;;
CREATE DEFINER=`admin`@`localhost` PROCEDURE `edit_arctype`(
	IN id INT,								-- 分类ID
	IN pid INT, 							-- 所属分类ID
	IN mid INT,								-- 文章模型ID
	IN typename VARCHAR(100), -- 分类名称
	IN jumplink VARCHAR(200), -- 预览链接
	IN dirs VARCHAR(50), 			-- 分类目录
	IN litpic VARCHAR(200),		-- 分类缩略图路径
	IN description text, 			-- 分类描述
	IN sorts INT,							-- 分类列表显示的排序值
	IN keywords text,					-- 关键字设置
	IN state INT,							-- 分类状态
	OUT status_code INT 			-- 返回状态码
)
leave_name:
BEGIN
	DECLARE count INT;
	DECLARE now_time INT;
	-- 获取时间戳
	SET now_time = UNIX_TIMESTAMP(NOW());
	-- 默认status_code = 0 操作成功
	SET status_code = 0;
	-- 初始化arctype_mod表数据
	SELECT count(*) INTO count from tb_arctype_mod;
	IF count = 0 THEN
		INSERT INTO `learn`.`tb_arctype_mod` (`name`, `operation`, `sorts`, `status`, `create_time`, `edit_time`) 
				VALUES ('文章模型', 'addonarticle', '1', '1', now_time, now_time);
	END IF;

	SELECT count(*) INTO count from tb_arctype WHERE tb_arctype.id !=id AND tb_arctype.pid=pid AND tb_arctype.typename=typename;

	-- 分类已经存在 无法进行编辑
	if count > 0 THEN
		SET status_code = -1000;
	-- 离开存储过程
		LEAVE leave_name;
	END IF;

	-- 进入修改模式
	IF id > 0 AND count = 0 THEN
		-- 修改语句
		update tb_arctype set tb_arctype.pid = pid, tb_arctype.mid = mid,
													tb_arctype.typename = typename,
													tb_arctype.jumplink = jumplink,
													tb_arctype.litpic = litpic,
													tb_arctype.dirs = dirs, 
													tb_arctype.description = description, 
													tb_arctype.sorts = sorts,
													tb_arctype.`status`= state,
													tb_arctype.keywords = keywords,
													tb_arctype.edit_time = now_time WHERE tb_arctype.id = id;

		-- 受影响行数为0  数据没有改变
		IF ROW_COUNT() = 0 THEN
			SET status_code = -4000;
		END IF;
		LEAVE leave_name;

	END IF;

	-- 进入插入模式
	IF count = 0 THEN
		-- 插入语句
		INSERT INTO tb_arctype(`pid`,`typename`,`jumplink`,`dirs`,`litpic`,`description`,`sorts`,`keywords`,`create_time`,`edit_time`)
			VALUES(pid,typename,jumplink,dirs,litpic,description,sorts,keywords,now_time,now_time);
		
		# 分类创建失败!
		IF ROW_COUNT() = 0 THEN
				SET status_code = -5000;
		END IF;
	END IF;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for register
-- ----------------------------
DROP PROCEDURE IF EXISTS `register`;
DELIMITER ;;
CREATE DEFINER=`admin`@`localhost` PROCEDURE `register`(
	IN username VARCHAR(50),
	IN passwd VARCHAR(32),
	IN ip VARCHAR(100),
	OUT status_code INT
)
BEGIN
	DECLARE count INT;
	DECLARE last_id INT;
	DECLARE create_time INT;
	# 出现异常进行事务回滚
	DECLARE EXIT HANDLER FOR SQLEXCEPTION SET status_code = -1 ;
	SELECT count(*) INTO count FROM tb_user WHERE tb_user.username = username;
	IF(count = 0) THEN
		SET create_time = unix_timestamp(NOW());
		START TRANSACTION;
		INSERT INTO tb_user(`username`,`password`,`create_time`,`edit_time`,`register_ip`) 
					VALUES(username,passwd,create_time,create_time,ip);
		SELECT MAX(`id`) INTO last_id from tb_user;
		
		INSERT INTO tb_user_info(`id`,`create_time`,`edit_time`) VALUES(last_id,create_time,create_time);
		IF status_code = -1 THEN
			ROLLBACK;
		ELSE
			COMMIT;
		END IF;
		# 注册成功
		SET status_code = 0;
	ELSE
		# 注册失败
		SET status_code = 1000;
	end if;
		
END
;;
DELIMITER ;