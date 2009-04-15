<?php
# FileName="Connection_php_mysql.htm"
# Type="MYSQL"
# HTTP="true"
$hostname_wtfimb = "localhost";
$database_wtfimb = "wtfimb";
$username_wtfimb = "root";
$password_wtfimb = "viewsonic";
$wtfimb = mysql_pconnect($hostname_wtfimb, $username_wtfimb, $password_wtfimb) or trigger_error(mysql_error(),E_USER_ERROR); 
?>