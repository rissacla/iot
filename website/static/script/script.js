// Resize user input box in chat
const textarea = document.getElementById("user-prompt");
const chatContainer = document.querySelector(".chat-input");
const imageContainer = document.getElementById("image-container");

textarea.addEventListener("input", function () {
    // Calculate the height of the textarea based on its content
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";

    // Check if the height exceeds the maximum height
    if (textarea.scrollHeight > 0.8 * window.innerHeight) {
        textarea.style.overflowY = "scroll";
        chatContainer.style.height = "20vh";
    } else {
        textarea.style.overflowY = "hidden";
        chatContainer.style.height = "auto";
    }
});

// Show uploaded image
const fileInput = document.getElementById("file-input");
fileInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = document.createElement("img");
            img.src = e.target.result;
            img.style.maxHeight = "80px";
            img.style.paddingLeft = "8px";
            img.style.paddingBottom = "8px";
            img.style.borderRadius = "22px";
            imageContainer.innerHTML = "";
            imageContainer.appendChild(img);
            adjustChatInputHeight();
        };
        reader.readAsDataURL(file);
    }
});

function adjustChatInputHeight() {
    const totalHeight = textarea.scrollHeight + imageContainer.scrollHeight;
    if (totalHeight > 0.8 * window.innerHeight) {
        chatContainer.style.height = "20vh";
    } else {
        chatContainer.style.height = "auto";
    }
}

// Scroll to the bottom of the chat window
document.addEventListener("DOMContentLoaded", function () {
    var chatWindow = document.querySelector(".chat-card");
    chatWindow.scrollTop = chatWindow.scrollHeight;
});
