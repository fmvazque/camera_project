function updateImage() {
  // Appending datetime as a query parameter to avoid browser caching
  document.getElementById("img_current_picture").src = '/pics/current/current.png?' + new Date().getTime().toString();
}
