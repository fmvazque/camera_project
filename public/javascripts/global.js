function refreshCurrentImage() {
  document.getElementById("img_current_picture").src = '/pics/current/current.png?' + new Date().getTime().toString();

  var lastCapturedDiv = document.getElementById("last_captured");
  if (lastCapturedDiv) {
    
    // remove all existing child elements of this DIV
    while (lastCapturedDiv.hasChildNodes()) {
      lastCapturedDiv.removeChild(lastCapturedDiv.lastChild);  
    }

    // adds images for the 10 most recent images
    if (g_lastImages) {
      //TODO
    }
  }

}
