/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : localhost:3306
 Source Schema         : knowledgegraph

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 23/03/2024 02:01:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for entity
-- ----------------------------
DROP TABLE IF EXISTS `entity`;
CREATE TABLE `entity`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `entity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16482716 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '实体表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for entity_copy1
-- ----------------------------
DROP TABLE IF EXISTS `entity_copy1`;
CREATE TABLE `entity_copy1`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `entity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16482716 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '实体表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for property
-- ----------------------------
DROP TABLE IF EXISTS `property`;
CREATE TABLE `property`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `property` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28855554 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '属性表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for property_copy1
-- ----------------------------
DROP TABLE IF EXISTS `property_copy1`;
CREATE TABLE `property_copy1`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `property` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28855554 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '属性表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for relation
-- ----------------------------
DROP TABLE IF EXISTS `relation`;
CREATE TABLE `relation`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `relation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 480537 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '关系表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for relation_copy1
-- ----------------------------
DROP TABLE IF EXISTS `relation_copy1`;
CREATE TABLE `relation_copy1`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `relation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 480537 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '关系表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for triple
-- ----------------------------
DROP TABLE IF EXISTS `triple`;
CREATE TABLE `triple`  (
  `object_id` int NULL DEFAULT NULL,
  `entity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `relation_id` int NULL DEFAULT NULL,
  `relation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `subject_id` int NULL DEFAULT NULL,
  `subject` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `subject_type` int NULL DEFAULT NULL COMMENT '目标类型，0：entity，1：property'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '三元组关系表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for triple_copy1
-- ----------------------------
DROP TABLE IF EXISTS `triple_copy1`;
CREATE TABLE `triple_copy1`  (
  `object_id` int NULL DEFAULT NULL,
  `entity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `relation_id` int NULL DEFAULT NULL,
  `relation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `subject_id` int NULL DEFAULT NULL,
  `subject` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `subject_type` int NULL DEFAULT NULL COMMENT '目标类型，0：entity，1：property'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '三元组关系表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
