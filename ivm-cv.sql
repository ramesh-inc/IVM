-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 01, 2019 at 08:44 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ivm-cv`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `job_type` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `company_name`, `address`, `phone`, `email`, `job_type`) VALUES
(1, 'Training Data', '241, Fake Street, Fake Town.', '0114589652', 'training@vacancy.com', 'Full Time');

-- --------------------------------------------------------

--
-- Table structure for table `cv_meta`
--

CREATE TABLE `cv_meta` (
  `id` int(11) NOT NULL,
  `metakey` varchar(255) NOT NULL,
  `metavalue` longtext NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cv_meta`
--

INSERT INTO `cv_meta` (`id`, `metakey`, `metavalue`) VALUES
(1, 'predict_cat', 'job'),
(2, 'predict_cat', 'salary');

-- --------------------------------------------------------

--
-- Table structure for table `cv_q`
--

CREATE TABLE `cv_q` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `skills` text NOT NULL,
  `currentjob` text NOT NULL,
  `projects` longtext NOT NULL,
  `experience_yrs` text NOT NULL,
  `university` text NOT NULL,
  `degree` text NOT NULL,
  `specialization` text NOT NULL,
  `objectives` longtext NOT NULL,
  `salary` text NOT NULL,
  `nbstatus` int(11) NOT NULL DEFAULT '0',
  `dtstatus` int(11) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cv_q`
--

INSERT INTO `cv_q` (`id`, `userid`, `age`, `skills`, `currentjob`, `projects`, `experience_yrs`, `university`, `degree`, `specialization`, `objectives`, `salary`, `nbstatus`, `dtstatus`) VALUES
(8, 8, 30, 'Java,OOP,AOP,JSP,REST,AJAX,JavaScript,CSS,HTML,JEE,EJB,JMS,XML,Hibernate,Spring,SQL', 'Senior Software Engineer', '', '5', 'University of Moratuwa', 'BSc(Hons) in Information Technology', 'Software Eng', '', '200000-250000', 1, 1),
(7, 7, 24, 'React Native,Android,Javascript', 'Trainee Software Engineer', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '15000-30000', 1, 1),
(6, 6, 24, 'Angular,.net', 'Associate software engineer', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software engineering', '', '60000-100000', 1, 1),
(4, 4, 20, 'Android,iOS,Java,C', 'Intern', '', '0', 'SLIIT', 'IT', 'IT', '', '10000-15000', 1, 1),
(5, 5, 23, 'Java,Php,MERN,Wordpress,C#,Python,CPP,C,SQL,JS,HTML,CSS', 'Associate Software Engineer', '', '1', 'Sri Lanka Institute of Information Technology', 'BSc(Hons) in Information Technology', 'Software Eng', '', '60000-100000', 1, 1),
(2, 2, 20, 'Java,C,Android', 'Associate Software Eng', '', '1', 'NSBM', 'SE', 'Software Eng', '', '30000-60000', 1, 1),
(3, 3, 25, 'PHP,Android,iOS', 'Software Eng', '', '4', 'CINEC', 'Cyber', 'Cyber Security', '', '60000-100000', 1, 1),
(9, 9, 22, 'React,React native,Angular,Ionic,C,C++,C#,Java,Python,Node,Swift', 'Associate Software Engineer', '', '1', 'SLIIT', 'Bsc(Hons) in Information Technology', 'Software Engineering', '', '30000-60000', 1, 1),
(10, 10, 23, 'Java', 'Associate Software Engineer', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '30000-60000', 1, 1),
(11, 11, 24, 'Java,c,c++', 'Trainee business analyst', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information technology', '', '15000-30000', 1, 1),
(12, 12, 25, 'Python,Java,Oracle,R', 'Data Engineer', '', '1', 'SLIIT', 'Bsc(Hons) in Information Technology', 'Data science', '', '30000-60000', 1, 1),
(13, 13, 23, 'Java,test case writing', 'Associate Quality Assurance Engineer', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information Technology', '', '30000-60000', 1, 1),
(14, 14, 22, 'Test case writing', 'Trainee QA', '', '1', 'SLIIT', 'BSc(Hons) in IT', 'Information Technology', '', '15000-30000', 1, 1),
(15, 15, 21, 'Test case writing', 'Intern QA', '', '0', 'SLIIT', 'BSc(Hons) in IT', 'IT', '', '10000-15000', 1, 1),
(16, 16, 23, 'Angular,.net', 'Associate software engineer', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software engineering', '', '60000-100000', 1, 1),
(17, 17, 24, 'Java', 'BA', '', '1', 'SLIIT', 'BSc in IT', 'Information Technology', '', '60000-100000', 1, 1),
(18, 18, 31, 'SEO,Angular,PHP,wordpress,graphics', 'Social media consultant', '', '7', 'SLIIT', 'Bsc.in IT', 'Information technology', '', '30000-60000', 1, 1),
(19, 19, 24, 'React,angular,java,c++,php,html,css,c#', 'Associate software engineer', '', '1', 'Sri lanka institute of information technology', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '60000-100000', 1, 1),
(20, 20, 23, 'C#,Java,Angular', 'Associate Software Engineer', '', '1', 'Esoft', 'BSc(Hons) in Information technology', 'Software engineering', '', '30000-60000', 1, 1),
(21, 21, 26, 'Java,C#,Angular,PHP', 'Software Engineer', '', '2', 'IIT', 'BSc(Hons) in Information technology', 'Information technology', '', '60000-100000', 1, 1),
(22, 22, 27, 'Java', 'QA Engineer', '', '2', 'IIT', 'BSc(Hons) in Information technology', 'Information Technology', '', '60000-100000', 1, 1),
(23, 23, 26, 'Use cases,UML diagrams', 'Business Analyst', '', '2', 'IIT', 'BSc(Hons) in Information technology', 'Information Technology', '', '60000-100000', 1, 1),
(24, 24, 32, 'Test cases,Java,Selenium', 'Associate QA lead', '', '7', 'SLIIT', 'BSc(Hons) In IT', 'IT', '', '150000-200000', 1, 1),
(25, 25, 33, 'Test cases', 'QA lead', '', '8', 'NIBM', 'BSc(Hons) in IT', 'IT', '', '150000-200000', 1, 1),
(26, 26, 25, 'Java', 'Business Analyst', '', '2', 'IIT', 'BSc (Hons) in IT', 'IT', '', '30000-60000', 1, 1),
(27, 27, 30, 'C#,Microservices,SAAS,PAAS,Clean and tested commits to GIT,JAva,C++,C,Android,React,PHP', 'Senior Software Engineer', '', '5', 'University of Moratuwa', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '200000-250000', 1, 1),
(28, 28, 29, 'Java,C++,Selenium,HTML,CSS,Test cases', 'Senior Software Quality Assurance Engineer', '', '4', 'University of Colombo', 'BSc in Computer Science', 'Computer Science', '', '100000-150000', 1, 1),
(29, 29, 31, 'Docker,Kubernates,Istio,AWS,Apache Kafka,Elastic,React,BDD,Test Automation,JAVA/J2EE,Spring,Hibernate/J PA,EJB,JMS,Node JS,Oracle', 'Senior Software Engineer', '', '5', 'University of Kelaniya', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '200000-250000', 1, 1),
(30, 30, 27, 'C#,Ajax,WebAPI,.Net 4.6/4.7,.Net core,LINQ,Entity framework,SQL server', 'Software Engineer', '', '2', 'University of Colombo', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '100000-150000', 1, 1),
(31, 31, 29, 'Java,.Net,SQL,C++,C,OOP,APEX', 'Senior Software Engineer', '', '4', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information Technology', '', '150000-200000', 1, 1),
(32, 32, 33, 'Java design patterns,Architecture patterns,JSP/servelets,Spring,Spring boot,Hibernate,SOA,Designing systems,Database and deployment architecture,React,React Native,Angular,Oracle,MYSQL,Linux and Windows operating systems,Experience in code reviewing,team grooming', 'Senior Software Engineer', '', '5', 'University of Moratuwa', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '200000-250000', 1, 1),
(33, 33, 30, 'Java,C++,SQL,Cake PHP,Laravel,Ruby on Rails,RESTful,SOAP,Experience on cross browser compatibility,W3C standards,Database concepts,Relational databases,Experience on Unix/Linux', 'Senior Software Engineer', '', '5', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '150000-200000', 1, 1),
(34, 34, 30, 'Java,Laravel,AWS,Bootstrap,React JS,Rest API,Unit testing framework', 'Senior Software Engineer', '', '4', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information Technology', '', '15000-30000', 1, 1),
(35, 35, 32, 'Java,C++,J2EE/JEE,Spring framework,Oracle,MSSQL,NoSQL,Unit testing,Engineering best practices,Build,Package and deployment tools', 'Senior Software Engineer', '', '5', 'University of Colombo', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '15000-30000', 1, 1),
(36, 36, 28, 'Java,NodeJs,ReactJS,AngularJs,Jquery,Javascript,HTML5,CSS,Oracle 11g,PL SQL', 'Senior Software Engineer', '', '4', 'University of Colombo', 'BSc(Hons) in Information Technology', 'Information Technology', '', '150000-200000', 1, 1),
(37, 37, 30, 'Java,OOP,C++,Selinium,Test cases,HTML,CSS', 'Senior Software Quality Assurance engineer', '', '3', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information Technology', '', '150000-200000', 1, 1),
(38, 38, 25, 'Java,Knowledge in Quality Assurance and testing,Test management(Manual),automation and performance tools,Selenium,Knowledge on Agile/Scrum', 'Associate Software Quality Engineer', '', '1', 'University of Colombo', 'BSc(Hons) in Information Technology', 'Information Technology', '', '60000-100000', 1, 1),
(39, 39, 26, 'Java,Knowledge on Software Quality Assurance and testing,Knowledge in automation and performance,Knowledge in software development', 'Software Quality Assurance Engineer', '', '1', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information Technology', '', '60000-100000', 1, 1),
(40, 40, 30, 'JEE,HTML,CSS,SOAP,REST,Spring,Spring Boot/Cloud,Hibernate,Java script,AngularJS,React,Linux,Database clustering,Multi-tenant application design,Load balancing,Designing time critical application and high transactional application,Jenkins,Elasticsearch,Artificial Intelligence,Activity Engine ', 'Senior Software Engineer', '', '3', 'University of Moratuwa', 'BSc (Hons) in IT', 'Information Technology', '', '100000-150000', 1, 1),
(41, 41, 29, 'JavaScript,HTML,CSS,OOP,MVC,MVVM,JQuery,Angular,React,Riot,Typescript,Webpack,RESTful API,Sass,LESS', 'Senior Software Engineer', '', '4', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Engineering', '', '150000-200000', 1, 1),
(42, 42, 31, 'Java,Functional,UI,Web services,Performance testing,Test cases,Selenium,OOP,Problem solving skills,JMeter,JIRA,Scrum process,Knowledge in Test management tools', 'Senior QA Engineer', '', '4', 'University of Moratuwa', 'BSc (Hons) in IT', 'Information Technology', '', '150000-200000', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `cv_q_meta`
--

CREATE TABLE `cv_q_meta` (
  `id` int(11) NOT NULL,
  `metakey` varchar(255) NOT NULL,
  `metavalue` longtext NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cv_q_meta`
--

INSERT INTO `cv_q_meta` (`id`, `metakey`, `metavalue`) VALUES
(1, 'age', '18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35'),
(2, 'skills', 'Internet of Things,Java,C,C++,Python,PHP,Android,iOS,HR Management,Marketing,Hybernate,JavaEE,Servlet,React,Angular,MERN,MEAN,NodeJS,ExpressJS,IOT,Machine Learning,ML,Virtual Reality,VR,Artificial Intelligence,AI,Blockchain,Augmented Reality,AR,Cloud Computing,Intelligent Apps,I–Apps,Big Data,Robotic Process Automation,RPA,.Net,Ruby,Wordpress,C#,CPP,SQL,JS,HTML,CSS,React Native,Javascript,OOP,AOP,JSP,REST,AJAX,JEE,EJB,JMS,XML,Hibernate,Spring,Ionic,Node,Swift,Oracle,R,test case writing,graphics,Use cases,UML diagrams,Test cases,Selenium,Microservices,SAAS,PAAS,Clean and tested commits to GIT,Docker,Kubernates,Istio,AWS,Apache Kafka,Elastic,BDD,Test Automation,Spring,Hibernate/J PA,Node JS,Oracle,WebAPI,.Net 4.6/4.7,.Net core,LINQ,Entity framework,SQL server,Java design patterns,Architecture patterns,JSP/servelets,Spring,Spring boot,Hibernate,SOA,Designing systems,Database and deployment architecture,MYSQL,Linux and Windows operating systems,Experience in code reviewing,team grooming,Cake PHP,Laravel,Ruby on Rails,RESTful,Experience on cross browser compatibility,W3C standards,Database concepts,Relational databases,Experience on Unix/Linux,Bootstrap,React JS,Rest API,Unit testing framework,Spring framework,MSSQL,NoSQL,Unit testing,Engineering best practices,Build,Package and deployment tools,Experience in one or more web and application servers,Oracle 11g,PL SQL,Jquery,Javascript,HTML5,Knowledge in Quality Assurance and testing,Test management(Manual),automation and performance tools,Selenium,Knowledge on Agile/Scrum,Knowledge in automation and performance,Knowledge in software development,Spring Boot/Cloud,Database clustering,Multi-tenant application design,Load balancing,Designing time critical application and high transactional application,Jenkins,Elasticsearch,Artificial Intelligence,Activity Engine,activity engine ,MVC,MVVM,Riot,Typescript,Webpack,RESTful API,Sass,LESS,Ability to work within deadlines,Problem solving and communication skills,Ability to learn new technologies quickly,Ability to understand the importance of customer service,Innovative and forward thinking,Functional,UI,Web services,Performance testing,Problem solving skills,JMeter,JIRA,Scrum process,Knowledge in Test management tools,SEO,java/j2ee,apex,soap,j2ee/jee,reactjs,angularjs,selinium,knowledge on software quality assurance and testing,java script,linux'),
(3, 'job', 'Associate Software Eng,Software Eng,Senior Software Eng,Assistant Account,Accountant,Devops Eng,Quality Assurance Eng,Intern,Cloud Architect,Cloud Consultant,Cloud Product and Project Manager,Cloud Services Developer,Cloud Software and Network Engineer,Cloud System Administrator,Cloud System Engineer,Computer and Information Research Scientist,Computer and Information Systems Manager,Computer Network Architect,Computer Systems Analyst,Computer Systems Manager,IT Analyst,IT Coordinator,Network Administrator,Network Architect,Network and Computer Systems Administrator,Network Engineer,Network Systems Administrator,Senior Network Architect,Senior Network Engineer,Senior Network System Administrator,Telecommunications Specialist,Customer Support Administrator,Customer Support Specialist,Desktop Support Manager,Desktop Support Specialist,Help Desk Specialist,Help Desk Technician,IT Support Manager,IT Support Specialist,IT Systems Administrator,Senior Support Specialist,Senior System Administrator,Support Specialist,Systems Administrator,Technical Specialist,Technical Support Engineer,Technical Support Specialist,Data Center Support Specialist,Data Quality Manager,Database Administrator,Senior Database Administrator,Application Support Analyst,Senior System Analyst,Systems Analyst,Systems Designer,Chief Information Officer,Chief Technology Officer,Director of Technology,IT Director,IT Manager,Management Information Systems Director,Technical Operations Officer,Information Security,Security Specialist,Senior Security Specialist,Application Developer,Applications Engineer,Associate Developer,Computer Programmer,Developer,Java Developer,Junior Software Engineer,.NET Developer,Programmer Analyst,Senior Applications Engineer,Senior Programmer,Senior Programmer Analyst,Senior Software Engineer,Senior System Architect,Senior System Designer,Senior Systems Software Engineer,Software Architect,Software Developer,Software Engineer,Software Quality Assurance Analyst,System Architect,Systems Software Engineer,Front End Developer,Senior Web Administrator,Senior Web Developer,Web Administrator,Web Developer,Webmaster,Associate Software Engineer,Software Engineering,Trainee Software Engineer,Associate Quality Assurance Engineer,Associate QA Engineer,Trainee QA,Intern QA,BA,Senior Software Engineer,Senior Software Quality Assurance Engineer,Associate Software Quality Engineer,Associate Software Quality Assurance Engineer,BSc in Computer Science,Information Technology or equivalent professional qualification,Senior QA Engineer,trainee business analyst,data engineer,social media consultant,qa engineer,business analyst,associate qa lead,qa lead,software quality assurance engineer'),
(4, 'experience_yrs', '0,1,2,3,4,5,6,7,8,9,10'),
(5, 'university', 'SLIIT,SAITM,CINEC,NIBM,NSBM,APIIT,ANC,KDU,University of Colombo,University of Peradeniya,University of Moratuwa,University of Kelaniya,University of Ruhuna,University of Sri Jayewardenepura,University of Jaffna,University of the Visual & Performing Arts,Open University of Sri Lanka,Wayamba University of Sri Lanka,Sabaragamuwa University of Sri Lanka,Eastern University of Sri Lanka,Rajarata University of Sri Lanka,South Eastern University of Sri Lanka,Uva Wellassa University,American College of Higher Education,Auston Institute,Australian College of Business and Technology,Business Management School,BMS,British College of Applied Studies,BCAS,eBusiness Academy,eBA,ESOFT Metro Campus,ESOFT,Excellence College of Management,Imperial Institute of Higher Education,Industrial Master,Informatics Institute of Technology,IIT,Institute of Technological Studies,International College of Business and Technology,ICBT,Northshore College of Business & Technology,Pioneer Institute of Business and Technology,Royal Institute of Colombo,South Asian Institute of Technology and Medicine,Sri Lanka Institute of Information Technology,Technoplus Automation,Edulink International Campus,KASP Learning Campus,KLC'),
(6, 'degree', 'IT,SE,Cyber,BM,EN,BSc(Hons) in Information Technology,BSc (Hons) in IT,BSc in Computer Science,Bachelor\'s degree or higher qualification in Computer Science/Engineering,Degree or similar educational qualification in IT or computer science,Degree related to Information Technology/Computer Science or Software Engineering,Bachelor\'s degree in Computer Science/MIS or equivalent experience,Bachelor\'s degree in Computing or Information Technology,BSc in Computer Science or related discipline or IT,BSc in Computer Science or related discipline or equivalent professional qualification,B.Sc. in Computer Science related discipline or equivalent professinal qualification,bsc(hons) in it,bsc in it,bsc.in it,BSc in Computer Science'),
(7, 'specialization', 'Software Eng,Cyber Security,IT,Account,Marketing,Software engineering,Information technology,BSc in Computer Science,data science,computer science'),
(8, 'salary', '10000-15000,15000-30000,30000-60000,60000-100000,100000-150000,150000-200000,200000-250000,250000-300000,300000-350000,350000-400000,400000-500000,500000-700000,700000-1000000,>1000000');

-- --------------------------------------------------------

--
-- Table structure for table `cv_q_predict`
--

CREATE TABLE `cv_q_predict` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `skills` text NOT NULL,
  `projects` longtext NOT NULL,
  `experience_yrs` text NOT NULL,
  `university` text NOT NULL,
  `degree` text NOT NULL,
  `specialization` text NOT NULL,
  `objectives` longtext NOT NULL,
  `nbstatus` int(11) NOT NULL DEFAULT '0',
  `dtstatus` int(11) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cv_q_predict`
--

INSERT INTO `cv_q_predict` (`id`, `userid`, `age`, `skills`, `projects`, `experience_yrs`, `university`, `degree`, `specialization`, `objectives`, `nbstatus`, `dtstatus`) VALUES
(1, 1, 18, 'C++,Java,Python', '', '0', 'SLIIT', 'IT', 'IT', '', 1, 1),
(3, 4, 28, 'Java,Android,C++', '', '3', 'SLIIT', 'SE', 'Software Eng', '', 1, 1),
(4, 5, 28, 'Hybernate,JavaEE,Servlet', '', '2', 'NSBM', 'IT', 'Software Eng', '', 1, 1),
(5, 7, 24, 'PHP,Android,JavaEE', '', '2', 'KDU', 'BSc(Hons) in Information Technology', 'Software Eng', '', 1, 1),
(6, 11, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Eng', '', 1, 1),
(21, 26, 30, 'MetaSploit,Kali Linux', '', '3', 'CINEC', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(18, 23, 23, 'C,CPP,Java,Python,C#', '', '3', 'CINEC', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(19, 24, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '5', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Eng', '', 1, 1),
(16, 21, 35, 'MetaSploit,Kali Linux', '', '4', 'SLIIT', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(20, 25, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '5', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Eng', '', 1, 1),
(22, 27, 30, 'MetaSploit,Kali Linux', '', '3', 'CINEC', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(23, 28, 32, 'MetaSploit,Kali Linux', '', '5', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Eng', '', 1, 1),
(24, 29, 33, 'C,CPP', '', '1', 'CINEC', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(25, 30, 33, 'C,CPP', '', '1', 'CINEC', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(26, 31, 33, 'C,CPP', '', '1', 'CINEC', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(27, 32, 33, 'C,CPP', '', '1', 'CINEC', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(28, 33, 25, 'MetaSploit,Kali Linux', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(29, 34, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(30, 35, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(31, 36, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(32, 37, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(33, 38, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(34, 39, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(35, 40, 23, 'C,CPP', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(38, 43, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Software Eng', '', 1, 1),
(37, 42, 22, 'C,CPP', '', '2', 'CINEC', 'BSc(Hons) in Information Technology', 'IT', '', 1, 1),
(39, 44, 24, 'C,CPP,Java,Python,C#', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Information technology', '', 1, 1),
(40, 45, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(41, 46, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(42, 47, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(43, 48, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1),
(44, 49, 23, 'C,CPP,Java,Python,C#,MERN,REACT', '', '2', 'SLIIT', 'BSc(Hons) in Information Technology', 'Cyber Security', '', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `dt_prediction`
--

CREATE TABLE `dt_prediction` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `jobPrediction` text,
  `jobPrecentage` varchar(10) DEFAULT NULL,
  `salary` text,
  `salPrecentage` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dt_prediction`
--

INSERT INTO `dt_prediction` (`id`, `userid`, `jobPrediction`, `jobPrecentage`, `salary`, `salPrecentage`) VALUES
(18, 5, 'intern', '100.0', '10000-15000', '100.0'),
(17, 4, 'associate software eng', '100.0', '30000-60000', '100.0'),
(16, 1, 'intern', '100.0', '10000-15000', '100.0'),
(21, 7, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(22, 11, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(24, 19, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(25, 21, 'senior software engineer', '0.0', '30000-60000', '0.0'),
(27, 23, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(28, 24, 'senior software engineer', '0.0', '200000-250000', '0.0'),
(29, 25, 'senior software engineer', '0.0', '200000-250000', '0.0'),
(30, 26, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(31, 27, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(32, 28, 'senior software engineer', '0.0', '200000-250000', '0.0'),
(33, 29, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(34, 30, 'senior software engineer', '0.0', '200000-250000', '0.0'),
(35, 31, 'senior software engineer', '0.0', '200000-250000', '0.0'),
(36, 32, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(37, 33, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(38, 34, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(39, 35, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(40, 36, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(41, 37, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(42, 38, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(43, 39, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(44, 40, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(46, 42, 'associate software eng', '0.0', '30000-60000', '0.0'),
(47, 43, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(48, 44, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(49, 45, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(50, 46, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(51, 47, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(52, 48, 'associate software engineer', '0.0', '60000-100000', '0.0'),
(53, 49, 'associate software engineer', '0.0', '60000-100000', '0.0');

-- --------------------------------------------------------

--
-- Table structure for table `ivm_anonimyzation`
--

CREATE TABLE `ivm_anonimyzation` (
  `id` int(11) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `nic` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ivm_anonimyzation`
--

INSERT INTO `ivm_anonimyzation` (`id`, `user_id`, `name`, `email`, `address`, `phone`, `nic`) VALUES
(7, '34', 'XXXmesh', 'XXX896@gmail.com', 'XXX0', 'XXXnd', 'XXX0'),
(8, '35', 'XXXmesh', 'XXX896@gmail.com', 'XXX0', 'XXXnd', 'XXX562654V'),
(9, '36', 'XXXmesh', 'XXX896@gmail.com', 'XXX0', 'XXXnd', 'XXX562654V'),
(10, '37', 'XXXmesh', 'XXX896@gmail.com', 'XXX0', 'XXXnd', 'XXX562654V'),
(11, '38', 'XXXmesh', 'XXX896@gmail.com', 'XXX0', 'XXXand', 'XXX562654V'),
(12, '39', 'XXXmesh', 'XXX896@gmail.com', 'XXXand', 'XXX0', 'XXX562654V'),
(13, '40', 'XXXmesh', 'XXX896@gmail.com', 'XXXand', 'XXX0', 'XXX562654V'),
(15, '42', 'XXXmal', 'XXXy@gmail.com', 'XXXemodara', 'XXX7005330', 'XXX54V'),
(17, '44', 'XXXthana', 'XXXhnayake@my.sliit.lk', 'XXXotagamuwa, Hikkaduwa', 'XXX0XXX7XXX6XXX7XXX0XXX0XXX5XXX3XXX3XXX0XXX', 'XXX9XXX4XXX3XXX5XXX6XXX2XXX6XXX5XXX4XXXVXXX'),
(18, '45', 'XXXrath', 'XXXail.com', 'XXX5XXX6XXXCXXX,XXX XXXBXXXuXXXsXXX XXXSXXXtXXXaXXXnXXXdXXX', 'XXX0XXX7XXX6XXX7XXX0XXX0XXX5XXX3XXX3XXX0XXX', 'XXX8XXX8XXX4XXX5XXX4XXX6XXX9XXX5XXX6XXX5XXXVXXX'),
(19, '46', 'XXXrath', 'XXXail.com', 'XXX5XXX6XXXCXXX,XXX XXXBXXXuXXXsXXX XXXSXXXtXXXaXXXnXXXdXXX', 'XXX0XXX7XXX6XXX7XXX0XXX0XXX5XXX3XXX3XXX0XXX', 'XXX8XXX8XXX4XXX5XXX4XXX6XXX9XXX5XXX6XXX5XXXVXXX'),
(20, '47', 'XXXrath', 'XXXail.com', 'XXX5XXX6XXXCXXX,XXX XXXBXXXuXXXsXXX XXXSXXXtXXXaXXXnXXXdXXX', 'XXX0XXX7XXX6XXX7XXX0XXX0XXX5XXX3XXX3XXX0XXX', 'XXX8XXX8XXX4XXX5XXX4XXX6XXX9XXX5XXX6XXX5XXXVXXX'),
(21, '48', 'XXXrath', 'XXXail.com', 'XXX5XXX6XXXCXXX,XXX XXXBXXXuXXXsXXX XXXSXXXtXXXaXXXnXXXdXXX', 'XXX0XXX7XXX6XXX7XXX0XXX0XXX5XXX3XXX3XXX0XXX', 'XXX8XXX8XXX4XXX5XXX4XXX6XXX9XXX5XXX6XXX5XXXVXXX'),
(22, '49', 'XXXrath', 'XXXail.com', 'XXX5XXX6XXXCXXX,XXX XXXBXXXuXXXsXXX XXXSXXXtXXXaXXXnXXXdXXX', 'XXX0XXX7XXX6XXX7XXX0XXX0XXX5XXX3XXX3XXX0XXX', 'XXX8XXX8XXX4XXX5XXX4XXX6XXX9XXX5XXX6XXX5XXXVXXX');

-- --------------------------------------------------------

--
-- Table structure for table `nb_prediction`
--

CREATE TABLE `nb_prediction` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `jobPrediction` text,
  `jobPrecentage` varchar(10) DEFAULT NULL,
  `salary` text,
  `salPrecentage` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nb_prediction`
--

INSERT INTO `nb_prediction` (`id`, `userid`, `jobPrediction`, `jobPrecentage`, `salary`, `salPrecentage`) VALUES
(32, 7, 'associate software engineer', '95.07', '60000-100000', '99.75'),
(28, 1, 'intern', '99.44', '10000-15000', '99.88'),
(29, 4, 'associate software eng', '70.38', '30000-60000', '90.22'),
(30, 5, 'associate software eng', '71.37', '30000-60000', '90.68'),
(33, 11, 'associate software engineer', '79.17', '60000-100000', '98.14'),
(47, 24, 'senior software engineer', '88.19', '200000-250000', '99.29'),
(44, 21, 'associate software engineer', '38.04', '60000-100000', '99.54'),
(57, 34, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(56, 33, 'associate software engineer', '44.98', '60000-100000', '98.2'),
(42, 19, 'associate software engineer', '84.06', '60000-100000', '99.7'),
(46, 23, 'associate software engineer', '49.22', '60000-100000', '98.56'),
(48, 25, 'senior software engineer', '88.19', '200000-250000', '99.29'),
(49, 26, 'senior software engineer', '84.73', '200000-250000', '95.3'),
(50, 27, 'senior software engineer', '84.73', '200000-250000', '95.3'),
(51, 28, 'senior software engineer', '87.97', '200000-250000', '99.28'),
(52, 29, 'associate software engineer', '89.33', '60000-100000', '99.82'),
(53, 30, 'associate software engineer', '89.33', '60000-100000', '99.82'),
(54, 31, 'associate software engineer', '89.33', '60000-100000', '99.82'),
(55, 32, 'associate software engineer', '89.33', '60000-100000', '99.82'),
(58, 35, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(59, 36, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(60, 37, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(61, 38, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(62, 39, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(63, 40, 'associate software engineer', '53.03', '60000-100000', '94.53'),
(65, 42, 'associate software engineer', '44.91', '60000-100000', '98.26'),
(66, 43, 'associate software engineer', '79.17', '60000-100000', '98.14'),
(67, 44, 'associate software engineer', '91.62', '60000-100000', '99.41'),
(68, 45, 'associate software engineer', '62.05', '60000-100000', '99.09'),
(69, 46, 'associate software engineer', '62.05', '60000-100000', '99.09'),
(70, 47, 'associate software engineer', '62.05', '60000-100000', '99.09'),
(71, 48, 'associate software engineer', '62.05', '60000-100000', '99.09'),
(72, 49, 'associate software engineer', '62.05', '60000-100000', '99.09');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `nic` varchar(15) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` int(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `age`, `name`, `address`, `nic`, `email`, `phone`) VALUES
(1, 18, '', '', '', '', 0),
(2, 20, '', '', '', '', 0),
(3, 25, '', '', '', '', 0),
(4, 30, '', '', '', '', 0),
(43, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(6, 24, '', '', '', '', 0),
(7, 30, '', '', '', '', 0),
(8, 18, '', '', '', '', 0),
(13, 24, '', '', '', '', 0),
(33, 25, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(11, 23, '', '', '', '', 0),
(21, 35, 'Test', 'test strt', '45212', 'test@yahoo.com', 9232),
(23, 23, 'Sanjay', '254A,Fake Street, Fake Town', '951970886V', 'sanjay@gmail.com', 758965445),
(24, 23, 'Ramesh', '56C, Bus Stand', '960681665V', 'ramesh030896@gmail.com', 767005330),
(25, 23, 'Ramesh', '56C, Bus Stand', '960681665V', 'ramesh030896@gmail.com', 767005330),
(26, 30, 'Cipher', 'Cipher _rd', '951970886V', 'cipher03.dev@gmail.com', 767005330),
(27, 30, 'Cipher', 'Cipher _rd', '951970886V', 'cipher03.dev@gmail.com', 767005330),
(28, 32, 'Leo', '56C, Bus Stand', '231232345X', 'leo@gmail.com', 767005330),
(29, 33, 'John', 'Otumba Estate, Demodara', '943562654V', 'johnwick@gmail.com', 767005330),
(30, 33, 'John', 'Otumba Estate, Demodara', '943562654V', 'johnwick@gmail.com', 767005330),
(31, 33, 'John', 'Otumba Estate, Demodara', '943562654V', 'johnwick@gmail.com', 767005330),
(32, 33, 'John', 'Otumba Estate, Demodara', '943562654V', 'johnwick@gmail.com', 767005330),
(34, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(35, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(36, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(37, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(38, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(39, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(40, 23, 'Ramesh', '56C, Bus Stand', '943562654V', 'ramesh030896@gmail.com', 767005330),
(42, 22, 'Sandamal', 'Otumba Estate, Demodara', '943562654V', 'sanjay@gmail.com', 767005330),
(44, 24, 'Chethana', 'M.K Wijayarathna, Thotagamuwa, Hikkaduwa', '943562654V', 'chethana.rathnayake@my.sliit.lk', 767005330),
(45, 23, 'Surath', '56C, Bus Stand', '8845469565V', 'ramesh030896@gmail.com', 767005330),
(46, 23, 'Surath', '56C, Bus Stand', '8845469565V', 'ramesh030896@gmail.com', 767005330),
(47, 23, 'Surath', '56C, Bus Stand', '8845469565V', 'ramesh030896@gmail.com', 767005330),
(48, 23, 'Surath', '56C, Bus Stand', '8845469565V', 'ramesh030896@gmail.com', 767005330),
(49, 23, 'Surath', '56C, Bus Stand', '8845469565V', 'ramesh030896@gmail.com', 767005330);

-- --------------------------------------------------------

--
-- Table structure for table `vacancies`
--

CREATE TABLE `vacancies` (
  `v_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `job` varchar(255) NOT NULL,
  `education` varchar(255) NOT NULL,
  `experience` varchar(255) NOT NULL,
  `ex_year` varchar(255) NOT NULL,
  `skills` varchar(255) NOT NULL,
  `other_skills` varchar(255) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vacancies`
--

INSERT INTO `vacancies` (`v_id`, `company_id`, `job`, `education`, `experience`, `ex_year`, `skills`, `other_skills`, `status`) VALUES
(21, 1, 'Senior QA Engineer', 'B.Sc. in Computer Science related discipline or equivalent professinal qualification ', '', '3+', 'Java,Functional,UI,Web services,Performance testing,Test cases,Selenium,OOP,Problem solving skills,JMeter,JIRA,Scrum process,Knowledge in Test management tools', 'Good oral and written communication skills,Outstanding player with a self-driven and self-motivated attitude,Ability to work within deadlines individually and as a team,Ability to carry out research and learn new technologies quickly, ability to understan', 0),
(20, 1, 'Senior Software Engineer', 'BSc in Computer Science,Information Technology or equivalent professional qualification', '4+', '3+', 'JavaScript,HTML,CSS,OOP,MVC,MVVM,JQuery,Angular,React,Riot,Typescript,Webpack,RESTful API,Sass,LESS', 'Ability to work within deadlines,Problem solving and communication skills,Ability to learn new technologies quickly,Ability to understand the importance of customer service,Innovative and forward thinking', 0),
(19, 1, 'Senior Software Engineer', 'BSc in Computer Science,Information Technology or equivalent professional qualification', '', '3+', 'JEE,HTML,CSS,SOAP,REST,Spring,Spring Boot/Cloud,Hibernate,Java script,AngularJS,React,Linux,Database clustering,Multi-tenant application design,Load balancing,Designing time critical application and high transactional application,Jenkins,Elasticsearch,Art', 'Multitask in demanding environment,Openness,Learn New Technologies,Good Written,Verbal Communication', 0),
(18, 1, 'Software Quality Assurance Engineer', 'BSc in Computer Science or related discipline or equivalent professional qualification', '', '1+', 'Java,Knowledge on Software Quality Assurance and testing,Knowledge in automation and performance,Knowledge in software development', 'Multitask in demanding environment,Openness,Learn New Technologies,Good Written,Verbal Communication', 0),
(17, 1, 'Associate Software Quality Engineer', 'BSc in Computer Science,Information Technology or equivalent professional qualification', '', '1+', 'Java,Knowledge in Quality Assurance and testing,Test management(Manual),automation and performance tools,Selenium,Knowledge on Agile/Scrum', 'Troubleshooting, Communication, Research and Develop', 0),
(16, 1, 'Senior Software Quality Assurance Engineer', 'BSc in Computer Science or related discipline or IT', '', '2+', 'Java,OOP,C++,Selinium,Test cases,HTML,CSS', 'Communication,Team Spirit,Researcher', 0),
(15, 1, 'Senior Software Engineer', 'Bachelor\'s degree in Computing or Information Technology', '', '3+', 'Java,NodeJs,ReactJS,AngularJs,Jquery,Javascript,HTML5,CSS,Oracle 11g,PL SQL', 'Communication,Team Spirit,Researcher', 0),
(14, 1, 'Senior Software Engineer', 'Bachelor\'s degree in Computer Science/MIS or equivalent experience', '', '3+', 'J2EE/JEE,Spring framework,Oracle,MSSQL,NoSQL,Unit testing,Engineering best practices,Build,Package and deployment tools', 'Experience in one or more web and application servers', 0),
(13, 1, 'Senior Software Engineer', 'Bachelor\'s degree or higher qualification in Computer Science/Engineering', '', '3+', 'Laravel,AWS,Bootstrap,React JS,Rest API,Unit testing framework', 'API design,development and documentation,Algorithm design and implementation,Technical writing', 0),
(12, 1, 'Senior Software Engineer', 'Bachelor\'s degree or higher qualification in Computer Science/ Engineering', '', '3+', 'Java,C++,SQL,Cake PHP,Laravel,Ruby on Rails,RESTful,SOAP,Experience on cross browser compatibility,W3C standards,Database concepts,Relational databases,Experience on Unix/Linux', 'Multitask in demanding environment,Openness,Learn New Technologies,Good Written,Verbal Communication', 0),
(11, 1, 'Senior Software Engineer', 'Bachelor\'s Degree in Computer Science/Information Technology/Software Engineering', '', '3+', 'Java design patterns,Architecture patterns,JSP/servelets,Spring,Spring boot,Hibernate,SOA,Designing systems,Database and deployment architecture,React,React Native,Angular,Oracle,MYSQL,Linux and Windows operating systems,Experience in code reviewing,team ', 'Experience in code reviewing,team grooming', 0),
(10, 1, 'Senior Software Engineer', 'Degree related to Information Technology/Computer Science or Software Engineering', '', '3+', 'Java,.Net,AJAX,OOP,C++', 'Knowledge in salesforce RCM,Must possess excellent spoken,written and presentation skills in English', 0),
(9, 1, 'Software Engineer', 'Degree or similar educational qualification in IT or computer science', '', '1+', 'C#,Ajax,WebAPI,.Net 4.6/4.7,.Net core,LINQ,Entity framework,SQL server', 'API design,development and documentation,Algorithm design and implementation,Technical writing', 0),
(8, 1, 'Senior Software Engineer', 'Bachelor\'s degree or higher qualification in Computer Science/Engineering', '', '4+', 'Docker,Kubernates,Istio,AWS,Apache Kafka,Elastic,React,BDD,Test Automation,JAVA/J2EE,Spring,Hibernate/JPA,EJB,JMS,Node JS,Oracle', 'Multitask in demanding environment,Openness,Learn New Technologies,Good Written,Verbal Communication', 0),
(7, 1, 'Senior Software Quality Assurance Engineer', 'Bachelor\'s degree or higher qualification in Computer Science/ Engineering', '', '4+', 'Java,C++,Selenium,HTML,CSS,Test cases', 'Troubleshooting,Communication,Research and Develop', 0),
(6, 1, 'Senior Software Engineer', 'Bachelor\'s Degree in Information Technology/ Software Engineering or any other related degree', '', '5+', 'C#,Microservices,SAAS,PAAS,Clean and tested commits to GIT,JAva,C++,C,Android,React,PHP', 'API design,development and documentation,Algorithm design and implementation,Technical writing', 0),
(5, 1, 'Software Eng', 'Gradute in Information Technology', '', '2', 'React,Java,JavaEE', 'Communication,Team Spirit,Researcher', 0),
(4, 1, 'Intern', 'Under Graduate in Software Engineering/ Computer Science', '', '', 'Java, Php, MySQL, MongoDB, Angular, NodeJS', 'Laravel, SOund Analytics, Problem Solving, Verbal Communication, Team Player', 0),
(3, 1, 'Software Eng', 'Bachelor\'s Degree in Information Technology/ Software Engineering or any other related degree', 'Angular JS, Javascript, HTML 5, CSS 3, Bootstrap, UML, Agile Methodology, Database Design, MySQL/MongoDB?PostreSQL', '1+', 'JAva EE, Spring, Spring boot, Hibernate, Design patterns, SOA, Restful Services, Version Controlling Systems', 'Multitask in demanding environment, Openness, Learn New Technologies, Good Written, Verbal Communication', 0),
(2, 1, 'associate software eng', 'Degree/Diploma', 'DevExpress & Telerik', '', '.NET, C#, ASP.net, Web forms, MVC, Web Services, Entity Framework, ADO.net, SQL, HTML5, Bootstrap 3, CSS3, Javascript', 'Troubleshooting, Communication, Research and Develop', 0);

-- --------------------------------------------------------

--
-- Table structure for table `vacancy_matching`
--

CREATE TABLE `vacancy_matching` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `vacid` int(11) NOT NULL,
  `nbmatching` text,
  `dtmatching` text
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cv_meta`
--
ALTER TABLE `cv_meta`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cv_q`
--
ALTER TABLE `cv_q`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cv_q_meta`
--
ALTER TABLE `cv_q_meta`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cv_q_predict`
--
ALTER TABLE `cv_q_predict`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dt_prediction`
--
ALTER TABLE `dt_prediction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ivm_anonimyzation`
--
ALTER TABLE `ivm_anonimyzation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nb_prediction`
--
ALTER TABLE `nb_prediction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vacancies`
--
ALTER TABLE `vacancies`
  ADD PRIMARY KEY (`v_id`);

--
-- Indexes for table `vacancy_matching`
--
ALTER TABLE `vacancy_matching`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `cv_meta`
--
ALTER TABLE `cv_meta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cv_q`
--
ALTER TABLE `cv_q`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `cv_q_meta`
--
ALTER TABLE `cv_q_meta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `cv_q_predict`
--
ALTER TABLE `cv_q_predict`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `dt_prediction`
--
ALTER TABLE `dt_prediction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `ivm_anonimyzation`
--
ALTER TABLE `ivm_anonimyzation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `nb_prediction`
--
ALTER TABLE `nb_prediction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `vacancies`
--
ALTER TABLE `vacancies`
  MODIFY `v_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `vacancy_matching`
--
ALTER TABLE `vacancy_matching`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1961;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
