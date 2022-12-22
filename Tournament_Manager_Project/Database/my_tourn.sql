-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema my_tourn
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema my_tourn
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `my_tourn` DEFAULT CHARACTER SET utf8 ;
USE `my_tourn` ;

-- -----------------------------------------------------
-- Table `my_tourn`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_tourn`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` CHAR(60) NULL,
  `is_manager` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_tourn`.`teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_tourn`.`teams` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `team_name` VARCHAR(45) NULL,
  `team_mascot` VARCHAR(45) NULL,
  `team_city` VARCHAR(45) NULL,
  `team_state` CHAR(2) NULL,
  `team_wins` INT NULL,
  `team_losses` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_tourn`.`tournaments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_tourn`.`tournaments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `seeds` INT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_tournaments_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tournaments_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `my_tourn`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_tourn`.`games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_tourn`.`games` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `venue` VARCHAR(45) NULL,
  `game_date` DATE NULL,
  `game_time` TIME NULL,
  `winner` VARCHAR(45) NULL,
  `loser` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tournament_id` INT NOT NULL,
  `tournament_user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_games_tournaments1_idx` (`tournament_id` ASC, `tournament_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_games_tournaments1`
    FOREIGN KEY (`tournament_id` , `tournament_user_id`)
    REFERENCES `my_tourn`.`tournaments` (`id` , `user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_tourn`.`teams_has_games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_tourn`.`teams_has_games` (
  `team_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  `is_winner` TINYINT NULL,
  PRIMARY KEY (`team_id`, `game_id`),
  INDEX `fk_teams_has_games_games1_idx` (`game_id` ASC) VISIBLE,
  INDEX `fk_teams_has_games_teams1_idx` (`team_id` ASC) VISIBLE,
  CONSTRAINT `fk_teams_has_games_teams1`
    FOREIGN KEY (`team_id`)
    REFERENCES `my_tourn`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_teams_has_games_games1`
    FOREIGN KEY (`game_id`)
    REFERENCES `my_tourn`.`games` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
