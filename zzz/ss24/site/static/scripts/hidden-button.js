function show(){
    document.addEventListener("keydown", function(event) {
        if (event.keyCode === 9) { // Check if tab key was pressed
          var button = document.getElementById("hiddenButton");
          button.style.display = "block"; // Reveal the hidden button
        }
      });

}