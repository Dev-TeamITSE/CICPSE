require("dotenv").config();
const express = require("express");
const mysql = require("mysql2");
const cors = require("cors");
const bcrypt = require("bcrypt");

const app = express();
app.use(express.json());
app.use(cors());

// Configuración de conexión segura a MySQL
const db = mysql.createConnection({
    host: process.env.DB_HOST || "localhost",
    user: process.env.DB_USER || "root",
    password: process.env.DB_PASS || "root",
    database: process.env.DB_NAME || "cicpseRegistro",
});

db.connect((err) => {
    if (err) {
        console.error("❌ Error conectando a la BD:", err);
        process.exit(1); // Detiene el servidor si no hay conexión
    }
    console.log("✅ Conectado a la base de datos.");
});

// 🔹 Obtener listado de usuarios
app.get("/listado", (req, res) => {
    db.query("SELECT id, nombreCompleto, email, area FROM usuarios", (err, result) => {
        if (err) {
            console.error("Error obteniendo usuarios:", err);
            return res.status(500).json({ error: "Error al obtener usuarios" });
        }
        res.json(result);
    });
});

// 🔹 Agregar nuevo usuario con contraseña cifrada
app.post("/create", async (req, res) => {
    const { nombreCompleto, email, password, area } = req.body;

    // Validaciones básicas
    if (!nombreCompleto || !email || !password || !area) {
        return res.status(400).json({ error: "Faltan datos en la solicitud" });
    }

    try {
        // Encriptar la contraseña antes de guardarla
        const hashedPassword = await bcrypt.hash(password, 10);

        const sql = "INSERT INTO usuarios (nombreCompleto, email, password, area) VALUES (?, ?, ?, ?)";
        db.query(sql, [nombreCompleto, email, hashedPassword, area], (err, result) => {
            if (err) {
                console.error("Error en la consulta SQL:", err);
                return res.status(500).json({ error: "Error al agregar usuario" });
            }
            res.json({ message: "Usuario agregado exitosamente", id: result.insertId });
        });
    } catch (error) {
        console.error("Error al encriptar contraseña:", error);
        res.status(500).json({ error: "Error interno en el servidor" });
    }
});

// 🔹 Eliminar usuario con confirmación
app.delete("/eliminar/:id", (req, res) => {
    const { id } = req.params;

    db.query("DELETE FROM usuarios WHERE id = ?", [id], (err, result) => {
        if (err) {
            console.error("Error eliminando usuario:", err);
            return res.status(500).json({ error: "Error al eliminar usuario" });
        }

        if (result.affectedRows > 0) {
            res.json({ message: "Usuario eliminado correctamente" });
        } else {
            res.status(404).json({ error: "Usuario no encontrado" });
        }
    });
});

// 🔹 Iniciar servidor en el puerto definido
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
});
