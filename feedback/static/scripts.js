// Get the file input element and buttons
const fileInput = document.getElementById('fileInput');
const txtButton = document.getElementById('txtButton');

txtButton.addEventListener('click', function () {
  fileInput.accept = '.txt'; // Set the file input to accept only TXT
  fileInput.click(); // Trigger the file input dialog
});
