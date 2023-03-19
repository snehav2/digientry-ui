function checkOtherDestination(selectObject) {
    // If "Other" option is selected for Destination then show input field to enter other destination
    let value = selectObject.value;
    if (value === "Others") {
      qrContentInput = document.getElementById("other_destination");
      qrContentInput.style.display = "block";
    }
}
  
  // Generate QR Code
  let qrContentInput = document.getElementById("destination");
  if (qrContentInput.value === "Others") {
    qrContentInput = document.getElementById("other_destination");
  }
  
  let qrGenerationForm = document.getElementById("qr-generation-form");
  let qrCode;
  
  function generateQrCode(qrContent) {
    return new QRCode("qr-code", {
      text: qrContent,
      width: 256,
      height: 256,
      colorDark: "#000000",
      colorLight: "#ffffff",
      correctLevel: QRCode.CorrectLevel.H,
    });
  }
  
  // Event listener for form submit event
  qrGenerationForm.addEventListener("submit", function (event) {
    // Prevent form submission
    event.preventDefault();
    let qrContent = qrContentInput.value;
    if (qrCode == null) {
      // Generate code initially
      qrCode = generateQrCode(qrContent);
    } else {
      // If code already generated then make
      // again using same object
      qrCode.makeCode(qrContent);
    }
  });