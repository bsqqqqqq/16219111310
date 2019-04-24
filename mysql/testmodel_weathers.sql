/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : test1

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-04-24 17:33:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for testmodel_weathers
-- ----------------------------
DROP TABLE IF EXISTS `testmodel_weathers`;
CREATE TABLE `testmodel_weathers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wCity` varchar(16) NOT NULL,
  `wDate` varchar(16) NOT NULL,
  `wWeather` varchar(64) NOT NULL,
  `wTemp` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testmodel_weathers
-- ----------------------------
INSERT INTO `testmodel_weathers` VALUES ('1', '北京', '8日（今天）', '多云转小雨', '17/5℃');
INSERT INTO `testmodel_weathers` VALUES ('2', '北京', '9日（明天）', '小雨转多云', '9/1℃');
INSERT INTO `testmodel_weathers` VALUES ('3', '北京', '10日（后天）', '多云', '17/5℃');
INSERT INTO `testmodel_weathers` VALUES ('4', '北京', '11日（周四）', '多云转晴', '18/5℃');
INSERT INTO `testmodel_weathers` VALUES ('5', '北京', '12日（周五）', '多云', '23/9℃');
INSERT INTO `testmodel_weathers` VALUES ('6', '北京', '13日（周六）', '多云转晴', '19/5℃');
INSERT INTO `testmodel_weathers` VALUES ('7', '北京', '14日（周日）', '晴', '24/9℃');
INSERT INTO `testmodel_weathers` VALUES ('8', '上海', '8日（今天）', '多云转小雨', '27/17℃');
INSERT INTO `testmodel_weathers` VALUES ('9', '上海', '9日（明天）', '中雨转小雨', '24/11℃');
INSERT INTO `testmodel_weathers` VALUES ('10', '上海', '10日（后天）', '阴', '15/11℃');
INSERT INTO `testmodel_weathers` VALUES ('11', '上海', '11日（周四）', '多云', '15/10℃');
INSERT INTO `testmodel_weathers` VALUES ('12', '上海', '12日（周五）', '晴转多云', '17/12℃');
INSERT INTO `testmodel_weathers` VALUES ('13', '上海', '13日（周六）', '多云', '19/12℃');
INSERT INTO `testmodel_weathers` VALUES ('14', '上海', '14日（周日）', '阴转多云', '20/11℃');
INSERT INTO `testmodel_weathers` VALUES ('15', '广州', '8日（今天）', '多云', '30/23℃');
INSERT INTO `testmodel_weathers` VALUES ('16', '广州', '9日（明天）', '多云', '30/23℃');
INSERT INTO `testmodel_weathers` VALUES ('17', '广州', '10日（后天）', '多云转阴', '30/23℃');
INSERT INTO `testmodel_weathers` VALUES ('18', '广州', '11日（周四）', '雷阵雨', '27/19℃');
INSERT INTO `testmodel_weathers` VALUES ('19', '广州', '12日（周五）', '中雨转阴', '23/20℃');
INSERT INTO `testmodel_weathers` VALUES ('20', '广州', '13日（周六）', '多云转中雨', '25/22℃');
INSERT INTO `testmodel_weathers` VALUES ('21', '广州', '14日（周日）', '中雨转暴雨', '25/18℃');
INSERT INTO `testmodel_weathers` VALUES ('22', '深圳', '8日（今天）', '多云', '29/24℃');
INSERT INTO `testmodel_weathers` VALUES ('23', '深圳', '9日（明天）', '多云', '29/23℃');
INSERT INTO `testmodel_weathers` VALUES ('24', '深圳', '10日（后天）', '多云', '30/23℃');
INSERT INTO `testmodel_weathers` VALUES ('25', '深圳', '11日（周四）', '雷阵雨', '29/20℃');
INSERT INTO `testmodel_weathers` VALUES ('26', '深圳', '12日（周五）', '雷阵雨转小雨', '25/21℃');
INSERT INTO `testmodel_weathers` VALUES ('27', '深圳', '13日（周六）', '小雨转阵雨', '26/21℃');
INSERT INTO `testmodel_weathers` VALUES ('28', '深圳', '14日（周日）', '阵雨转小雨', '26/22℃');
