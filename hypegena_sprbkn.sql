-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 28, 2022 at 04:59 PM
-- Server version: 8.0.28
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hypegena_sprbkn`
--

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE `file` (
  `ID` int NOT NULL,
  `tc_no` varchar(255) NOT NULL,
  `file_url` varchar(255) NOT NULL,
  `kayit_date` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`ID`, `tc_no`, `file_url`, `kayit_date`) VALUES
(23, '45124514272', './static/uploads/plantCellSignalingData.txt', '2021-12-27 00:47:42');

-- --------------------------------------------------------

--
-- Table structure for table `grub_user`
--

CREATE TABLE `grub_user` (
  `id` int NOT NULL,
  `ad_soyad` varchar(255) NOT NULL,
  `oda_numarasi` int NOT NULL,
  `grup_durumu` tinyint(1) NOT NULL,
  `date1` datetime NOT NULL,
  `date2` datetime NOT NULL,
  `kayit_tarihi` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `imza_file`
--

CREATE TABLE `imza_file` (
  `imzaID` int NOT NULL,
  `imza_tc` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `imza_file` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `imza_file`
--

INSERT INTO `imza_file` (`imzaID`, `imza_tc`, `imza_file`) VALUES
(75, '45124514286', './app/static/imza_uploader/45124514286_2021-12-26 20:41:0.png'),
(74, '4512451428ABC', './static/imza_uploader/4512451428ABC_2021-12-23 23:36:1.png'),
(73, '45124514211', './static/imza_uploader/45124514211_2021-12-23 23:25:3.png'),
(72, '45124514286', './static/imza_uploader/45124514286_2021-12-23 23:25:1.png'),
(71, '42571787584', './static/imza_uploader/42571787584_2021-12-15 11:33:0.png');

-- --------------------------------------------------------

--
-- Table structure for table `kayit_formu`
--

CREATE TABLE `kayit_formu` (
  `kayitID` int NOT NULL,
  `giris_tarihi` date NOT NULL,
  `cikis_tarihi` date NOT NULL,
  `oda_numarasi` int NOT NULL,
  `kisiID` int NOT NULL,
  `resepsiyon_notu` varchar(500) NOT NULL,
  `grup_durumu` tinyint(1) NOT NULL,
  `yemek_durumu` tinyint(1) NOT NULL,
  `kayit_tarihi` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kayit_formu`
--

INSERT INTO `kayit_formu` (`kayitID`, `giris_tarihi`, `cikis_tarihi`, `oda_numarasi`, `kisiID`, `resepsiyon_notu`, `grup_durumu`, `yemek_durumu`, `kayit_tarihi`) VALUES
(94, '2021-12-05', '2021-12-28', 3213222, 120, 'testxx', 1, 1, '2021-12-23'),
(95, '2021-12-23', '2021-12-24', 123, 121, 'ASDADSA', 1, 1, '2021-12-23'),
(96, '2021-12-23', '2021-12-24', 12321, 121, 'ASDDSAS', 1, 1, '2021-12-23'),
(97, '2021-12-05', '2021-12-28', 3213222, 120, 'testxx', 1, 1, '2021-12-26'),
(98, '2021-12-27', '2021-12-29', 123, 125, 'xx', 1, 1, '2021-12-27'),
(101, '2021-12-27', '2021-12-28', 123, 128, 'xxx', 1, 1, '2021-12-27'),
(102, '2021-12-28', '2021-12-28', 1212, 120, 'xx', 1, 1, '2021-12-28'),
(103, '2021-12-28', '2021-12-28', 1231, 120, 'xxx', 1, 1, '2021-12-28'),
(104, '2021-12-28', '2021-12-29', 111, 120, '0', 1, 1, '2021-12-28'),
(105, '2021-12-27', '2022-01-03', 111, 120, 'xx', 1, 1, '2021-12-28'),
(106, '2021-12-28', '2021-12-29', 12, 137, 'GRUP MİSAFİR', 1, 1, '2021-12-28'),
(107, '2021-12-28', '2021-12-29', 11, 141, 'GRUP MİSAFİR', 1, 1, '2021-12-28'),
(108, '2021-12-28', '2021-12-29', 3055, 142, 'son test', 1, 1, '2021-12-28'),
(109, '2021-12-28', '2021-12-30', 21, 144, 'test2', 1, 1, '2021-12-28'),
(110, '2021-12-28', '2021-12-30', 21, 145, 'GRUP MİSAFİR', 1, 1, '2021-12-28'),
(111, '2021-12-28', '2021-12-29', 22, 146, 'xxx', 1, 1, '2021-12-28'),
(112, '2021-12-28', '2021-12-29', 22, 147, 'GRUP MİSAFİR', 1, 1, '2021-12-28'),
(113, '2022-02-04', '2022-02-11', 123, 120, 'xx', 1, 1, '2022-02-04'),
(114, '2022-02-10', '2022-02-11', 11, 120, 'a', 1, 1, '2022-02-09');

-- --------------------------------------------------------

--
-- Table structure for table `kisisel_bilgiler`
--

CREATE TABLE `kisisel_bilgiler` (
  `kisiID` int NOT NULL,
  `ad_soyad` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tcno` varchar(11) NOT NULL,
  `meslek` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tel` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `plaka` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `kamu_durumu` tinyint(1) NOT NULL,
  `mail` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `sicil_numarasi` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `data_url` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kisisel_bilgiler`
--

INSERT INTO `kisisel_bilgiler` (`kisiID`, `ad_soyad`, `tcno`, `meslek`, `tel`, `plaka`, `kamu_durumu`, `mail`, `sicil_numarasi`, `data_url`) VALUES
(119, 'Emre Yıldız', '42571787584', 'Bilgisayar Mühendisi', '5418629190', '34EY3434', 0, 'admin', '', './static/database_ıd/42571787584.png'),
(120, 'Emre Yıldız', '45124514286', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514286.png'),
(121, 'Emre Yıldız', '45124514211', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', ''),
(122, 'Emre Yıldız', '45124514211', 'MİSAFİR', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514211.png'),
(123, 'Emre Yıldız', '4512451428A', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/4512451428ABC.png'),
(124, 'Emre Yıldız', '45124514286', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514286.png'),
(125, 'Emre Yıldız', '45124514273', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514273.png'),
(126, 'Emre Yıldız', '45124514272', 'evv', '11111', '11111', 0, 'admin', '1111', ''),
(127, 'Emre Yıldız', '45124514272', 'evv', '11111', '11111', 0, 'admin', '1111', './static/database_ıd/45124514272.png'),
(128, 'Emre Yıldız', '45124514121', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514121.png'),
(129, 'Emre Yıldız', '45124514286', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514286.png'),
(130, 'Emre Yıldız', '45124514286', 'SİVİL', '5434124123', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514286.png'),
(131, 'Emre Yıldız', '45124514286', '0', '0', '0', 0, 'admin', '0', ''),
(132, 'Emre Yıldız', '45124514286', 'MİSAFİR', '0', '0', 0, 'admin', '0', ''),
(133, 'Emre Yıldız', '45124514286', 'MİSAFİR', '0', '0', 0, 'admin', '0', ''),
(134, 'MERVE KURUCAK', '45124514286', 'MİSAFİR', '0', '0', 0, 'admin', '0', './static/database_ıd/45124514286.png'),
(135, 'emre yıldız', '45124514299', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(136, 'MERVE KURUCAK', '45124514212', 'MİSAFİR', '0', '0', 0, 'admin', '0', './static/database_ıd/451245142123.png'),
(137, 'Ali Gökkaya', '41234567897', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(138, 'MERYEM DED', '45124514211', 'MİSAFİR', '5418629190', '11111', 0, 'admin', '', './static/database_ıd/451245142111.png'),
(139, 'Ali Gökkaya', '45198765111', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(140, 'MERVE KURUCAK', '45124514286', 'MİSAFİR', '0', '0', 0, 'admin', '0', './static/database_ıd/4512451428612.png'),
(141, 'NİMET ÖZDEMİR', '34567891234', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(142, 'MERVE KURUCAK', '45124514010', 'MİSAFİR', '0', '0', 0, 'admin', '0', ''),
(143, 'ABDURRAHMAN GÖKKAYA', '45198765111', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(144, 'KAFİYE XX1', '45196511800', 'ev hanımı', '5555555', '0000', 0, 'admin', '', ''),
(145, 'ABDURRAHMAN YILDIZ', '45196511801', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(146, 'ABDURRAHMAN2 YILDIZ', '45196511802', 'MİSAFİR', '-', '-', 0, 'admin', '-', ''),
(147, 'FATİH ŞAHİN', '45196511803', 'MİSAFİR', '-', '-', 1, '-', '-', '-'),
(148, 'Emre Yıldız', '45124514286', 'Bilgisayar Mühendisi', '5418629190', '31AKP31', 0, 'admin', '', './static/database_ıd/45124514286.png'),
(149, 'EMRE YILDIZ', '45124514286', 'Bilgisayar Mühendisi', '5418629190', '31AKP31', 0, 'admin', '987654331', '');

-- --------------------------------------------------------

--
-- Table structure for table `makbuz`
--

CREATE TABLE `makbuz` (
  `makbuzID` int NOT NULL,
  `tarih` date NOT NULL,
  `oda_numarasi` int NOT NULL,
  `ad_soyad` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `vd_no` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tahsilat_sekli` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tutar_sayi` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `tutar_yazi` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `aciklama` varchar(500) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `görevli_adi` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `makbuz`
--

INSERT INTO `makbuz` (`makbuzID`, `tarih`, `oda_numarasi`, `ad_soyad`, `vd_no`, `tahsilat_sekli`, `tutar_sayi`, `tutar_yazi`, `aciklama`, `görevli_adi`) VALUES
(67, '2021-12-27', 1, 'EMRE YILDIZ', '99', 'KK', '1111111111', 'BirMilyarYüzOnBirMilyonYüzOnBirBinYüzOnBir', 'x', 'x'),
(66, '2021-12-27', 101, 'EMRE YILDIZ', '45124514286', 'KK', '12500', 'OnİkiBinBeşYüz', 'X', 'X'),
(65, '2021-12-27', 1, 'EMRE YILDIZ', '99', 'KK', '1111111111', 'BirMilyarYüzOnBirMilyonYüzOnBirBinYüzOnBir', 'sadsdas', 'MERVE '),
(64, '2021-12-27', 1, 'EMRE YILDIZ', '99', 'kk', '10000', 'OnBin', 'evet', 'hayr'),
(63, '2021-12-27', 1, 'EMRE YILDIZ', '99', 'KK', '1111111111', 'BirMilyarYüzOnBirMilyonYüzOnBirBinYüzOnBir', 'asd', 'saddsadas'),
(62, '2021-12-23', 111, 'ali', '432', 'nakit', '1111', 'BinYüzOnBir', 'ödeme alınacak', 'merve'),
(61, '2021-11-29', 213, 'ali', '432', 'nakit', '2342', 'İkiBinÜçYüzKırkİki', '2342', '2342'),
(60, '2021-12-14', 123, 'ali', '432', 'nakit', '2342', 'İkiBinÜçYüzKırkİki', 'edre', 'ali'),
(59, '2021-12-23', 1, 'EMRE YILDIZ', '99', 'KK', '1000', 'Bin', '19.112021-20.11.2021 TARİHLERİ ARASINDA KONAKLAMA BEDELİ', 'MERVE ');

-- --------------------------------------------------------

--
-- Table structure for table `old_reminder`
--

CREATE TABLE `old_reminder` (
  `id` int NOT NULL,
  `text` varchar(255) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reminder`
--

CREATE TABLE `reminder` (
  `id` int NOT NULL,
  `text` varchar(255) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userID` int NOT NULL,
  `username` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `password` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `mail` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `name_surname` varchar(256) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `yetki` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userID`, `username`, `password`, `mail`, `name_surname`, `yetki`) VALUES
(1, 'admin', 'admin', 'admin@info.com', 'yönetici', 1),
(2, 'kullanıcı1', 'kullanıcı1', 'kullanici@gmail.com', 'admin', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `file`
--
ALTER TABLE `file`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `grub_user`
--
ALTER TABLE `grub_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `imza_file`
--
ALTER TABLE `imza_file`
  ADD PRIMARY KEY (`imzaID`);

--
-- Indexes for table `kayit_formu`
--
ALTER TABLE `kayit_formu`
  ADD PRIMARY KEY (`kayitID`),
  ADD KEY `kisiID` (`kisiID`);

--
-- Indexes for table `kisisel_bilgiler`
--
ALTER TABLE `kisisel_bilgiler`
  ADD PRIMARY KEY (`kisiID`);

--
-- Indexes for table `makbuz`
--
ALTER TABLE `makbuz`
  ADD PRIMARY KEY (`makbuzID`);

--
-- Indexes for table `old_reminder`
--
ALTER TABLE `old_reminder`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reminder`
--
ALTER TABLE `reminder`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `file`
--
ALTER TABLE `file`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `grub_user`
--
ALTER TABLE `grub_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `imza_file`
--
ALTER TABLE `imza_file`
  MODIFY `imzaID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `kayit_formu`
--
ALTER TABLE `kayit_formu`
  MODIFY `kayitID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=115;

--
-- AUTO_INCREMENT for table `kisisel_bilgiler`
--
ALTER TABLE `kisisel_bilgiler`
  MODIFY `kisiID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=150;

--
-- AUTO_INCREMENT for table `makbuz`
--
ALTER TABLE `makbuz`
  MODIFY `makbuzID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT for table `old_reminder`
--
ALTER TABLE `old_reminder`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `reminder`
--
ALTER TABLE `reminder`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=133;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kayit_formu`
--
ALTER TABLE `kayit_formu`
  ADD CONSTRAINT `kayit_formu_ibfk_2` FOREIGN KEY (`kisiID`) REFERENCES `kisisel_bilgiler` (`kisiID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
