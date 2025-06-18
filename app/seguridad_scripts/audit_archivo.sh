#!/bin/bash
# Script para activar auditoría de acceso a un archivo usando auditctl

if [ -z "$1" ]; then
  echo "Uso: $0 /ruta/al/archivo"
  exit 1
fi

ARCHIVO="$1"
sudo auditctl -w "$ARCHIVO" -p rwxa -k auditoria_archivo
echo "Auditoría activada para: $ARCHIVO"
