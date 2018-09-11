/*
Navicat MySQL Data Transfer

Source Server         : learn
Source Server Version : 50639
Source Host           : 127.0.0.1:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50639
File Encoding         : 65001

Date: 2018-09-11 14:31:58
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_archive
-- ----------------------------
INSERT INTO `tb_archive` VALUES ('1', '6', '1', 'CentOS 7系统配置国内yum源和epel源', 'p', 'ea4ae75adb62bfdb71287b464b878ce8fcc02a39.jpg', '/detail/6', 'CentOS,yum,epel源', '\n\n**1. 进入/etc/yum.repos.d/目录下，新建一个repo_bak目录，用于保存系统中原来的repo文件**\n\n```\n[roo@localhost ~]$ cd /etc/yum.repos.d/\n[roo@localhost yum.repos.d]$ sudo mkdir resp_bak\n[roo@localhost yum.repos.d]$ sudo mv *.repo repo_bak/\n```\n</br>\n\n**2. 在CentOS中配置使用网易的开源镜像**\n\n```\n[roo@localhost yum.repos.d]$ sudo wget http://mirrors.163.com/.help/CentOS7-Base-163.repo\n[roo@localhost yum.repos.d]$ ls\nCentOS7-Base-163.repo repo_bak\n```\n</br>\n\n**3. 清除yum缓存并生成新的yum缓存**\n\n```\n[roo@localhost yum.repos.d]$ yum clean all    # 清除系统所有的yum缓存\n[roo@localhost yum.repos.d]$ yum makecache		# 生成yum缓存\n```\n</br>\n\n**4. 安装epel源**\n\n```\n[root@localhost yum.repos.d]$ sudo yum install -y epel-release\n[roo@localhost yum.repos.d]$ ls\nCentOS7-Base-163.repo  epel.repo  epel-testing.repo  repo_bak\n```\n</br>\n\n**5. 使用阿里开源镜像提供的epel源**\n\n```\n[roo@localhost yum.repos.d]$ sudo wget -O /etc/yum.repos.d/epel-7.repo http://mirrors.aliyun.com/repo/epel-7.repo\n[roo@localhost yum.repos.d]$ ls\nCentOS7-Base-163.repo  epel-7.repo  epel.repo  epel-testing.repo  repo_bak\n```\n</br>\n\n**6. 再次清楚系统yum缓存，并重新生成新的yum缓存**\n\n```\n[roo@localhost yum.repos.d]$ yum clean all\n[roo@localhost yum.repos.d]$ yum makecache\n```\n</br>\n\n**7. 查看系统可用的yum源和所有的yum源**\n\n```\n[roo@localhost yum.repos.d]$ yum repolist enabled\n[roo@localhost yum.repos.d]$ yum repolist all\n```\n\n\n', '这是一篇介绍在CentOS中如何配置国内yum源和epel源的文章。', '42', '0', '1', '1536638951', '1536638951');
INSERT INTO `tb_archive` VALUES ('2', '6', '1', 'CentOS 7搭建python2.7虚拟环境', 'p', 'ea4ae75adb62bfdb71287b464b878ce8fcc02a39.jpg', '/detail/6', 'Centos,python', '\n**1. 安装 virtualenv和virtualenvwrapper**\n\n> [roo@localhost ~]$ pip install virtualenv  virtualenvwrapper\n\n<br/>\n\n**2. 配置virtualenvwrapper**\n\n* 打开.bashrc文件\n\n> [roo@localhost ~]$ vi ~/.bashrc\n\n+ 增加下列代码\n\n> [roo@localhost ~]$ source /usr/bin/virtualenvwrapper.sh \n\n+ 运行命令\n\n> [roo@localhost ~]$ source ~/.bashrc\n\n<br/>\n\n**3. 查看根目录下是否创建.virtualenvs**\n\n> [roo@localhost ~]$ ls -a | grep virtualenvs\n> .virtualenvs\n\n<br/>\n\n**4. 常用操作**\n\n+ mkvirtualenv envname      # 创建虚拟环境\n\n+ workon [evnname]                # 不加参数可以列出环境列表\n\n+ lsvirtualenv                           # 列出所有环境\n\n+ deactivate                             # 注销当前环境\n\n+ rmvirtualenv  envname      # 删除指定环境\n\n+ wipeenv                                 # 清除环境内所有第三方包\n', '这是一篇介绍如何在Centos上搭建python2.7的虚拟环境的文章。值得参考~', '22', '0', '1', '1536640176', '1536640176');

-- ----------------------------
-- Table structure for tb_arctype
-- ----------------------------
DROP TABLE IF EXISTS `tb_arctype`;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_arctype
-- ----------------------------
INSERT INTO `tb_arctype` VALUES ('1', '1', '0', '文档分类', '/category/category', 'category', '<i class=\"fa fa-list\"></i>', '367958c8bde938df5099163731cabae2a5cb03e9.jpg', '### 记录敲代码的日常', '1', '1', 'category,文档分类', '1536637790', '1536637790');
INSERT INTO `tb_arctype` VALUES ('2', '2', '0', '单页', '/category/page', 'page', '<i class=\"fa fa-file-text\"></i>', '', '### 网站简介', '2', '1', 'page,单页', '1536637873', '1536637873');
INSERT INTO `tb_arctype` VALUES ('3', '2', '2', '关于我', '/category/about_me', 'about_me', '<i class=\"fa fa-circle-o\"></i>', '', '![image.jpg](/api/download/64c802693adb72e8f2147b780d93e7459ccd60a6.jpg)\n\n\n##### 一个热爱学习的年轻小伙~', '50', '1', 'Vue-Flask-Blog,关于我', '1536638303', '1536638303');
INSERT INTO `tb_arctype` VALUES ('4', '2', '2', '系统更新日志', '/category/system_update', 'system_update', '<i class=\"fa fa-circle-o\"></i>', '', '> 2018-9-11\n\n1. 前后端分离构建完毕\n2. 前端vue构建页面\n3. 后端python-flask实现逻辑\n4. 数据库MySQL实现关系处理\n5. redis实现站点统计与其他缓存', '50', '1', '系统更新日志', '1536638557', '1536640004');
INSERT INTO `tb_arctype` VALUES ('5', '2', '2', '留言板', '/category/guestbook', 'guestbook', '<i class=\"fa fa-circle-o\"></i>', '', '留言成功不会立即显示出来，仅自己可见，会审核留言内容才会显示出来！\n\n说点什么吧......我会接受到你的留言邮件，会尽快回复你！！！', '50', '1', '留言板', '1536638607', '1536638607');
INSERT INTO `tb_arctype` VALUES ('6', '1', '1', 'CentOS', '/category/centos', 'centos', '<i class=\"fa fa-circle-o\"></i>', 'ea4ae75adb62bfdb71287b464b878ce8fcc02a39.jpg', '##### 本分类专门收录一些CentOS的使用文章', '50', '1', 'linux,CentOS', '1536638772', '1536638772');

-- ----------------------------
-- Table structure for tb_arctype_mod
-- ----------------------------
DROP TABLE IF EXISTS `tb_arctype_mod`;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_arctype_mod
-- ----------------------------
INSERT INTO `tb_arctype_mod` VALUES ('1', '文章模型', 'addonaricle', '1', '1', '1536637554', '1536637554');
INSERT INTO `tb_arctype_mod` VALUES ('2', '单页', 'addonpage', '2', '1', '1536637570', '1536637570');

-- ----------------------------
-- Table structure for tb_auth_group
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_group`;
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

-- ----------------------------
-- Records of tb_auth_group
-- ----------------------------
INSERT INTO `tb_auth_group` VALUES ('1', '管理员', '超级管理员', '9999', '1', '权限大佬！！', '1536637148', '1536642220');

-- ----------------------------
-- Table structure for tb_auth_group_rule
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_group_rule`;
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

-- ----------------------------
-- Records of tb_auth_group_rule
-- ----------------------------
INSERT INTO `tb_auth_group_rule` VALUES ('1', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('2', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('3', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('4', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('5', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('6', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('7', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('8', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('9', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('10', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('11', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('12', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('13', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('14', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('15', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('16', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('17', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('18', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('19', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('20', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('22', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('23', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('24', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('26', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('27', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('30', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('31', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('32', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('33', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('34', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('35', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('36', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('37', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('38', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('39', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('40', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('41', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('42', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('43', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('44', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('45', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('46', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('47', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('48', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('49', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('50', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('51', '1', '1536637148', '1536637148');
INSERT INTO `tb_auth_group_rule` VALUES ('52', '1', '1536642220', '1536642220');
INSERT INTO `tb_auth_group_rule` VALUES ('53', '1', '1536642220', '1536642220');

-- ----------------------------
-- Table structure for tb_auth_rule
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_rule`;
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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_auth_rule
-- ----------------------------
INSERT INTO `tb_auth_rule` VALUES ('1', '0', '0', '1', '后台首页', 'GET', '/api/admin', '1', '1000', '1536605600', '1536607095');
INSERT INTO `tb_auth_rule` VALUES ('2', '0', '0', '1', '文章管理', 'MENU', '/api/arcitle/manage', '1', '1100', '1536606174', '1536607001');
INSERT INTO `tb_auth_rule` VALUES ('3', '2', '2', '2', '文章分类', 'GET', '/api/arctype/index', '1', '1', '1536606254', '1536607030');
INSERT INTO `tb_auth_rule` VALUES ('4', '2', '3', '3', '新增分类', 'POST', '/api/arctype', '1', '1', '1536606317', '1536607044');
INSERT INTO `tb_auth_rule` VALUES ('5', '2', '3', '3', '编辑分类', 'PUT', '/api/arctype', '1', '2', '1536606341', '1536607054');
INSERT INTO `tb_auth_rule` VALUES ('6', '2', '3', '3', '删除分类', 'DELETE', '/api/arctype/index', '1', '3', '1536606366', '1536607551');
INSERT INTO `tb_auth_rule` VALUES ('7', '2', '2', '2', '文章列表', 'GET', '/api/archive/index', '1', '2', '1536606515', '1536607462');
INSERT INTO `tb_auth_rule` VALUES ('8', '2', '7', '3', '新增文章', 'POST', '/api/archive', '1', '1', '1536606537', '1536607564');
INSERT INTO `tb_auth_rule` VALUES ('9', '2', '7', '3', '编辑文章', 'PUT', '/api/archive', '1', '2', '1536606567', '1536607575');
INSERT INTO `tb_auth_rule` VALUES ('10', '2', '7', '3', '删除文章', 'DELETE', '/api/archive/index', '1', '3', '1536606590', '1536607583');
INSERT INTO `tb_auth_rule` VALUES ('11', '2', '2', '2', '文章模型管理', 'GET', '/api/arctype/model/index', '1', '3', '1536606636', '1536607531');
INSERT INTO `tb_auth_rule` VALUES ('12', '2', '11', '3', '删除模型', 'DELETE', '/api/arctype/model/index', '1', '3', '1536606668', '1536606811');
INSERT INTO `tb_auth_rule` VALUES ('13', '2', '11', '3', '新增模型', 'POST', '/api/arctype/model', '1', '1', '1536606769', '1536607593');
INSERT INTO `tb_auth_rule` VALUES ('14', '2', '11', '3', '编辑模型', 'PUT', '/api/arctype/model', '1', '2', '1536606795', '1536607602');
INSERT INTO `tb_auth_rule` VALUES ('15', '0', '0', '1', '用户管理', 'MENU', '/api/user/manage', '1', '1200', '1536607645', '1536635321');
INSERT INTO `tb_auth_rule` VALUES ('16', '15', '15', '2', '用户列表', 'GET', '/api/user/index', '1', '1', '1536607720', '1536607720');
INSERT INTO `tb_auth_rule` VALUES ('17', '15', '15', '2', '角色管理', 'GET', '/api/user/group/index', '1', '2', '1536607792', '1536607792');
INSERT INTO `tb_auth_rule` VALUES ('18', '15', '15', '2', '角色节点列表', 'GET', '/api/user/group/rule/index', '1', '3', '1536607844', '1536607844');
INSERT INTO `tb_auth_rule` VALUES ('19', '15', '16', '3', '新增用户', 'POST', '/api/user', '1', '1', '1536607890', '1536607890');
INSERT INTO `tb_auth_rule` VALUES ('20', '15', '16', '3', '编辑用户', 'PUT', '/api/user', '1', '2', '1536607922', '1536607922');
INSERT INTO `tb_auth_rule` VALUES ('21', '15', '16', '3', '删除用户', 'DELETE', '/api/user/index', '1', '3', '1536607952', '1536607952');
INSERT INTO `tb_auth_rule` VALUES ('22', '15', '16', '3', '授权角色', 'POST', '/api/user/auth', '1', '4', '1536608111', '1536608111');
INSERT INTO `tb_auth_rule` VALUES ('23', '15', '17', '3', '新增角色', 'POST', '/api/user/group', '1', '1', '1536634120', '1536634120');
INSERT INTO `tb_auth_rule` VALUES ('24', '15', '17', '3', '编辑角色', 'PUT', '/api/user/group', '1', '2', '1536634141', '1536634141');
INSERT INTO `tb_auth_rule` VALUES ('25', '15', '17', '3', '删除角色', 'DELETE', '/api/user/group/index', '1', '3', '1536634169', '1536634169');
INSERT INTO `tb_auth_rule` VALUES ('26', '15', '18', '3', '新增节点', 'POST', '/api/user/group/rule', '1', '1', '1536634222', '1536634222');
INSERT INTO `tb_auth_rule` VALUES ('27', '15', '18', '3', '编辑节点', 'PUT', '/api/user/group/rule', '1', '2', '1536634248', '1536634248');
INSERT INTO `tb_auth_rule` VALUES ('29', '15', '18', '3', '删除节点', 'DELETE', '/api/user/group/rule/index', '1', '3', '1536634828', '1536634828');
INSERT INTO `tb_auth_rule` VALUES ('30', '0', '0', '1', '消息管理', 'MENU', '/api/comment', '1', '1300', '1536634899', '1536634899');
INSERT INTO `tb_auth_rule` VALUES ('31', '30', '30', '2', '留言列表', 'GET', '/api/comment/guestBook/index', '1', '1', '1536634954', '1536634954');
INSERT INTO `tb_auth_rule` VALUES ('32', '30', '30', '2', '文章评论列表', 'GET', '/api/comment/archive/index', '1', '2', '1536634983', '1536634983');
INSERT INTO `tb_auth_rule` VALUES ('33', '30', '31', '3', '编辑留言', 'POST', '/api/comment', '1', '1', '1536635062', '1536635062');
INSERT INTO `tb_auth_rule` VALUES ('34', '30', '31', '3', '删除留言', 'DELETE', '/api/comment/guestBook/index', '1', '2', '1536635093', '1536635093');
INSERT INTO `tb_auth_rule` VALUES ('35', '30', '32', '3', '编辑评论', 'POST', '/api/comment', '1', '1', '1536635121', '1536635121');
INSERT INTO `tb_auth_rule` VALUES ('36', '30', '32', '3', '删除评论', 'DELETE', '/api/comment/archive/index', '1', '2', '1536635150', '1536635150');
INSERT INTO `tb_auth_rule` VALUES ('37', '0', '0', '1', '系统管理', 'MENU', '/api/config/manage', '1', '1400', '1536635217', '1536635298');
INSERT INTO `tb_auth_rule` VALUES ('38', '0', '0', '1', '站长工具', 'MENU', '/api/port/manage', '1', '1500', '1536635274', '1536635536');
INSERT INTO `tb_auth_rule` VALUES ('39', '0', '0', '1', '数据库管理', 'MENU', '/api/database/manage', '1', '1600', '1536635360', '1536635360');
INSERT INTO `tb_auth_rule` VALUES ('40', '37', '37', '2', '系统配置字段', 'GET', '/api/config/index', '1', '1', '1536635414', '1536635414');
INSERT INTO `tb_auth_rule` VALUES ('41', '37', '40', '3', '新增字段', 'POST', '/api/config', '1', '1', '1536635448', '1536635498');
INSERT INTO `tb_auth_rule` VALUES ('42', '37', '40', '3', '编辑字段', 'PUT', '/api/config', '1', '2', '1536635461', '1536635507');
INSERT INTO `tb_auth_rule` VALUES ('43', '37', '40', '3', '删除字段', 'DELETE', '/api/config/index', '1', '3', '1536635477', '1536635528');
INSERT INTO `tb_auth_rule` VALUES ('44', '38', '38', '2', '登录日志', 'GET', '/api/login_log/index', '1', '1', '1536635710', '1536635710');
INSERT INTO `tb_auth_rule` VALUES ('45', '38', '44', '3', '删除日志', 'DELETE', '/api/login_log/index', '1', '1', '1536635747', '1536635747');
INSERT INTO `tb_auth_rule` VALUES ('46', '39', '39', '2', '数据库列表', 'GET', '/api/database/index', '1', '1', '1536635787', '1536635870');
INSERT INTO `tb_auth_rule` VALUES ('47', '39', '39', '2', '还原数据库', 'GET', '/api/database/backup', '1', '2', '1536635808', '1536636032');
INSERT INTO `tb_auth_rule` VALUES ('48', '39', '46', '3', '备份数据库', 'POST', '/api/database/backup', '1', '1', '1536636016', '1536636016');
INSERT INTO `tb_auth_rule` VALUES ('49', '39', '47', '3', '还原', 'PUT', '/api/database/backup/recovery', '1', '1', '1536636181', '1536636181');
INSERT INTO `tb_auth_rule` VALUES ('50', '39', '47', '3', '下载', 'GET', '/api/database/backup/download', '1', '2', '1536636228', '1536636228');
INSERT INTO `tb_auth_rule` VALUES ('51', '39', '47', '3', '删除', 'DELETE', '/api/database/backup', '1', '3', '1536636267', '1536636267');
INSERT INTO `tb_auth_rule` VALUES ('52', '30', '32', '3', '改变状态', 'PUT', '/api/comment/refstate', '1', '3', '1536642111', '1536642111');
INSERT INTO `tb_auth_rule` VALUES ('53', '30', '31', '3', '改变状态', 'PUT', '/api/comment/refstate', '1', '3', '1536642143', '1536642143');

-- ----------------------------
-- Table structure for tb_auth_user_group
-- ----------------------------
DROP TABLE IF EXISTS `tb_auth_user_group`;
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

-- ----------------------------
-- Records of tb_auth_user_group
-- ----------------------------
INSERT INTO `tb_auth_user_group` VALUES ('1', '1', '1536637222', '1536637222');

-- ----------------------------
-- Table structure for tb_comment
-- ----------------------------
DROP TABLE IF EXISTS `tb_comment`;
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
  `status` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_comment_archive_r` (`type`),
  KEY `FK_comment_user_r` (`username`),
  CONSTRAINT `FK_comment_archive_r` FOREIGN KEY (`type`) REFERENCES `tb_archive` (`id`) ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_comment
-- ----------------------------
INSERT INTO `tb_comment` VALUES ('1', '0', '0', '1', '1249205951@qq.com', '测试人', '测试下评论', '1536641055', '1536641055', '1');
INSERT INTO `tb_comment` VALUES ('4', '0', '0', '1', '124920512@qq.com', '测试人员1 ', '评论测试', '1536644188', '1536644188', '1');
INSERT INTO `tb_comment` VALUES ('5', '0', '0', null, '12312@qq.com', '测试人', '留言+1', '1536644740', '1536644740', '1');
INSERT INTO `tb_comment` VALUES ('6', '0', '5', null, '232@qq.com', '12323', '留言 +2', '1536646139', '1536646139', '1');
INSERT INTO `tb_comment` VALUES ('7', '0', '6', null, '12323@qq.com', '阿达达', '留言 +3 ', '1536646183', '1536646183', '1');
INSERT INTO `tb_comment` VALUES ('8', '0', '7', null, '2132@qq.com', '阿斯顿', '不盖楼了 就这样', '1536646213', '1536646213', '1');
INSERT INTO `tb_comment` VALUES ('9', '0', '0', null, '23232123@qq.com', '阿斯顿', '测试人2', '1536646243', '1536646243', '1');
INSERT INTO `tb_comment` VALUES ('10', '0', '9', null, '232312@qq.com', '阿萨德 ', '测试人 2', '1536646275', '1536646275', '1');

-- ----------------------------
-- Table structure for tb_config
-- ----------------------------
DROP TABLE IF EXISTS `tb_config`;
CREATE TABLE `tb_config` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `key` varchar(30) NOT NULL,
  `value` varchar(200) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `type` enum('web','sys') DEFAULT 'sys',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_config
-- ----------------------------
INSERT INTO `tb_config` VALUES ('1', 'web_author', 'Y-先生', '前端作者显示~', 'web');
INSERT INTO `tb_config` VALUES ('2', 'git_fork_url', 'https://gitee.com/suxiaoxin/Tp5-TuFanInc-Admin/members', 'github_fork链接', 'web');
INSERT INTO `tb_config` VALUES ('3', 'web_title', '天行健，君子以自强不息！地势坤，君子以厚德载物！', '网站页面警句', 'web');
INSERT INTO `tb_config` VALUES ('4', 'web_footer', 'Copyright © 2017-2018 Y-先生', '网站页脚', 'web');
INSERT INTO `tb_config` VALUES ('5', 'web_talk', '杨文杰个人博客，是一个记录自己生活点滴、互联网技术的原创独立博客。', '', 'web');

-- ----------------------------
-- Table structure for tb_login_log
-- ----------------------------
DROP TABLE IF EXISTS `tb_login_log`;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_login_log
-- ----------------------------
INSERT INTO `tb_login_log` VALUES ('2', '1', '127.0.0.1', '中国', '', '', '', '1', '1536605008', '1536605008');
INSERT INTO `tb_login_log` VALUES ('3', '1', '127.0.0.1', '中国', '', '', '', '1', '1536605047', '1536605047');
INSERT INTO `tb_login_log` VALUES ('4', '1', '127.0.0.1', '中国', '', '', '', '1', '1536606932', '1536606932');
INSERT INTO `tb_login_log` VALUES ('5', '1', '127.0.0.1', '中国', '', '', '', '1', '1536634041', '1536634041');
INSERT INTO `tb_login_log` VALUES ('6', '1', '127.0.0.1', '中国', '', '', '', '1', '1536634064', '1536634064');
INSERT INTO `tb_login_log` VALUES ('7', '1', '127.0.0.1', '中国', '', '', '', '1', '1536635884', '1536635884');
INSERT INTO `tb_login_log` VALUES ('8', '1', '127.0.0.1', '中国', '', '', '', '1', '1536637698', '1536637698');
INSERT INTO `tb_login_log` VALUES ('9', '1', '127.0.0.1', '中国', '', '', '', '1', '1536637718', '1536637718');
INSERT INTO `tb_login_log` VALUES ('10', '1', '127.0.0.1', '中国', '', '', '', '1', '1536639784', '1536639784');
INSERT INTO `tb_login_log` VALUES ('11', '1', '127.0.0.1', '中国', '', '', '', '1', '1536641674', '1536641674');
INSERT INTO `tb_login_log` VALUES ('12', '1', '127.0.0.1', '中国', '', '', '', '1', '1536643511', '1536643511');
INSERT INTO `tb_login_log` VALUES ('13', '1', '127.0.0.1', '中国', '', '', '', '1', '1536646154', '1536646154');

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
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

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('1', 'admin', '21232f297a57a5a743894a0e4a801fc3', 'Y-先生', '1249205951@qq.com', '15280553351', '13', null, null, '', null, null, '1');

-- ----------------------------
-- Table structure for tb_user_info
-- ----------------------------
DROP TABLE IF EXISTS `tb_user_info`;
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

-- ----------------------------
-- Records of tb_user_info
-- ----------------------------
INSERT INTO `tb_user_info` VALUES ('1', '64c802693adb72e8f2147b780d93e7459ccd60a6.jpg', '0', '1249205951', '1997-02-17', '> 这个人特别懒 \n\n****\n### 佛性更新\n', null, null);

-- ----------------------------
-- Procedure structure for auth
-- ----------------------------
DROP PROCEDURE IF EXISTS `auth`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `auth`(
	IN uid INT,
	IN path VARCHAR(200),
	IN method VARCHAR(30)
)
BEGIN
DECLARE gid INT;

SELECT tb_auth_user_group.group_id INTO gid FROM tb_auth_user_group WHERE tb_auth_user_group.uid = uid;

IF UPPER(method) != 'GET' THEN
	SELECT route FROM tb_auth_group_rule AS gr LEFT JOIN tb_auth_rule AS r ON gr.rule_id=r.id 
		WHERE gr.group_id=gid AND r.method=method ;

END IF;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for edit_arctype
-- ----------------------------
DROP PROCEDURE IF EXISTS `edit_arctype`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `edit_arctype`(
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
	IN icon VARCHAR(50),			-- 分类图标
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

	SELECT count(*) INTO count from tb_arctype WHERE tb_arctype.id !=id AND tb_arctype.pid=pid 
			AND tb_arctype.typename=typename;

	
	-- 分类已经存在 无法进行编辑
	if count > 0 THEN
		SET status_code = -1000;
	-- 离开存储过程
		LEAVE leave_name;
	END IF;

	-- 进入修改模式
	IF id > 0 AND count = 0 THEN
		-- 修改语句
		update tb_arctype set tb_arctype.pid = pid, tb_arctype.model_id = mid,
													tb_arctype.typename = typename,
													tb_arctype.jumplink = jumplink,
													tb_arctype.litpic = litpic,
													tb_arctype.dirs = dirs, 
													tb_arctype.description = description, 
													tb_arctype.sorts = sorts,
													tb_arctype.`status`= state,
													tb_arctype.keywords = keywords,
													tb_arctype.icon = icon,
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
		INSERT INTO tb_arctype(`pid`,`typename`,`jumplink`,`dirs`,`litpic`,`description`,`sorts`,`keywords`,`create_time`,`edit_time`,`model_id`,`icon`)
			VALUES(pid,typename,jumplink,dirs,litpic,description,sorts,keywords,now_time,now_time,mid, icon);
		
		# 分类创建失败!
		IF ROW_COUNT() = 0 THEN
				SET status_code = -5000;
		END IF;
	END IF;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for get_routes
-- ----------------------------
DROP PROCEDURE IF EXISTS `get_routes`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_routes`(
	IN uid INT,
	IN method VARCHAR(30)
)
BEGIN
DECLARE gid INT;

SELECT tb_auth_user_group.group_id INTO gid FROM tb_auth_user_group WHERE tb_auth_user_group.uid = uid;

IF UPPER(method) != 'GET' THEN

	SELECT route FROM tb_auth_group_rule AS gr LEFT JOIN tb_auth_rule AS r ON gr.rule_id=r.id 
		WHERE gr.group_id=gid AND r.method=method ;

END IF;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for init_index
-- ----------------------------
DROP PROCEDURE IF EXISTS `init_index`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `init_index`(
	IN _first INT,
	IN _end INT,
	OUT users INT,
	OUT article_total INT,
	OUT user_near_num INT,
	OUT comment_near_num INT
)
BEGIN
	SELECT `ip`,`country`, `province`, `city`, `district`, FROM_UNIXTIME(create_time) as login_time FROM tb_login_log ORDER BY create_time DESC LIMIT _first,_end;
	SELECT count(*) INTO users FROM tb_user;
	SELECT count(*) INTO article_total FROM tb_archive;
	SELECT count(*) INTO user_near_num FROM tb_user WHERE DATE_SUB(CURDATE(),INTERVAL 7 DAY) <= DATE(FROM_UNIXTIME(create_time));
	SELECT count(*) INTO comment_near_num FROM tb_comment WHERE DATE_SUB(CURDATE(),INTERVAL 7 DAY) <= DATE(FROM_UNIXTIME(create_time));
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for proc_test
-- ----------------------------
DROP PROCEDURE IF EXISTS `proc_test`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `proc_test`(
	IN int_code INT,
	OUT out_code INT
)
BEGIN
DECLARE decalre_code INT DEFAULT 0;
SELECT decalre_code;
SELECT int_code;
IF decalre_code = int_code THEN
SET out_code = 1;
ELSE
SET out_code = 0;
END IF;

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for register
-- ----------------------------
DROP PROCEDURE IF EXISTS `register`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `register`(
	IN username VARCHAR(50),  -- 用户名
	IN passwd VARCHAR(32),		-- 密码
	IN nickname VARCHAR(100),	-- 昵称
	IN email VARCHAR(100),		-- 邮箱
	IN mobile VARCHAR(50),		-- 手机号
	IN state TINYINT,					-- 状态
	IN ip VARCHAR(100),				-- 注册ip
	OUT status_code INT				-- 返回状态码
)
BEGIN
	DECLARE count INT;
	-- 插入数据的自增ID
	DECLARE last_id INT;
	DECLARE create_time INT;
	# 出现异常进行事务回滚
	DECLARE EXIT HANDLER FOR SQLEXCEPTION SET status_code = -1 ;
	SELECT count(*) INTO count FROM tb_user WHERE tb_user.username = username;
	IF(count = 0) THEN
		SET create_time = unix_timestamp(NOW());
		START TRANSACTION;
		INSERT INTO tb_user(`username`,`password`,`create_time`,`edit_time`,`register_ip`,`nickname`,`email`,`mobile`, `status`) 
					VALUES(username,passwd,create_time,create_time,ip,nickname, email, mobile, state);
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
		SET status_code = -1000;
	end if;
		
END
;;
DELIMITER ;
