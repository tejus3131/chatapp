const chatMessages = document.getElementById('chat-messages');
const inputMessage = document.getElementById('input-message');
const btnSend = document.getElementById('btn-send');

function fetchMessages() {
    fetch('https://chatapp3131-tejus3131.vercel.app/messages')
        .then(response => response.json())
        .then(messages => {
            chatMessages.innerHTML = '';
            messages.forEach(message => {
                const messageElement = document.createElement('div');
                messageElement.innerHTML = `=> ${message.content}`;
                chatMessages.appendChild(messageElement);
            });
            scrollToBottom();
        })
        .catch(error => console.error(error));
}

function sendMessage() {
    const content = inputMessage.value.trim();
    const sender = 'User';

    if (content === '') {
        return;
    }

    const message = { content, sender };

    fetch('https://chatapp3131-tejus3131.vercel.app/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(message)
    })
        .then(response => response.json())
        .then(newMessage => {
            const messageElement = document.createElement('div');
            messageElement.innerHTML = `=> ${newMessage.content}`;
            chatMessages.appendChild(messageElement);
            inputMessage.value = '';
            scrollToBottom();
        })
        .catch(error => console.error(error));
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Fetch messages on page load
fetchMessages();

// Set interval to fetch messages periodically
setInterval(fetchMessages, 2000);

// Event listeners
btnSend.addEventListener('click', sendMessage);
inputMessage.addEventListener('keypress', event => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
