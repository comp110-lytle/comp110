if (localStorage.getItem('loggedIn') === 'true') {
    document.getElementById("log-in").classList.add('hidden')
} else {
    document.getElementById("content-wrapper").classList.add('blur');
    document.body.classList.remove('absolute-page');
}