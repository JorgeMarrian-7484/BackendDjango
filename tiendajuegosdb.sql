-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2025 a las 15:36:57
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tiendajuegosdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add desarrolladora_model', 7, 'add_desarrolladora_model'),
(26, 'Can change desarrolladora_model', 7, 'change_desarrolladora_model'),
(27, 'Can delete desarrolladora_model', 7, 'delete_desarrolladora_model'),
(28, 'Can view desarrolladora_model', 7, 'view_desarrolladora_model'),
(29, 'Can add editora_model', 8, 'add_editora_model'),
(30, 'Can change editora_model', 8, 'change_editora_model'),
(31, 'Can delete editora_model', 8, 'delete_editora_model'),
(32, 'Can view editora_model', 8, 'view_editora_model'),
(33, 'Can add esrb_model', 9, 'add_esrb_model'),
(34, 'Can change esrb_model', 9, 'change_esrb_model'),
(35, 'Can delete esrb_model', 9, 'delete_esrb_model'),
(36, 'Can view esrb_model', 9, 'view_esrb_model'),
(37, 'Can add genero_model', 10, 'add_genero_model'),
(38, 'Can change genero_model', 10, 'change_genero_model'),
(39, 'Can delete genero_model', 10, 'delete_genero_model'),
(40, 'Can view genero_model', 10, 'view_genero_model'),
(41, 'Can add plataforma_model', 11, 'add_plataforma_model'),
(42, 'Can change plataforma_model', 11, 'change_plataforma_model'),
(43, 'Can delete plataforma_model', 11, 'delete_plataforma_model'),
(44, 'Can view plataforma_model', 11, 'view_plataforma_model'),
(45, 'Can add resena_model', 12, 'add_resena_model'),
(46, 'Can change resena_model', 12, 'change_resena_model'),
(47, 'Can delete resena_model', 12, 'delete_resena_model'),
(48, 'Can view resena_model', 12, 'view_resena_model'),
(49, 'Can add titulo_model', 13, 'add_titulo_model'),
(50, 'Can change titulo_model', 13, 'change_titulo_model'),
(51, 'Can delete titulo_model', 13, 'delete_titulo_model'),
(52, 'Can view titulo_model', 13, 'view_titulo_model');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$Pt6tLTGb1xOo9lNude7YSu$7YKXhRN6kTuOafTYUB1G6zu2mKya0eu8aMKGQhrdjqU=', '2025-11-21 14:10:06.000000', 1, 'Alan', '', '', '', 1, 1, '2025-11-21 14:09:46.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desarrolladora`
--

CREATE TABLE `desarrolladora` (
  `id` bigint(20) NOT NULL,
  `pais` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  `logo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `desarrolladora`
--

INSERT INTO `desarrolladora` (`id`, `pais`, `nombre`, `descripcion`, `logo`) VALUES
(3, 'Japon', 'Sega', 'sega japon', 'SEGA_logo_B7MRuSW.png'),
(4, 'Japon', 'Nintendo', 'nitendo', 'Nintendo_uQXeqkd.png'),
(5, 'Japon', 'Capcom', 'capcom japon', 'Capcom_logo.png'),
(6, 'Japon', 'Playstation', 'PS japon', 'Playstation.png'),
(7, 'Japon', 'Atlus', 'atlus', 'atlus.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'AlanJorgeApp', 'desarrolladora_model'),
(8, 'AlanJorgeApp', 'editora_model'),
(9, 'AlanJorgeApp', 'esrb_model'),
(10, 'AlanJorgeApp', 'genero_model'),
(11, 'AlanJorgeApp', 'plataforma_model'),
(12, 'AlanJorgeApp', 'resena_model'),
(13, 'AlanJorgeApp', 'titulo_model'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'AlanJorgeApp', '0001_initial', '2025-11-21 14:08:20.000000'),
(2, 'contenttypes', '0001_initial', '2025-11-21 14:08:20.000000'),
(3, 'auth', '0001_initial', '2025-11-21 14:08:22.000000'),
(4, 'admin', '0001_initial', '2025-11-21 14:08:22.000000'),
(5, 'admin', '0002_logentry_remove_auto_add', '2025-11-21 14:08:23.000000'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2025-11-21 14:08:23.000000'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-11-21 14:08:23.000000'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-11-21 14:08:23.000000'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-11-21 14:08:23.000000'),
(10, 'auth', '0004_alter_user_username_opts', '2025-11-21 14:08:23.000000'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-11-21 14:08:23.000000'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-11-21 14:08:23.000000'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-11-21 14:08:23.000000'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-11-21 14:08:23.000000'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-11-21 14:08:23.000000'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-11-21 14:08:23.000000'),
(17, 'auth', '0011_update_proxy_permissions', '2025-11-21 14:08:23.000000'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-11-21 14:08:23.000000'),
(19, 'sessions', '0001_initial', '2025-11-21 14:08:23.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('o80xu46yi1yg0o9wpy9q3q4kd708g04c', '.eJxVjMsOwiAQRf-FtSGAw6Mu3fcbyDADUjU0Ke3K-O_apAvd3nPOfYmI21rj1vMSJxYXocXpd0tIj9x2wHdst1nS3NZlSnJX5EG7HGfOz-vh_h1U7PVbwxm8sgmcyZpSKdoaAgjKKLCF2DkMXrGhELzDARG4hKKALJMZUkLx_gDLdTf5:1vMRpu:yDNIxBvviDmvKNrpDhb-g3GIDeGXnl-m7tbpt9SB2cQ', '2025-12-05 14:10:06.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editora`
--

CREATE TABLE `editora` (
  `id` bigint(20) NOT NULL,
  `pais` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  `logo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `editora`
--

INSERT INTO `editora` (`id`, `pais`, `nombre`, `descripcion`, `logo`) VALUES
(1, 'Japon', 'Sega', 'sega desarrolla', 'SEGA_logo_TIObVvi.png'),
(2, 'Japon', 'Nintendo', 'japon editora', 'Nintendo_Wb8sNDh.png'),
(3, 'Japon', 'Capcom', 'capcom editora', 'Capcom_logo_nuhohDF.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `esrb`
--

CREATE TABLE `esrb` (
  `id` bigint(20) NOT NULL,
  `clasificacion` varchar(50) NOT NULL,
  `logo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `esrb`
--

INSERT INTO `esrb` (`id`, `clasificacion`, `logo`) VALUES
(1, 'E', 'E.png'),
(2, 'M', 'M.png'),
(3, 'T', 'T.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id` bigint(20) NOT NULL,
  `genero` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id`, `genero`) VALUES
(1, 'Accion'),
(2, 'RPG'),
(3, 'Pelea'),
(4, 'MOBA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juego`
--

CREATE TABLE `juego` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(20) NOT NULL,
  `fecha_lanzamiento` date NOT NULL,
  `precio` int(11) NOT NULL,
  `descripcion` longtext NOT NULL,
  `etiquetas` varchar(50) NOT NULL,
  `portada` varchar(100) NOT NULL,
  `desarrolladora_id` bigint(20) NOT NULL,
  `editora_id` bigint(20) NOT NULL,
  `esrb_id` bigint(20) NOT NULL,
  `genero_id` bigint(20) NOT NULL,
  `plataforma_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `juego`
--

INSERT INTO `juego` (`id`, `titulo`, `fecha_lanzamiento`, `precio`, `descripcion`, `etiquetas`, `portada`, `desarrolladora_id`, `editora_id`, `esrb_id`, `genero_id`, `plataforma_id`) VALUES
(1, 'Silkson', '2025-11-21', 50, 'dasdas', 'Mutli', 'Silksong_cover.webp', 3, 2, 1, 1, 1),
(2, 'The legend of zelda', '2025-11-21', 50, 'asdasd', 'Mundo abierto', 'tokt1-cover.jpg', 7, 2, 3, 2, 1),
(3, 'Sonic', '2025-11-21', 600, 'asdagda', 'Mutli', 'sonic_superstars-cover.webp', 3, 1, 1, 1, 1),
(4, 'Witcher 3', '2025-11-19', 70, 'dagsdf', 'Mundo abierto', 'The-Withcer-cover.webp', 6, 1, 2, 3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plataforma`
--

CREATE TABLE `plataforma` (
  `id` bigint(20) NOT NULL,
  `director` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  `logo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `plataforma`
--

INSERT INTO `plataforma` (`id`, `director`, `nombre`, `descripcion`, `logo`) VALUES
(1, 'Gabe newell', 'Playstation', 'siisisi', 'Playstation_i8adnoB.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resena`
--

CREATE TABLE `resena` (
  `id` bigint(20) NOT NULL,
  `fuente` varchar(50) NOT NULL,
  `puntuacion` int(11) NOT NULL,
  `fecha_resena` date NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `resena`
--

INSERT INTO `resena` (`id`, `fuente`, `puntuacion`, `fecha_resena`, `descripcion`) VALUES
(1, 'ign', 2, '2025-11-21', 'mish');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `desarrolladora`
--
ALTER TABLE `desarrolladora`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `editora`
--
ALTER TABLE `editora`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `esrb`
--
ALTER TABLE `esrb`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `juego`
--
ALTER TABLE `juego`
  ADD PRIMARY KEY (`id`),
  ADD KEY `juego_desarrolladora_id_4a0b20a4_fk_desarrolladora_id` (`desarrolladora_id`),
  ADD KEY `juego_editora_id_f825850b_fk_editora_id` (`editora_id`),
  ADD KEY `juego_esrb_id_de40fd3b_fk_esrb_id` (`esrb_id`),
  ADD KEY `juego_genero_id_a6c15546_fk_genero_id` (`genero_id`),
  ADD KEY `juego_plataforma_id_76ff8521_fk_plataforma_id` (`plataforma_id`);

--
-- Indices de la tabla `plataforma`
--
ALTER TABLE `plataforma`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `resena`
--
ALTER TABLE `resena`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `desarrolladora`
--
ALTER TABLE `desarrolladora`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `editora`
--
ALTER TABLE `editora`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `esrb`
--
ALTER TABLE `esrb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `juego`
--
ALTER TABLE `juego`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `plataforma`
--
ALTER TABLE `plataforma`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `resena`
--
ALTER TABLE `resena`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `juego`
--
ALTER TABLE `juego`
  ADD CONSTRAINT `juego_desarrolladora_id_4a0b20a4_fk_desarrolladora_id` FOREIGN KEY (`desarrolladora_id`) REFERENCES `desarrolladora` (`id`),
  ADD CONSTRAINT `juego_editora_id_f825850b_fk_editora_id` FOREIGN KEY (`editora_id`) REFERENCES `editora` (`id`),
  ADD CONSTRAINT `juego_esrb_id_de40fd3b_fk_esrb_id` FOREIGN KEY (`esrb_id`) REFERENCES `esrb` (`id`),
  ADD CONSTRAINT `juego_genero_id_a6c15546_fk_genero_id` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`),
  ADD CONSTRAINT `juego_plataforma_id_76ff8521_fk_plataforma_id` FOREIGN KEY (`plataforma_id`) REFERENCES `plataforma` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
