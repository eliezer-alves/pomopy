import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')


conn.cursor().execute("DROP DATABASE IF EXISTS `pomopy`;")
conn.commit()

criar_tabelas = '''

-- MySQL Script generated by MySQL Workbench
-- Sun Oct 24 20:27:03 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pomopy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pomopy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pomopy` DEFAULT CHARACTER SET utf8 ;
USE `pomopy` ;

-- -----------------------------------------------------
-- Table `pomopy`.`achievements`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`achievements` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`achievements` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NULL,
  `icon` VARCHAR(500) NULL,
  PRIMARY KEY (`id`, `name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pomopy`.`cycles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`cycles` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`cycles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `duration_in_minutes` INT NULL,
  `status` TINYINT NULL DEFAULT 0,
  `tags_id` INT NOT NULL,
  `tasks_id` INT NULL DEFAULT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `tags_id`, `users_id`),
  INDEX `fk_cycles_tags1_idx` (`tags_id` ASC) VISIBLE,
  INDEX `fk_cycles_tasks1_idx` (`tasks_id` ASC) VISIBLE,
  INDEX `fk_cycles_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_cycles_tags1`
    FOREIGN KEY (`tags_id`)
    REFERENCES `pomopy`.`tags` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cycles_tasks1`
    FOREIGN KEY (`tasks_id`)
    REFERENCES `pomopy`.`tasks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cycles_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `pomopy`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pomopy`.`groups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`groups` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pomopy`.`tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`tags` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pomopy`.`tasks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`tasks` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(500) NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`),
  INDEX `fk_tasks_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_tasks_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `pomopy`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pomopy`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`users` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(15) CHARACTER SET 'ascii' NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `groups_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_groups_idx` (`groups_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_groups`
    FOREIGN KEY (`groups_id`)
    REFERENCES `pomopy`.`groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pomopy`.`users_has_achievements`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pomopy`.`users_has_achievements` ;

CREATE TABLE IF NOT EXISTS `pomopy`.`users_has_achievements` (
  `users_idusers` INT NOT NULL,
  `achievements_id` INT NOT NULL,
  PRIMARY KEY (`users_idusers`, `achievements_id`),
  INDEX `fk_users_has_achievements_achievements1_idx` (`achievements_id` ASC) VISIBLE,
  INDEX `fk_users_has_achievements_users1_idx` (`users_idusers` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_achievements_users1`
    FOREIGN KEY (`users_idusers`)
    REFERENCES `pomopy`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_achievements_achievements1`
    FOREIGN KEY (`achievements_id`)
    REFERENCES `pomopy`.`achievements` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


    '''

conn.cursor().execute(criar_tabelas)
conn.commit()
conn.cursor.close()