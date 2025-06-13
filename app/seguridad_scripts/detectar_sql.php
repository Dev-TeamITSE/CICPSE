<?php
// detectar_sql.php: detecta inyecciones SQL en $_GET
function contieneSQL($input) {
  $patrones = ['/\bSELECT\b/i', '/\bUNION\b/i', '/\bINSERT\b/i', '/\bOR\b/i', '/--/'];
  foreach ($patrones as $patron) {
    if (preg_match($patron, $input)) return true;
  }
  return false;
}

$riesgo = false;
foreach ($_GET as $param => $valor) {
  if (contieneSQL($valor)) {
    $riesgo = true;
    echo "⚠️ Posible SQL Injection detectada en '$param': $valor<br>";
  }
}

if (!$riesgo) echo "✅ Parámetros seguros.";
?>
