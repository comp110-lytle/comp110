function hideshow() {
  // get doc id
  var doc = document.getElementById("overview-links");
  var contentDoc = document.getElementById("content");
  var boxDoc = document.getElementById("box");
  var arrow = document.getElementById("button-img");
  var button = document.getElementById("overview-button");

  // if there currently isn't anything displayed, show block
  // otherwise hide current displays
  if (doc.style.display === "none") {
    doc.style.display = "block";
    contentDoc.className = "content box col-xl-9 col-lg-9 order-2 order-lg-1 pt-3";
    boxDoc.className = "toc col-xl-3 col-lg-3 order-1 order-lg-2";
    arrow.src = "/static/components/Itinerary/arrow-up.svg";
    button.childNodes[0].nodeValue = "Overview";
  } else {
    doc.style.display = "none";
    contentDoc.className = "content box col-xl-9 col-lg-9 order-2 order-lg-1 pt-3";
    boxDoc.className = "toc col-xl-3 col-lg-3 order-1 order-lg-2";
    arrow.style = "height:15px; padding-left: 4px;";
    arrow.src = "/static/components/Itinerary/arrow-down.svg";
    button.childNodes[0].nodeValue = "Overview";
  }
}
