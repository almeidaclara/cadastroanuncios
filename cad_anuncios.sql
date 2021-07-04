-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 05-Jul-2021 às 00:20
-- Versão do servidor: 10.4.19-MariaDB
-- versão do PHP: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `anuncios`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cad_anuncios`
--

CREATE TABLE IF NOT EXISTS `cad_anuncios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `cliente` varchar(20) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  `data_fim` date DEFAULT NULL,
  `invest_dia` decimal(10,0) DEFAULT NULL,
  `qt_dias` decimal(10,0) DEFAULT NULL,
  `invest_tot` decimal(10,0) DEFAULT NULL,
  `qt_visu` int(11) DEFAULT NULL,
  `qt_clique` int(11) DEFAULT NULL,
  `qt_comp` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `cad_anuncios`
--

INSERT INTO `cad_anuncios` (`id`, `nome`, `cliente`, `data_inicio`, `data_fim`, `invest_dia`, `qt_dias`, `invest_tot`, `qt_visu`, `qt_clique`, `qt_comp`) VALUES
(1, 'anuncio1', 'cliente1', '2000-01-01', '2000-02-01', '2', '31', '62', 4858, 583, 75),
(2, 'anuncio2', 'cliente2', '2000-01-01', '2001-01-01', '1', '366', '366', 28676, 3441, 442),
(3, 'anuncio3', 'empresa3', '2020-02-02', '2020-02-04', '4', '2', '8', 627, 75, 10);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
