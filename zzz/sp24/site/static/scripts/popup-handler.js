function popFunction(e) {
    if ((e && e.keyCode == 13) || e == 0) {
        localStorage.setItem('poppedOut', 'true');
        window.open("https://bit.ly/Hack11021f", '_blank')
        window.location.reload();
    }
}