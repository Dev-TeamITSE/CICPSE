<?php
// log_login.php: registra intentos de login
$user = $_GET['user'] ?? 'desconocido';
$pass = $_GET['pass'] ?? '';
$date = date('Y-m-d H:i:s');
$log = "[{$date}] Intento de login: usuario={$user}, pass={$pass}\n";
file_put_contents("login_logs.txt", $log, FILE_APPEND);
echo "Login registrado.";
?>
