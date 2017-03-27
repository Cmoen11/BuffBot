/*
Navicat SQLite Data Transfer

Source Server         : db
Source Server Version : 31300
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 31300
File Encoding         : 65001

Date: 2017-03-27 14:16:06
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for game_restriction
-- ----------------------------
DROP TABLE IF EXISTS "main"."game_restriction";
CREATE TABLE "game_restriction" (
"channel_ID"  varchar NOT NULL,
"title"  TEXT NOT NULL,
"allowed"  INTEGER NOT NULL,
PRIMARY KEY ("channel_ID" ASC, "title")
);
PRAGMA foreign_keys = ON;
