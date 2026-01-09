function myFunction(e) {
    if ((e && e.keyCode == 13) || e == 0) {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        if (username === "team110" && password === "cpuhat") {
            localStorage.setItem('loggedIn', 'true');
            window.location.reload();
        }
    }
}