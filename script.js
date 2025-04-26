// Basic client-side validation
document.querySelector("form").addEventListener("submit", function(e) {
    let message = document.querySelector("textarea[name='message']").value;
    let shift = document.querySelector("input[name='shift']").value;
    if (!message.trim() || shift < 0 || shift > 25) {
        e.preventDefault();
        alert("Please enter a valid message and a shift between 0 and 25.");
    }
});

console.log("Caesar Cipher Web App Loaded");