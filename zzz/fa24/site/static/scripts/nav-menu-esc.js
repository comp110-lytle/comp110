// Get the hamburger menu button element
function esc_key(){
    var menuButton = document.querySelector('.navbar-toggler');
    // Add an event listener for the keydown event
    document.addEventListener('keydown', function(event) {
    // Check if the pressed key is the "Escape" key
    if (event.key === 'Escape') {
        // Check if the menu is open
        if (menuButton.getAttribute('aria-expanded') === 'true') {
        // Trigger a click on the menu button to close it
        menuButton.click();
        }
    }
    });
}