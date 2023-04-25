<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'example_db' );

/** Database username */
define( 'DB_USER', 'user' );

/** Database password */
define( 'DB_PASSWORD', 'password' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '5YAT&?SzVT2cg ifS^m)vNnp_TvU):yck|;D5]fLUDci&&BvL`PU&RT_=l>m@vnI' );
define( 'SECURE_AUTH_KEY',  'slgjE8s;(J1adFQ{%|9<4NeDsYWJmnhENITg{-Dh%E<i!()DJQ|W=U>7Z$Hd}Ba0' );
define( 'LOGGED_IN_KEY',    'o6uq^Hkts<#Rdw!]AA2Tj!J0{1cZ<l#$O2Su;iMVpXM#nUiaosB#7Ce96)<_6&Rp' );
define( 'NONCE_KEY',        'PA%:4iF_p}PQ(2gB!bxh8`QZrLDWdXK1g% AkO#0|}I$`BkavP}yqSG}4OHS4b<{' );
define( 'AUTH_SALT',        '>*pw>=KFw.GB_8n/$&d]Ps-)1v}1Za+/ZtPQiZ;B}K|-wcF2reD3Dh[8;Vu4NQH2' );
define( 'SECURE_AUTH_SALT', 'JZ.[$*Z{V|G4k2u7T>kSS(4K^H}9%t(8ra[-oa7Au!QnDO/ntE+Bw*b;R.icMeXX' );
define( 'LOGGED_IN_SALT',   'KJn=t6(.,`5!TS^-5H[p~t0>fRH2J)/n)Dy.M`6u3](1b<>k|gAJEz:fn(Np8)(r' );
define( 'NONCE_SALT',       '}2P5</.,$Z>l_qMsrw3Pihok}V1AcVdDD`@2c- p6w=I)`4B+1+&bt.a$ue&&a/J' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
