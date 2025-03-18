-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: faculdade
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aluno`
--

DROP TABLE IF EXISTS `aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno` (
  `nome` varchar(255) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `matricula` varchar(10) NOT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aluno`
--

LOCK TABLES `aluno` WRITE;
/*!40000 ALTER TABLE `aluno` DISABLE KEYS */;
INSERT INTO `aluno` VALUES ('Lucas Pereira','2001-05-14','1001','Rua A, 123'),('Fernanda Lima','2002-03-05','1002','Rua B, 456'),('Gustavo Martins','2003-07-22','1003','Avenida C, 789'),('Beatriz Oliveira','2002-11-15','1004','Rua D, 101'),('Ricardo Alves','2001-01-09','1005','Rua E, 202'),('Roberta Costa','2000-09-14','1006','Avenida F, 303'),('Larissa Costa','2003-02-19','1007','Rua G, 404'),('Mariana Ribeiro','2001-05-20','1008','Rua H, 505'),('Paulo Souza','2001-04-10','1009','Rua I, 606'),('João Pereira','2002-07-25','1010','Rua J, 707'),('Juliana Oliveira','2001-11-30','1011','Avenida K, 808'),('Fernanda Costa','2003-01-15','1012','Rua L, 909'),('Gabriela Mendes','2002-09-28','1013','Rua M, 110'),('Ricardo Costa','2002-12-03','1014','Rua N, 120'),('Marcos Silva','2001-03-21','1015','Avenida O, 130'),('Isabela Pereira','2002-02-11','1016','Rua P, 140'),('Bruna Santos','2001-07-02','1017','Rua Q, 150'),('Carlos Eduardo','2003-05-30','1018','Avenida R, 160'),('Ana Carolina','2001-08-25','1019','Rua S, 170'),('Tiago Lima','2002-12-01','1020','Rua T, 180'),('Felipe Almeida','2001-04-07','1021','Avenida U, 190'),('Amanda Ramos','2003-10-12','1022','Rua V, 200'),('Daniel Silva','2002-01-17','1023','Rua W, 210'),('Vitoria Costa','2001-10-28','1024','Rua X, 220'),('Ricardo Santos','2002-05-11','1025','Rua Y, 230'),('Leonardo Rocha','2002-04-13','1026','Avenida Z, 240'),('Camila Lima','2003-07-20','1027','Rua AA, 250'),('Marcio Alves','2002-06-15','1028','Rua BB, 260'),('Sophia Santos','2002-10-23','1029','Rua CC, 270'),('Eduardo Costa','2003-04-01','1030','Rua DD, 280');
/*!40000 ALTER TABLE `aluno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aluno_disciplina`
--

DROP TABLE IF EXISTS `aluno_disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno_disciplina` (
  `matricula` varchar(10) NOT NULL,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`matricula`,`nome`),
  KEY `nome` (`nome`),
  CONSTRAINT `aluno_disciplina_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `aluno` (`matricula`),
  CONSTRAINT `aluno_disciplina_ibfk_2` FOREIGN KEY (`nome`) REFERENCES `disciplina` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aluno_disciplina`
--

LOCK TABLES `aluno_disciplina` WRITE;
/*!40000 ALTER TABLE `aluno_disciplina` DISABLE KEYS */;
INSERT INTO `aluno_disciplina` VALUES ('1001','Artes'),('1016','Artes'),('1002','Biologia'),('1017','Biologia'),('1004','Educação Física'),('1019','Educação Física'),('1005','Filosofia'),('1020','Filosofia'),('1006','Física'),('1021','Física'),('1008','Geografia'),('1023','Geografia'),('1009','História'),('1010','História'),('1024','História'),('1025','História'),('1011','Inglês'),('1026','Inglês'),('1007','Matemática'),('1012','Matemática'),('1022','Matemática'),('1027','Matemática'),('1013','Português'),('1028','Português'),('1003','Química'),('1014','Química'),('1018','Química'),('1029','Química'),('1015','Sociologia'),('1030','Sociologia');
/*!40000 ALTER TABLE `aluno_disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avaliacao`
--

DROP TABLE IF EXISTS `avaliacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avaliacao` (
  `prof_cpf` varchar(11) NOT NULL,
  `data_hora` datetime NOT NULL,
  `comentario` varchar(500) DEFAULT NULL,
  `nota` int DEFAULT NULL,
  PRIMARY KEY (`prof_cpf`,`data_hora`),
  CONSTRAINT `avaliacao_ibfk_1` FOREIGN KEY (`prof_cpf`) REFERENCES `professor` (`cpf`),
  CONSTRAINT `avaliacao_chk_1` CHECK (((`nota` <= 10) and (`nota` >= 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avaliacao`
--

LOCK TABLES `avaliacao` WRITE;
/*!40000 ALTER TABLE `avaliacao` DISABLE KEYS */;
INSERT INTO `avaliacao` VALUES ('11223344556','2025-03-13 08:30:00','Aula excelente, mas achei um pouco rápida.',9),('11223344556','2025-03-14 10:00:00','A aula foi boa, mas as explicações poderiam ser mais lentas.',7),('11223344556','2025-03-15 11:30:00','Muito bom, adorei a interação e os exemplos práticos.',10),('11223344556','2025-03-16 13:00:00','A aula foi boa, mas o conteúdo foi um pouco difícil de entender.',6),('12345678901','2025-03-13 10:00:00','O conteúdo foi bom, mas o professor poderia ter explicado mais detalhadamente.',7),('12345678901','2025-03-14 11:30:00','Achei o conteúdo bom, mas senti falta de mais exemplos práticos.',8),('12345678901','2025-03-15 13:00:00','A aula foi interessante, mas não consegui acompanhar em alguns momentos.',5),('12345678901','2025-03-17 08:30:00','Muito interessante, o professor explicou bem, mas senti falta de mais exercícios.',8),('22334455678','2025-03-13 11:30:00','Muito interessante, mas algumas partes poderiam ser mais dinâmicas.',8),('22334455678','2025-03-14 13:00:00','Difícil de entender, algumas explicações não ficaram claras.',4),('22334455678','2025-03-16 08:30:00','Gostei muito do conteúdo, mas a explicação foi um pouco rápida.',8),('22334455678','2025-03-17 10:00:00','A aula foi boa, mas achei o ritmo muito rápido para absorver tudo.',7),('33445566789','2025-03-13 13:00:00','Fiquei um pouco perdido em algumas partes, mas no geral foi boa.',6),('33445566789','2025-03-15 08:30:00','Excelente aula, aprendi bastante, mas o tempo foi curto.',9),('33445566789','2025-03-16 10:00:00','Foi uma boa aula, mas algumas partes poderiam ter mais detalhes.',7),('33445566789','2025-03-17 11:30:00','Aula boa, mas o conteúdo poderia ser mais detalhado.',6),('98765432100','2025-03-14 08:30:00','Adorei a aula, muito bem explicada e com exemplos claros.',10),('98765432100','2025-03-15 10:00:00','Conteúdo bom, mas a aula foi um pouco monótona.',6),('98765432100','2025-03-16 11:30:00','Muito bom, gostei da abordagem prática e teórica.',9),('98765432100','2025-03-17 13:00:00','Achei difícil de entender, precisava de mais explicações e exemplos.',5);
/*!40000 ALTER TABLE `avaliacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `local` varchar(255) DEFAULT NULL,
  `prof_chefe_cpf` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prof_chefe_cpf` (`prof_chefe_cpf`),
  CONSTRAINT `departamento_ibfk_1` FOREIGN KEY (`prof_chefe_cpf`) REFERENCES `professor` (`cpf`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Exatas','Bloco A','12345678901'),(2,'Linguagens','Bloco B',NULL),(3,'Natureza','Bloco C',NULL),(4,'Humanas','Bloco D',NULL);
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina` (
  `nome` varchar(100) NOT NULL,
  `carga_horaria` int NOT NULL DEFAULT '30',
  `ementa` text,
  `disc_pre_requisito` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`nome`),
  KEY `disc_pre_requisito` (`disc_pre_requisito`),
  CONSTRAINT `disciplina_ibfk_1` FOREIGN KEY (`disc_pre_requisito`) REFERENCES `disciplina` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina`
--

LOCK TABLES `disciplina` WRITE;
/*!40000 ALTER TABLE `disciplina` DISABLE KEYS */;
INSERT INTO `disciplina` VALUES ('Artes',40,'Expressão artística, história da arte e atividades práticas',NULL),('Biologia',80,'Estudos sobre organismos, células e genética','Química'),('Educação Física',40,'Atividades físicas, esportes e saúde',NULL),('Filosofia',40,'Pensamento filosófico e história da filosofia',NULL),('Física',80,'Leis da física, experimentos e cálculos','Matemática'),('Geografia',60,'Estudo do espaço geográfico e suas transformações','História'),('História',60,'História antiga, moderna e contemporânea',NULL),('Inglês',50,'Leitura, escrita e conversação em inglês',NULL),('Matemática',60,'Cálculos, álgebra, geometria e trigonometria',NULL),('Português',50,'Gramática, literatura e interpretação de textos',NULL),('Química',70,'Reações químicas, tabela periódica e composição das substâncias',NULL),('Sociologia',40,'Estudo das sociedades, cultura e comportamento social',NULL);
/*!40000 ALTER TABLE `disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor` (
  `inicio_contrato` date DEFAULT NULL,
  `nome` varchar(255) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `depto_id` int DEFAULT NULL,
  PRIMARY KEY (`cpf`),
  KEY `depto_id` (`depto_id`),
  CONSTRAINT `professor_ibfk_1` FOREIGN KEY (`depto_id`) REFERENCES `departamento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES ('2020-03-10','Carlos Souza','11223344556',NULL),('2022-02-01','João Silva','12345678901',NULL),('2019-07-20','Patrícia Santos','22334455678',NULL),('2023-01-15','Ricardo Oliveira','33445566789',NULL),('2021-08-15','Maria Oliveira','98765432100',NULL);
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor_contato`
--

DROP TABLE IF EXISTS `professor_contato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor_contato` (
  `prof_cpf` varchar(11) NOT NULL,
  `contato` varchar(14) NOT NULL,
  PRIMARY KEY (`prof_cpf`,`contato`),
  CONSTRAINT `professor_contato_ibfk_1` FOREIGN KEY (`prof_cpf`) REFERENCES `professor` (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor_contato`
--

LOCK TABLES `professor_contato` WRITE;
/*!40000 ALTER TABLE `professor_contato` DISABLE KEYS */;
INSERT INTO `professor_contato` VALUES ('11223344556','31987654321'),('12345678901','11987654321'),('22334455678','41987654321'),('33445566789','51987654321'),('98765432100','21987654321');
/*!40000 ALTER TABLE `professor_contato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor_disciplina`
--

DROP TABLE IF EXISTS `professor_disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor_disciplina` (
  `cpf` varchar(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`cpf`,`nome`),
  KEY `nome` (`nome`),
  CONSTRAINT `professor_disciplina_ibfk_1` FOREIGN KEY (`cpf`) REFERENCES `professor` (`cpf`),
  CONSTRAINT `professor_disciplina_ibfk_2` FOREIGN KEY (`nome`) REFERENCES `disciplina` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor_disciplina`
--

LOCK TABLES `professor_disciplina` WRITE;
/*!40000 ALTER TABLE `professor_disciplina` DISABLE KEYS */;
INSERT INTO `professor_disciplina` VALUES ('98765432100','Artes'),('33445566789','Biologia'),('12345678901','Educação Física'),('11223344556','Filosofia'),('11223344556','Física'),('22334455678','Física'),('98765432100','Geografia'),('33445566789','História'),('12345678901','Inglês'),('11223344556','Matemática'),('12345678901','Matemática'),('98765432100','Português'),('22334455678','Química'),('33445566789','Química'),('22334455678','Sociologia');
/*!40000 ALTER TABLE `professor_disciplina` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-11  8:56:41
