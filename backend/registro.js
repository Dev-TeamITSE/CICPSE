const API_URL = "http://localhost:3001";

// Obtener listado de usuarios
async function obtenerListado() {
    try {
        const response = await fetch(`${API_URL}/listado`);
        if (!response.ok) throw new Error("Error al obtener datos");
        
        const datos = await response.json();
        mostrarLista(datos);
    } catch (error) {
        console.error("Error al obtener listado:", error);
    }
}

// Mostrar listado en la tabla HTML
function mostrarLista(datos) {
    const tbody = document.getElementById("listaUsuarios");
    if (!tbody) return;

    tbody.innerHTML = ""; // Limpia la tabla antes de cargar nuevos datos

    datos.forEach((usuario) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td class="border px-4 py-2">${usuario.id}</td>
            <td class="border px-4 py-2">${usuario.nombreCompleto}</td>
            <td class="border px-4 py-2">${usuario.email}</td>
            <td class="border px-4 py-2">${usuario.area}</td>
            <td class="border px-4 py-2">
                <button class="bg-green-500 text-white px-2 py-1 rounded" onclick="confirmarUsuario(${usuario.id})">Confirmar</button>
                <button class="bg-red-500 text-white px-2 py-1 rounded" onclick="eliminarUsuario(${usuario.id})">Eliminar</button>
            </td>
        `;
        tbody.appendChild(fila);
    });
}

// Mostrar alerta al confirmar usuario
function confirmarUsuario(id) {
    Swal.fire({
        title: "Usuario confirmado",
        text: `El usuario con ID ${id} ha sido confirmado exitosamente.`,
        icon: "success",
        confirmButtonText: "OK"
    });
}

// Agregar nuevo usuario
async function agregarUsuario() {
    const nombreCompleto = document.getElementById("nombreCompletoBox")?.value;
    const email = document.getElementById("emailBox")?.value;
    const password = document.getElementById("passBox")?.value;
    const area = document.getElementById("areaBox")?.value;

    if (!nombreCompleto || !email || !password || !area) {
        Swal.fire("Error", "Completa todos los campos.", "warning");
        return;
    }

    const nuevoUsuario = { nombreCompleto, email, password, area };

    try {
        const response = await fetch(`${API_URL}/create`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(nuevoUsuario)
        });

        if (response.ok) {
            Swal.fire("Éxito", "Usuario agregado exitosamente", "success");
            obtenerListado();
            limpiarCampos();
        }
    } catch (error) {
        console.error("Error al agregar usuario:", error);
    }
}

// Confirmación antes de eliminar usuario
async function eliminarUsuario(id) {
    const confirmacion = await Swal.fire({
        title: "¿Eliminar usuario?",
        text: "Esta acción no se puede deshacer.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar"
    });

    if (confirmacion.isConfirmed) {
        try {
            const response = await fetch(`${API_URL}/eliminar/${id}`, { method: "DELETE" });

            if (response.ok) {
                Swal.fire("Eliminado", "Usuario eliminado correctamente.", "success");
                obtenerListado();
            }
        } catch (error) {
            console.error("Error al eliminar usuario:", error);
        }
    }
}

// Limpiar campos del formulario
function limpiarCampos() {
    document.getElementById("nombreCompletoBox").value = "";
    document.getElementById("emailBox").value = "";
    document.getElementById("passBox").value = "";
    document.getElementById("areaBox").value = "";
}

// Ejecutar al cargar la página
document.addEventListener("DOMContentLoaded", obtenerListado);
