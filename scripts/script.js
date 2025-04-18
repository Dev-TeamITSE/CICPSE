function login() {
    const email = document.getElementById('emailBox').value.trim();
    const password = document.getElementById('passBox').value.trim();

    const userEmail = "admin@patrimonio.com";
    const userPassword = "devteam24";

    if (email === "" || password === "") {
        Swal.fire({
            icon: "error",
            title: "Ups",
            text: "Debes completar los campos."
        });
        return;
    }

    if (email !== userEmail || password !== userPassword) {
        Swal.fire({
            icon: "error",
            title: "Ups",
            text: "Correo o contraseña incorrecta."
        });
        return;
    }

    // Mostrar alerta con opciones
    Swal.fire({
        title: "Bienvenido al CICPSE",
        text: "¿Desea registrar usuario o continuar?",
        imageUrl: "img/favi_patrimonio.png",
        imageWidth: 100,
        imageHeight: 100,
        showCancelButton: true,
        confirmButtonText: "Continuar",
        cancelButtonText: "Registrar"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "welcome.html"; // Redirigir a la página de bienvenida
        } else {
            window.location.href = "registro.html"; // Redirigir a la página de registro
        }
    });
}

function user() {
    const email = document.getElementById('emailBox').value.trim();

    if (email === "") {
        Swal.fire({
            icon: "error",
            title: "Ups!",
            text: "Debes ingresar un correo electrónico."
        });
        return;
    }

    Swal.fire({
        title: `Se ha enviado una confirmación a ${email}.`,
        imageUrl: "img/favi_patrimonio.png",
        imageWidth: 100,
        imageHeight: 100,
        confirmButtonText: "Aceptar"
    }).then(() => {
        window.location.href = "index.html"; // Redirigir después de aceptar
    });
}

