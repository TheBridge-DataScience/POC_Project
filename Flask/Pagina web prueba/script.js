const dialog = document.querySelector('.dialog');
const doctorBubble = document.querySelector('.bubble.doctor');
const nurseBubble = document.querySelector('.bubble.nurse');

doctorBubble.style.display = 'block';

function showNurseBubble() {
  nurseBubble.style.display = 'block';
}

setTimeout(showNurseBubble, 2000);


function predictResult() {
	var image = document.getElementById("image").files[0];
	var result = processImage(image);
	var conversation = document.getElementById("conversation");
	var p = document.createElement("p");
	p.textContent = "Result: " + result;
	conversation.appendChild(p);
}

function processImage(image) {
	// Process the image and return the result
	// ...
	return "positive";
}