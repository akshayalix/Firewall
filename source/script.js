 // Call the Python function using Eel

// For outbound Rule
function outbound_rule() {
    eel.outbound_rule();
}

// For Inbound Rule
function inbound_rule() {
    eel.inbound_rule();
}

// To Remove Rule
function remove_rule() {
    eel.remove_rule();
}

// To open Github Page
function open_github(){
    eel.open_github()
}

eel.expose(updateConsole);

function updateConsole(text) {
    const consoleDiv = document.getElementById('console');
    // consoleDiv.innerText += text;
    consoleDiv.innerText = text; // Clear the existing content and replace with new text
    consoleDiv.scrollTop = consoleDiv.scrollHeight; // Automatically scroll to the bottom
}
