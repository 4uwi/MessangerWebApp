-- MariaDB dump 10.19  Distrib 10.5.12-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: messenger
-- ------------------------------------------------------
-- Server version	10.5.12-MariaDB

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
`id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'id of the message',
`id_sender` int(10) NOT NULL COMMENT 'id of the message sender',
`id_receiver` int(10) NOT NULL COMMENT 'id of the message receiver',
`datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'date and time the message was sent',
`text` varchar(255) DEFAULT NULL COMMENT 'Contains the message text',
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;


--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'Id number of user',
  `login` varchar(63) NOT NULL COMMENT 'Login aka name of the user',
  `password` varchar(25) NOT NULL COMMENT 'Password from the account of user',
  `name` varchar(255) DEFAULT NULL COMMENT 'User name to show',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='Users of messenger';

-- Dump completed on 2021-10-19  7:59:10
