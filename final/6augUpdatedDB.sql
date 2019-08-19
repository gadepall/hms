-- MySQL dump 10.15  Distrib 10.0.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: shd_hospital
-- ------------------------------------------------------
-- Server version	10.0.38-MariaDB-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_addpanel`
--

DROP TABLE IF EXISTS `admin_addpanel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_addpanel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) DEFAULT NULL,
  `panel_name` varchar(20) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_addpanel`
--

LOCK TABLES `admin_addpanel` WRITE;
/*!40000 ALTER TABLE `admin_addpanel` DISABLE KEYS */;
INSERT INTO `admin_addpanel` VALUES (1,1,'LFT TEST',0),(2,1,'LIPID PROFILE TEST',0),(3,1,'KFT TEST',0),(4,1,'PROTHOMBIN TEST',0),(5,1,'THYROID FUNCTION TES',0),(6,1,'ELECTROLYTES TEST',0),(7,5,'CSF FLUID',0),(8,6,'SUGAR',0),(9,6,'OCCULT BLOOD',0);
/*!40000 ALTER TABLE `admin_addpanel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_addsample`
--

DROP TABLE IF EXISTS `admin_addsample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_addsample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sample_name` varchar(20) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_addsample`
--

LOCK TABLES `admin_addsample` WRITE;
/*!40000 ALTER TABLE `admin_addsample` DISABLE KEYS */;
INSERT INTO `admin_addsample` VALUES (1,'SERUM',0),(2,'BLOOD',0),(3,'URINE',0),(4,'PLASMA',0),(5,'FLUID',0),(6,'STOOL',0);
/*!40000 ALTER TABLE `admin_addsample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_addtest`
--

DROP TABLE IF EXISTS `admin_addtest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_addtest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `test_name` varchar(20) DEFAULT NULL,
  `Male_Range_min` varchar(10) DEFAULT NULL,
  `Male_Range_max` varchar(10) DEFAULT NULL,
  `Female_Range_min` varchar(20) DEFAULT NULL,
  `Female_Range_max` varchar(20) DEFAULT NULL,
  `Unit` varchar(10) DEFAULT NULL,
  `amount` varchar(10) DEFAULT '0',
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_addtest`
--

LOCK TABLES `admin_addtest` WRITE;
/*!40000 ALTER TABLE `admin_addtest` DISABLE KEYS */;
INSERT INTO `admin_addtest` VALUES (1,1,1,'SGOT','00','46','00','46','I/U','60',0),(2,1,1,'SGPT','00','49','00','49','I/U','60',0),(3,1,1,'ALK PHOSPHATE','80','306','64','306','I/U','60',0),(4,1,1,'BILLI T','00','1.2','00','1.2','mg/dl','30',0),(5,1,1,'BILLI D','00','0.4','00','0.4','mg/dl','30',0),(6,1,1,'HBSAG','NEGATIVE','NEGATIVE','NEGATIVE','NEGATIVE',' -','60',0),(7,1,2,'CHO','-','-','-','-','mg/dl','80',0),(8,1,2,'TG','60','165','60','165','mg/dl','80',0),(9,1,2,'HDL','35','80','42','88','mg/dl','120',0),(10,1,2,'LDL','50','130','50','130','mg/dl','120',0),(11,1,3,'UREA','20','40','20','40','mg/dl','50',0),(12,1,3,'CREAT','0.6','1.1','0.5','0.8','mg/dl','50',0),(13,1,4,'PT TEST','11','13.5','11','13.5','SEC.','100',0),(14,1,4,'INR','0.8','1.1','0.8','1.1','-','50',0),(15,1,4,'20 MIN. CLOTTING TIM','20 MIN','20 MIN','20 MIN','20 MIN','-','20',0),(16,1,5,'T3','60','150','60','150','ng/dl','150',0),(17,1,5,'T4','4.66','9.33','4.66','9.33','ug/dl','150',0),(18,1,5,'TSH','0.25','5.5','0.25','5.5','uU/ml','150',0),(19,1,6,'Na','135','145','135','145','mmol/L','50',0),(20,1,6,'K','3.5','5.5','3.5','5.5','mmol/L','50',0),(21,1,6,'CL','90','115','90','115','mmol/L','50',0),(22,2,0,'HB','13.8','17.1','12.1','15.0','%','20',0),(23,2,0,'BLOOD GROUP','-','-','-','-','-','30',0),(24,2,0,'TLC','4000','11000','4000','11000','/CUMM','20',0),(25,2,0,'AEC','100','600','100','600','/CUMM','20',0),(26,2,0,'PLATELET','150000','450000','150000','450000','/CUMM','20',0),(27,2,0,'ESR','<10','<10','<15','<15','mm/1st Hr.','20',0),(28,2,0,'HBA1C','4.6','6.2','4.6','6.2','%','300',0),(29,2,0,'HB ELECTROPHORESIS','-','-','-','-','-','400',0),(30,2,0,'MP QBC','-','-','-','-','-','200',0),(31,2,0,'SICKLING','-','-','-','-','-','20',0),(32,2,0,'CBC','-','-','-','-','-','100',0),(33,2,0,'MP ','-','-','-','-','-','20',0),(34,2,0,'PS ANEMIA','-','-','-','-','-','40',0),(35,2,0,'BT','2','5','2','5','Minute','10',0),(36,2,0,'CT','4','7','4','7','Minute','10',0),(37,1,0,'FBS','60','110','60','110','mg/dl','50',0),(38,1,0,'PPBS','70','140','70','140','mg/dl','50',0),(39,1,0,'RBS','70','120','70','120','mg/dl','50',0),(40,0,0,'B.UREA','10','45','10','45','mg/dl','50',0),(41,1,0,'S.CREAT','0.6','1.1','0.5','0.8','mg/dl','50',0),(42,1,0,'URIC ACID','3.6','7.7','2.5','6.8','mg/dl','70',0),(43,1,0,'TOTAL PROTIEN','6.2','8.0','6.2','8.0','gm/dl','70',0),(44,1,0,'S.ALBUMIN','3.5','5.5','3.5','5.5','gm/dl','60',0),(45,1,0,'CALCIUM','8.8','10.2','8.8','10.2','mg/dl','80',0),(46,1,0,'S.AMYLASE','25','86','25','86','U/L','150',0),(47,1,0,'ASO','00','200','00','200','IU/ML','150',0),(48,1,0,'RA','00','20','00','20','IU/ML','150',0),(49,1,0,'CRP','00','06','00','06','IU/ML','150',0),(50,1,0,'HIV','-','-','-','-','-','100',0),(51,1,0,'VDRL','-','-','-','-','-','60',0),(52,1,0,'TPSA','0.2','6.7','0.2','6.7','ng/ml','400',0),(53,1,0,'TROPONIN','<1.5','19','<1.5','19','ng/l','500',0),(54,1,0,'ANA','-','-','-','-','-','500',0),(55,1,0,'TORCH','-','-','-','-','-','1500',0),(56,0,0,'HEPATITIS E','-','-','-','-','-','600',0),(57,3,0,'URINE SUGAR','-','-','-','-','-','20',0),(58,3,0,'URINE ALBUMINE','-','-','-','-','-','20',0),(59,3,0,'UPT','-','-','-','-','-','50',0),(60,3,0,'KETON BODY','-','-','-','-','-','20',0),(61,3,0,'URO BILLI','-','-','-','-','-','20',0),(62,3,0,'MICRO ALBUMINE',' 00','< 25','00','< 25','mg/dl','200',0),(63,1,0,'S.LIPASE','23','85','23','85','U/L','150',0),(64,3,0,'KETON BODY','-','-','-','-','-','20',0),(65,6,0,'SUGAR','..','..','..','..','..','20',0),(66,6,9,'OCCULT BLOOD','..','..','..','..','..','20',0);
/*!40000 ALTER TABLE `admin_addtest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_addtest_properties`
--

DROP TABLE IF EXISTS `admin_addtest_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_addtest_properties` (
  `tpid` int(11) NOT NULL AUTO_INCREMENT,
  `id` int(11) DEFAULT NULL,
  `tpname` varchar(30) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`tpid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_addtest_properties`
--

LOCK TABLES `admin_addtest_properties` WRITE;
/*!40000 ALTER TABLE `admin_addtest_properties` DISABLE KEYS */;
INSERT INTO `admin_addtest_properties` VALUES (1,1,'Size',0),(2,1,'color',0),(3,2,'SELF',0);
/*!40000 ALTER TABLE `admin_addtest_properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_company`
--

DROP TABLE IF EXISTS `admin_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_company` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(30) DEFAULT NULL,
  `deletestatus` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_company`
--

LOCK TABLES `admin_company` WRITE;
/*!40000 ALTER TABLE `admin_company` DISABLE KEYS */;
INSERT INTO `admin_company` VALUES (-3,'CMSS','-3'),(-2,'Staff','-2'),(-1,'General','-1'),(1,'Godawari','0'),(2,'Dalli','0'),(3,'Ravi Transport','0');
/*!40000 ALTER TABLE `admin_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_conAnomaly`
--

DROP TABLE IF EXISTS `admin_conAnomaly`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_conAnomaly` (
  `caid` int(11) NOT NULL AUTO_INCREMENT,
  `canomaly` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`caid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_conAnomaly`
--

LOCK TABLES `admin_conAnomaly` WRITE;
/*!40000 ALTER TABLE `admin_conAnomaly` DISABLE KEYS */;
INSERT INTO `admin_conAnomaly` VALUES (1,'Leg.'),(2,'Hand.');
/*!40000 ALTER TABLE `admin_conAnomaly` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_deathreason`
--

DROP TABLE IF EXISTS `admin_deathreason`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_deathreason` (
  `deathid` int(11) NOT NULL AUTO_INCREMENT,
  `deathreason` varchar(100) DEFAULT NULL,
  `deletestatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`deathid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_deathreason`
--

LOCK TABLES `admin_deathreason` WRITE;
/*!40000 ALTER TABLE `admin_deathreason` DISABLE KEYS */;
INSERT INTO `admin_deathreason` VALUES (1,'Heart Attack','0');
/*!40000 ALTER TABLE `admin_deathreason` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_deliverytype`
--

DROP TABLE IF EXISTS `admin_deliverytype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_deliverytype` (
  `dtid` int(11) NOT NULL AUTO_INCREMENT,
  `deliverytype` varchar(30) DEFAULT NULL,
  `amount` varchar(5) DEFAULT NULL,
  `deletestatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`dtid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_deliverytype`
--

LOCK TABLES `admin_deliverytype` WRITE;
/*!40000 ALTER TABLE `admin_deliverytype` DISABLE KEYS */;
INSERT INTO `admin_deliverytype` VALUES (1,'LSCS.','6000','0'),(2,'Normal','300','0');
/*!40000 ALTER TABLE `admin_deliverytype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_delmsg`
--

DROP TABLE IF EXISTS `admin_delmsg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_delmsg` (
  `delid` int(11) NOT NULL AUTO_INCREMENT,
  `delmsg` varchar(500) NOT NULL,
  PRIMARY KEY (`delid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_delmsg`
--

LOCK TABLES `admin_delmsg` WRITE;
/*!40000 ALTER TABLE `admin_delmsg` DISABLE KEYS */;
INSERT INTO `admin_delmsg` VALUES (1,'माँ  का  दूध  बच्चे का सर्वोत्तम आहार है | 6 महीने तक माँ का  दूध ही पिलायें'),(2,'भ्रूण की जांच एक दंडनीय अपराध है।'),(3,'जचकी के बाद माँ को पौष्टिक भोजन दें। '),(4,'गर्भवती महिला को भरपेट भोजन करायें। माँ स्वस्थ तो बच्चा स्वस्थ।'),(5,'अपने बच्चो को समय पर रोग प्रतिरोधक टीकों की पूरी मात्रा लगवायें।');
/*!40000 ALTER TABLE `admin_delmsg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_diagno`
--

DROP TABLE IF EXISTS `admin_diagno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_diagno` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `diagnosis` varchar(50) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=272 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_diagno`
--

LOCK TABLES `admin_diagno` WRITE;
/*!40000 ALTER TABLE `admin_diagno` DISABLE KEYS */;
INSERT INTO `admin_diagno` VALUES (1,'1ST GRAVIDA WITH LABOUR PAIN',0),(2,'2nd GRAVIDA WITH LABOUR PAIN',0),(3,'3rd GRAVIDA WITH LABOUR PAIN',0),(4,'4th GRAVIDA WITH LABOUR PAIN',0),(5,'5th GRAVIDA WITH LABOUR PAIN',0),(6,'6th GRAVIDA WITH LABOUR PAIN',0),(7,'7th GRAVIDA WITH LABOUR PAIN',0),(8,'ABSCESS',0),(9,'ACUTE ORGANOPHOSPHOROUS POISONING',0),(10,'ACUTE FEBRILE ILLNESS',0),(11,'ACUTE PANCREATITIS',0),(12,'ACUTE PSYCHOSIS',0),(13,'ACUTE RETENTION OF URINE',0),(14,'ACUTE TONSILITIS',0),(15,'ACUTE TRANSVERSE MYELITIS',0),(16,'AIDS',0),(17,'ALCOHOLIC DEPENDANCE ',0),(18,'ALCOHOLIC INTOXICATION ',0),(19,'ALCOHOLIC WITHDRAWL SYNDROME',0),(20,'ALLERGIC ',0),(21,'ALLERGIC RHINITIS',0),(22,'ANEMIA',0),(23,'APENDICITIS',0),(24,'ARTHRITIS',0),(25,'ASTHMA',0),(26,'BIPOLAR DISORDER (DEPRESSION)',0),(27,'BIPOLAR DISORDER (MANIC)',0),(28,'BIRTH ASPHYXIA',0),(29,'BRONCHITIS',0),(30,'CA ABDOMEN',0),(31,'CA BREAST',0),(32,'CA CERVIX',0),(33,'CA LUNG',0),(34,'CA PANCREAS',0),(35,'CARDIOMEGALY',0),(36,'CELLULITIS',0),(37,'CEREBRAL PALSY',0),(38,'CERVICAL POLYP',0),(39,'CHICKEN POX',0),(40,'CHOLECYSTITIS',0),(41,'CHOLELITHIASIS',0),(42,'CHOLERA',0),(43,'CHRONIC PANCREATITIS',0),(44,'CIRRHOSIS LIVER',0),(45,'COMPLETE ABORTION',0),(46,'COMPLETE UTERINE PROLAPSE',0),(47,'CONGENITAL HERNIA',0),(48,'CONGENITAL HYDROCELE',0),(49,'CONGENITAL HYPERTROPHIC PYLORIC STENOSIS',0),(50,'CORD AROUND NECK',0),(51,'CORD PROLAPSE',0),(52,'COUGH & COLD',0),(53,'DELUSIONAL DISORDER',0),(54,'DEPRESSION',0),(55,'DIABETIC FOOT',0),(56,'DILATED CARDIOMYPATHY',0),(57,'DRUG INDUCED HYPERTHERMIA',0),(58,'DYSELECTROLYTEMIA',0),(59,'ECLAMPSIA',0),(60,'EMPHYSEMA',0),(61,'EPIDIDYMO ORCHITIS',0),(62,'EPIGASTRIC HERNIA',0),(63,'EPILEPSY',0),(64,'EPISTAXIS',0),(65,'ERECTILE DISORDER',0),(66,'EXTRA PULMONARY TUBERCULOSIS',0),(67,'FEMUR ( RT)',0),(68,'FEMUR (LEFT)',0),(69,'FEMUR SHAFT (LEFT)',0),(70,'FEMUR SHAFT (RT)',0),(71,'FIBULA (LEFT)',0),(72,'FIBULA (RT)',0),(73,'FIBROID',0),(74,'GENERALISED ANXIETY DISORDER',0),(75,'HAEMATURIA',0),(76,'HEPATITIS A',0),(77,'HEPATITIS B',0),(78,'HERPES ZOSTER',0),(79,'HIV',0),(80,'HUMERUS (LEFT)',0),(81,'HUMERUS (RT)',0),(82,'HUMERUS SHAFT (LEFT)',0),(83,'HUMERUS SHAFT (RT)',0),(84,'HYDROCELE ',0),(85,'HYPERCALCEMIA',0),(86,'HYPEREMESIS GRAVIDERUM',0),(87,'HYPERPYREXIA',0),(88,'HYPERTHYOIDISM',0),(89,'HYPOGLYCEMIA',0),(90,'HYPOKALAMIA',0),(91,'HYPOTHRMIA',0),(92,'HYPOTHYROIDISM',0),(93,'HYSTERIA',0),(94,'INCHEORECTAL ABSCESS (RT)',0),(95,'INGUINAL HERNIA',0),(96,'INSOMNIA',0),(97,'INTELLECTUAL DISABILLITY',0),(98,'INTENTIONAL SELF HARM',0),(99,'INTESTINAL OBSTRUCTION',0),(100,'INTESTINAL PERFORATION',0),(101,'INTRACEREBRAL HEAMORRHAGE',0),(102,'IRRITABLE BOWEL SYNDROME',0),(103,'KELOID',0),(104,'LATERAL (ACROMIDIA) END OF RT CLAVIDA MULTIPLE RIB',0),(105,'LEPROSY',0),(106,'LICHEN SIMPLEX',0),(107,'LIPOMA',0),(108,'LOWER END OF FIBULA (RT)',0),(109,'LT SHAFT FEMUR',0),(110,'MANDIBLE',0),(111,'MEASLES',0),(112,'MENINGITIS',0),(113,'METATARSAL ( RT)',0),(114,'METATARSAL (LEFT)',0),(115,'NECK & FEMUR',0),(116,'METASTASIS',0),(117,'NEONATAL JAUNDICE',0),(118,'NOCTURENAL ENEUROSIS ',0),(119,'OBSESSIVE COMPULSIVE DISORDER',0),(120,'OLIGOHYDROAMNIOS',0),(121,'PANCYTOPENIA',0),(122,'PANIC DISORDER',0),(123,'PATELLA (BOTH SIDE)',0),(124,'PATELLA (LEFT)',0),(125,'PATELLA (RT)',0),(126,'PROXMAL PHALAX LT 5TH FINGER',0),(127,'PERFORATION',0),(128,'PNEUMONIA',0),(129,'PREECLAMPSIA',0),(130,'PREGANANCY INDUCE HYPERTENTION',0),(131,'PREMATURE BIRTH',0),(132,'RUBELLA',0),(133,'SCHIZOPHRENIA',0),(134,'SNAKE BITE',0),(135,'SOMATOFORM DISORDER',0),(136,'SUBSTANCE ABUSE DISORDER',0),(137,'SUICIDAL IDEATION',0),(138,'JAUNDICE',0),(139,'CONGENITAL JAUNDICE',0),(140,'LUMP',0),(141,'MULTIPLE SCLEROSIS',0),(142,'NECROSIS',0),(143,'NEPHRITIS',0),(144,'NEPHROLITHIASIS',0),(145,'NEPHROPATHY',0),(146,'NEPHROTIC SYNDROME',0),(147,'NEUROPATHY',0),(148,'PORTAL HYPERTENSION',0),(149,'POST ECLAMPSIA',0),(150,'POST PARTUM PSYCHOSIS',0),(151,'PSYCHO-SEXUAL DISORDER',0),(152,'VAGINITIS ',0),(153,'LEUCORRHOEA',0),(154,'AMENORRHEA',0),(155,'PURIPERIAL SEPSIS',0),(156,'DYSMENORRHEA',0),(157,'PV BLEEDING',0),(158,'PYOTHORAX',0),(159,'RECTAL PROLAPSE',0),(160,'RECTO PLACENTAL CLOT',0),(161,'RENAL COLIC',0),(162,'FISSURE IN ANO',0),(163,'FISTULA',0),(164,'PILES',0),(165,'RETAINED PLACENTA',0),(166,'OVARIAN CYST',0),(167,'POLYCYSTIC OVARIAN DISEASE',0),(168,'RADIUS (LEFT)',0),(169,'RADIUS (RT)',0),(170,'RT CLAVICLE',0),(171,'SCABIES',0),(172,'IMPETIGO',0),(173,'SCROTAL ABSESS',0),(174,'SHEFT FEMUR',0),(175,'SEPTICEMIA',0),(176,'ANOREXIA',0),(177,'HEADACH',0),(178,'MALNUTRITION',0),(179,'STROKE',0),(180,'SHOCK',0),(181,'SYSTEMIC LUMPUS ERYTHMATOUSUS',0),(182,'THALASEMIA',0),(183,'TIBIA (LEFT)',0),(184,'TIBIA (RT)',0),(185,'TRANSIENT ISCHEMIC ATTACK',0),(186,'TRAUMATIC PARAPLEGIA',0),(187,'PARAPLEGIA',0),(188,'TROPHIC ULCER',0),(189,'TROPICAL SPRUE',0),(190,'TUBERCULAR MENINGITIS',0),(191,'SPONDYLITIS',0),(192,'TYPHOID FEVER',0),(193,'ULCERATIVE COLITIS',0),(194,'ULNA (RT)',0),(195,'ULNA (LEFT)',0),(196,'UMBILICAL HERNIA',0),(197,'URTICARIA',0),(198,'UREMIA',0),(199,'VAGINAL VAULT PROLAPS',0),(200,'VERTIGO',0),(201,'VIRAL ENCEPHALITIS',0),(202,'VOLVULUS',0),(203,'XTENSIVE ADHESIONS ABDOMEN',0),(204,'ACUTE GRASTROENTERITIS',0),(205,'ACUTE GLOMERULONEPHRITIS',0),(206,'ACUTE RENAL FAILURE',0),(207,'ACUTE RESPIRATORY INFECTION ',0),(208,'ANTENATAL CARE',0),(209,'ARTIAL FIBRILLATION ',0),(210,'ACUTE MYLELOID LEUKAMIA',0),(211,'ACID PEPTIC DISORDER',0),(212,'ANTE PARTUM HEMORRHAGE',0),(213,'BENIGN PROSTATIC HYPERPLASIA',0),(214,'CHRONIC RENAL FAILURE',0),(215,'CHRONIC OBSTRUCTIVE PULMONARY DISEASE',0),(216,'CONGESTIVE CARDIAC FAILURE',0),(217,'CEREBRO VASCULAR ACCIDENT',0),(218,'CHRONIC KIDNEY DISEASES',0),(219,'CHRONIC MYELOID LEUKEMIA',0),(220,'CHRONIC PULMONARY DISEASES ',0),(221,'CARDIAC RESUSCITATION THERAPY ',0),(222,'CEREBRAL PALSY ',0),(223,'DIABETESE MELLITUS ',0),(224,'DIABETESE MELLITUS TYPE 1',0),(225,'DIABETESE MELLITUS TYPE 2',0),(226,'DRUG INDUCED HYPERTHERMIA ',0),(227,'DYSFUNCTIONAL UTERINE BLEEDING',0),(228,'DEVELOPMENTAL DYSPLASIA ',0),(229,'DEEP VEIN THROMBOSIS ',0),(230,'DIALATATION AND EVACUATION',0),(231,'DIALATATION AND CURETTAGE',0),(232,'FULL TERM NORMAL DELIVERY ',0),(233,'GASTROENTERITIS',0),(234,'HYPERTENTION',0),(235,'INSULIN DEPENDENT DIABETES MELLITUS ',0),(236,'IRRITABLE BOWEL SYNDROM',0),(237,'INTELLECTUAL DISABILITY ',0),(238,'ISCHEMIC HEART DISEASE',0),(239,'INTRA UTERINE DEATH',0),(240,'INTRA UTERINE FEATAL DEATH',0),(241,'LOWER RESPIRATORY TRACT INFECTION',0),(242,'LEFT VENTRICULAR FAILURE',0),(243,'LOW BIRTH WEIGHT ',0),(244,'LOWER SEGMENT CAESAREAN SECTION ',0),(245,'MEDICAL TERMINATION OF PREGANANCY ',0),(246,'MAYOCARDIAL INFARCTION',0),(247,'MAGNETIC RESONANCE IMAGING',0),(248,'MULTI DRUG RESISTANT TUBERCULOSIS',0),(249,'NON INSULINE DEPENDENT DIABETESE ',0),(250,'MULTIPAL SCEROSIS',0),(251,'NON DESCENT VAGINAL HYSTERECTOMY',0),(252,'POST NATAL CARE',0),(253,'PELVIC INFLAMMATORY DISEASE',0),(254,'POSTPARTUM HEAMORRHAGE',0),(255,'POLYCYSTIC OVARY SYNDROM',0),(256,'FALCIPERUM MALARIA',0),(257,'PROLAPSED INTER VERTEBRAL DISC',0),(258,'PULMONARY TUBERCULOSIS ',0),(259,'RESPIRATORY TRACT INFECTION',0),(260,'RHUMATIC HEART DISEASE',0),(261,'ROAD TRAFFIC ACCIDENT',0),(262,'SICKLE CELL ANEMIA',0),(263,'SICKLE CELL DISEASE',0),(264,'SICKLE CELL TRAIT',0),(265,'SYSTEMIC LUMPUS ERYTHEMATOUSUS',0),(266,'SUPRAVENTRICULAR TACHYCARDIA',0),(267,'TUBECTOMY',0),(268,'TRANSIENT ISCHEMIC ATTACK',0),(269,'TUBERCULOSIS',0),(270,'UPPER REPIRATORY INFECTION ',0),(271,'URINARY TRACT INFECTION ',0);
/*!40000 ALTER TABLE `admin_diagno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_district`
--

DROP TABLE IF EXISTS `admin_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_district` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `disname` varchar(50) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_district`
--

LOCK TABLES `admin_district` WRITE;
/*!40000 ALTER TABLE `admin_district` DISABLE KEYS */;
INSERT INTO `admin_district` VALUES (1,'BALOD',0),(2,'BALODA BAZAR',0),(3,'BALRAMPUR',0),(4,'BASTAR',0),(5,'BEMETARA',0),(6,'BIJAPUR',0),(7,'BILASPUR',0),(8,'DANTEWADA',0),(9,'DHAMTARI',0),(10,'DURG',0),(11,'GARIYABAND',0),(12,'JANJGIR-CHAMPA',0),(13,'JASHPUR',0),(14,'KABIRDHAM',0),(15,'KANKER',0),(16,'KONDAGAON',0),(17,'KORBA',0),(18,'KORIYA',0),(19,'MAHASAMUND',0),(20,'MUNGELI',0),(21,'NARAYANPUR',0),(22,'RAIGARH',0),(23,'RAIPUR',0),(24,'RAJNANDGAON',0),(25,'SUKMA',0),(26,'SURAJPUR',0),(27,'SURGUJA',0);
/*!40000 ALTER TABLE `admin_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_dressing`
--

DROP TABLE IF EXISTS `admin_dressing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_dressing` (
  `drsid` int(11) NOT NULL AUTO_INCREMENT,
  `drsname` varchar(50) DEFAULT NULL,
  `drsamount` varchar(10) DEFAULT NULL,
  `deletestatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`drsid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_dressing`
--

LOCK TABLES `admin_dressing` WRITE;
/*!40000 ALTER TABLE `admin_dressing` DISABLE KEYS */;
INSERT INTO `admin_dressing` VALUES (1,'D-1','60','0'),(2,'D-2','50','0'),(3,'D-3','40','0'),(4,'D-4','30','0'),(5,'D-5','20','0');
/*!40000 ALTER TABLE `admin_dressing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_generalmsg`
--

DROP TABLE IF EXISTS `admin_generalmsg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_generalmsg` (
  `genid` int(11) NOT NULL AUTO_INCREMENT,
  `genmsg` varchar(500) NOT NULL,
  PRIMARY KEY (`genid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_generalmsg`
--

LOCK TABLES `admin_generalmsg` WRITE;
/*!40000 ALTER TABLE `admin_generalmsg` DISABLE KEYS */;
INSERT INTO `admin_generalmsg` VALUES (1,'अपने बच्चो को समय पर रोग प्रतिरोधक टीकों की पूरी मात्रा लगवायें।'),(2,'संतुलित आहार ही अच्छे स्वास्थ्य की कुंजी है। '),(3,'मलेरिया से बचने के लिए मच्छरदानी का उपयोग करे। '),(4,'दूषित पानी अधिकतर रोगों की जड़ है।पानी को उबालकर पियें।'),(5,'भोजन के पहले तथा भोजन के बाद, हाथ अच्छी तरह से धोयें। '),(6,'दो हफ्तों या उससे ज्यादा खांसी आए तो नजदीकी अस्पताल में जांच करायें।'),(7,'खुले में शौंच ना करे ,शौचालय का उपयोग करें। शौंच के बाद हाथों को अच्छी तरह साबुन से धोएं।');
/*!40000 ALTER TABLE `admin_generalmsg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_govsch`
--

DROP TABLE IF EXISTS `admin_govsch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_govsch` (
  `gsid` int(11) NOT NULL AUTO_INCREMENT,
  `gsname` varchar(50) DEFAULT NULL,
  `deletestatus` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`gsid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_govsch`
--

LOCK TABLES `admin_govsch` WRITE;
/*!40000 ALTER TABLE `admin_govsch` DISABLE KEYS */;
INSERT INTO `admin_govsch` VALUES (-1,'Not Eligible','-1'),(1,'RSBY','1'),(2,'MSPY','0'),(3,'Ayusman Bharat','0');
/*!40000 ALTER TABLE `admin_govsch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_medtype`
--

DROP TABLE IF EXISTS `admin_medtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_medtype` (
  `mtid` int(11) NOT NULL AUTO_INCREMENT,
  `mtype` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`mtid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_medtype`
--

LOCK TABLES `admin_medtype` WRITE;
/*!40000 ALTER TABLE `admin_medtype` DISABLE KEYS */;
INSERT INTO `admin_medtype` VALUES (1,'Tablets.');
/*!40000 ALTER TABLE `admin_medtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_physiotherapy`
--

DROP TABLE IF EXISTS `admin_physiotherapy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_physiotherapy` (
  `phyid` int(11) NOT NULL AUTO_INCREMENT,
  `phyname` varchar(50) DEFAULT NULL,
  `phyamount` varchar(10) DEFAULT NULL,
  `deletestatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`phyid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_physiotherapy`
--

LOCK TABLES `admin_physiotherapy` WRITE;
/*!40000 ALTER TABLE `admin_physiotherapy` DISABLE KEYS */;
INSERT INTO `admin_physiotherapy` VALUES (1,'ASSESMENT','20','0'),(2,'EXSERCISE','40','0'),(3,'1 MODALITY','20','0'),(4,'2 MODALITY','40','0'),(5,'3 MODALITY','60','0'),(6,'MORE THAN 3 MODALITY','100','0');
/*!40000 ALTER TABLE `admin_physiotherapy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_prOfSurgery`
--

DROP TABLE IF EXISTS `admin_prOfSurgery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_prOfSurgery` (
  `posid` int(11) NOT NULL AUTO_INCREMENT,
  `pos` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`posid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_prOfSurgery`
--

LOCK TABLES `admin_prOfSurgery` WRITE;
/*!40000 ALTER TABLE `admin_prOfSurgery` DISABLE KEYS */;
INSERT INTO `admin_prOfSurgery` VALUES (1,'LSCS.'),(2,'trrt.'),(3,'yyy.');
/*!40000 ALTER TABLE `admin_prOfSurgery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_subname`
--

DROP TABLE IF EXISTS `admin_subname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_subname` (
  `subid` int(11) NOT NULL AUTO_INCREMENT,
  `xid` int(11) DEFAULT NULL,
  `subxray` varchar(50) DEFAULT NULL,
  `amount` int(3) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`subid`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_subname`
--

LOCK TABLES `admin_subname` WRITE;
/*!40000 ALTER TABLE `admin_subname` DISABLE KEYS */;
INSERT INTO `admin_subname` VALUES (1,1,'CHEST AP VIEW',200,0),(2,1,'CHEST PA VIEW',200,0),(3,1,'CHEST LAT VIEW',200,0),(4,1,'CHEST OBLIQUE VIEW',200,0),(5,3,'Chest U14 PA View',200,0),(6,3,'Chest U14 AP View',200,0),(7,3,'Chest U14 LAT View',200,0),(8,3,'Chest U14 OBLIQUE View',200,0),(9,5,'ABDOMEN AP VIEW',200,0),(10,5,'ABDOMEN PA VIEW',200,0),(11,6,'Abdomen U14 AP View',200,0),(12,6,'Abdomen U14 PA View',200,0),(13,7,'KUB AP VIEW',250,0),(14,8,'KUB AP View U14',250,0),(15,2,'L.S. SPINE',250,0),(16,2,'DORSAL SPINE AP&LAT',250,0),(17,2,'CERVICAL SPINE AP&LAT',250,0),(18,2,'SKULL AP VIEW',250,0),(19,2,'SKULL PA VIEW',250,0),(20,2,'SKULL LATERAL',250,0),(21,2,'P.N.S. PA VIEW',250,0),(22,2,'PELVIC BOTH HIP AP',250,0),(23,2,'THIGH AP',250,0),(24,2,'THIGH LAT',250,0),(25,2,'THIGH AP&LAT',250,0),(26,2,'SHOULDER AP',250,0),(27,2,'SHOULDER AP&OBLIQUE',250,0),(28,2,'ARM AP&LAT',250,0),(29,2,'ELBOW AP&LAT',250,0),(30,2,'HAND AP&LAT',250,0),(31,2,'WRIST AP&LAT',250,0),(32,2,'FOOT AP&LAT',250,0),(33,4,'L.S SPINE U14',250,0),(34,4,'Dorsel Spine AP&LAT U14',250,0),(35,4,'P.N.S PA U14',250,0),(36,4,'Skull AP U14',250,0),(37,4,'Skull PA U14',250,0),(38,4,'Skull LAT U14',250,0),(39,4,'Pelvic Both Hip AP U14',250,0),(40,4,'Pelvic Both Hip PA U14',250,0),(41,4,'Thigh AP&LAT U14',250,0),(42,4,'Thigh AP U14',250,0),(43,4,'Thigh LAT U14',250,0),(44,4,'Shoulder AP&OBLIQUE U14',250,0),(45,4,'Shoulder AP',250,0),(46,4,'Skull AP&LAT U14',250,0),(47,4,'Skull PA&LAT U14',250,0),(48,4,'Cervical Spine AP&LAT U14',250,0),(49,4,'Knee AP&LAT U14',250,0),(50,4,'Leg AP&LAT U14',250,0),(51,4,'Shoulder AP&LAT U14',250,0),(52,4,'ARM AP&LAT U14',250,0),(53,4,'Elbow AP&LAT U14',250,0),(54,4,'Hand AP&LAT U14',250,0),(55,4,'Wrist AP&LAT U14',250,0),(56,4,'Foot AP&LAT',250,0),(57,2,'PELVIC BOTH HIP PA',250,0),(58,2,'SKULL AP&LAT',250,0),(59,2,'SKULL PA&LAT',250,0),(60,2,'SHOULDER AP&LAT',250,0),(61,9,'ANUS PA View U14',200,0),(62,9,'Anus AP View U14',200,0),(63,2,'CHEST PA VIEW',200,0),(64,2,'CHEST AP VIEW',200,0),(65,2,'CHEST LAT VIEW',200,0),(66,2,'CHEST OBLIQUE VIEW',200,0),(67,4,'CHEST PA View U14',200,0),(68,4,'CHEST AP View U14',200,0),(69,4,'CHEST LAT View U14',200,0),(70,4,'CHEST OBLIQUE View U14',200,0);
/*!40000 ALTER TABLE `admin_subname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_surgery_procedure`
--

DROP TABLE IF EXISTS `admin_surgery_procedure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_surgery_procedure` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sprocedure` varchar(100) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  `spamount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_surgery_procedure`
--

LOCK TABLES `admin_surgery_procedure` WRITE;
/*!40000 ALTER TABLE `admin_surgery_procedure` DISABLE KEYS */;
INSERT INTO `admin_surgery_procedure` VALUES (1,'LSCS',0,'5000.0'),(2,'TT',0,'3000.0'),(3,'LSCS+TT',0,'5500.0'),(4,'VEG.HYSTERECTOMY',0,'7000.0'),(5,'TAH',0,'6000.0'),(6,'HERNIA',0,'4000.0'),(7,'HERNIA WITH MESH',0,'5000.0'),(8,'GASTRIC PERFORATION',0,'7000.0'),(9,'APPENDIX',0,'5000.0'),(10,'HYDROCELE',0,'2000.0'),(11,'HYDROCELE BL',0,'4000.0'),(12,'AMPUTATION ABOVE KNEE',0,'5000.0'),(13,'AMPUTATION BELOW KNEE',0,'5000.0'),(14,'AMPUTATION HAND',0,'4000.0'),(15,'AMPUTATION DIGITS',0,'1000.0'),(16,'TUBOPLASTY',0,'5000.0'),(17,'SKIN GRAFTING LARG',0,'7000.0'),(18,'SKIN GRAFTING MEDIUM',0,'5000.0'),(19,'SKIN GRAFTING SMALL',0,'3000.0'),(20,'CYST LARG',0,'1000.0'),(21,'CYST SMALL',0,'500.0'),(22,'ID LARG',0,'2000.0'),(23,'ID MEDIUM',0,'1000.0'),(24,'ID SMALL',0,'500.0'),(25,'CHOLECYSTECTOMY',0,'7000.0'),(26,'COLOSTOMY',0,'5000.0'),(27,'RAMSTEDT OPERATION',0,'3000.0'),(28,'INTESTINAL RESECTION ANASTOMOSIS',0,'7000.0'),(29,'CIRCUMCISION PEDIATRIC',0,'1000.0'),(30,'CIRCUMCISION ADULT',0,'1500.0'),(31,'GANGLION REMOVAL',0,'1000.0'),(32,'VENTRAL HERNIA WITH MESH',0,'8000.0'),(33,'VENTRAL HERNIA WITHOUT MESH',0,'5000.0'),(34,'VASECTOMY',0,'1500.0'),(35,'OVARIAN CYSTECTOMY',0,'4500.0'),(36,'THYROIDECTOMY',0,'7000.0'),(37,'FIBROADENOMA BREAST WITH LOCAL',0,'1000.0'),(38,'FIBROADENOMA BREAST WITH GA',0,'2000.0'),(39,'MASTECTOMY',0,'7000.0'),(40,'SHOULDER DISLOCATION',0,'2000.0'),(41,'VAGINAL POLYPECTOMY',0,'2000.0'),(42,'FISSURECTOMY',0,'2000.0'),(43,'DE',0,'3000.0'),(44,'DE + TT',0,'4000.0'),(45,'FISTULECTOMY',0,'1000.0'),(46,'URETHRAL DILATATION',0,'500.0'),(47,'OPENING OF VAGINAL WALL',0,'1500.0'),(48,'NORMAL',0,'700.0'),(49,'EPISIOTOMY/ PERINEAL TEAR',0,'800.0'),(50,'FORCEPS',0,'900.0');
/*!40000 ALTER TABLE `admin_surgery_procedure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_therapy`
--

DROP TABLE IF EXISTS `admin_therapy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_therapy` (
  `adm_therapyid` int(11) NOT NULL AUTO_INCREMENT,
  `adm_therapyname` varchar(50) DEFAULT NULL,
  `adm_therapyamount` varchar(10) DEFAULT NULL,
  `deletestatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`adm_therapyid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_therapy`
--

LOCK TABLES `admin_therapy` WRITE;
/*!40000 ALTER TABLE `admin_therapy` DISABLE KEYS */;
INSERT INTO `admin_therapy` VALUES (1,'THERAPY1','6','0'),(2,'THERAPY2','1','0'),(3,'THERAPY3','10','0');
/*!40000 ALTER TABLE `admin_therapy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_ward_bdname`
--

DROP TABLE IF EXISTS `admin_ward_bdname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_ward_bdname` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `bname` varchar(20) DEFAULT NULL,
  `wid` int(11) DEFAULT NULL,
  `bstatus` int(1) DEFAULT '1',
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_ward_bdname`
--

LOCK TABLES `admin_ward_bdname` WRITE;
/*!40000 ALTER TABLE `admin_ward_bdname` DISABLE KEYS */;
INSERT INTO `admin_ward_bdname` VALUES (1,'C-1',3,1,0),(2,'C-2',3,1,0),(3,'C-3',3,1,0),(4,'C-4',3,1,0),(5,'C-5',3,1,0),(6,'C-6',3,1,0),(7,'C-7',3,1,0),(8,'C-8',3,1,0),(9,'C-9',3,1,0),(10,'C-10',3,1,0),(11,'C-11',3,1,0),(12,'C-12',3,1,0),(13,'C-13',3,1,0),(14,'C-14',3,1,0),(15,'C-15',3,1,0),(16,'C-16',3,1,0),(17,'C-17',3,1,0),(18,'C-18',3,1,0),(19,'F-1',1,1,0),(20,'F-2',1,1,0),(21,'F-3',1,1,0),(22,'F-4',1,1,0),(23,'F-5',1,1,0),(24,'F-6',1,1,0),(25,'F-7',1,1,0),(26,'F-8',1,1,0),(27,'F-9',1,1,0),(28,'F-10',1,1,0),(29,'F-11',1,1,0),(30,'F-12',1,1,0),(31,'F-13',1,1,0),(32,'P-14',1,1,0),(33,'P-15',1,1,0),(34,'K-1',2,1,0),(35,'K-2',2,1,0),(36,'K-3',2,1,0),(37,'K-4',2,1,0),(38,'K-5',2,1,0),(39,'K-6',2,1,0),(40,'K-7',2,1,0),(41,'K-8',2,1,0),(42,'K-9',2,1,0),(43,'K-10',2,1,0),(44,'K-11',2,1,0),(45,'K-12',2,1,0),(46,'K-13',2,1,0),(47,'K-14',2,1,0),(48,'K-15',2,1,0),(49,'K-16',2,1,0),(50,'K-17',2,1,0),(51,'K-18',2,1,0),(52,'K-19',2,1,0),(53,'K-20',2,1,0),(54,'K-21',2,1,0),(55,'K-22',2,1,0),(56,'K-23',2,1,0),(57,'K-24',2,1,0),(58,'K-25',2,1,0),(59,'K-26',2,1,0),(60,'K-27',2,1,0),(61,'K-28',2,1,0),(62,'S-1',4,1,0),(63,'S-2',4,1,0),(64,'S-3',4,1,0),(65,'S-4',4,1,0),(66,'S-5',4,1,0),(67,'S-6',4,1,0),(68,'S-7',4,1,0),(69,'S-8',4,1,0),(70,'S-9',4,1,0),(71,'S-10',4,1,0),(72,'S-11',4,1,0),(73,'S-12',4,1,0),(74,'S-13',4,1,0),(75,'S-14',4,1,0),(76,'S-15',4,1,0),(77,'S-16',4,1,0),(78,'S-17',4,1,0),(79,'S-18',4,1,0),(80,'S-19',4,1,0),(81,'S-20',4,1,0),(82,'M-1',4,1,0),(83,'M-2',4,1,0),(84,'M-3',4,1,0),(85,'M-4',4,1,0),(86,'M-5',4,1,0),(87,'M-6',4,1,0),(88,'M-7',4,1,0),(89,'M-8',4,1,0),(90,'M-9',4,1,0),(91,'M-10',4,1,0),(92,'M-11',4,1,0),(93,'M-12',4,1,0),(94,'M-13',4,1,0),(95,'M-14',4,1,0),(96,'M-15',4,1,0),(97,'M-16',4,1,0),(98,'M-17',4,1,0),(99,'M-18',4,1,0),(100,'M-19',4,1,0),(101,'M-20',4,1,0),(102,'M-21',4,1,0),(103,'M-22',4,1,0),(104,'M-23',4,1,0),(105,'M-24',4,1,0),(106,'G-1',4,0,0),(107,'G-2',4,1,0),(108,'G-3',4,1,0),(109,'G-4',4,1,0),(110,'G-5',4,1,0),(111,'G-6',4,1,0),(112,'G-7',4,1,0),(113,'G-8',4,1,0),(114,'G-9',4,1,0),(115,'G-10',4,0,0),(116,'G-11',4,1,0),(117,'G-12',4,1,0),(118,'G-13',4,0,0),(119,'G-14',4,1,0),(120,'G-15',4,1,0),(121,'G-16',4,1,0),(122,'G-17',4,1,0),(123,'G-18',4,1,0),(124,'P4B',1,0,0);
/*!40000 ALTER TABLE `admin_ward_bdname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_wardname`
--

DROP TABLE IF EXISTS `admin_wardname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_wardname` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `wname` varchar(30) DEFAULT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_wardname`
--

LOCK TABLES `admin_wardname` WRITE;
/*!40000 ALTER TABLE `admin_wardname` DISABLE KEYS */;
INSERT INTO `admin_wardname` VALUES (1,'Female(Delivery) Ward',0),(2,'K- Ward',0),(3,'Child Ward',0),(4,'Male Ward',0),(5,'Laboratory Department',0),(6,'Nursery Ward',0),(7,'Pharmacy',0),(8,'OT Department',0);
/*!40000 ALTER TABLE `admin_wardname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_xname`
--

DROP TABLE IF EXISTS `admin_xname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_xname` (
  `xid` int(11) NOT NULL AUTO_INCREMENT,
  `xrayname` varchar(50) NOT NULL,
  `deletestatus` int(1) DEFAULT '0',
  PRIMARY KEY (`xid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_xname`
--

LOCK TABLES `admin_xname` WRITE;
/*!40000 ALTER TABLE `admin_xname` DISABLE KEYS */;
INSERT INTO `admin_xname` VALUES (1,'Chest',0),(2,'Orthopedics',0),(3,'Chest_U14',0),(4,'Orthopedics_U14',0),(5,'Abdomen',0),(6,'Abdomen_U14',0),(7,'KUB',0),(8,'KUB_U14',0),(9,'Anus_U14',0);
/*!40000 ALTER TABLE `admin_xname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_first_visit`
--

DROP TABLE IF EXISTS `anc_first_visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_first_visit` (
  `FiV_id` int(11) NOT NULL AUTO_INCREMENT,
  `anc_id` int(11) DEFAULT NULL,
  `FiV_seen_doctor` varchar(20) DEFAULT NULL,
  `FiV_seen_sister` varchar(20) DEFAULT NULL,
  `FiV_date` date DEFAULT NULL,
  `FiV_wt` varchar(10) DEFAULT NULL,
  `FiV_ht` varchar(10) DEFAULT NULL,
  `FiV_bmi` varchar(10) DEFAULT NULL,
  `FiV_systolic` varchar(10) DEFAULT NULL,
  `FiV_diastolic` varchar(10) DEFAULT NULL,
  `FiV_pulse` varchar(10) DEFAULT NULL,
  `FiV_heart` varchar(50) DEFAULT NULL,
  `FiV_lungs` varchar(50) DEFAULT NULL,
  `FiV_breast` varchar(50) DEFAULT NULL,
  `FiV_anaemia` varchar(50) DEFAULT NULL,
  `FiV_jaundice` varchar(50) DEFAULT NULL,
  `FiV_tongue` varchar(50) DEFAULT NULL,
  `FiV_thyroid` varchar(50) DEFAULT NULL,
  `FiV_neckglds` varchar(50) DEFAULT NULL,
  `FiV_teeth` varchar(50) DEFAULT NULL,
  `FiV_gum` varchar(50) DEFAULT NULL,
  `FiV_throat` varchar(50) DEFAULT NULL,
  `FiV_kidneys` varchar(50) DEFAULT NULL,
  `FiV_oedema` varchar(50) DEFAULT NULL,
  `FiV_spleen` varchar(50) DEFAULT NULL,
  `FiV_liver` varchar(50) DEFAULT NULL,
  `FiV_variveins` varchar(50) DEFAULT NULL,
  `FiV_pallor` varchar(50) DEFAULT NULL,
  `FiV_icterus` varchar(50) DEFAULT NULL,
  `FiV_others` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`FiV_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_first_visit`
--

LOCK TABLES `anc_first_visit` WRITE;
/*!40000 ALTER TABLE `anc_first_visit` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_first_visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_followup_visit`
--

DROP TABLE IF EXISTS `anc_followup_visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_followup_visit` (
  `FoV_id` int(11) NOT NULL AUTO_INCREMENT,
  `anc_id` int(11) DEFAULT NULL,
  `FoV_seen_doctor` varchar(20) DEFAULT NULL,
  `FoV_seen_sister` varchar(20) DEFAULT NULL,
  `FoV_date` date DEFAULT NULL,
  `FoV_wt` varchar(10) DEFAULT NULL,
  `FoV_ht` varchar(10) DEFAULT NULL,
  `FoV_bmi` varchar(10) DEFAULT NULL,
  `FoV_systolic` varchar(10) DEFAULT NULL,
  `FoV_diastolic` varchar(10) DEFAULT NULL,
  `FoV_pulse` varchar(10) DEFAULT NULL,
  `FoV_bodytemp` varchar(10) DEFAULT NULL,
  `FoV_resprate` varchar(20) DEFAULT NULL,
  `FoV_utsize` varchar(50) DEFAULT NULL,
  `FoV_oedema` varchar(50) DEFAULT NULL,
  `FoV_no_foetus` varchar(50) DEFAULT NULL,
  `FoV_fhs` varchar(100) DEFAULT NULL,
  `FoV_pallor` varchar(50) DEFAULT NULL,
  `FoV_cyanosis` varchar(50) DEFAULT NULL,
  `FoV_icterus` varchar(50) DEFAULT NULL,
  `FoV_variveins` varchar(50) DEFAULT NULL,
  `FoV_immstatus` varchar(20) DEFAULT NULL,
  `FoV_others` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`FoV_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_followup_visit`
--

LOCK TABLES `anc_followup_visit` WRITE;
/*!40000 ALTER TABLE `anc_followup_visit` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_followup_visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_gravida_history`
--

DROP TABLE IF EXISTS `anc_gravida_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_gravida_history` (
  `gh_id` int(11) NOT NULL AUTO_INCREMENT,
  `anc_id` int(11) DEFAULT NULL,
  `gh_date` date DEFAULT NULL,
  `gravida` int(2) DEFAULT NULL,
  `parity_live` int(2) DEFAULT NULL,
  `dopa` date DEFAULT NULL,
  `dop` varchar(10) DEFAULT NULL,
  `aop` varchar(100) DEFAULT NULL,
  `lsch` varchar(100) DEFAULT NULL,
  `delivery_type` varchar(100) DEFAULT NULL,
  `no_babies` int(2) DEFAULT NULL,
  `baby_status` varchar(100) DEFAULT NULL,
  `puerperium` varchar(100) DEFAULT NULL,
  `childsex` varchar(20) DEFAULT NULL,
  `baby_wt` varchar(20) DEFAULT NULL,
  `brstfed_btlefed` varchar(20) DEFAULT NULL,
  `gh_others` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`gh_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_gravida_history`
--

LOCK TABLES `anc_gravida_history` WRITE;
/*!40000 ALTER TABLE `anc_gravida_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_gravida_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_lab_checkup`
--

DROP TABLE IF EXISTS `anc_lab_checkup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_lab_checkup` (
  `lc_id` int(11) NOT NULL AUTO_INCREMENT,
  `anc_id` int(11) DEFAULT NULL,
  `lc_date` date DEFAULT NULL,
  `lc_testdone` varchar(20) DEFAULT NULL,
  `lc_sugar` varchar(20) DEFAULT NULL,
  `lc_albumin` varchar(20) DEFAULT NULL,
  `lc_microscopy` varchar(20) DEFAULT NULL,
  `lc_hb` varchar(20) DEFAULT NULL,
  `lc_bldgrp` varchar(20) DEFAULT NULL,
  `lc_sickling` varchar(20) DEFAULT NULL,
  `lc_vdrl` varchar(20) DEFAULT NULL,
  `lc_hbsag` varchar(20) DEFAULT NULL,
  `lc_hiv` varchar(20) DEFAULT NULL,
  `lc_rbs` varchar(20) DEFAULT NULL,
  `lc_tsh` varchar(20) DEFAULT NULL,
  `lc_others` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`lc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_lab_checkup`
--

LOCK TABLES `anc_lab_checkup` WRITE;
/*!40000 ALTER TABLE `anc_lab_checkup` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_lab_checkup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_main`
--

DROP TABLE IF EXISTS `anc_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_main` (
  `anc_id` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `anc_date` date DEFAULT NULL,
  `patient_history` int(1) DEFAULT '0',
  `gravida_history` int(1) DEFAULT '0',
  `first_visit` int(1) DEFAULT '0',
  `follow_visit` int(2) DEFAULT '0',
  `lab_checkup` int(1) DEFAULT '0',
  `usg_report` int(1) DEFAULT '0',
  `anc_status` int(1) DEFAULT '1',
  PRIMARY KEY (`anc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_main`
--

LOCK TABLES `anc_main` WRITE;
/*!40000 ALTER TABLE `anc_main` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_patient_history`
--

DROP TABLE IF EXISTS `anc_patient_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_patient_history` (
  `ph_id` int(11) NOT NULL AUTO_INCREMENT,
  `anc_id` int(11) DEFAULT NULL,
  `ph_date` date DEFAULT NULL,
  `ph_age` int(3) DEFAULT NULL,
  `duration` varchar(10) DEFAULT NULL,
  `cycle` varchar(10) DEFAULT NULL,
  `lmp` date DEFAULT NULL,
  `edd` varchar(20) DEFAULT NULL,
  `occupation` varchar(10) DEFAULT NULL,
  `martial_status` varchar(10) DEFAULT NULL,
  `past_history` varchar(200) DEFAULT NULL,
  `family_history` varchar(200) DEFAULT NULL,
  `contraceptive_history` varchar(200) DEFAULT NULL,
  `ph_others` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ph_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_patient_history`
--

LOCK TABLES `anc_patient_history` WRITE;
/*!40000 ALTER TABLE `anc_patient_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_patient_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `anc_usg_report`
--

DROP TABLE IF EXISTS `anc_usg_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anc_usg_report` (
  `usg_id` int(11) NOT NULL AUTO_INCREMENT,
  `anc_id` int(11) DEFAULT NULL,
  `usg_date` date DEFAULT NULL,
  `usg_testdone` varchar(20) DEFAULT NULL,
  `usg_gravida` int(2) DEFAULT NULL,
  `usg_lmp` date DEFAULT NULL,
  `usg_edd` varchar(20) DEFAULT NULL,
  `usg_foetus` varchar(20) DEFAULT NULL,
  `usg_presentation` varchar(20) DEFAULT NULL,
  `usg_placenta` varchar(20) DEFAULT NULL,
  `usg_liquor` varchar(20) DEFAULT NULL,
  `usg_crl` varchar(20) DEFAULT NULL,
  `usg_fa1` varchar(20) DEFAULT NULL,
  `usg_edd1` date DEFAULT NULL,
  `usg_bpd` varchar(20) DEFAULT NULL,
  `usg_fa2` varchar(20) DEFAULT NULL,
  `usg_edd2` date DEFAULT NULL,
  `usg_hc` varchar(20) DEFAULT NULL,
  `usg_fa3` varchar(20) DEFAULT NULL,
  `usg_edd3` date DEFAULT NULL,
  `usg_ac` varchar(20) DEFAULT NULL,
  `usg_fa4` varchar(20) DEFAULT NULL,
  `usg_edd4` date DEFAULT NULL,
  `usg_fl` varchar(20) DEFAULT NULL,
  `usg_fa5` varchar(20) DEFAULT NULL,
  `usg_edd5` date DEFAULT NULL,
  `usg_fa6` varchar(20) DEFAULT NULL,
  `usg_edd6` date DEFAULT NULL,
  `usg_fhr` varchar(20) DEFAULT NULL,
  `usg_fwt` varchar(20) DEFAULT NULL,
  `usg_hc_ae` varchar(20) DEFAULT NULL,
  `usg_fl_he` varchar(20) DEFAULT NULL,
  `usg_fl_ae` varchar(20) DEFAULT NULL,
  `usg_others` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`usg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anc_usg_report`
--

LOCK TABLES `anc_usg_report` WRITE;
/*!40000 ALTER TABLE `anc_usg_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `anc_usg_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `billing_medicine`
--

DROP TABLE IF EXISTS `billing_medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `billing_medicine` (
  `bmid` int(11) NOT NULL AUTO_INCREMENT,
  `bmdate` date DEFAULT NULL,
  `regno` varchar(13) DEFAULT NULL,
  `givenby` varchar(30) DEFAULT NULL,
  `docid` int(11) DEFAULT NULL,
  `billstatus` varchar(10) DEFAULT NULL,
  `opdid` int(11) DEFAULT NULL,
  `netamount` varchar(15) DEFAULT '0',
  `printstatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`bmid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing_medicine`
--

LOCK TABLES `billing_medicine` WRITE;
/*!40000 ALTER TABLE `billing_medicine` DISABLE KEYS */;
/*!40000 ALTER TABLE `billing_medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `billing_medicine_detail`
--

DROP TABLE IF EXISTS `billing_medicine_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `billing_medicine_detail` (
  `mbmid` int(11) NOT NULL AUTO_INCREMENT,
  `bmid` int(11) DEFAULT NULL,
  `meddet_id` int(11) DEFAULT NULL,
  `iqty` int(11) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`mbmid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing_medicine_detail`
--

LOCK TABLES `billing_medicine_detail` WRITE;
/*!40000 ALTER TABLE `billing_medicine_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `billing_medicine_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery_child`
--

DROP TABLE IF EXISTS `delivery_child`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delivery_child` (
  `child_id` int(11) NOT NULL AUTO_INCREMENT,
  `delivery_id` int(11) DEFAULT NULL,
  `born_date` date DEFAULT NULL,
  `born_time` time DEFAULT NULL,
  `child_sex` varchar(20) DEFAULT NULL,
  `child_weight` varchar(10) DEFAULT NULL,
  `child_status` varchar(20) DEFAULT NULL,
  `live_child` varchar(50) DEFAULT NULL,
  `cdtime` time DEFAULT NULL,
  `cddate` date DEFAULT NULL,
  `cdreason` varchar(200) DEFAULT NULL,
  `presenting_part` varchar(50) DEFAULT NULL,
  `apgar_score1` int(2) DEFAULT NULL,
  `apgar_score2` int(2) DEFAULT NULL,
  `apgar_score3` int(2) DEFAULT NULL,
  `cabnormal` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`child_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_child`
--

LOCK TABLES `delivery_child` WRITE;
/*!40000 ALTER TABLE `delivery_child` DISABLE KEYS */;
/*!40000 ALTER TABLE `delivery_child` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distributor_detail`
--

DROP TABLE IF EXISTS `distributor_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `distributor_detail` (
  `distdet_id` int(11) NOT NULL AUTO_INCREMENT,
  `distributor_name` varchar(15) DEFAULT NULL,
  `dist_type_id` int(11) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  `drug_license` varchar(50) DEFAULT NULL,
  `gst_no` varchar(20) DEFAULT NULL,
  `aadhar_no` varchar(15) DEFAULT NULL,
  `pancard_no` varchar(15) DEFAULT NULL,
  `deletestatus` varchar(1) DEFAULT '0',
  PRIMARY KEY (`distdet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distributor_detail`
--

LOCK TABLES `distributor_detail` WRITE;
/*!40000 ALTER TABLE `distributor_detail` DISABLE KEYS */;
INSERT INTO `distributor_detail` VALUES (1,'OPD Pharmacy',2,'Shaheed Hospital','med.shaheedhospital@gmail.com','1234','1234','1234','1234','1234','0'),(2,'RAKESH MEDICALS',1,'NEW MARKET, DALLI RAJHARA','','9425562207','20B-21031,21B-21033','22ACGPJ6289C1ZR','','','0'),(3,'PHARMA DEAL',1,'SHYAM TALKIES ROAD, RAIPUR CHHATTISGARH','prembagree@yahoo.co.in','0771253789','20B-28858,21B-28859/31/12/2022','22AACHP3103M1ZI','','','0'),(4,'SUBHASH MEDICAL',1,'NEW MARKET, MAIN ROAD, DALLI RAJHARA, CHHATTISGARH','','9425562207','20B-21031,21B-21033','22ACGPJ6289C1ZE','','','0'),(5,'Central Stores',1,'Shaheed Hospital','med.shaheedhospital@gmail.com','123456','12345','123456','123456','123456','0');
/*!40000 ALTER TABLE `distributor_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distributor_type_detail`
--

DROP TABLE IF EXISTS `distributor_type_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `distributor_type_detail` (
  `dist_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `dist_type_name` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`dist_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distributor_type_detail`
--

LOCK TABLES `distributor_type_detail` WRITE;
/*!40000 ALTER TABLE `distributor_type_detail` DISABLE KEYS */;
INSERT INTO `distributor_type_detail` VALUES (1,'Medicines '),(2,'Medicine O');
/*!40000 ALTER TABLE `distributor_type_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `ename` varchar(40) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `contact` varchar(12) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `emptype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'admin','shd','00000','shd@shd.com','Admin'),(2,'staff','shd','00000','shd@shd.com','Staff'),(3,'Ramesh','Durg','00000','r@gmail.com','Doctor');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_detail`
--

DROP TABLE IF EXISTS `inventory_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory_detail` (
  `inv_id` int(11) NOT NULL AUTO_INCREMENT,
  `distdet_id` int(11) NOT NULL,
  `med_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `hsn_code` varchar(10) DEFAULT NULL,
  `quantity` varchar(10) DEFAULT NULL,
  `rate` float DEFAULT NULL,
  `unitprice` float DEFAULT NULL,
  `batch_no` varchar(15) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `manufacturing_date` date DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `free_med` varchar(5) DEFAULT NULL,
  `mrp` float DEFAULT NULL,
  `pack` varchar(5) DEFAULT NULL,
  `taxable_amt` float DEFAULT NULL,
  `cgst` float DEFAULT NULL,
  `sgst` float DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `rack_no` varchar(5) DEFAULT NULL,
  `temp_quantity` varchar(5) DEFAULT NULL,
  `drugdept_type` varchar(15) DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  `totalqty` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`inv_id`)
) ENGINE=InnoDB AUTO_INCREMENT=334 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_detail`
--

LOCK TABLES `inventory_detail` WRITE;
/*!40000 ALTER TABLE `inventory_detail` DISABLE KEYS */;
INSERT INTO `inventory_detail` VALUES (1,1,1,'2019-07-26','000','260',8,10,'FT331813','2021-07-31','2018-07-31',0,'0',10,'1 Tab',2080,0,0,2080,'1','0','','','260'),(2,1,3,'2019-07-26','0001','265',4,5,'IPAT-002','2021-09-30','2018-09-30',0,'0',5,'1 tab',1060,0,0,1060,'R1','0','','','265'),(3,1,7,'2019-07-26','001','200',8,10,'ZRC0001','2021-12-31','2018-12-31',0,'',10,'1 TAB',1600,0,0,1600,'R1','0','','','200'),(4,1,6,'2019-07-26','001','169',8,10,'VPT-18411D','2020-07-31','2018-07-31',0,'',10,'1 TAB',1352,0,0,1352,'R1','0','','','169'),(5,1,5,'2019-07-26','001','102',18,20,'VPT-18100T','2020-02-28','2018-02-28',0,'',20,'1 TAB',1836,0,0,1836,'R1','0','','','102'),(6,1,4,'2019-07-26','001','215',2,3,'W25829','2021-01-31','2018-01-31',0,'0',3,'1 tAB',430,0,0,430,'R1','0','','','215'),(7,1,12,'2019-07-26','001','1400',1.2,1.5,'VY0572','2022-04-30','2020-04-30',0,'',1.5,'1 TAB',1680,0,0,1680,'R1','0','','','1400'),(8,1,9,'2019-07-26','001','1200',0.8,1,'TA-8039','2020-10-31','2019-10-31',0,'',1,'1 TAB',960,0,0,960,'R1','0','','','1200'),(9,1,8,'2019-07-26','001','60',0.8,1,'AKT2073','2019-10-31','2018-10-31',0,'0',1,'1 TAB',48,0,0,48,'R1','0','','','60'),(10,1,18,'2019-07-26','001','394',0.8,1,'ZD1811029','2020-09-30','2018-09-30',0,'',1,'1 TAB',315.2,0,0,315.2,'R1','0','','','394'),(11,1,17,'2019-07-26','001','159',9,10,'ZA18018','2020-03-31','2019-03-31',0,'',10,'1 TAB',1431,0,0,1431,'R1','0','','','159'),(12,1,14,'2019-07-26','001','300',0.8,1,'ASK7002R','2019-08-31','2018-08-31',0,'0',1,'1 TAB',240,0,0,240,'R1','0','','','300'),(13,1,31,'2019-07-26','001','200',6,7,'SSD80718','2020-01-31','2018-01-31',0,'',7,'1 TAB',1200,0,0,1200,'R1','0','','','200'),(14,1,30,'2019-07-26','001','220',8,9,'EMP2877','2020-10-31','2018-10-31',0,'',9,'1 TAB',1760,0,0,1760,'R1','0','','','220'),(15,1,29,'2019-07-26','001','108',14,15,'8443017','2020-09-30','2018-09-30',0,'',15,'1 TAB',1512,0,0,1512,'R1','0','','','108'),(16,1,28,'2019-07-26','001','945',4,5,'FLT804','0020-01-31','2019-01-31',0,'',5,'1 TAB',3780,0,0,3780,'R1','0','','','945'),(17,1,27,'2019-07-26','001','360',3.3,3.5,'M0T181391','2021-01-31','2020-01-31',0,'',3.5,'1 TAB',1188,0,0,1188,'R1','0','','','360'),(18,1,26,'2019-07-26','001','160',1.3,1.5,'ZD19192','2021-02-28','2019-02-28',0,'0',1.5,'1 TAB',208,0,0,208,'R1','0','','','160'),(19,1,38,'2019-07-26','001','245',7,8,'LBB8003','2021-01-31','2020-01-31',0,'',8,'1 TAB',1715,0,0,1715,'R1','0','','','245'),(20,1,37,'2019-07-26','001','339',3,4,'LBA8011','2021-07-30','2019-07-30',0,'',4,'1 TAB',1017,0,0,1017,'R1','0','','','339'),(21,1,35,'2019-07-26','001','150',6,7,'UTCSXA8143','2020-05-31','2018-05-31',0,'',7,'1 TAB',900,0,0,900,'R1','0','','','150'),(22,1,34,'2019-07-26','001','1200',2.3,2.5,'NZB9001','2021-01-31','2019-01-31',0,'',2.5,'1 TAB',2760,0,0,2760,'R1','0','','','1200'),(23,1,33,'2019-07-26','001','1440',1.8,2,'PRB-190302','2021-02-28','2019-02-28',0,'0',2,'1 TAB',2592,0,0,2592,'R1','0','','','1440'),(24,1,54,'2019-07-26','01','91',7.9,8,'MGT-17569','2019-11-30','2018-11-30',0,'',8,'1 TAB',718.9,0,0,718.9,'R1','0','','','91'),(25,1,53,'2019-07-26','01','135',7.9,8,'EMU0999','2022-03-30','2019-03-30',0,'',8,'1 TAB',1066.5,0,0,1066.5,'R1','0','','','135'),(26,1,52,'2019-07-26','01','145',44.9,45,'KAVA9012','2020-01-30','2019-01-30',0,'',45,'1 TAB',6510.5,0,0,6510.5,'R1','0','','','145'),(27,1,51,'2019-07-26','01','200',2.9,3,'4189001','2021-02-28','2021-02-28',0,'',3,'1 TAB',580,0,0,580,'R1','0','','','200'),(28,1,50,'2019-07-26','01','220',0.9,1,'ZD18590','2020-05-30','2020-05-30',0,'',1,'1 TAB',198,0,0,198,'R1','0','','','220'),(29,1,49,'2019-07-26','001','42',5.9,6,'LVC18126','2020-02-28','2019-02-28',0,'',6,'1 TAB',247.8,0,0,247.8,'R1','0','','','42'),(30,1,48,'2019-07-26','001','250',0.9,1,'T-11669','2020-07-30','2019-07-30',0,'',1,'1 TAB',225,0,0,225,'R1','0','','','250'),(31,1,47,'2019-07-26','001','1000',0.9,1,'VLB8005','2021-06-30','2019-06-30',0,'',1,'1 TAB',900,0,0,900,'R1','0','','','1000'),(32,1,46,'2019-07-26','001','930',0.9,1,'AL3407','2020-11-30','2019-11-30',0,'',1,'1 TAB',837,0,0,837,'R1','0','','','930'),(33,1,45,'2019-07-26','001','110',0.9,1,'RID1805','2021-10-30','2019-10-30',0,'',1,'1 TAB',99,0,0,99,'R1','0','','','110'),(34,1,44,'2019-07-26','001','110',6.9,7,'ZD18776','2020-07-31','2019-07-31',0,'',7,'1 TAB',759,0,0,759,'R1','0','','','110'),(35,1,43,'2019-07-26','001','370',2.9,3,'MOT18557','2020-08-30','2019-08-30',0,'',3,'1 TAB',1073,0,0,1073,'R1','0','','','370'),(36,1,42,'2019-07-26','001','200',2.9,3,'AR5T-021','2021-04-30','2019-04-30',0,'',3,'1 TAB',580,0,0,580,'R1','0','','','200'),(37,1,41,'2019-07-26','001','455',4.6,4.8,'SA74279','2020-08-30','2018-08-30',0,'',4.8,'1 TAB',2093,0,0,2093,'R1','0','','','455'),(38,1,40,'2019-07-26','001','255',2,3,'JK19014','2022-01-31','2019-01-31',0,'',3,'1 TAB',510,0,0,510,'R1','0','','','255'),(39,1,39,'2019-07-26','001','220',0.4,0.5,'CGT0211','2022-10-31','2018-10-31',0,'0',0.5,'1 TAB',88,0,0,88,'R1','0','','','220'),(40,1,67,'2019-07-26','01','120',4.9,5,'GPD067009AS','2021-02-28','2019-02-28',0,'',5,'1 TAB',588,0,0,588,'R1','0','','','120'),(41,1,66,'2019-07-26','01','1000',1.4,1.5,'VPT-18647D','2020-11-30','2019-11-30',0,'',1.5,'1 TAB',1400,0,0,1400,'R1','0','','','1000'),(42,1,65,'2019-07-26','01','303',2.9,3,'LOT27S17015','2019-10-30','2019-10-30',0,'',3,'1 TAB',878.7,0,0,878.7,'R1','0','','','303'),(43,1,64,'2019-07-26','01','340',1.9,2,'GLIMEPERIDE TAB','0020-04-30','2020-04-30',0,'',2,'1 TAB',646,0,0,646,'R1','0','','','340'),(44,1,63,'2019-07-26','01','440',3.9,4,'TPPKAJ03','2020-08-30','2019-08-30',0,'',4,'1 TAB',1716,0,0,1716,'R1','0','','','440'),(45,1,62,'2019-07-26','01','1000',0.9,1,'AP9029','2021-01-30','2020-01-30',0,'',1,'1 TAB',900,0,0,900,'R1','0','','','1000'),(46,1,61,'2019-07-26','1','500',0.4,0.5,'7-11591','2020-06-30','2020-06-30',0,'',0.5,'1 TAB',200,0,0,200,'R1','0','','','500'),(47,1,60,'2019-07-26','01','273',2.9,3,'FRUSEMIDE AND S','2021-07-30','2021-07-30',0,'',3,'1 TAB',791.7,0,0,791.7,'R1','0','','','273'),(48,1,59,'2019-07-26','01','900',0.9,1,'SHP8CP1','2020-11-30','2020-11-30',0,'',1,'1 TAB',810,0,0,810,'R1','0','','','900'),(49,1,58,'2019-07-26','01','29',9.9,10,'G1228003','2020-03-30','2020-03-30',0,'',10,'1 TAB',287.1,0,0,287.1,'R1','0','','','29'),(50,1,57,'2019-07-26','01','1800',0.9,1,'T-0542/18','2020-10-30','2020-10-30',0,'',1,'1 TAB',1620,0,0,1620,'R1','0','','','1800'),(51,1,56,'2019-07-26','01','100',13.9,14,'BSS2768','2019-11-30','2018-11-30',0,'',14,'1 TAB',1390,0,0,1390,'R1','0','','','100'),(52,1,55,'2019-07-26','01','67',3.9,4,'JK17006','2020-01-31','2019-01-31',0,'0',4,'1 TAB',261.3,0,0,261.3,'R1','0','','','67'),(53,1,78,'2019-07-26','01','28',9.9,10,'G802728','2020-03-30','2019-03-30',0,'',10,'1 TAB',277.2,0,0,277.2,'R1','0','','','28'),(54,1,77,'2019-07-26','01','4600',0.9,1,'I2D18033','2020-10-30','2019-10-30',0,'',1,'1 TAB',4140,0,0,4140,'R1','0','','','4600'),(55,1,76,'2019-07-26','01','792',1.65,1.66,'001A8ABC','2019-10-30','2018-10-30',0,'',1.66,'1 TAB',1306.8,0,0,1306.8,'R1','0','','','792'),(56,1,75,'2019-07-26','01','120',6.5,6.6,'SLH-17104','2020-11-30','2019-11-30',0,'',6.6,'1 TAB',780,0,0,780,'R1','0','','','120'),(57,1,74,'2019-07-26','01','200',9.9,10,'LKD1T010','2020-05-30','2019-05-30',0,'',10,'1 TAB',1980,0,0,1980,'R1','0','','','200'),(58,1,73,'2019-07-26','01','95',5.9,6,'PC8003','2019-12-30','2018-12-30',0,'',6,'1 TAB',560.5,0,0,560.5,'R1','0','','','95'),(59,1,72,'2019-07-26','01','38',19,20,'EV19001','2021-12-30','2019-12-30',0,'',20,'1 TAB',722,0,0,722,'R1','0','','','38'),(60,1,71,'2019-07-26','01','900',0.5,0.6,'SBB8027','2020-04-30','2019-04-30',0,'',0.6,'1 TAB',450,0,0,450,'R1','0','','','900'),(61,1,70,'2019-07-26','01','200',0.9,1,'IMIPREMIN HYDRO','2019-12-30','2018-12-30',0,'',1,'1 TAB',180,0,0,180,'R1','0','','','200'),(62,1,69,'2019-07-26','01','172',0.9,1,'C171217','2020-09-30','2019-09-30',0,'',1,'1 TAB',154.8,0,0,154.8,'R1','0','','','172'),(63,1,68,'2019-07-26','01','200',1.9,2,'BSA19003','2021-12-31','2019-12-31',0,'0',2,'1 TAB',380,0,0,380,'R1','0','','','200'),(64,2,79,'2019-07-26','01','',10.5,50,'ILKS-013','2020-10-30','2018-11-30',0,'0',50,'1 BOT',210,6,6,235.2,'S1','0','','','20'),(65,1,69,'2019-07-26','01','172',0.9,1,'C171217','2020-09-30','2020-09-30',0,'',1,'1 TAB',154.8,0,0,154.8,'R1','0','','','172'),(66,1,68,'2019-07-26','01','200',1.9,2,'BSA19003','2021-12-30','2019-12-30',0,'0',2,'1 TAB',380,0,0,380,'R1','0','','','200'),(67,1,104,'2019-07-26','01','1800',0.7,0.8,'BR9731068','2021-03-30','2020-03-30',0,'',0.8,'1 TAB',1260,0,0,1260,'R1','0','','','1800'),(68,1,103,'2019-07-26','01','40',7.9,8,'BA83472','2020-08-30','2019-08-30',0,'',8,'1 TAB',316,0,0,316,'R1','0','','','40'),(69,1,102,'2019-07-26','01','90',5.9,6,'140','2019-09-30','2018-09-30',0,'',6,'1 TAB',531,0,0,531,'R1','0','','','90'),(70,1,101,'2019-07-26','01','140',4.9,5,'JK18003','2022-02-28','2020-02-28',0,'',5,'1 TAB',686,0,0,686,'R1','0','','','140'),(71,1,100,'2019-07-26','1','870',0.9,1,'MT182340','2021-02-28','2019-02-28',0,'',1,'1 TAB',783,0,0,783,'R1','0','','','870'),(72,1,99,'2019-07-26','01','500',0.9,1,'PCD0535','2021-08-30','2019-08-30',0,'',1,'1 TAB',450,0,0,450,'R1','0','','','500'),(73,1,98,'2019-07-26','01','420',0.9,1,'X55977','2020-06-30','2019-06-30',0,'',1,'1 TAB',378,0,0,378,'R1','0','','','420'),(74,1,97,'2019-07-26','01','1000',1.1,1.2,'S703125','2019-11-30','2018-11-30',0,'',1.2,'1 TAB',1100,0,0,1100,'R1','0','','','1000'),(75,1,96,'2019-07-26','01','482',1.9,2,'GDB8008','2021-09-30','2020-09-30',0,'',2,'1 TAB',915.8,0,0,915.8,'R1','0','','','482'),(76,1,95,'2019-07-26','01','78',3.9,4,'9NA003','2021-07-30','2020-07-30',0,'',4,'1 TAB',304.2,0,0,304.2,'R1','0','','','78'),(77,1,94,'2019-07-26','01','206',0.9,1,'VVD0226','2019-10-30','2018-10-30',0,'',1,'1 TAB',185.4,0,0,185.4,'R1','0','','','206'),(78,1,1,'2019-07-26','01','260',9.9,10,'FT331813','2021-07-30','2019-07-30',0,'',10,'1 TAB',2574,0,0,2574,'R1','0','','','260'),(79,1,93,'2019-07-26','1','140',4.9,5,'19043','2020-12-30','2019-12-30',0,'',5,'1 TAB',686,0,0,686,'R1','0','','','140'),(80,1,92,'2019-07-26','1','100',6.9,7,'S756259','2021-03-30','2019-03-30',0,'',7,'1 TAB',690,0,0,690,'R1','0','','','100'),(81,1,91,'2019-07-26','01','101',3.9,4,'17NT1032','2019-09-30','2018-09-30',0,'',4,'1 TAB',393.9,0,0,393.9,'R1','0','','','101'),(82,1,90,'2019-07-26','01','965',3.9,4,'AAAA29','2021-01-30','2019-01-30',0,'',4,'1 TAB',3763.5,0,0,3763.5,'R1','0','','','965'),(83,1,89,'2019-07-26','01','128',6.9,7,'112218009','2020-04-30','2019-04-30',0,'',7,'1 TAB',883.2,0,0,883.2,'R1','0','','','128'),(84,1,88,'2019-07-26','01','420',0.9,1,'ACG8029','2021-11-30','2019-11-30',0,'',1,'1 TAB',378,0,0,378,'R1','0','','','420'),(85,1,87,'2019-07-26','01','110',7.9,8,'MT182387','2021-02-28','2020-02-28',0,'',8,'1 TAB',869,0,0,869,'R1','0','','','110'),(86,1,86,'2019-07-26','01','710',2.9,3,'INA8020','2020-02-28','2018-02-28',0,'',3,'1 TAB',2059,0,0,2059,'R1','0','','','710'),(87,1,85,'2019-07-26','01','89',0.9,1,'T1709192','2019-08-30','2019-08-30',0,'0',1,'1 TAB',80.1,0,0,80.1,'R1','0','','','89'),(88,1,117,'2019-07-26','01','241',1.9,2,'SB80337','0019-10-30','2018-10-30',0,'',2,'1 TAB',457.9,0,0,457.9,'R1','0','','','241'),(89,1,116,'2019-07-26','01','300',1.9,2,'TE19128','2020-10-30','2019-10-30',0,'',2,'1 TAB',570,0,0,570,'R1','0','','','300'),(90,1,115,'2019-07-26','01','294',1.2,1.3,'2F79E011','2021-08-30','2020-08-30',0,'',1.3,'1 TAB',352.8,0,0,352.8,'R1','0','','','294'),(91,1,114,'2019-07-26','01','200',13.9,14,'AKT3545','2020-08-30','2020-08-30',0,'',14,'1 TAB',2780,0,0,2780,'R1','0','','','200'),(92,1,113,'2019-07-26','01','1000',0.9,1,'R0356E','2020-10-30','2019-10-30',0,'',1,'1 TAB',900,0,0,900,'R1','0','','','1000'),(93,1,112,'2019-07-26','01','600',0.7,0.8,'1904034','2021-03-30','2020-03-30',0,'',0.8,'1 TAB',420,0,0,420,'R1','0','','','600'),(94,1,111,'2019-07-26','01','69',13.9,14,'TZ2T-023','2021-11-30','2021-11-30',0,'',14,'1 TAB',959.1,0,0,959.1,'R1','0','','','69'),(95,1,109,'2019-07-26','01','260',5.9,6,'77EPB18006','2020-11-30','2019-11-30',0,'',6,'1 TAB',1534,0,0,1534,'R1','0','','','260'),(96,1,108,'2019-07-26','01','253',3.9,4,'AP8042','2020-01-30','2019-01-30',0,'',4,'1 TAB',986.7,0,0,986.7,'R1','0','','','253'),(97,1,2,'2019-07-26','01','86',4.9,5,'HT3073','2019-10-30','2018-10-30',0,'',5,'1 TAB',421.4,0,0,421.4,'R1','0','','','86'),(98,1,107,'2019-07-26','01','390',0.15,0.16,'K470175','2020-05-30','2019-05-30',0,'',0.16,'1 TAB',58.5,0,0,58.5,'R1','0','','','390'),(99,1,106,'2019-07-26','01','380',7.9,8,'QD18135','2020-06-30','2019-06-30',0,'0',8,'1 TAB',3002,0,0,3002,'R1','0','','','380'),(100,1,212,'2019-07-26','01','130',4.9,5,'A706979','2020-06-30','2019-06-30',0,'',5,'1 CAP',637,0,0,637,'C1','0','','','130'),(101,1,211,'2019-07-26','01','190',4.9,5,'A706979','2019-10-30','2018-10-30',0,'0',5,'1 CAP',931,0,0,931,'C1','0','','','190'),(102,1,192,'2019-07-26','01','80',4.9,5,'KD1902001','2020-07-30','2019-07-30',0,'',5,'1 CAP',392,0,0,392,'C1','0','','','80'),(103,1,188,'2019-07-26','01','160',22.9,23,'DNZX1C-007','2021-04-30','2020-04-30',0,'',23,'1 CAP',3664,0,0,3664,'C1','0','','','160'),(104,1,183,'2019-07-26','01','65',11.9,12,'ZC18033','2020-04-30','2019-04-30',0,'',12,'1 CAP',773.5,0,0,773.5,'C1','0','','','65'),(105,1,180,'2019-07-26','1','200',4.9,5,'8283418','2020-11-30','2019-11-30',0,'0',5,'1 CAP',980,0,0,980,'C1','0','','','200'),(106,1,199,'2019-07-26','01','330',0.9,1,'M819166','2020-05-30','2019-05-30',0,'',1,'1 CAP',297,0,0,297,'C1','0','','','330'),(107,1,197,'2019-07-26','01','410',0.9,1,'229','2020-10-30','2019-10-30',0,'',1,'1 CAP',369,0,0,369,'C1','0','','','410'),(108,1,196,'2019-07-26','01','150',4.9,5,'NP673001','2020-06-30','2020-06-30',0,'',5,'1 CAP',735,0,0,735,'C1','0','','','150'),(109,1,195,'2019-07-26','01','220',8.9,9,'CC-180042','2020-06-30','2019-06-30',0,'',9,'1 CAP',1958,0,0,1958,'C1','0','','','220'),(110,1,194,'2019-07-26','01','409',2.4,2.5,'MC18-09','2021-02-28','2020-02-28',0,'',2.5,'1 CAP',981.6,0,0,981.6,'C1','0','','','409'),(111,1,249,'2019-07-26','01','188',6.7,7,'58CDS536','2020-03-30','2019-03-30',0,'0',7,'1 CAP',1259.6,0,0,1259.6,'C1','0','','','188'),(112,1,208,'2019-07-26','01','28',24.9,25,'0061218D','2020-11-30','2019-11-30',0,'',25,'1 CAP',697.2,0,0,697.2,'C1','0','','','28'),(113,1,207,'2019-07-26','1','155',0.9,1,'VHF18073','2020-08-30','2019-08-30',0,'',1,'1 CAP',139.5,0,0,139.5,'C1','0','','','155'),(114,1,206,'2019-07-26','1','331',14.9,15,'FT181105','2020-09-30','2019-09-30',0,'',15,'1 CAP',4931.9,0,0,4931.9,'C1','0','','','331'),(115,1,205,'2019-07-26','1','200',3.9,4,'PWRAS02','2020-06-30','2019-06-30',0,'',4,'1 CAP',780,0,0,780,'C1','0','','','200'),(116,1,202,'2019-07-26','01','210',12.9,13,'DM660','2020-08-30','2020-08-30',0,'',13,'1 CAP',2709,0,0,2709,'C1','0','','','210'),(117,1,200,'2019-07-26','1','440',1.9,2,'PC9035','2020-12-30','2020-12-30',0,'0',2,'1 CAP',836,0,0,836,'C1','0','','','440'),(118,1,212,'2019-07-26','01','130',4.9,5,'C-12076','2020-06-30','2019-06-30',0,'',5,'1 CAP',637,0,0,637,'C1','0','','','130'),(119,1,211,'2019-07-26','1','190',4.9,5,'A706979','2019-10-30','2019-10-30',0,'',5,'1 CAP',931,0,0,931,'C1','0','','','190'),(120,1,210,'2019-07-26','01','334',2.9,3,'ITGC-002','2020-03-30','2019-03-30',0,'',3,'1 CAP',968.6,0,0,968.6,'C1','0','','','334'),(121,1,209,'2019-07-26','1','290',1.9,2,'M26BP19050','2021-04-30','2020-04-30',0,'0',2,'1 CAP',551,0,0,551,'C1','0','','','290'),(122,4,282,'2019-07-27','3004','50',12.06,3.05,'PMB-18002','2021-09-30','2018-10-01',0,'',30.5,'10 TA',603,6,6,675.36,'TR4 L','500','','','500'),(123,4,128,'2019-07-27','3004','80',5.5,3.364,'B680606','2021-07-30','0000-00-00',0,'0',33.64,'10 TA',440,6,6,492.8,'TR1 L','800','','','800'),(124,4,284,'2019-07-27','3004','',4.75,320,'JTDI-019','2021-04-30','2019-05-01',0,'0',320,'2 ML',475,6,6,532,'IR10 ','100','','','100'),(125,4,285,'2019-07-27','3004','',4,25,'PC-212','2020-08-30','2018-09-01',0,'0',25,'10 ML',796,6,6,891.52,'IR9 L','199','','','199'),(126,1,223,'2019-07-26','3004','',12.5,45.48,'CD180324','2020-11-30','2018-12-01',0,'',45.48,'30 ML',62.5,6,6,70,'SR1','0','','','5'),(127,1,17,'2019-07-26','2004','50',50,10,'ZA18018','2020-03-30','2018-10-01',0,'0',60,'6 TAB',2500,6,6,2800,'LC1','0','','','300'),(128,1,287,'2019-07-26','3004','',80,123,'8085','2020-05-30','2018-12-01',0,'',123,'200 M',240,0,0,240,'SR1','0','','','3'),(129,1,286,'2019-07-26','3004','',40,55.6,'ZA18453','2019-12-30','2018-07-01',0,'',55.6,'100 M',200,0,0,200,'SR1','0','','','5'),(130,1,79,'2019-07-26','3004','',30,66.5,'ILKS-013','2020-10-30','2018-11-01',0,'0',66.5,'100 M',600,0,0,600,'SR1','0','','','20'),(131,1,289,'2019-07-26','3004','',80,105,'19407','2021-04-30','2019-05-01',0,'',105,'100 M',480,0,0,480,'SR1','0','','','6'),(132,1,288,'2019-07-26','3004','',15,39,'133','2020-12-30','2019-01-01',0,'',39,'400 M',45,0,0,45,'SR1','0','','','3'),(133,1,222,'2019-07-26','3004','',80,120,'SL0305','2020-01-30','2018-08-01',0,'0',120,'200 M',240,0,0,240,'SR1','0','','','3'),(134,1,292,'2019-07-26','3004','',50,77,'IKML-009','2021-08-30','2018-09-01',0,'',77,'170 M',600,0,0,600,'SR1','12','','','12'),(135,1,291,'2019-07-26','3004','',15,27.3,'ATPB8005DA','2020-11-30','2018-12-01',0,'',27.3,'30 ML',300,0,0,300,'SR1','20','','','20'),(136,1,290,'2019-07-26','3004','',10,20,'SO180055','2020-09-30','2018-10-01',0,'0',20,'60 ML',250,0,0,250,'SR1','0','','','25'),(137,1,58,'2019-07-26','3004','150',7,10,'G1228003','2020-03-30','2018-04-01',0,'',10,'1 TAB',1050,0,0,1050,'TR2 L','0','','','150'),(138,1,57,'2019-07-26','3004','120',7,1,'T-0542/18','2020-10-30','2018-11-01',0,'0',10,'10 TA',840,0,0,840,'TR2 L','0','','','1200'),(139,1,59,'2019-07-26','3004','100',30,1,'SHT8871','2020-10-30','2018-11-01',0,'0',45,'45 TA',3000,0,0,3000,'TR2 L','0','','','4500'),(140,1,82,'2019-07-26','3004','120',20,2,'PRB-190302','2021-02-28','2019-03-01',0,'0',30,'15 TA',2400,0,0,2400,'TR1 L','0','','','1800'),(141,1,182,'2019-07-26','3004','20',40,5,'C-12076','2020-06-30','2018-07-01',0,'',50,'10 CA',800,0,0,800,'R3 L1','0','','','200'),(142,1,293,'2019-07-26','3004','40',40,5,'B283418','2020-11-30','2018-12-01',0,'0',50,'10 CA',1600,0,0,1600,'R3 L1','0','','','400'),(143,5,294,'2019-07-30','001','',6,8,'RPF318','2021-02-28','2019-02-28',0,'0',8,'10 ML',480,0,0,480,'R8','80','','','80'),(144,5,295,'2019-07-30','001','',40,46.8,'RPF318','2021-02-28','2019-02-28',0,'0',46.8,'40 GM',3280,0,0,3280,'R9','82','','','82'),(145,5,300,'2019-07-30','001','',70,77.2,'219DP003','2022-05-31','2018-12-31',0,'',77.2,'1 GM',1750,0,0,1750,'9','25','','','25'),(146,5,300,'2019-07-30','011','',28,31,'47688','2019-12-31','2018-12-31',0,'',31,'1 GM',224,0,0,224,'9','8','','','8'),(147,5,299,'2019-07-30','001','',18,20,'I-6463C','2020-05-31','2019-03-31',0,'',20,'1.5 M',1620,0,0,1620,'9','90','','','90'),(148,5,297,'2019-07-30','001','',30,36.06,'19180616','2021-08-31','2019-03-31',0,'',36.06,'1 GM',600,0,0,600,'9','20','','','20'),(149,5,262,'2019-07-30','001','',50,56.67,'ICX-0491','2020-11-30','2018-12-31',0,'0',56.67,'1 GM',13000,0,0,13000,'9','220','','','260'),(150,2,302,'2019-07-29','3004','',48,50,'8A096','2020-08-30','2018-09-01',0,'',50,'3 ML',576,6,6,645.12,'IR7 L','12','','','12'),(151,2,114,'2019-07-29','3004','100',63,14,'TRC-1901','2021-05-30','2019-06-30',0,'0',140,'10 TA',6300,2.5,2.5,6615,'TR5 L','1000','','','1000'),(152,5,295,'2019-07-30','001','',42,46.8,'RPF318','2021-02-28','2019-02-28',0,'',46.8,'40 mg',2352,0,0,2352,'9','56','','','56'),(153,5,295,'2019-07-30','001','',42,46.76,'C03860','2020-05-31','2018-12-31',0,'',46.76,'40 MG',924,0,0,924,'9','22','','','22'),(154,5,0,'2019-07-30','001','',300,325.6,'WIC1710','2020-11-30','2020-12-31',0,'',325.6,'1 GM',300,0,0,300,'9','1','','','1'),(155,5,262,'2019-07-30','001','',53,56.67,'ICX-0567','2019-05-31','2019-06-30',0,'',56.67,'1 GM',53,0,0,53,'9','1','','','1'),(156,5,301,'2019-07-30','001','',23,25,'RC-G61','2021-03-31','2019-04-30',0,'0',25,'10 ML',552,0,0,552,'9','24','','','24'),(157,5,304,'2019-07-30','001','',110,116,'RTE117','2020-10-31','2018-11-30',0,'',116,'1 ML',3740,0,0,3740,'9','34','','','34'),(158,5,285,'2019-07-30','001','',20,25.53,'237','2021-02-28','2019-03-31',0,'0',25.53,'10 ML',1780,0,0,1780,'9','89','','','89'),(159,4,98,'2019-07-30','000','120',15,1.33333,'75333S','2021-01-30','2019-02-01',0,'',20,'15 TA',1800,6,6,2016,'TR4 L','1800','','','1800'),(160,4,257,'2019-07-30','000','',85,150,'A19027PP','2021-04-01','2019-05-01',0,'',150,'1 GM',4250,6,6,4760,'IR8 L','50','','','50'),(161,4,306,'2019-07-30','000','',105,120,'QT10143','2020-08-30','2018-09-01',0,'',120,'10 ML',5250,2.5,2.5,5512.5,'BF','50','','','50'),(162,4,305,'2019-07-30','000','',15,20,'920-092025','2020-12-30','2019-01-01',0,'',20,'1 ML',7500,6,6,8400,'SF','400','','','500'),(163,4,209,'2019-07-30','000','100',22,2.5,'M16BP19250','2021-06-30','2019-04-01',0,'',25,'10 CA',2200,6,6,2464,'TR3 L','1000','','','1000'),(164,4,178,'2019-07-30','000','900',21.6,0.075,'02962P','2021-05-30','2019-02-01',0,'',1.5,'20 TA',19440,6,6,21772.8,'TR1 L','18000','','','18000'),(165,4,284,'2019-07-30','000','',16.6,20,'949233','2021-04-30','2019-04-01',0,'',20,'2 ML',1660,6,6,1859.2,'IR10 ','100','','','100'),(166,4,100,'2019-07-30','000','200',5.5,1,'MOT181476','2021-02-28','2019-03-01',0,'',10,'10 TA',1100,6,6,1232,'TR4 L','2000','','','2000'),(167,4,1,'2019-07-30','000','40',83,10,'FT331907','2021-09-30','2019-04-01',0,'',100,'10 TA',3320,6,6,3718.4,'TR4 L','400','','','400'),(168,4,252,'2019-07-30','000','',9.71,20,'820-07195J','2020-11-30','2018-12-01',0,'',20,'12 LA',485.5,6,6,543.76,'IR8 L','50','','','50'),(169,4,303,'2019-07-30','000','',44,59.98,'LPR-988','2021-04-30','2019-05-01',0,'0',59.98,'200 M',2200,6,6,2464,'S2 L1','50','','','50'),(170,5,59,'2019-07-30','000','350',4.62,0.465,'6189','2021-02-28','2019-03-01',0,'',4.65,'10 TA',1617,0,0,1617,'S4 L2','3500','','','3500'),(171,5,194,'2019-07-30','000','100',12.9,1.29,'6139','2020-11-30','2018-12-01',0,'',12.9,'10 CA',1290,0,0,1290,'S4 L2','1000','','','1000'),(172,5,126,'2019-07-30','000','25',5,0.5,'6162','2021-01-30','2019-02-01',0,'',5,'10 TA',125,0,0,125,'S4 L2','250','','','250'),(173,5,193,'2019-07-30','000','200',21.9,3,'6218','2021-04-30','2019-05-01',0,'',30,'10 CA',4380,0,0,4380,'S4 L2','2000','','','2000'),(174,5,314,'2019-07-30','000','',72.5,72.5,'E48','2021-02-28','2019-03-01',0,'',72.5,'30 GR',4132.5,0,0,4132.5,'S4 L2','57','','','57'),(175,5,313,'2019-07-30','000','300',28,2.8,'6157','2021-01-30','2019-02-01',0,'',28,'10 TA',8400,0,0,8400,'S4 L2','3000','','','3000'),(176,5,312,'2019-07-30','000','',820,820,'LC-137','2021-11-30','2018-12-01',0,'',820,'4.5 L',1640,0,0,1640,'S4 L1','2','','','2'),(177,5,311,'2019-07-30','000','',18.5,18.5,'B390','2020-09-30','2018-10-01',0,'',18.5,'15 GM',3681.5,0,0,3681.5,'S4 L1','199','','','199'),(178,5,310,'2019-07-30','000','480',45,4.95,'26210','2021-07-30','2019-02-01',0,'',49.5,'10 TA',21600,0,0,21600,'S4 L2','4800','','','4800'),(179,5,309,'2019-07-30','000','2',270,0.275,'PR4391R','2020-09-30','2019-04-01',0,'',275,'1000 ',540,0,0,540,'S4 L1','2000','','','2000'),(180,5,308,'2019-07-30','000','50',12,1.433,'25938','2020-10-30','2018-05-10',0,'',14.33,'10 TA',600,0,0,600,'S4 L1','500','','','500'),(181,5,13,'2019-07-30','000','650',4,0.565,'6217','2021-04-30','2019-05-01',0,'',5.65,'10 TA',2600,0,0,2600,'S4 L1','6500','','','6500'),(182,5,28,'2019-07-30','000','120',130,13.966,'PG0060','2024-06-30','2019-01-01',0,'0',139.66,'10 TA',15600,0,0,15600,'S4 L1','1200','','','1200'),(183,5,318,'2019-07-30','000','',16,18.8,'ASM9006','2022-02-28','2019-03-01',0,'',18.8,'60 ML',368,0,0,368,'S1 L1','23','','','23'),(184,5,289,'2019-07-30','000','',80,105,'19028-02','2020-12-30','2019-01-01',0,'',105,'100 M',4080,0,0,4080,'S1 L1','51','','','51'),(185,5,292,'2019-07-30','000','',70,77,'IKML-009','2021-08-30','2018-09-01',0,'',77,'170 M',2100,0,0,2100,'S1 L1','30','','','30'),(186,5,317,'2019-07-30','000','',168,168,'BB1903092','2021-02-28','2019-03-01',0,'',168,'1 PCS',8400,0,0,8400,'S1 LT','50','','','50'),(187,5,288,'2019-07-30','000','',30,39,'133','2020-12-30','2019-01-01',0,'',39,'400 M',510,0,0,510,'S2 L3','17','','','17'),(188,5,316,'2019-07-30','000','',40,45.92,'GRA8013','2020-01-30','2018-08-01',0,'',45.92,'100 M',0,0,0,0,'S2 L3','0','','','0'),(189,5,315,'2019-07-30','000','',60,67.2,'TPE0104','2021-04-30','2019-05-01',0,'',67.2,'200 M',960,0,0,960,'S2 L2','16','','','16'),(190,5,57,'2019-07-30','000','400',3,0.3,'FF-1812','2020-10-30','2018-11-01',0,'0',3,'10 TA',1200,0,0,1200,'S4 L2','4000','','','4000'),(191,5,319,'2019-07-30','000','',90,95,'5557','2020-11-30','2018-12-01',0,'',95,'400 M',3780,0,0,3780,'S1 L2','42','','','42'),(192,5,319,'2019-07-30','000','',140,150,'EX2137','2020-12-30','2019-01-01',0,'',150,'400 M',4620,0,0,4620,'S1 L2','33','','','33'),(193,5,290,'2019-07-30','000','',15,20,'SO180055','2020-09-30','2018-10-01',0,'0',20,'60 ML',9735,0,0,9735,'S1 L2','649','','','649'),(194,5,324,'2019-07-30','001','',40,45,'2213','2023-04-30','2018-04-30',0,'',45,'400 G',200,0,0,200,'9','5','','','5'),(195,5,323,'2019-07-30','001','',300,314,'9053661L1','2020-02-28','2019-02-28',0,'',314,'400 G',300,0,0,300,'9','1','','','1'),(196,5,322,'2019-07-30','001','',450,475,'D180408','2020-02-28','2018-08-31',0,'',475,'400 G',450,0,0,450,'9','1','','','1'),(197,5,322,'2019-07-30','001','',375,400,'038D001','2019-09-30','2018-04-30',0,'',400,'400 G',1875,0,0,1875,'9','5','','','5'),(198,5,320,'2019-07-30','001','',1400,1428,'NP573002','2021-02-28','2017-03-31',0,'',1428,'250 M',8400,0,0,8400,'9','6','','','6'),(199,5,320,'2019-07-30','001','',1600,1650,'NP573002','2020-09-30','2016-10-31',0,'0',1650,'250 M',11200,0,0,11200,'9','7','','','7'),(200,5,62,'2019-07-30','000','300',2.92,1,'6196','2022-03-30','2019-04-01',0,'',10,'10 TA',876,0,0,876,'TR2 L','3000','','','3000'),(201,5,63,'2019-07-30','000','300',4.48,4,'6234','2021-05-30','2019-06-01',0,'',40,'10 TA',1344,0,0,1344,'TR2 L','3000','','','3000'),(202,5,120,'2019-07-30','000','175',1.2,0.3,'6209','2022-03-30','2019-04-01',0,'',3,'10 TA',210,0,0,210,'TR1 L','1750','','','1750'),(203,5,183,'2019-07-30','000','100',37,4,'LC19107','2021-02-02','2019-03-01',0,'',40,'10 CA',3700,0,0,3700,'R3 L2','1000','','','1000'),(204,5,321,'2019-07-30','000','',12,15.9,'Z-18TP005','2021-10-30','2018-11-01',0,'',15.9,'10 ML',1200,0,0,1200,'R6 L4','100','','','100'),(205,5,43,'2019-07-30','000','200',20,3,'NT-181219','2020-11-30','2018-12-01',0,'0',30,'10 TA',4000,0,0,4000,'TR1 L','2000','','','2000'),(206,5,325,'2019-07-30','001','',400,410,'AB90182','2021-01-31','2019-08-22',0,'0',410,'300 M',4000,0,0,4000,'9','10','','','10'),(207,5,326,'2019-07-30','001','',20,25,'268115','2023-05-31','2018-06-30',0,'0',25,'1 PCS',44000,0,0,44000,'R10 L','2200','','','2200'),(208,2,327,'2019-07-30','3004','',3.3,5,'7371010G2','2022-08-30','2017-09-01',0,'0',5,'1 PCS',544.5,6,6,609.84,'SYR 1','165','','','165'),(209,5,331,'2019-07-31','001','',210,222.25,'905','2021-04-30','2019-05-31',0,'',222.25,'20',10920,0,0,10920,'F1','52','','','52'),(210,5,330,'2019-07-31','001','',12,14.5,'ILMI-002','2019-09-30','2018-04-30',0,'',14.5,'1',540,0,0,540,'F1','45','','','45'),(211,5,329,'2019-07-31','001','',15,17.8,'18AE46','2020-10-31','2018-11-30',0,'',17.8,'75',2700,0,0,2700,'F1','180','','','180'),(212,5,242,'2019-07-31','001','',2140,2243.57,'A10019001','2020-12-31','2019-12-31',0,'',2243.57,'300',8560,0,0,8560,'F1','4','','','4'),(213,5,328,'2019-07-31','001','',140,147.74,'19016','2021-12-31','2019-02-28',0,'0',147.74,'40',7140,0,0,7140,'F1','51','','','51'),(214,5,336,'2019-07-31','001','',1700,1819.04,'LSTKB2802','2020-02-28','2018-03-31',0,'',1819.04,'15000',3400,0,0,3400,'F1','2','','','2'),(215,5,335,'2019-07-31','001','',10,11.95,'KP32045','2020-10-31','2017-11-30',0,'',11.95,'1',100,0,0,100,'F1','10','','','10'),(216,5,242,'2019-07-31','001','',2100,2243.57,'A10018008','2020-04-30','2018-05-31',0,'',2243.57,'300',2100,0,0,2100,'F1','1','','','1'),(217,5,334,'2019-07-31','001','',40,42.24,'JACB7036','2020-02-28','2018-05-31',0,'',42.24,'15',480,0,0,480,'F1','12','','','12'),(218,5,332,'2019-07-31','001','',1400,1509.9,'SM2021','2019-12-31','2018-12-31',0,'0',1509.9,'3',7000,0,0,7000,'F1','5','','','5'),(219,5,112,'2019-07-31','001','50',100,107.52,'1904034','2021-03-30','2019-04-01',0,'0',107.52,'100',8100,0,0,8100,'R5 L1','8100','','','5000'),(220,5,340,'2019-07-26','001','',80,95,'ZA18495','2020-07-30','2018-08-01',0,'0',95,'200 M',1200,0,0,1200,'S2 L1','0','','','15'),(221,5,219,'2019-08-26','001','',30,50,'S193053','2021-02-28','2019-03-01',0,'0',50,'170 M',270,0,0,270,'S2 L1','0','','','9'),(222,5,314,'2019-08-26','001','',60,72.5,'E48','2021-02-28','2019-03-01',0,'',72.5,'30 GM',1200,0,0,1200,'S2 L1','0','','','20'),(223,5,343,'2019-08-26','001','',40,50,'DQN8004','2020-03-30','2018-04-01',0,'0',50,'10 GM',960,0,0,960,'R6 L2','0','','','24'),(224,5,346,'2019-08-26','001','',30,50,'N1901','2021-03-30','2019-04-01',0,'0',50,'15 GM',360,0,0,360,'R6 L2','0','','','12'),(225,5,341,'2019-07-31','001','17',25,5.52,'BNP48640','2020-12-31','2018-12-31',0,'0',27.6,'5 TAB',425,0,0,425,'F1','85','','','85'),(226,5,141,'2019-07-26','001','3',80,0.5,'G1873','2021-12-30','2019-12-30',0,'0',100,'200 T',240,0,0,240,'TR1 L','0','','','600'),(227,5,347,'2019-07-26','001','4',160,1,'DDL652','2020-10-30','2019-10-30',0,'0',200,'200 T',640,0,0,640,'TR1 L','0','','','800'),(228,5,97,'2019-07-26','001','5',100,1.2,'ZD18125','2020-11-30','2018-12-01',0,'',120,'100 T',500,0,0,500,'R6 L2','0','','','500'),(229,5,34,'2019-07-26','001','5',370,2.5,'NZB9006','2021-04-30','2019-05-01',0,'0',250,'100 T',1850,0,0,1850,'R5 L2','0','','','500'),(230,5,209,'2019-07-26','001','8',15,2,'M16BP19109','2021-06-30','2019-04-01',0,'',20,'10 CA',120,0,0,120,'R3 L1','0','','','80'),(231,5,50,'2019-07-26','001','18',8,1,'ZT1808','2020-07-30','2018-08-01',0,'0',10,'10 TA',144,0,0,144,'TR1 L','0','','','180'),(232,5,0,'2019-07-31','001','20',10,13.8,'BNP29192','2021-11-30','2018-12-31',0,'0',13.8,'5 TAB',1000,0,0,1000,'F1','100','','','100'),(233,5,180,'2019-07-26','001','40',30,5,'8283418','2020-11-30','2018-12-30',0,'0',50,'10 CA',1200,0,0,1200,'R3 L1','400','','','400'),(234,5,35,'2019-07-26','001','20',50,7,'UTGSZA8113','2020-05-30','2018-12-30',0,'',70,'10 TA',1000,0,0,1000,'R1 L3','0','','','200'),(235,5,63,'2019-07-26','001','140',25,4,'PPKAJ03','2020-08-30','2019-08-30',0,'0',40,'10 TA',3500,0,0,3500,'TR2 L','0','','','1400'),(236,5,344,'2019-07-31','001','10',30,6.98,'BNP48750','2022-12-31','2019-02-28',0,'',34.9,'5 TAB',300,0,0,300,'F1','50','','','50'),(237,5,344,'2019-07-31','001','14',30,6.98,'BNP48749','2021-11-30','2018-12-31',0,'',34.9,'5 TAB',420,0,0,420,'F1','70','','','70'),(238,5,348,'2019-07-31','001','20',65,13.8,'BNP29192','2021-11-30','2018-12-31',0,'0',69,'5 TAB',1300,0,0,1300,'F1','100','','','100'),(239,5,12,'2019-07-26','001','100',10,1.5,'BY0572','2020-04-30','2018-11-30',0,'',15,'10 TA',1000,0,0,1000,'TR1 L','0','','','1000'),(240,5,15,'2019-07-26','001','10',65,13,'LVC18126','2020-02-28','2018-09-30',0,'',78,'6 TAB',650,0,0,650,'TR1 L','0','','','60'),(241,5,27,'2019-07-26','001','30',40,5,'FLT804','2020-01-30','2019-01-30',0,'',50,'10 TA',1200,0,0,1200,'TR1 L','0','','','300'),(242,5,182,'2019-07-26','001','20',40,6,'C-12076','2020-06-30','2018-07-30',0,'',60,'10 CA',800,0,0,800,'R3 L1','0','','','200'),(243,5,62,'2019-07-26','001','200',7,1,'AP9029','2021-01-30','2019-02-28',0,'',10,'10 TA',1400,0,0,1400,'R2 L2','0','','','2000'),(244,5,113,'2019-07-26','001','5',80,1,'1904034','2021-03-30','2019-03-30',0,'',100,'100 T',400,0,0,400,'R5 L1','0','','','500'),(245,5,112,'2019-07-26','001','4',60,0.8,'R0356E','2020-10-30','2019-04-30',0,'0',80,'100 T',240,0,0,240,'R5 L1','0','','','400'),(246,5,345,'2019-07-31','001','',210,212.66,'IHEPB1828','2020-09-30','2018-10-31',0,'',212.66,'5 ML',630,0,0,630,'F1','3','','','3'),(247,5,345,'2019-07-31','001','',210,212.66,'IHEPB1834','2020-11-30','2018-12-31',0,'0',212.66,'5 ML',6300,0,0,6300,'F1','30','','','30'),(248,5,199,'2019-07-26','001','8',10,1,'M819166','2020-05-30','2018-12-30',0,'',15,'15 TA',80,0,0,80,'CR3 L','0','','','120'),(249,5,197,'2019-07-26','001','30',7,1,'229','2020-10-30','2019-10-30',0,'',10,'10 CA',210,0,0,210,'CR3 L','0','','','300'),(250,5,108,'2019-07-26','001','20',25,4,'AP8042','2020-01-30','2019-01-30',0,'',40,'10 TA',500,0,0,500,'TR4 L','0','','','200'),(251,5,200,'2019-07-26','001','150',15,2,'PC9132','2021-04-30','2019-05-30',0,'',20,'10 CA',2250,0,0,2250,'CR3 L','0','','','1500'),(252,5,120,'2019-07-26','001','80',7,1,'IG667','2021-10-30','2018-09-30',0,'',10,'10 TA',560,0,0,560,'TR1 L','0','','','800'),(253,5,196,'2019-07-26','001','10',35,5,'NP673007','2021-02-28','2019-03-30',0,'',50,'10 CA',350,0,0,350,'TR3 L','0','','','100'),(254,5,92,'2019-07-26','001','10',50,7,'5758259','2021-03-30','2018-04-30',0,'',70,'10 TA',500,0,0,500,'TR4 L','0','','','100'),(255,5,349,'2019-07-26','001','10',40,5,'KD1902001','2020-07-30','2019-02-28',0,'0',50,'10 CA',400,0,0,400,'CR3 L','0','','','100'),(256,5,339,'2019-07-31','001','24',120,25.284,'DLA18034','2020-05-31','2019-02-28',0,'',126.42,'5 TAB',2880,0,0,2880,'F1','120','','','120'),(257,5,338,'2019-07-31','001','20',40,8.86,'SC19004','2020-12-31','2019-12-31',0,'',44.3,'5 TAB',800,0,0,800,'F1','100','','','100'),(258,5,350,'2019-07-31','001','',140,148.38,'QT101443','2020-08-31','2018-09-30',0,'',148.38,'40 IU',7000,0,0,7000,'F1','50','','','50'),(259,5,339,'2019-07-31','001','1',110,24.16,'T701079','2020-09-30','2016-12-31',0,'',120.8,'5 TAB',110,0,0,110,'F1','5','','','5'),(260,5,339,'2019-07-31','001','6',110,24.16,'T900011','2021-08-31','2018-09-30',0,'',120.8,'5 TAB',660,0,0,660,'F1','30','','','30'),(261,5,338,'2019-07-31','001','9',40,8.568,'1700939','2020-08-31','2017-09-30',0,'0',42.84,'5 MG',360,0,0,360,'F1','45','','','45'),(263,5,352,'2019-07-31','001','',280,290,'08906038070195','2021-12-31','2018-08-31',0,'',290,'100 I',2800,0,0,2800,'F1','10','','','10'),(264,5,351,'2019-07-31','001','',23,26.13,'23081003D','2021-12-31','2018-02-28',0,'',26.13,'1.25 ',1150,0,0,1150,'F1','50','','','50'),(265,5,351,'2019-07-31','001','',25,27.04,'I86T0X0094','2021-08-31','2018-09-30',0,'0',27.04,'1.25 ',1175,0,0,1175,'F1','47','','','47'),(266,5,90,'2019-07-26','001','60',30,5,'AAAA29','2021-01-30','2019-01-30',0,'',50,'10 TA',1800,0,0,1800,'TR2 L','0','','','600'),(267,5,128,'2019-07-26','001','35',3,0.2,'V801009','2020-08-30','2018-09-30',0,'',3,'15 TA',105,0,0,105,'TR2 L','0','','','525'),(268,5,7,'2019-07-26','001','100',8,10,'ZRC0001','2021-12-30','2019-01-30',0,'',10,'1 TAB',800,0,0,800,'TR1 L','0','','','100'),(269,5,100,'2019-07-26','001','30',7,1,'MOT181476','2021-02-28','2019-03-30',0,'',10,'10 TA',210,0,0,210,'TR4 L','0','','','300'),(270,5,50,'2019-07-26','000','10',7,1,'EM0J1261','2021-04-30','2018-08-30',0,'',10,'10 TA',70,0,0,70,'TR1 L','0','','','100'),(271,5,44,'2019-07-26','001','10',35,7,'ZD18776','2020-07-30','2018-08-30',0,'',42,'6 TAB',350,0,0,350,'TR1 L','0','','','60'),(272,5,27,'2019-07-26','001','50',30,3.5,'MOT81391','2021-01-30','2019-02-28',0,'',35,'10 TA',1500,0,0,1500,'TR1 L','0','','','500'),(273,5,133,'2019-07-26','000','30',20,1,'IG900652','2022-02-28','2019-04-30',0,'0',30,'30 TA',600,0,0,600,'TR2 L','0','','','900'),(274,5,158,'2019-07-26','001','2',200,0.5,'3A9001A','2021-12-30','2019-01-30',0,'',250,'500 T',400,0,0,400,'TR4 L','0','','','1000'),(275,5,353,'2019-07-26','001','50',20,1.5,'02962T','2021-05-30','2019-04-30',0,'',30,'20 TA',1000,0,0,1000,'TR1 L','0','','','1000'),(276,5,207,'2019-07-26','001','20',7,1,'VTF1808073','2020-08-30','2019-08-30',0,'0',10,'10 CA',140,0,0,140,'CR1','0','','','200'),(277,2,356,'2019-07-31','3004','',3.75,4.92,'GE258102D','2021-09-30','2018-10-30',0,'0',4.92,'2 ML',375,6,6,420,'IR8 L','100','','','100'),(278,5,357,'2019-07-31','001','',50,54.94,'KMI804','2021-05-31','2018-06-30',0,'',54.94,'5 ML',50,0,0,50,'F1','1','','','1'),(279,5,355,'2019-07-31','001','',340,351.15,'19K0RA035','2022-04-30','2019-05-31',0,'',351.15,'1 VIA',1700,0,0,1700,'F1','5','','','5'),(280,5,337,'2019-07-31','001','',4900,4998,'BIAGB00222','2020-11-28','2017-11-30',0,'',4998,'100 M',9800,0,0,9800,'F1','2','','','2'),(281,5,354,'2019-07-31','001','',550,566.29,'A05318033','2022-02-28','2018-03-31',0,'',566.29,'1 VIA',38500,0,0,38500,'F1','70','','','70'),(282,5,328,'2019-07-31','001','',30,33.34,'INGLA1809','2020-12-31','2018-02-28',0,'0',33.34,'25 MG',750,0,0,750,'F1','25','','','25'),(283,4,71,'2019-07-31','001','83',30,0.7728,'SBB8027','2020-04-30','2018-11-30',0,'',38.64,'50 TA',2490,6,6,2788.8,'TR4 L','4150','','','4150'),(284,4,34,'2019-07-31','001','30',327,4.0366,'NZB9006','2021-04-30','2019-05-30',0,'',403.66,'100 T',9810,6,6,10987.2,'TR5 L','3000','','','3000'),(285,4,11,'2019-07-31','001','20',98,12.4,'9NA0006','2022-03-30','2019-04-30',0,'',124,'10 TA',1960,6,6,2195.2,'TR1 L','200','','','200'),(286,4,13,'2019-07-31','001','1200',2.6,2.64,'AFD19011','2022-04-30','2019-05-30',0,'',26.4,'10 TA',3120,6,6,3494.4,'TR1 L','12000','','','12000'),(287,4,358,'2019-07-31','0001','500',5,1.848,'OVTE1883','2020-08-30','2018-09-30',0,'0',18.48,'10 TA',2500,6,6,2800,'TR2 L','5000','','','5000'),(288,5,77,'2019-08-01','001','160',7,1,'IZD16033','2020-09-30','2018-10-30',0,'',20,'20 TA',1120,0,0,1120,'TR2 L','2200','','','3200'),(289,5,200,'2019-08-01','001','150',15,2,'PC9132','2021-04-30','2019-05-30',0,'0',20,'10 CA',2250,0,0,2250,'C3 L3','0','','','1500'),(290,5,63,'2019-07-31','001','300',12,1.4,'6234','2021-05-31','2019-06-30',0,'',14,'10 ta',3600,0,0,3600,'S3 L3','3000','','','3000'),(291,5,120,'2019-07-31','001','175',3,0.32,'6209','2022-03-31','2019-04-30',0,'',3.2,'10 TA',525,0,0,525,'S3 L2','1750','','','1750'),(292,5,183,'2019-07-31','001','100',40,4.2,'LC19107','2021-02-28','2019-03-31',0,'',42,'10 TA',4000,0,0,4000,'S3L2','1000','','','1000'),(293,5,321,'2019-07-31','001','',12,15.9,'Z-18TP005','2020-11-30','2018-12-31',0,'',15.9,'10 ML',1200,0,0,1200,'S3 L2','100','','','100'),(294,5,43,'2019-07-31','001','200',70,7.302,'NT-181219','2020-11-30','2018-12-31',0,'0',73.02,'10 TA',14000,0,0,14000,'SL,L3','2000','','','2000'),(295,5,361,'2019-07-31','001','',22,24,'29036','2021-02-28','2019-03-31',0,'',24,'15 MG',8800,0,0,8800,'S3 L3','400','','','400'),(296,5,197,'2019-07-31','001','25',15,1.8,'6107','2020-09-30','2018-10-31',0,'',18,'10 TA',375,0,0,375,'S3 L3','250','','','250'),(297,5,196,'2019-07-31','001','125',60,6.75,'6190','2021-02-28','2019-03-31',0,'',67.5,'10 TA',7500,0,0,7500,'S3 L3','1250','','','1250'),(298,5,62,'2019-07-31','001','300',5,0.53,'6196','2022-03-31','2019-04-30',0,'',5.3,'10 TA',1500,0,0,1500,'S3 L3','3000','','','3000'),(299,5,360,'2019-07-31','001','',675,700,'E232','2021-02-28','2019-02-28',0,'0',700,'5 LIT',1350,0,0,1350,'S3 L3','2','','','2'),(300,5,219,'2019-08-01','001','',55,70,'S-193053','2021-02-28','2019-03-30',0,'0',70,'170 M',4235,0,0,4235,'SY6 T','68','','','77'),(301,5,287,'2019-07-31','001','',120,123,'8085','2020-05-31','2018-12-31',0,'',123,'200 M',480,0,0,480,'S2 L2','4','','','4'),(302,5,363,'2019-07-31','001','',95,98,'27419','2021-02-28','2017-03-31',0,'',98,'10 SE',7790,0,0,7790,'S2 L1','82','','','82'),(305,5,93,'2019-07-31','001','70',55,6.006,'19043','2020-12-31','0019-12-31',0,'',60.06,'10 TA',3850,0,0,3850,'S4 L3','700','','','700'),(308,5,144,'2019-08-01','001','40',30,5,'ZD181045','2020-09-30','2018-10-30',0,'',50,'10 TA',1200,0,0,1200,'TR2 L','0','','','400'),(309,5,158,'2019-08-01','001','2',330,1,'3A9001A','2021-12-30','2019-01-30',0,'0',500,'500 T',660,0,0,660,'TR4 L','0','','','1000'),(310,5,97,'2019-07-31','001','300',15,1.633,'26223','2021-08-31','2019-03-31',0,'',16.33,'10 TA',4500,0,0,4500,'S4 L3','3000','','','3000'),(311,5,158,'2019-07-31','001','40',5,0.7,'6203','2022-03-31','2019-04-30',0,'0',7,'10 TA',200,0,0,200,'S4 L3','400','','','400'),(312,5,37,'2019-08-01','001','31',25,4,'LBA8002','2021-02-28','2018-03-30',0,'',40,'10 TA',775,0,0,775,'TR2 L','310','','','310'),(313,5,104,'2019-08-01','001','20',18,0.8,'BR9731017','2021-02-28','2019-03-30',0,'0',24,'30 TA',360,0,0,360,'TR4 L','600','','','600'),(314,5,29,'2019-07-31','001','660',40,13.9,'6242','2021-05-31','2019-06-30',0,'',41.7,'3 TAB',26400,0,0,26400,'S3 L1','1980','','','1980'),(315,5,17,'2019-07-31','001','16.8',110,11.33,'ZA18018','2020-03-31','2018-10-31',0,'',113.3,'10 TA',1848,0,0,1848,'S3 L1','168','','','168'),(316,5,9,'2019-07-31','001','96',15,1.96,'25966','2020-11-30','2018-06-30',0,'',19.6,'10 TA',1440,0,0,1440,'S3 L1','960','','','960'),(317,5,7,'2019-07-31','001','100',20,2.19,'6210','2022-03-31','2019-04-30',0,'',21.9,'10 TA',2000,0,0,2000,'S3 L1','1000','','','1000'),(318,5,365,'2019-07-31','001','',35,39,'134','2021-04-30','2019-05-31',0,'0',39,'400 M',1085,0,0,1085,'S4 L4','31','','','31'),(319,4,366,'2019-08-02','001','',14,60,'K80223','2020-09-30','2018-10-30',0,'',60,'5 ML',1400,2.5,2.5,1470,'IR9 L','100','','','100'),(320,4,17,'2019-08-02','001','250',38,15,'THM19136','2020-06-30','2019-01-30',0,'',90,'6 TAB',9500,6,6,10640,'TR1 L','1500','','','1500'),(321,4,238,'2019-08-02','001','',26,80,'DI1960258','2021-04-30','2019-05-30',0,'',80,'60 MG',1560,2.5,2.5,1638,'IR8 L','60','','','60'),(322,4,293,'2019-08-02','001','300',20,6,'0088PB011','2020-07-30','2018-08-30',0,'0',60,'10 CA',6000,6,6,6720,'C3 L1','3000','','','3000'),(323,2,77,'2019-08-03','30043190','500',7.5,1,'IZD18051','2020-10-30','2018-11-30',0,'0',20,'20 TA',3750,6,6,4200,'TR2 R','9000','','','10000'),(324,2,369,'2019-08-03','3004','',15,96,'0746','2020-08-30','2018-09-30',0,'',96,'15 G',600,6,6,672,'R6 L2','40','','','40'),(325,2,128,'2019-08-03','3004','300',6,3,'AFB8E69','2020-11-30','2018-12-30',0,'',30,'10 TA',1800,6,6,2016,'TR2 L','3000','','','3000'),(326,2,295,'2019-08-03','3004','',9.85,60,'RPF318','2021-02-28','2019-03-30',0,'',60,'40 MG',394,6,6,441.28,'IR9 L','40','','','40'),(327,2,188,'2019-08-03','3004','60',90,2.3,'DNZS1C005','2021-05-30','2019-06-30',0,'',23,'10 CA',5400,6,6,6048,'CR3 L','600','','','600'),(328,2,368,'2019-08-03','30043190','',6,20,'IMT6572','2021-01-30','2019-02-28',0,'0',20,'10 ML',600,6,6,672,'IR8 L','100','','','100'),(329,5,370,'2019-07-31','001','',2,3.24,'ULN1869','2020-07-30','2018-06-30',0,'',3.24,'2 ML',100,0,0,100,'IR10 ','50','','','50'),(330,5,370,'2019-07-31','001','',2,3.4,'RRE77','2020-06-30','2018-07-30',0,'',3.4,'2 ML',100,0,0,100,'IR10 ','50','','','50'),(331,5,370,'2019-07-31','001','',2,3.4,'RRF315','2021-02-28','2019-03-30',0,'',3.4,'2 ML',200,0,0,200,'IR10 ','100','','','100'),(332,5,370,'2019-07-31','001','',2,3.4,'RRF111','2020-12-30','2019-01-30',0,'',3.4,'2 ML',600,0,0,600,'IR10 ','250','','','300'),(333,5,325,'2019-07-31','001','',300,410,'AB90182','2023-04-30','2018-04-30',0,'0',410,'300 M',3000,0,0,3000,'IR9 L','10','','','10');
/*!40000 ALTER TABLE `inventory_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipdvisit`
--

DROP TABLE IF EXISTS `ipdvisit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ipdvisit` (
  `ipdid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `patientfrom` varchar(50) DEFAULT NULL,
  `ipddate` date DEFAULT NULL,
  `ipdtime` time DEFAULT NULL,
  `ptype` varchar(5) DEFAULT NULL,
  `govscheme` varchar(70) DEFAULT NULL,
  `urnno` varchar(30) DEFAULT NULL,
  `advmoney` varchar(6) DEFAULT '0',
  `moneyreceivedby` varchar(50) DEFAULT NULL,
  `wardid` int(11) DEFAULT NULL,
  `pstatus` varchar(20) DEFAULT NULL,
  `dischargedate` date DEFAULT NULL,
  `dischargetime` time DEFAULT NULL,
  PRIMARY KEY (`ipdid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipdvisit`
--

LOCK TABLES `ipdvisit` WRITE;
/*!40000 ALTER TABLE `ipdvisit` DISABLE KEYS */;
INSERT INTO `ipdvisit` VALUES (1,'2019SHD3','ABDOMINAL PAIN ','EMERGENCY','2019-08-02','18:01:00','NEW','3','','0','',4,NULL,NULL,NULL),(2,'2019SHD5','pregnancy, abdominal pain ','EMERGENCY','2019-08-02','18:21:00','NEW','3','','0','',1,NULL,NULL,NULL),(3,'2019SHD7','omiting','OUTPATIENT','2019-08-03','00:07:00','NEW','2','','0','',4,NULL,NULL,NULL);
/*!40000 ALTER TABLE `ipdvisit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_sample_collect`
--

DROP TABLE IF EXISTS `lab_sample_collect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_sample_collect` (
  `accession_no` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `source_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `source` varchar(13) DEFAULT NULL,
  `test_validation` int(1) DEFAULT '0',
  `validation_date` date DEFAULT '0000-00-00',
  PRIMARY KEY (`accession_no`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_sample_collect`
--

LOCK TABLES `lab_sample_collect` WRITE;
/*!40000 ALTER TABLE `lab_sample_collect` DISABLE KEYS */;
INSERT INTO `lab_sample_collect` VALUES (1,'2019SHD2',2,'2019-08-02','OPD',1,'2019-08-02'),(2,'2019SHD3',1,'2019-08-02','Male Ward',1,'2019-08-02'),(3,'2019SHD8',4,'2019-08-03','Male Ward',1,'2019-08-03'),(4,'2019SHD8',4,'2019-08-03','Male Ward',0,'0000-00-00'),(5,'2019SHD8',4,'2019-08-03','Male Ward',0,'0000-00-00');
/*!40000 ALTER TABLE `lab_sample_collect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_test_data`
--

DROP TABLE IF EXISTS `lab_test_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab_test_data` (
  `ltid` int(11) NOT NULL AUTO_INCREMENT,
  `accession_no` int(11) NOT NULL,
  `tid` int(11) DEFAULT NULL,
  `test_value` varchar(15) DEFAULT '',
  PRIMARY KEY (`ltid`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_test_data`
--

LOCK TABLES `lab_test_data` WRITE;
/*!40000 ALTER TABLE `lab_test_data` DISABLE KEYS */;
INSERT INTO `lab_test_data` VALUES (1,1,32,'done'),(2,1,59,'Positive'),(3,2,23,'B-'),(4,2,31,'due'),(5,2,32,'done'),(6,2,39,'148.15'),(7,2,41,'1.98'),(8,3,1,'279.00'),(9,3,2,'61.71'),(10,3,3,'454.38'),(11,3,4,'7.42'),(12,3,5,'5.48'),(13,3,6,'NEGATIVE'),(14,3,31,'DUE'),(15,5,30,''),(16,5,31,''),(17,5,1,'279.00'),(18,5,2,'61.71'),(19,5,3,'454.38'),(20,5,4,''),(21,5,5,''),(22,5,6,''),(23,5,39,'');
/*!40000 ALTER TABLE `lab_test_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_medicine`
--

DROP TABLE IF EXISTS `main_medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_medicine` (
  `med_id` int(11) NOT NULL AUTO_INCREMENT,
  `drugname` varchar(250) DEFAULT NULL,
  `medicine_type` varchar(50) DEFAULT NULL,
  `min_value` varchar(10) DEFAULT NULL,
  `max_value` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`med_id`)
) ENGINE=InnoDB AUTO_INCREMENT=371 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_medicine`
--

LOCK TABLES `main_medicine` WRITE;
/*!40000 ALTER TABLE `main_medicine` DISABLE KEYS */;
INSERT INTO `main_medicine` VALUES (1,'Pancreatin Tablet ','Tablet','100','1000'),(2,'Setraline HydroChrloride 50mg','Tablet','100','1000'),(3,'ACECLOFENAC AND PARACETAMOL 100MG','Tablet','100','1000    '),(4,'ACETOZOLAMIDE (DIAMOX)','Tablet','100','1000'),(5,'ACICLOVIR TABLET  800mg                ','Tablet','100','1000'),(6,'ACICLOVIR TABLETS  400mg                ','Tablet','100','1000'),(7,'ALBENDAZOLE  400mg        ','Tablet','100','1000'),(8,'ALLOPURINOL-100 MG','Tablet','100','1000'),(9,'ALPRAZOLAM  0.5mg','Tablet','100','1000'),(10,'AMINOPHYLLIN 100Mg','Tablet','100','1000'),(11,'AMIODARONE- 200Mg','Tablet','100','1000'),(12,'AMITRIPHYLINE HYDROCHLORIDE 25mg ','Tablet','100','1000'),(13,'AMLODEPINE 5Mg','Tablet','100','1000'),(14,'AMOXICILLIN TRIHYDRATE T-125 ','Tablet','100','1000'),(15,'AMOXYCILLIN AND POTASSIUM CLAVULANATE   228.5 MG','Tablet','100','1000'),(16,'AMOXYCILLIN AND POTASSIUM CLAVULANATE   375MG','Tablet','100','1000'),(17,'AMOXYCILLIN AND POTASSIUM CLAVULANATE TABLET   625MG','Tablet','100','1000'),(18,'ANTACID TABLETS','Tablet','100','1000'),(19,'ARTEMETHER AND LUMEFANTRINE   100 MG','Tablet','100','1000'),(20,'ARTESUNATE,SULPHADOXINE AND PYRIMITHAMINE     100 MG','Tablet','100','1000'),(21,'ARTESUNATE,SULPHADOXINE AND PYRIMITHAMINE 50 MG','Tablet','100','1000'),(22,'ASPIRIN 150 MG','Tablet','100','1000'),(23,'ASPIRIN 300 MG','Tablet','100','1000'),(24,'ASPIRIN 75 MG','Tablet','100','1000'),(25,'Asthalyne 4 MG','Tablet','100','1000'),(26,'ATENELOL TABLET 50 MG','Tablet','100','1000'),(27,'ATORVASTALINE TABLET 10 MG','Tablet','100','1000'),(28,'ATORVASTATINE 20 MG','Tablet','100','1000'),(29,'AZYTHROMYCIN 500 MG','Tablet','100','1000'),(30,'BACLOFEN 10MG TABLET','Tablet','100','1000'),(31,'BETAHISTINE TABLETS 16MG','Tablet','100','1000'),(32,'BISCODYL 5MG','Tablet','100','1000'),(33,'CALCIUM AND VITAMIN D3 TABLET IP 500 MG','Tablet','100','1000'),(34,'CARBIMAZOLE  10 Mg','Tablet','100','1000'),(35,'CEFIXIME DISPERSIBLE  200 MG','Tablet','100','1000'),(36,'CEFUROXIME AXETIL 500 MG','Tablet','100','1000'),(37,'CHLORDIAZEPOXIDE 10 MG','Tablet','100','1000'),(38,'CHLORDIAZEPOXIDE 25 MG','Tablet','100','1000'),(39,'CHLORPROMAZIN TABLETS 50MG','Tablet','100','1000'),(40,'Ciprofloxacin Hydrochloriden500 MG','Tablet','100','1000'),(41,'CLOMIFEN 25 MG','Tablet','100','1000'),(42,'CLONAZEPAM 0.5 MG','Tablet','100','1000'),(43,'CLOPIDOGRAL TABLETS 75 MG','Tablet','100','1000'),(44,'CLOTRIMAZOLE VAGINAL TABLETS 100MG','Tablet','100','1000'),(45,'COTRIMOXAZOLE-SS','Tablet','100','1000'),(46,'DI-ETHYLCARBAMAZINECITRATE 100 MG','Tablet','500','2000'),(47,'DIAZEPAM 5 MG','Tablet','500','2000'),(48,'DIGOXIN  0.25 MG','Tablet','100','500'),(49,'DISPERSIBLE AMOCYCILLIN AND CLAVULANATE TAB 228.5 MG','Tablet','100','1000'),(50,'DOMPERIDOM  10 MG','Tablet','200','500'),(51,'DOXYLAMINE SUCCINATE With PYRIDOXINE HYDROCHLORIDE AND FOLIC ACID 10 MG','Tablet','100','1000'),(52,'Dydrogesterone tab 10 MG Duphaston','Tablet','100','1000'),(53,'ESCITALOPRAM TABLETS 10MG','Tablet','100','1000'),(54,'ETAMSYLATE  500 MG','Tablet','100','500'),(55,'ETHAMBUTOL 800 MG','Tablet','100','1000'),(56,'FENOFIBRATE (STANLIP) 145 MG','Tablet','100','1000'),(57,'FERROUS FUMARATE,FOLIC ACID AND ZINC SULPHATE (Iron )  ','Tablet','5000','15000    '),(58,'FLUCONAZOLE 150 MG','Tablet','250','1000'),(59,'FOLIC ACID TABLET 5 MG','Tablet','1000','5000'),(60,'FRUSEMIDE AND SPIRONOLACTONE  50MG','Tablet','100','1000'),(61,'FRUSEMIDE TABLETS 40MG','Tablet','500','2000'),(62,'GLIBEN CLAMIDE 5 MG (Dionil)                                 ','Tablet','1000','5000'),(63,'GLIMEPERIDE TABLET 2 MG','Tablet','1000','5000'),(64,'GLIMEPERIDE TABLETS 1 MG','Tablet','1000','5000'),(65,'HALOPERIDOL  5 MG (serenes)','Tablet','100','200'),(66,'HYDROCHLORITHIOZIDE TABLET 25 MG','Tablet','500','2000'),(67,'HYDROXYCHLOROQUINE TABLETS 200MG','Tablet','100','500'),(68,'HYOSCINE BUTYL BROMID 10 MG','Tablet','200','1000'),(69,'IBUPROFEN PARACETAMOL 400 MG','Tablet','500','2000'),(70,'IMIPREMIN HYDROCHLORIDE 25 MG','Tablet','500','2000'),(71,'ISOSORBIDE DI -NITRATE 10 MG','Tablet','500','3000'),(72,'IVERMECTIN DISPERSIBLE TABLETS ','Tablet','30','150'),(73,'LEVOFLOXACIN   500 MG ','Tablet','100','300'),(74,'LOBETALOL 100 MG','Tablet','100','200'),(75,'LOSARTON POTTASIUM 50mg AND HYDROCHLOTHIAZIDE 12.5 MG','Tablet','100','500'),(76,'MEBENDAZOLE  100 MG','Tablet','200','1000'),(77,'METFORMIN HYDROCHLORIDE-500 MG','Tablet','1000','10000'),(78,'METHOTREXATE 7.5 MG','Tablet','50','150'),(79,'DISODIUM HYDROGEN CITRATE SYR 100ML','Syrup','50','200'),(80,'Bitadin Clotrimazole vaginal 100MG','Tablet','100','200'),(82,'CALCIUM CARBONATE AND VITAMIN D3 ','Tablet','1000','3000'),(84,'CARBAMAZEPINE 200 MG     ','Tablet','200','500'),(85,'METOCLOPROMAMIDE HYDROCHLORIC 10 Mg         ','Tablet','500','2000'),(86,'METOPROLOL TARTRATE  50 MG','Tablet','300','500'),(87,'MIRTAZAPINE  15 MG            ','Tablet','200','500'),(88,'NIFEDEFIN  10 MG                     ','Tablet','500','2000'),(89,'NITROFURANTOIN SR TABLETS 100 MG','Tablet','300','1000'),(90,'NORETHISTERONE TABLETS 5 MG','Tablet','100','1000'),(91,'OFLOXACIN 200 MG                 ','Tablet','500','2000'),(92,'OFLOXACIN 400 MG                  ','Tablet','500','2000'),(93,'OLANZAPINE MOUTH DISSOLVING TAB 10 MG  ','Tablet','500','2000'),(94,'PENICILLIN G POTASSIUM   400 MG ','Tablet','500','1000'),(95,'Pentoxifylline Extended 400 MG','Tablet','100','1000'),(96,'PHENOBARBITONE TABLETS 60 MG           ','Tablet','500','1000'),(97,'PHENYTOIN    100 MG               ','Tablet','1000','3000'),(98,'PREDNISOLONE DISPERSIBLE 10 MG','Tablet','1000','3000'),(99,'PROMETHAZINE HYDROCHLORIDE 10 MG','Tablet','1000','2000'),(100,'PROPANOLOL HYDROCHLORIDE TABLETS 10 MG         ','Tablet','1000','3000'),(101,'PYRAZINAMIDE    750 MG                   ','Tablet','500','1000'),(102,'QUETIAPINE          50 MG','Tablet','100','1000'),(103,'RAMIPRIL TABLETS 5 MG','Tablet','100','1000'),(104,'RANITIDINE TABLETS  150 MG                   ','Tablet','3000','5000'),(105,'RIFAMPICIN AND ISONICID TABLETS   150 MG  ','Tablet','200','300    '),(106,'ROSUVASTATIN CALCIUM TABLETS 10MG','Tablet','100','1000'),(107,'SALBUTAMOL SULPHATE TABLETS 4MG','Tablet','100','1000'),(108,'SODIUM VALPORATE AND  VALPROIC ACID CR 300 MG','Tablet','300','500'),(109,'SODIUM VALPORATE AND VALPROIC ACID 500 MG','Tablet','300','500'),(110,'TELMISARTAN 40 MG','Tablet','100','1000'),(111,'Terbinafine 250 MG','Tablet','100','1000'),(112,'THYROXINE 50 MG ','Tablet','300','500'),(113,'THYROXINE SODIUM  100 MG ','Tablet','300','500'),(114,'TRANEXAMIC ACID  500 MG','Tablet','300','1000'),(115,'Trifluoperazine AND Benzahexal Hydrochloride','Tablet','300','500'),(116,'VITAMIN C  500                            ','Tablet','200','500'),(117,'WARFARIN SODIUM 5 MG    ','Tablet','150','300'),(118,'CARBIMAZOLE  5 MG','Tablet','100','1000'),(119,'CEFIXIME DISPERSIBLE  400MG','Tablet','100','1000'),(120,'CETRIZINE   10 MG','Tablet','500','1000'),(121,'CHLOROQUIN PHOSPHATE 250 MG','Tablet','100','1000'),(122,'CHLOROQUIN PHOSPHATE 500 MG                        ','Tablet','100','1000'),(123,'CHLORPHENERAMINE MALEATE   4MG','Tablet','100','1000'),(124,'CHOLECALCEFERAL (D-SHINE)','Tablet','100','1000'),(125,'CLOMIFEN 50 MG','Tablet','100','1000'),(126,'DICLOFENAC SODIUM  50 MG               ','Tablet','100','1000'),(127,'DISULFIRAM 250 MG                             ','Tablet','100','1000'),(128,'ENAPRIL MALEAT 5 MG                  ','Tablet','100','1000'),(129,'ETAMSYLATE 250 MG','Tablet','100','1000'),(130,'ETHAMBUTOL 400 MG','Tablet','100','1000'),(131,'ETHAMBUTOL 600 MG','Tablet','100','1000'),(132,'ETHINYL ESTRADIOL 0.01 MG','Tablet','100','1000'),(133,'ETOFYLLINE THEOPHYLLINE PROLONGED  300 R                   ','Tablet','100','1000'),(134,'FAMOTIDINE 40 MG                  ','Tablet','100','1000'),(135,'FLUNARAZINE 10 MG','Tablet','100','1000'),(136,'FRUSEMIDE  40mg (Lasix )  ','Tablet','100','1000'),(137,'GABAPENTINE AND MECOBALAMINE ','Tablet','100','1000'),(138,'GRISEOFULVIN  250 MG                                                 ','Tablet','100','1000'),(139,'HALOPERIDOL  0.5 MG (serenes)                    ','Tablet','100','1000'),(140,'HYDROXYZINE HYDROCHLORIDE 25 MG','Tablet','100','1000'),(141,'IBUPROFEN 200 MG','Tablet','100','1000'),(142,'LEVONORGESTREL ETHINYLO ESTRADIOL  Primilate N   ','Tablet','100','1000'),(143,'LOPERAMIDE HYDROCHORIDE 2 MG   ','Tablet','100','1000'),(144,'LOSARTAN 50 MG                                  ','Tablet','100','1000'),(145,'MEDROXYPROGESTERONE        ','Tablet','100','1000'),(146,'METHYLDOPA   500 MG','Tablet','100','1000'),(147,'METHYLDOPA   500 MG                          ','Tablet','100','1000'),(148,'  METRONIDAZOLE 200 MG','Tablet','100','1000'),(149,'METRONIDAZOLE 400 MG','Tablet','100','1000'),(150,'MISOPROSTAL 200 MCG       ','Tablet','100','1000'),(151,'MISOPROSTAL 25 MCG','Tablet','100','1000'),(152,'NIMODIPINE','Tablet','100','1000'),(153,'Norfloxacin AND Betadex 400 MG ','Tablet','100','1000  '),(154,'OLANZAPINE MOUTH DISSOLVING TAB 5 MG','Tablet','100','1000'),(155,'OLANZAPINE ORALLY   DISINTEGRATING 5 MG','Tablet','100','1000'),(156,'OLANZAPINE ORALLY DISINTEGRATING 10 MG','Tablet','100','1000'),(157,'Omiprazole','Tablet','100','1000'),(158,'PARACETAMOL 500 MG','Tablet','100','1000'),(159,'PREDNISOLONE DISPERSIBLE   5 MG','Tablet','100','1000'),(160,'PRIMAQUIN PHOSPHATE  7.5 MG       ','Tablet','100','1000'),(161,'PROCHLORPERAZINE MALEATE5 MG             ','Tablet','100','1000'),(162,'PYRIMETHAMINEAND SULPHADOXINE','Tablet','100','1000'),(163,'RANITIDINE   150 MG                   ','Tablet','100','1000'),(164,'RESPERIDONE AND TRI HEXYPHENOL HYDROCHLORIDE        ','Tablet','100','1000  '),(165,'RIFAMPICIN AND ISONICID  150+100 MG  ','Tablet','100','1000'),(166,'SEPTRAN D.S','Tablet','100','1000'),(167,'SERTRALINE 50 MG                     ','Tablet','100','1000'),(168,'SILDENAFIL CITRATE  25 MG  ','Tablet','100','1000'),(169,'SPIRONOLACTONE   100 MG','Tablet','100','1000'),(170,'TAMOXIFEN CITRATE  20 MG','Tablet','100','1000'),(171,'Tamsulocin Hydrochloride 0.4MG(MODIFIED RELEASE) AND FINASTERID 5MG','Tablet','100','1000'),(172,'TINIDAZOLE 500 MG                                  ','Tablet','100','1000'),(173,'TRAZODONE HYDROCHLORIDE 50 MG','Tablet','100','1000'),(174,'Trihexaphenidyl (Pacitone)','Tablet','100','1000'),(175,'TRIMETHOPRIME80MG AND  SULPHAMETHOXAZOLE400  ','Tablet','100','1000'),(176,'VERAPAMIL HYDROCHLORIDE                 ','Tablet','100','1000'),(177,'VITAMIN A AND  D ','Tablet','100','1000'),(178,'VITAMIN B-COMPLEX With VIT.C AND BIOTIN 260 MG      ','Tablet','100','1000'),(179,'AMOXYCILLIN  250 MG','Capsule','500','2000'),(180,'AMOXYCILLIN  TRIHYDRATE  500 MG ','Capsule','3000','5000'),(181,'AMPICILLIN TRIHYDRATE 250 MG','Capsule','250','2000'),(182,'AMPICILLIN TRIHYDRATE 500 MG','Capsule','1000','3000'),(183,'CEPHALEXIN  500 MG','Capsule','1000','3000'),(184,'CHLORAMPHENICOL 250 MG','Capsule','200','500'),(185,'CHLORAMPHENICOL 500 MG','Capsule','200','500'),(188,'DANAZOL 100 MG','Capsule','500','2000'),(192,'DICLOXACILLIN SODIUM  250 MG  ','Capsule','300','2000'),(193,'DOXYCYCLINE  100MG','Capsule','300','2000'),(194,'FLUOXETINE 20MG                ','Capsule','300','1000'),(195,'GABAPENTIN 300 MG','Capsule','300','2000'),(196,'HYDROXYUREA 500 MG','Capsule','300','3000'),(197,'INDOMETHACINE 25 MG','Capsule','200','1000'),(198,'LOPERAMIDE  2 MG','Capsule','200','500'),(199,'NIFEDEPINE 10 MG ','Capsule','300','1000'),(200,'OMEPRAZOLE 20 MG','Capsule','300','2000'),(201,'PREGABALIN AND MECOBALAMINE  ','Capsule','200','1000'),(202,'Progesteron 100 MG','Capsule','200','500'),(203,'Progesteron 200 MG','Capsule','200','500'),(204,'REFAMPICINE(R-CINEX)','Capsule','100','1000'),(205,'TRAMADOL HYDROCHLORIDE  50 MG      ','Capsule','500','1000'),(206,'TRAMSULOSIN HYDROCHLORIDE 0.4 MG  AND FINASTERIDE 5 MG','Capsule','500','1500'),(207,'VITAMIN A AND D ','Capsule','300','1000'),(208,'CHOLECALCIFEROL CAPSULE ','Capsule','100','1000'),(209,'VITAMIN E CAPSULE 400 MG','Capsule','100','1000'),(210,'TETRACYCLINE HYDROCHLORIDE CAPSULES 250 MG','Capsule','100','1000'),(211,'RIFAMPICIN AND ISONICID CAPSULES USP 450 plus 300MG  ','Capsule','100','1000    '),(212,'AMPICILLIN TRIHYDRATE CAPSULE IP','Capsule','100','1000'),(213,'DANAZOL 100 MG','Capsule','100','1000'),(214,'Alkasol 100 ML','Syrup','100','200'),(215,'Amoxycillin 30 ML','Syrup','100','200'),(216,'Ampi clox 30 ML','Syrup','50','100'),(217,'Asthalin100 ML','Syrup','10','20'),(218,'Albedazole 10 ML','Syrup','50','100'),(219,'Antacid 170 ML','Syrup','50','100'),(220,'Azythromicine15 ML','Syrup','25','50'),(221,'Bitadin lotion lit.','Syrup','3','10'),(222,'Calcium Syrup 200 ML','Syrup','10','20  '),(223,'Ceffixim 30 ML','Syrup','50','100'),(224,'Cloroquine 60 ML','Syrup','10','20'),(225,'Clorum phenical 60 ML`','Syrup','20','40'),(226,'Codeine syr 100 ML','Syrup','10','20'),(227,'Creemafin 170 ML','Syrup','20','50'),(228,'Fenergon/Promethsone400ML 60ML','Syrup','5','10'),(229,'xylokin viscus 100 ML','Syrup','2','5'),(230,'Gardinal 100 ML','Syrup','5','10'),(231,'Lactolus 200 ML','Syrup','15','50'),(232,'Phenotwin 200 ML','Syrup','5','10'),(233,'Pyriginamide 100 ML','Syrup','3','5'),(234,'Refompicin 200 ML','Syrup','3','5'),(235,'Mertrogil 60 ML','Syrup','25','50'),(237,'Anti Rabies Vaccine','Injection','30','50'),(238,'Artisunate 60 MG','Injection','30','50'),(239,'Atropine0.6 MG','Injection','2000','5000'),(240,'Amikacin 500 MG','Injection','100','300'),(241,'Albomin Sero albomin 25%','Injection','10','1000'),(242,'Anti D inj 300 MCG ','Injection','5','10'),(243,'Adrenalin ','Injection','50','50'),(244,'Aminophylene 25 MG','Injection','50','100'),(245,'Ampicillin 500 MG','Injection','100','200'),(246,'(AVIL)  PHENIREMINE 22.75   ','Injection','10','15'),(247,'Arithropytin 4000 IU','Injection','10','1000'),(248,'Anti Titanus 250 IU ','Injection','10','1000'),(249,'DOXYCYCLINE AND LACTIC ACID BACILLUS CAPSULES 100 MG','Capsule','100','1000'),(250,'BACILLUS CALMETTE','Injection','10','1000'),(251,'B.complex 10 ML vial','Injection','30','50'),(252,'Benzathine Penicillin 12 L','Injection','50','100'),(253,'Benzathine Penicillin 6 L','Injection','30','50'),(254,'Betaloc inj 5 MG','Injection','30','50'),(255,'HYASCINE BUTYL  (Buscopan  amp).10MG','Injection','50','200'),(256,'BENZYL PENICILLIN(10 LAC)  C.P','Injection','10','1000'),(257,'Cefepime/ 1g','Injection','200','500'),(258,'Cefuroxime 750 ML','Injection','500','2000'),(259,'Cefoperazone 5 &  salbutamol 5 (cefprazs)1G ','Injection','200','500  '),(260,'Calcium','Injection','50','50'),(261,'Cefotaxim  1 GM.','Injection','100','200'),(262,'Ceftriaxone  1 GM.','Injection','500','2000'),(263,'Chlorphenicol 1000 MG','Injection','50','300'),(264,'Chlorpromazine  I/v','Injection','10','1000'),(265,'Chloroquin amp.','Injection','10','1000'),(266,'DIAGOXIN   0.5MG','Injection','10','10'),(267,'(Etofylline & Theophylline) -Deriphyllin ','Injection','100','1000'),(268,'Dexamethasone  vial/ 20 ML','Injection','20','50'),(269,'Dextrose 25% amp.','Injection','50','100'),(270,'Dextrose 50% amp.','Injection','50','100'),(271,'Diclofenac  30 ML. vial','Injection','10','30'),(272,'Diclofenac  Sodium 30 ML','Injection','10','1000'),(273,'Dopamine 40 m pML 5ML','Injection','10','100'),(274,'DIAZIPAM 10 ML Vial ','Injection','10','1000'),(275,'Ethamsylate Inj 250 MG','Injection','50','200'),(276,'Frusemide /Lesix','Injection','100','300'),(277,'Gentamicine 30 ML','Injection','50','200'),(278,'Gardinal Phenobarbitone','Injection','50','200'),(279,'Heparin  25000 unit','Injection','30','50'),(280,'Hydro Cortisan 100 MG','Injection','100','500'),(281,'Heloperidol   (Serenace)','Injection','50','100'),(282,'PRIMAQUINE TAB 15 MG','Tablet','200','1000'),(284,'TRAMADOL HYDROCHLORIDE INJ 50 MG 2 ML','Injection','100','300'),(285,'POTASSIUM CHLORIDE INJ 10 ML','Injection','30','100'),(286,'B COMPLEX SYRUP 100 ML','Syrup','100','200'),(287,'TONOFERON SYR 200 ML','Syrup','15','20'),(288,'PROMETHAZINE HTDROCHLORIDE SYR 400 ML','Syrup','50','200'),(289,'LACTULOSE SYR 100 ML','Syrup','100','200'),(290,'PARACETAMOL PAEDIATRIC SYR 60 ML','Syrup','100','200'),(291,'OFLOXACIN SYR 30 ML','Syrup','100','300'),(292,'KREMAFIN SYR 170 ML','Syrup','100','300'),(293,'AMOXICILLIN CAPSULES 500 MG','Capsule','3000','5000'),(294,'VITAMIN B INJ 10 ML','Injection','10','1000'),(295,'PANTAPRAZOLE INJ 40 GM  ','Injection','10','100  '),(296,'K. CL (POTACIUM)','Injection','10','1000'),(297,'I.S. CEFOTAXIME SODIUM','Injection','10','1000'),(298,'I.S. CEFOTAXIME SODIUM','Injection','10','1000'),(299,'VITAMIN C INJ. 1.5 ML','Injection','10','1000'),(300,'CHLORMPHENICOL SODIUM SUC.','Injection','10','1000'),(301,'CALCIUM GLUCONATE 10 ML','Injection','10','1000'),(302,'AMIODARONE INTRAVENOUS INJ 3 ML','Injection','10','50'),(303,'POTASSIUM CHLORIDE SYR 200 ML','Syrup','25','50'),(304,'TRIMCINOLONE ACCTONIDE  1ML','Injection','10','1000  '),(305,'OXYTOCIN INJ 1ML','Injection','200','600'),(306,'INSULIN REGULAR INJ 10 ML','Injection','10','50'),(307,'INSULIN M 30/70 INJ 10 ML','Injection','25','100'),(308,'AMITRIPTYLINE TAB 10 MG LC ','Tablet','100','1000    '),(309,'VITAMIN B COMPLEX LC','Tablet','500','2000'),(310,'AMITRYPTYLINE TAB LC 75 MG ','Tablet','500','1000'),(311,'BECLAMETHASONE NEOMYCIN SULPHATE OINT LC 15 G','Ointment','200','1000'),(312,'PARACETAMOL  SYR LC 4.5 LTR','Syrup','1','5'),(313,'CIPROFLOXACIN TAB LC 500 MG','Tablet','500','3000'),(314,'DICLOFENAC GEL LC 30 GRM','Ointment','500','3000'),(315,'PHENYTOIN SYR 200 ML','Syrup','10','100'),(316,'PHENOBARBITONE SYR 100 ML','Syrup','20','100'),(317,'BLOOD BAG 100 ML','Consumable','50','100'),(318,'METRONIDAZOLE BENZOATE SYR 60 ML','Syrup','30','100'),(319,'SURGICAL SPIRIT 400 ML','General','50','200'),(320,'HALOTHANE B.P. 250 ML','Injection','10','1000'),(321,'CIPROFLOXACIN EYE DROPS 10 ML','Drop','50','200'),(322,'SOYAL MILK','General','10','20'),(323,'LACTOGEN POWDER','General','10','20'),(324,'MAGNESIUM SULPHATE POWDER','General','10','20'),(325,'LINEZOLID IV INJ','Injection','10','50'),(326,'NEEDLE 21 X 1 - 1/2','Consumable','1000','3000'),(327,'DISPO SYRINGE 10 ML DV','Consumable','200','500'),(328,'NITROGLYCERINE INJ USP 25 MG 5ML','Injection','10','100'),(329,'DICLOFENAC SODIUM 75 MG/ML','Injection','10','100'),(330,'METHYLERGOMETRINE INJ IP 1ML','Injection','10','100'),(331,'LABETALOL HYDROCHLORIDE INJ IP 20 MG/4ML','Injection','10','100'),(332,'SOMATOSTATIN INJ 3 MG','Injection','10','20'),(333,'SOMATOSTATIN INJ 3 MG >  Injection  > MinValue: 10 > MaxValue: 20  > medid: 332','Injection','10','20'),(334,'VITAMIN D3 INJ 15 MG','Injection','10','100'),(335,'GLYCOPYRROLATE INJ USP 1 ML','Injection','10','100'),(336,'STREPTOKINASE INJ IP 1500000 IU','Injection','10','20'),(337,'ALBUTEIN 20% USP INJ 20 G/ 100ML','Injection','2','5'),(338,'BISACODYL SUPPOSITORIES IP 5 MG ','Tablet','10','100  '),(339,'BISACODYL SUPPOSITORIES IP 10 MG ','Tablet','10','100  '),(340,'MUCAINE GEL SYR 200 ML','Syrup','20','40'),(341,'PARACETAMOL SUPPOSITORIES B.P. NEOMAL - 80 MG','Tablet','10','100'),(343,'TERBINAFINE OINT 10GM','Ointment','10','50'),(344,'PARACETAMOL SUPPOSITORIES B.P. NEOMAL -170 MG','Tablet','10','100'),(345,'Heparin  25000 unit  INJ 5 ML','Injection','30','50'),(346,'SONADERM NM OINT 15 GM','Ointment','25','100'),(347,'IBUPROFEN 400 MG TAB','Tablet','1000','3000'),(348,'PARACETAMOL SUPPOSITORIES B.P. NEOMAL- 250 MG','Tablet','10','100'),(349,'DICLOXACILLIAN SODIUM CAPS 500MG','Capsule','500','2000'),(350,'INSULINE INJ 40IU/ML','Injection','10','100'),(351,'TETANUS VACCINE 5 ML IP 1.25 MG','Injection','10','100'),(352,'BIPHASIC ISOPHANE ISULINE INJ IP 100 IU/ML','Injection','10','100'),(353,'B COMPLEX TABLET ','Tablet','3000','5000'),(354,'SNAKE VENOM ANTISERUM I.P.','Injection','10','100'),(355,'RABIES VACCINE HUMAN IP','Injection','5','20'),(356,'METOCLOPRAMIDE HYDROCHLORIDE INJ 2 ML','Injection','50','100'),(357,'KETAMIN HYDROCLORIDE INJ IP 5 ML','Injection','5','10'),(358,'HYDROCHLOROTHIAZIDE TAB 25 MG','Tablet','1000','5000'),(359,'CLOPIDOGREL 75 MG','Tablet','1000','2000'),(360,'ARIHANT ELECTRODEGEL','Ointment','2','5'),(361,'MICONAZOLE 2% 15 MG','Ointment','100','500'),(362,'SHARK LATEX EXAM GLOVES','Consumable','10','100'),(363,'INFUSION SET','Consumable','10','100'),(364,'SILVER SULPHADIZINE + CHLORHEXIDINE 15 MG','Ointment','100','500'),(365,'PROMETHAZINE 5 MG/ 5 ML','Syrup','10','50'),(366,'TRANEXAMIC ACID INJECTION 5 ML','Injection','50','100'),(367,'COTRIMOXAZOLE TAB DS','Tablet','500','2000'),(368,'METOCLOPRAMIDE HCL INJECTION 10ML','Injection','10','30'),(369,'TERBINAFINE HYDROCHLORIDE CREAM 15 G ','Ointment','50','100'),(370,'RANITIDINE HYDROCHLORIDE INJ 2ML','Injection','100','500');
/*!40000 ALTER TABLE `main_medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine_outward_detail`
--

DROP TABLE IF EXISTS `medicine_outward_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicine_outward_detail` (
  `meddet_id` int(11) NOT NULL AUTO_INCREMENT,
  `outw_id` int(11) NOT NULL,
  `inv_id` int(11) NOT NULL,
  `issued_qty` varchar(10) DEFAULT NULL,
  `fix_issued_qty` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`meddet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine_outward_detail`
--

LOCK TABLES `medicine_outward_detail` WRITE;
/*!40000 ALTER TABLE `medicine_outward_detail` DISABLE KEYS */;
INSERT INTO `medicine_outward_detail` VALUES (1,1,1,'10','10'),(2,2,2,'265','265'),(3,2,6,'215','215'),(4,2,4,'169','169'),(5,2,5,'102','102'),(6,2,3,'200','200'),(7,2,8,'1200','1200'),(8,2,9,'60','60'),(9,2,7,'1400','1400'),(10,2,11,'159','159'),(11,2,12,'300','300'),(12,2,10,'394','394'),(13,2,16,'945','945'),(14,2,17,'360','360'),(15,2,18,'160','160'),(16,2,15,'108','108'),(17,2,14,'220','220'),(18,2,13,'200','200'),(19,2,22,'1200','1200'),(20,2,21,'150','150'),(21,2,19,'245','245'),(22,2,20,'339','339'),(23,3,39,'220','220'),(24,3,38,'255','255'),(25,3,37,'455','455'),(26,3,36,'200','200'),(27,3,35,'370','370'),(28,3,34,'110','110'),(29,3,33,'110','110'),(30,3,33,'110','110'),(31,3,33,'110','110'),(32,3,33,'110','110'),(33,3,32,'930','930'),(34,3,31,'1000','1000'),(35,3,30,'250','250'),(36,3,29,'42','42'),(37,3,33,'110','110'),(38,3,27,'200','200'),(39,3,28,'220','220'),(40,3,26,'145','145'),(41,3,26,'145','145'),(42,3,27,'200','200'),(43,3,28,'220','220'),(44,3,29,'42','42'),(45,3,29,'42','42'),(46,3,30,'250','250'),(47,3,31,'1000','1000'),(48,3,32,'930','930'),(49,6,43,'340','340'),(50,6,44,'440','440'),(51,6,45,'1000','1000'),(52,7,23,'1440','1440'),(53,7,24,'91','91'),(54,7,25,'135','135'),(55,7,40,'120','120'),(56,8,1,'509','250'),(57,8,41,'1000','1000'),(58,8,42,'303','303'),(59,8,46,'500','500'),(60,8,47,'273','273'),(61,9,48,'900','900'),(62,9,49,'29','29'),(63,9,50,'1800','1800'),(64,9,51,'100','100'),(65,9,52,'67','67'),(66,10,64,'20','20'),(67,11,53,'28','28'),(68,11,54,'4600','4600'),(69,11,55,'792','792'),(70,11,56,'120','120'),(71,11,57,'200','200'),(72,11,58,'95','95'),(73,12,59,'38','38'),(74,12,60,'900','900'),(75,12,61,'200','200'),(76,12,62,'172','172'),(77,12,63,'200','200'),(78,12,65,'172','172'),(79,12,66,'200','200'),(80,13,67,'1800','1800'),(81,13,68,'40','40'),(82,13,69,'90','90'),(83,13,70,'140','140'),(84,13,71,'870','870'),(85,13,72,'500','500'),(86,14,73,'420','420'),(87,14,74,'1000','1000'),(88,14,75,'482','482'),(89,14,76,'78','78'),(90,14,77,'206','206'),(91,14,78,'260','260'),(92,14,79,'140','140'),(93,15,80,'100','100'),(94,15,81,'101','101'),(95,15,82,'965','965'),(96,15,83,'128','128'),(97,15,84,'420','420'),(98,15,85,'110','110'),(99,15,86,'710','710'),(100,15,87,'89','89'),(101,17,88,'241','241'),(102,17,89,'300','300'),(103,17,90,'294','294'),(104,17,91,'200','200'),(105,17,92,'1000','1000'),(106,17,93,'600','600'),(107,17,94,'69','69'),(108,18,95,'260','260'),(109,18,96,'253','253'),(110,18,97,'86','86'),(111,18,98,'390','390'),(112,18,99,'380','380'),(113,19,100,'130','130'),(114,19,101,'190','190'),(115,20,102,'80','80'),(116,20,103,'160','160'),(117,20,104,'65','65'),(118,20,105,'200','200'),(119,20,106,'330','330'),(120,21,107,'410','410'),(121,21,108,'150','150'),(122,21,109,'220','220'),(123,21,110,'409','409'),(124,21,111,'188','188'),(125,21,112,'28','28'),(126,22,113,'155','155'),(127,22,114,'331','331'),(128,22,115,'200','200'),(129,22,116,'210','210'),(130,22,117,'440','440'),(131,22,118,'130','130'),(132,23,119,'190','190'),(133,23,120,'334','334'),(134,23,121,'290','290'),(135,24,126,'5','5'),(136,24,128,'3','3'),(137,24,129,'5','5'),(138,24,130,'20','20'),(139,24,131,'6','6'),(140,24,132,'3','3'),(141,24,133,'3','3'),(142,25,127,'300','300'),(143,26,139,'4500','4500'),(144,26,138,'1200','1200'),(145,26,137,'150','150'),(146,27,140,'1800','1800'),(147,28,141,'200','200'),(148,29,221,'9','9'),(149,29,220,'15','15'),(150,30,222,'20','20'),(151,30,223,'24','24'),(152,31,224,'12','12'),(153,32,226,'600','600'),(154,33,227,'800','800'),(155,34,229,'500','500'),(156,34,228,'500','500'),(157,35,231,'180','180'),(158,35,230,'80','80'),(159,36,142,'400','400'),(160,37,235,'1400','1400'),(161,37,234,'200','200'),(162,38,245,'400','400'),(163,38,244,'500','500'),(164,38,243,'2000','2000'),(165,38,242,'200','200'),(166,38,241,'300','300'),(167,39,240,'60','60'),(168,39,239,'1000','1000'),(169,41,274,'1000','1000'),(170,41,275,'1000','1000'),(171,41,276,'200','200'),(172,41,255,'100','100'),(173,41,254,'100','100'),(174,42,253,'100','100'),(175,42,252,'800','800'),(176,42,251,'1500','1500'),(177,42,250,'200','200'),(178,43,249,'300','300'),(179,43,248,'120','120'),(180,43,273,'900','900'),(181,43,272,'500','500'),(182,43,271,'60','60'),(183,43,270,'100','100'),(184,44,269,'300','300'),(185,44,268,'100','100'),(186,44,267,'525','525'),(187,44,266,'600','600'),(188,45,289,'1500','1500'),(189,45,288,'1000','1000'),(190,46,136,'25','25'),(191,47,300,'9','9'),(192,48,308,'400','400'),(193,48,309,'1000','1000'),(194,49,323,'1000','1000'),(195,50,149,'20','20'),(196,50,162,'100','100'),(197,51,149,'20','20'),(198,52,332,'50','50');
/*!40000 ALTER TABLE `medicine_outward_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine_return`
--

DROP TABLE IF EXISTS `medicine_return`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicine_return` (
  `medret_id` int(11) NOT NULL AUTO_INCREMENT,
  `inv_id` int(11) DEFAULT NULL,
  `wardname` varchar(10) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `person_name` varchar(20) DEFAULT NULL,
  `return_qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`medret_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine_return`
--

LOCK TABLES `medicine_return` WRITE;
/*!40000 ALTER TABLE `medicine_return` DISABLE KEYS */;
/*!40000 ALTER TABLE `medicine_return` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification` (
  `Not_id` int(11) NOT NULL AUTO_INCREMENT,
  `inv_id` int(11) DEFAULT NULL,
  `filter_type` varchar(10) DEFAULT NULL,
  `flag` int(11) DEFAULT '0',
  PRIMARY KEY (`Not_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (1,12,'Expiry',0),(2,9,'Expiry',0),(3,9,'Expiry',0),(5,9,'Expiry',0),(6,12,'Expiry',0),(7,42,'Expiry',0),(8,9,'Expiry',0),(9,12,'Expiry',0),(10,42,'Expiry',0),(11,55,'Expiry',0),(12,69,'Expiry',0),(13,77,'Expiry',0),(14,9,'Expiry',0),(15,12,'Expiry',0),(16,42,'Expiry',0),(17,55,'Expiry',0),(18,69,'Expiry',0),(20,9,'Expiry',0),(22,9,'Expiry',0),(23,12,'Expiry',0);
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdClinicalHistory`
--

DROP TABLE IF EXISTS `opdClinicalHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdClinicalHistory` (
  `hcid` int(11) NOT NULL AUTO_INCREMENT,
  `conid` int(11) DEFAULT NULL,
  `hiscli` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`hcid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdClinicalHistory`
--

LOCK TABLES `opdClinicalHistory` WRITE;
/*!40000 ALTER TABLE `opdClinicalHistory` DISABLE KEYS */;
INSERT INTO `opdClinicalHistory` VALUES (1,1,'GHJLK'),(2,2,'rtujryjuy');
/*!40000 ALTER TABLE `opdClinicalHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdDiagnosis`
--

DROP TABLE IF EXISTS `opdDiagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdDiagnosis` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `conid` int(11) DEFAULT NULL,
  `diagnosisId` int(11) DEFAULT NULL,
  `diagnosisType` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdDiagnosis`
--

LOCK TABLES `opdDiagnosis` WRITE;
/*!40000 ALTER TABLE `opdDiagnosis` DISABLE KEYS */;
INSERT INTO `opdDiagnosis` VALUES (1,1,9,'Provisional Diagnosis'),(2,1,53,'Provisional Diagnosis'),(3,1,103,'Provisional Diagnosis');
/*!40000 ALTER TABLE `opdDiagnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdDocument`
--

DROP TABLE IF EXISTS `opdDocument`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdDocument` (
  `docid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `doc_name` varchar(100) DEFAULT NULL,
  `doc_date` date DEFAULT NULL,
  `doc_file_loc` varchar(100) DEFAULT NULL,
  `doc_from` varchar(20) DEFAULT NULL,
  `entry_date` date DEFAULT NULL,
  PRIMARY KEY (`docid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdDocument`
--

LOCK TABLES `opdDocument` WRITE;
/*!40000 ALTER TABLE `opdDocument` DISABLE KEYS */;
/*!40000 ALTER TABLE `opdDocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdbillingdetail`
--

DROP TABLE IF EXISTS `opdbillingdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdbillingdetail` (
  `bdid` int(11) NOT NULL AUTO_INCREMENT,
  `opmid` int(11) DEFAULT NULL,
  `invtype` varchar(50) DEFAULT NULL,
  `invname` varchar(30) DEFAULT NULL,
  `amnt` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`bdid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdbillingdetail`
--

LOCK TABLES `opdbillingdetail` WRITE;
/*!40000 ALTER TABLE `opdbillingdetail` DISABLE KEYS */;
INSERT INTO `opdbillingdetail` VALUES (1,1,'LAB','MP ','20'),(2,1,'LAB','CBC','100');
/*!40000 ALTER TABLE `opdbillingdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdbillingmain`
--

DROP TABLE IF EXISTS `opdbillingmain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdbillingmain` (
  `opmid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `opdid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `payment_status` varchar(30) DEFAULT NULL,
  `totalamount` varchar(15) DEFAULT NULL,
  `recievedby` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`opmid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdbillingmain`
--

LOCK TABLES `opdbillingmain` WRITE;
/*!40000 ALTER TABLE `opdbillingmain` DISABLE KEYS */;
INSERT INTO `opdbillingmain` VALUES (1,'2019SHD1',1,'2019-08-02','Paid','120.00','vilsan');
/*!40000 ALTER TABLE `opdbillingmain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdconsultmain`
--

DROP TABLE IF EXISTS `opdconsultmain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdconsultmain` (
  `conid` int(11) NOT NULL AUTO_INCREMENT,
  `opdid` int(11) DEFAULT NULL,
  `regno` varchar(13) DEFAULT NULL,
  `condate` date DEFAULT NULL,
  `docid` int(11) DEFAULT NULL,
  PRIMARY KEY (`conid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdconsultmain`
--

LOCK TABLES `opdconsultmain` WRITE;
/*!40000 ALTER TABLE `opdconsultmain` DISABLE KEYS */;
INSERT INTO `opdconsultmain` VALUES (1,41,'2019SHD48','2019-08-05',101),(2,48,'2019SHD14','2019-08-06',101);
/*!40000 ALTER TABLE `opdconsultmain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdreferInfo`
--

DROP TABLE IF EXISTS `opdreferInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdreferInfo` (
  `refid` int(11) NOT NULL AUTO_INCREMENT,
  `conid` int(11) DEFAULT NULL,
  `reason` varchar(60) DEFAULT '',
  `hname` varchar(50) DEFAULT NULL,
  `referby` int(11) DEFAULT NULL,
  `referto` int(11) DEFAULT NULL,
  PRIMARY KEY (`refid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdreferInfo`
--

LOCK TABLES `opdreferInfo` WRITE;
/*!40000 ALTER TABLE `opdreferInfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `opdreferInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opdvisit`
--

DROP TABLE IF EXISTS `opdvisit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `opdvisit` (
  `opdid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `ptype` varchar(5) DEFAULT NULL,
  `vdate` date DEFAULT NULL,
  `vtime` time DEFAULT NULL,
  `height` varchar(5) DEFAULT NULL,
  `weight` varchar(5) DEFAULT NULL,
  `bmi` varchar(5) DEFAULT NULL,
  `temp` varchar(3) DEFAULT NULL,
  `pulse` varchar(3) DEFAULT NULL,
  `rrate` varchar(3) DEFAULT NULL,
  `systolic` varchar(3) DEFAULT NULL,
  `diastolic` varchar(3) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `status` varchar(10) DEFAULT '',
  PRIMARY KEY (`opdid`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opdvisit`
--

LOCK TABLES `opdvisit` WRITE;
/*!40000 ALTER TABLE `opdvisit` DISABLE KEYS */;
INSERT INTO `opdvisit` VALUES (1,'2019SHD1','NEW','2019-08-02','13:47:00','90','9','11.11','98.','','','','','fever',''),(2,'2019SHD2','NEW','2019-08-02','13:52:00','','','','','','','','','body pain',''),(3,'2019SHD3','NEW','2019-08-02','16:12:00','','','','','','','','','ABDOMINAL PAIN ',''),(4,'2019SHD4','NEW','2019-08-02','16:23:00','','','','','','','','','LOOSE MOTION ',''),(5,'2019SHD5','NEW','2019-08-02','17:56:00','','','','','','','','','pregnancy, abdominal pain ',''),(6,'2019SHD7','NEW','2019-08-02','21:20:00','','','','','','','','','omiting',''),(7,'2019SHD8','NEW','2019-08-02','21:57:00','','','','','','','','','abdomen pain',''),(8,'2019SHD9','NEW','2019-08-02','23:17:00','','','','','','','','','abdomen pain',''),(9,'2019SHD10','NEW','2019-08-02','23:40:00','','','','','','','','','fever',''),(10,'2019SHD11','NEW','2019-08-03','00:36:00','','','','','','','','','delivery',''),(11,'2019SHD13','NEW','2019-08-03','08:41:00','140','40','20.41','','','','110','80','LOOSE MOTION ','');
/*!40000 ALTER TABLE `opdvisit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outward_detail`
--

DROP TABLE IF EXISTS `outward_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outward_detail` (
  `outw_id` int(11) NOT NULL AUTO_INCREMENT,
  `ward_id` int(11) NOT NULL,
  `issued_date` date DEFAULT NULL,
  `person_name` varchar(20) DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`outw_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outward_detail`
--

LOCK TABLES `outward_detail` WRITE;
/*!40000 ALTER TABLE `outward_detail` DISABLE KEYS */;
INSERT INTO `outward_detail` VALUES (1,8,'2019-07-26','abc','10:10:00'),(2,7,'2019-07-26','Pharmacy','03:18:00'),(3,7,'2019-07-26','PHARMACY','12:10:00'),(6,7,'2019-07-26','PHARMACY','12:10:00'),(7,7,'2019-07-26','PHARMACY','12:10:00'),(8,7,'2019-07-26','PHARMACY','12:10:00'),(9,7,'2019-07-26','PHARMACY','12:10:00'),(10,7,'2019-07-26','LOKESH','07:41:00'),(11,7,'2019-07-26','Pharmacy','12:10:00'),(12,7,'2019-07-26','PHARMACY','12:10:00'),(13,7,'2019-07-26','PHARMACY','12:10:00'),(14,7,'2019-07-26','PHARMACY','12:10:00'),(15,7,'2019-07-26','PHARMACY','12:10:00'),(16,7,'2019-07-26','PHARMACY','12:10:00'),(17,7,'2019-07-26','PHARMACY','12:10:00'),(18,7,'2019-07-26','PHARMACY','12:10:00'),(19,7,'2019-07-26','PHARMACY','12:10:00'),(20,7,'2019-07-26','PHARMACY','12:10:00'),(21,7,'2019-07-26','PHARMACY','12:10:00'),(22,7,'2019-07-26','PHARMACY','12:10:00'),(23,7,'2019-07-26','PHARMACY','12:10:00'),(24,7,'2019-07-26','LOKESH','08:00:00'),(25,7,'2019-07-26','LOKESH','08:00:00'),(26,7,'2019-07-26','LOKESH','08:00:00'),(27,7,'2019-07-26','LOKESH','08:00:00'),(28,7,'2019-07-26','LOKESH','08:00:00'),(29,7,'2019-08-26','LOKESH','12:00:00'),(30,7,'2019-07-26','LOKESH','12:00:00'),(31,7,'2019-07-26','LOKESH','12:00:00'),(32,7,'2019-07-26','LOKESH','12:00:00'),(33,7,'2019-07-26','LOKESH','12:00:00'),(34,7,'2019-07-26','LOKESH','12:00:00'),(35,7,'2019-07-26','LOKESH','12:00:00'),(36,7,'2019-07-26','LOKESH','12:00:00'),(37,7,'2019-07-26','LOKESH','12:00:00'),(38,7,'2019-07-26','LOKESH','12:00:00'),(39,7,'2019-07-26','LOKESH','12:00:00'),(41,7,'2019-07-26','LOKESH','12:00:00'),(42,7,'2019-07-26','LOKESH','12:00:00'),(43,7,'2019-07-26','LOKESH','12:00:00'),(44,7,'2019-07-26','LOKESH','12:00:00'),(45,7,'2019-08-01','LOKESH','08:00:00'),(46,7,'2019-08-01','LOKESH','08:00:00'),(47,7,'2019-08-01','LOKESH','08:00:00'),(48,7,'2019-08-01','LOKESH','08:00:00'),(49,7,'2019-08-05','TORANBHAIYA','08:00:00'),(50,1,'2019-08-05','SUMAN','11:21:00'),(51,4,'2019-08-05','ROSHNI','10:52:00'),(52,4,'2019-08-01','SUMAN','11:30:00');
/*!40000 ALTER TABLE `outward_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_registration`
--

DROP TABLE IF EXISTS `patient_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient_registration` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) NOT NULL,
  `pfname` varchar(20) DEFAULT NULL,
  `pmname` varchar(10) DEFAULT NULL,
  `psname` varchar(20) DEFAULT NULL,
  `rtype` varchar(10) DEFAULT NULL,
  `rfname` varchar(20) DEFAULT NULL,
  `rmname` varchar(10) DEFAULT NULL,
  `rsname` varchar(20) DEFAULT NULL,
  `regdate` date DEFAULT NULL,
  `regtime` time DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `agetype` varchar(7) DEFAULT NULL,
  `sex` varchar(12) DEFAULT NULL,
  `education` varchar(20) DEFAULT NULL,
  `occupation` varchar(25) DEFAULT NULL,
  `contactno` varchar(12) DEFAULT NULL,
  `pclass` varchar(15) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `tahsil` varchar(20) DEFAULT '',
  `district` varchar(20) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `cast` varchar(10) DEFAULT NULL,
  `aadharNo` varchar(12) DEFAULT '',
  `rationcard` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `regno` (`regno`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_registration`
--

LOCK TABLES `patient_registration` WRITE;
/*!40000 ALTER TABLE `patient_registration` DISABLE KEYS */;
INSERT INTO `patient_registration` VALUES (1,'2019SHD1','nehar','','thakur','Father','ishu','','thakur','2019-08-02','13:45:00','3','Years','Male','','','','-1','balod','balod','1','gadaindhi','ST','','APL'),(2,'2019SHD2','deepali','','dugga','Father','suklal','','dugga','2019-08-02','13:52:00','18','Years','Female','10','','00','1','khadgao','manpur','24','dorba','ST','','APL'),(3,'2019SHD3','omprakash ','','','Father','laxman singh','','','2019-08-02','16:11:00','54','Years','Male','','','9770731403','-1','DUNDERA ','GUNDERDEHI ','1','PARNA ','ST','00','BPL'),(4,'2019SHD4','VISHNU RAM ','BHUARYA ','','Father','MAHA SINGH ','','','2019-08-02','16:23:00','63','Years','Male','','','7646835392','-1','DALLI RAJHARA ','DONDI ','1','DALLI RAJHARA  WARD 18','ST','0','BPL'),(5,'2019SHD5','Pratima ','','','Husband','durgesh ','','dewangan','2019-08-02','17:56:00','23','Years','Female','8','','7354553181','-1','dhamtari ','dhamtari ','9','achhota','OBC','463849534929','BPL'),(7,'2019SHD7','Gopal','ram','','Father','duwaru','','','2019-08-02','21:20:00','50','Years','Male','5','mistri','7647850039','-1','mokadaah','mohla','24','serpar','ST','','BPL'),(8,'2019SHD8','harish  nishad','','','Father','manrakhan ','lal','nishad','2019-08-02','21:56:00','45','Years','Male','graduation','farmer','9179841732','-1','ghotiya ','dondi','1','pendri','OBC','','BPL'),(9,'2019SHD9','minakshi yadav','','','Husband','vijay yadav','','','2019-08-02','23:16:00','19','Years','Female','10th','house wife','9981324733','-1','chikhalakasa','dondi','1','chikhalakasa','OBC','','BPL'),(10,'2019SHD10','kavya  nayak','','','Father','harish kumar nayak','','','2019-08-02','23:39:00','11','Months','Female','no','no','8827614643','-1','','','1','WARD NO 4 DALLI RAJHARA','ST','','NONE'),(11,'2019SHD11','sawali ','','','Husband','dileshwar','','','2019-08-03','00:36:00','23','Years','Female','10th','house wife','939907212','-1','dudhli','dondi','1','korkuda','OBC','','BPL'),(13,'2019SHD13','saroj','','bai','Husband','dwarika','','prasad','2019-08-03','08:36:00','30','Years','Female','Below 10th','','8820407245','-1','balod','balod','1','sakra j','SC','','APL');
/*!40000 ALTER TABLE `patient_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surgery_details`
--

DROP TABLE IF EXISTS `surgery_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `surgery_details` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `sdate` date DEFAULT NULL,
  `stime` time DEFAULT NULL,
  `surgeon` varchar(30) DEFAULT NULL,
  `anesthesiologist` varchar(30) DEFAULT NULL,
  `ksurgerytype` varchar(10) DEFAULT NULL,
  `stype` varchar(20) DEFAULT NULL,
  `anstype` varchar(13) DEFAULT NULL,
  `psurgery` varchar(150) DEFAULT NULL,
  `spamount` varchar(10) DEFAULT NULL,
  `disease` varchar(200) DEFAULT NULL,
  `pfrom` varchar(15) DEFAULT NULL,
  `wrd_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surgery_details`
--

LOCK TABLES `surgery_details` WRITE;
/*!40000 ALTER TABLE `surgery_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `surgery_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surgery_procedure`
--

DROP TABLE IF EXISTS `surgery_procedure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `surgery_procedure` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sprocedure` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surgery_procedure`
--

LOCK TABLES `surgery_procedure` WRITE;
/*!40000 ALTER TABLE `surgery_procedure` DISABLE KEYS */;
/*!40000 ALTER TABLE `surgery_procedure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `eid` int(11) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin123',1),(2,'staff','staff123',2),(3,'jana','jana123',3);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_billing`
--

DROP TABLE IF EXISTS `ward_billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_billing` (
  `wrdbillno` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `bedcharge` varchar(15) DEFAULT '0',
  `servicecharge` varchar(15) DEFAULT '0',
  `othercharge` varchar(15) DEFAULT '0',
  `rebateamount` varchar(15) DEFAULT '0',
  `medamount` varchar(15) DEFAULT '0',
  `insalamount` varchar(15) DEFAULT '0',
  `insulineamount` varchar(15) DEFAULT '0',
  `pinjamount` varchar(15) DEFAULT '0',
  `conamount` varchar(15) DEFAULT '0',
  `suramount` varchar(15) DEFAULT '0',
  `labamount` varchar(15) DEFAULT '0',
  `xamount` varchar(15) DEFAULT '0',
  `ecgamount` varchar(15) DEFAULT '0',
  `dreamount` varchar(15) DEFAULT '0',
  `phyamount` varchar(15) DEFAULT '0',
  `therapyamount` varchar(15) DEFAULT '0',
  `paymentdate` date DEFAULT NULL,
  `paymentstatus` varchar(20) DEFAULT NULL,
  `receivedby` varchar(25) DEFAULT '',
  `totalamount` varchar(15) DEFAULT '0',
  `netamount` varchar(15) DEFAULT '0',
  PRIMARY KEY (`wrdbillno`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_billing`
--

LOCK TABLES `ward_billing` WRITE;
/*!40000 ALTER TABLE `ward_billing` DISABLE KEYS */;
INSERT INTO `ward_billing` VALUES (1,3,'10','50','1210','0','0','0','0','0','0','0','890.0','0','0','0','0','0','2019-08-04','Paid','padmini','2160','2160'),(3,3,'10','50','1210','0','0','0','0','0','0','0','890.0','0','0','0','0','0','2019-08-04','Paid','padmini','2160','2160'),(4,4,'54','56','560','0','0','0','0','0','0','0','0','0','0','0','0','0','2019-08-04','Paid','padmini','670','-330'),(5,6,'50','10','500','0','0','0','0','0','0','0','0','0','0','0','0','0','2019-08-06','Paid','rohit','560','60');
/*!40000 ALTER TABLE `ward_billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_consume_chart`
--

DROP TABLE IF EXISTS `ward_consume_chart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_consume_chart` (
  `wccid` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `wccdate` date DEFAULT NULL,
  `wcctime` time DEFAULT NULL,
  `cgivenby` varchar(20) DEFAULT NULL,
  `conname` int(11) DEFAULT NULL,
  `cqty` varchar(10) DEFAULT NULL,
  `camount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`wccid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_consume_chart`
--

LOCK TABLES `ward_consume_chart` WRITE;
/*!40000 ALTER TABLE `ward_consume_chart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_consume_chart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_delivery`
--

DROP TABLE IF EXISTS `ward_delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) NOT NULL,
  `regno` varchar(13) DEFAULT NULL,
  `deliverydate` date DEFAULT NULL,
  `m_edu` varchar(20) DEFAULT NULL,
  `f_edu` varchar(20) DEFAULT NULL,
  `gravida` varchar(20) DEFAULT NULL,
  `noflivechild` varchar(30) DEFAULT NULL,
  `ut_height` varchar(10) DEFAULT NULL,
  `dtype` varchar(50) DEFAULT NULL,
  `mstatus` varchar(20) DEFAULT NULL,
  `dreason` varchar(200) DEFAULT NULL,
  `deathtime` time DEFAULT NULL,
  `ddate` date DEFAULT NULL,
  `doctorname` varchar(50) DEFAULT NULL,
  `sistername` varchar(50) DEFAULT NULL,
  `bcareby` varchar(50) DEFAULT NULL,
  `enterby` varchar(50) DEFAULT NULL,
  `nofbaby` int(2) DEFAULT NULL,
  `damount` varchar(10) DEFAULT NULL,
  `placenta_delivered` varchar(30) DEFAULT NULL,
  `pph` varchar(10) DEFAULT NULL,
  `pstatus` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_delivery`
--

LOCK TABLES `ward_delivery` WRITE;
/*!40000 ALTER TABLE `ward_delivery` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_dressing`
--

DROP TABLE IF EXISTS `ward_dressing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_dressing` (
  `dressing_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `dressing_date` date DEFAULT NULL,
  `dressing_name` int(11) DEFAULT NULL,
  `dressing_amount` varchar(10) DEFAULT NULL,
  `dressing_doneby` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dressing_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_dressing`
--

LOCK TABLES `ward_dressing` WRITE;
/*!40000 ALTER TABLE `ward_dressing` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_dressing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_intake_chart`
--

DROP TABLE IF EXISTS `ward_intake_chart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_intake_chart` (
  `intake_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `idate` date DEFAULT NULL,
  `itime` time DEFAULT NULL,
  `iintaketype` varchar(15) DEFAULT NULL,
  `meddet_id` int(11) DEFAULT NULL,
  `idose` varchar(10) DEFAULT NULL,
  `iunit` varchar(5) DEFAULT NULL,
  `igivenby` varchar(30) DEFAULT NULL,
  `iamount` varchar(10) DEFAULT '0',
  PRIMARY KEY (`intake_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_intake_chart`
--

LOCK TABLES `ward_intake_chart` WRITE;
/*!40000 ALTER TABLE `ward_intake_chart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_intake_chart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_main`
--

DROP TABLE IF EXISTS `ward_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_main` (
  `wrd_id` int(11) NOT NULL AUTO_INCREMENT,
  `ipdid` int(11) DEFAULT NULL,
  `regno` varchar(13) DEFAULT NULL,
  `wid` varchar(30) DEFAULT NULL,
  `bedno` int(11) DEFAULT NULL,
  `wardstatus` int(1) DEFAULT '1',
  `dischargestatus` varchar(2) DEFAULT '0',
  `history` varchar(1000) DEFAULT '',
  `diagnosis` varchar(1000) DEFAULT '',
  `advice` varchar(1000) DEFAULT '',
  `patientstatus` varchar(20) DEFAULT '',
  `death_refer_reason` varchar(1500) DEFAULT '',
  `othernotes` varchar(1500) DEFAULT '',
  `dischargeby` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`wrd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_main`
--

LOCK TABLES `ward_main` WRITE;
/*!40000 ALTER TABLE `ward_main` DISABLE KEYS */;
INSERT INTO `ward_main` VALUES (1,1,'2019SHD3','4',106,1,'0','','','','','','',NULL),(2,2,'2019SHD5','1',124,1,'0','','','','','','',NULL),(3,4,'2019SHD8','4',118,0,'3','','','','Cured','Cured','','dr s jana');
/*!40000 ALTER TABLE `ward_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_medicine_chart`
--

DROP TABLE IF EXISTS `ward_medicine_chart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_medicine_chart` (
  `wmcid` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `meddet_id` int(11) DEFAULT NULL,
  `wmcdate` date DEFAULT NULL,
  `schedule` varchar(20) DEFAULT NULL,
  `time_dose` varchar(150) DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `givenby` varchar(30) DEFAULT NULL,
  `quantity` varchar(10) DEFAULT NULL,
  `amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`wmcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_medicine_chart`
--

LOCK TABLES `ward_medicine_chart` WRITE;
/*!40000 ALTER TABLE `ward_medicine_chart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_medicine_chart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_medicine_transfer`
--

DROP TABLE IF EXISTS `ward_medicine_transfer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_medicine_transfer` (
  `medtrans_id` int(11) NOT NULL AUTO_INCREMENT,
  `fromward` int(11) DEFAULT NULL,
  `trans_by` varchar(50) DEFAULT NULL,
  `toward` int(11) DEFAULT NULL,
  `reciverd_by` varchar(50) DEFAULT NULL,
  `trans_date` date DEFAULT NULL,
  `trans_time` time DEFAULT NULL,
  `outw_id` int(11) DEFAULT NULL,
  `meddet_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`medtrans_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_medicine_transfer`
--

LOCK TABLES `ward_medicine_transfer` WRITE;
/*!40000 ALTER TABLE `ward_medicine_transfer` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_medicine_transfer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_nursery`
--

DROP TABLE IF EXISTS `ward_nursery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_nursery` (
  `ns_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `regno` varchar(13) DEFAULT NULL,
  `ns_mother_name` varchar(30) DEFAULT NULL,
  `ns_mother_regno` varchar(13) DEFAULT NULL,
  `ns_mother_bedno` varchar(10) DEFAULT NULL,
  `ns_doa` date DEFAULT NULL,
  `ns_toa` time DEFAULT NULL,
  `ns_wt_adm` varchar(10) DEFAULT NULL,
  `ns_dob` date DEFAULT NULL,
  `ns_tob` time DEFAULT NULL,
  `ns_wt_birth` varchar(10) DEFAULT NULL,
  `ns_edd` date DEFAULT NULL,
  `ns_apgar0` int(2) DEFAULT NULL,
  `ns_apgar1` int(2) DEFAULT NULL,
  `ns_apgar5` int(2) DEFAULT NULL,
  `ns_delivery_from` varchar(20) DEFAULT NULL,
  `ns_mod` varchar(30) DEFAULT NULL,
  `ns_cdd` varchar(30) DEFAULT NULL,
  `ns_baby` varchar(30) DEFAULT NULL,
  `ns_color` varchar(30) DEFAULT NULL,
  `ns_thrive` varchar(30) DEFAULT NULL,
  `ns_sucking` varchar(30) DEFAULT NULL,
  `ns_complaints` varchar(500) DEFAULT NULL,
  `ns_others` varchar(500) DEFAULT NULL,
  `ns_diagnosis` varchar(500) DEFAULT NULL,
  `ns_registered_by` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ns_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_nursery`
--

LOCK TABLES `ward_nursery` WRITE;
/*!40000 ALTER TABLE `ward_nursery` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_nursery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_nursery_therapy`
--

DROP TABLE IF EXISTS `ward_nursery_therapy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_nursery_therapy` (
  `therapy_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `therapy_date` date DEFAULT NULL,
  `therapy_givenby` varchar(20) DEFAULT NULL,
  `therapy_name` varchar(20) DEFAULT NULL,
  `therapy_starttime` time DEFAULT NULL,
  `therapy_endtime` time DEFAULT NULL,
  `therapy_duration` varchar(20) DEFAULT NULL,
  `therapy_amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`therapy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_nursery_therapy`
--

LOCK TABLES `ward_nursery_therapy` WRITE;
/*!40000 ALTER TABLE `ward_nursery_therapy` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_nursery_therapy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_nursery_tprchart`
--

DROP TABLE IF EXISTS `ward_nursery_tprchart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_nursery_tprchart` (
  `ns_tpr_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `tpr_date` date DEFAULT NULL,
  `tpr_givenby` varchar(20) DEFAULT NULL,
  `tpr_time` time DEFAULT NULL,
  `tpr_temp` varchar(10) DEFAULT NULL,
  `tpr_respiration` varchar(10) DEFAULT NULL,
  `tpr_urine` varchar(10) DEFAULT NULL,
  `tpr_stool` varchar(10) DEFAULT NULL,
  `tpr_spo2` varchar(10) DEFAULT NULL,
  `tpr_weight` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ns_tpr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_nursery_tprchart`
--

LOCK TABLES `ward_nursery_tprchart` WRITE;
/*!40000 ALTER TABLE `ward_nursery_tprchart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_nursery_tprchart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_patient_transfer`
--

DROP TABLE IF EXISTS `ward_patient_transfer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_patient_transfer` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `from_wid` int(11) DEFAULT NULL,
  `from_bid` int(11) DEFAULT NULL,
  `to_wid` int(11) DEFAULT NULL,
  `to_bid` int(11) DEFAULT NULL,
  `trans_reason` varchar(100) DEFAULT NULL,
  `transfer_by` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_patient_transfer`
--

LOCK TABLES `ward_patient_transfer` WRITE;
/*!40000 ALTER TABLE `ward_patient_transfer` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_patient_transfer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_physiotherapy`
--

DROP TABLE IF EXISTS `ward_physiotherapy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_physiotherapy` (
  `physiotherapy_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `physiotherapy_date` date DEFAULT NULL,
  `physiotherapy_name` int(11) DEFAULT NULL,
  `physiotherapy_amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`physiotherapy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_physiotherapy`
--

LOCK TABLES `ward_physiotherapy` WRITE;
/*!40000 ALTER TABLE `ward_physiotherapy` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_physiotherapy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_poision_chart`
--

DROP TABLE IF EXISTS `ward_poision_chart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_poision_chart` (
  `pos_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `pdate` date DEFAULT NULL,
  `ptime` time DEFAULT NULL,
  `pinjection` int(11) DEFAULT NULL,
  `pdose` varchar(10) DEFAULT NULL,
  `punit` varchar(10) DEFAULT NULL,
  `pgivenby` varchar(30) DEFAULT NULL,
  `pamount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`pos_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_poision_chart`
--

LOCK TABLES `ward_poision_chart` WRITE;
/*!40000 ALTER TABLE `ward_poision_chart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_poision_chart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_sugar_chart`
--

DROP TABLE IF EXISTS `ward_sugar_chart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_sugar_chart` (
  `sugar_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `sdate` date DEFAULT NULL,
  `stime` time DEFAULT NULL,
  `sugarlevel` varchar(30) DEFAULT NULL,
  `sinsuline` int(11) DEFAULT NULL,
  `sdose` varchar(10) DEFAULT NULL,
  `sunit` varchar(10) DEFAULT NULL,
  `sgivenby` varchar(30) DEFAULT NULL,
  `samount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`sugar_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_sugar_chart`
--

LOCK TABLES `ward_sugar_chart` WRITE;
/*!40000 ALTER TABLE `ward_sugar_chart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_sugar_chart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ward_tpr_chart`
--

DROP TABLE IF EXISTS `ward_tpr_chart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ward_tpr_chart` (
  `tpr_id` int(11) NOT NULL AUTO_INCREMENT,
  `wrd_id` int(11) DEFAULT NULL,
  `tdate` date DEFAULT NULL,
  `ttime` time DEFAULT NULL,
  `ttemp` varchar(10) DEFAULT NULL,
  `tpulse` varchar(10) DEFAULT NULL,
  `tsystolic` varchar(10) DEFAULT NULL,
  `tdiastolic` varchar(10) DEFAULT NULL,
  `trespiration` varchar(10) DEFAULT NULL,
  `tfhs` varchar(10) DEFAULT NULL,
  `tspo2` varchar(10) DEFAULT NULL,
  `tgivenby` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`tpr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ward_tpr_chart`
--

LOCK TABLES `ward_tpr_chart` WRITE;
/*!40000 ALTER TABLE `ward_tpr_chart` DISABLE KEYS */;
/*!40000 ALTER TABLE `ward_tpr_chart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xray`
--

DROP TABLE IF EXISTS `xray`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xray` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `regno` varchar(13) DEFAULT NULL,
  `xdate` date DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `xtype` varchar(25) NOT NULL,
  `stype` varchar(25) NOT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `upload` varchar(500) DEFAULT NULL,
  `location` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xray`
--

LOCK TABLES `xray` WRITE;
/*!40000 ALTER TABLE `xray` DISABLE KEYS */;
/*!40000 ALTER TABLE `xray` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-06  1:37:30
