localStorage.setItem("poppedOut", 'true');


if (localStorage.getItem('poppedOut') === 'true') {
    document.getElementById("popup").classList.add('hidden')
} else {
    document.getElementById("content-wrapper").classList.add('blur');
    document.body.classList.remove('absolute-page');
}