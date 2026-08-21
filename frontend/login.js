const loginForm = document.getElementById("loginForm");
const loginMessage = document.getElementById("loginMessage");

loginForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    loginMessage.textContent = "Logging in...";

    try {

        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {

            loginMessage.textContent = data.message;

            loginMessage.style.color = "#65d99a";

            setTimeout(() => {
                window.location.href = "index.html";
            }, 1000);

        } else {

            loginMessage.textContent = data.detail;
            loginMessage.style.color = "#ff6b7a";
        }

    } catch (error) {

        loginMessage.textContent =
            "Cannot connect to backend.";

        loginMessage.style.color = "#ff6b7a";
    }
});