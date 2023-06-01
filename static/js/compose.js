// Add event listener for form submission
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    var recipient = document.querySelector('#recipient').value;
    var subject = document.querySelector('#subject').value;
    var message = document.querySelector('#message').innerHTML;

    // Perform further processing or AJAX request to send the email
    console.log('Recipient:', recipient);
    console.log('Subject:', subject);
    console.log('Message:', message);

    // Reset form fields
    document.querySelector('form').reset();
    document.querySelector('#message').innerHTML = '';
});

// Function to format text
function formatText(command) {
    document.execCommand(command, false, null);
}

// Function to handle file selection
function handleFileSelect(event) {
    const files = event.target.files;
    const fileList = document.getElementById('file-list');
    fileList.innerHTML = '';

    // Iterate over selected files
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const listItem = document.createElement('span');
        listItem.textContent = file.name;

        if (i !== files.length - 1) {
            listItem.textContent += ',';
        }

        fileList.appendChild(listItem);
    }
}

// Event listener for file input change
const fileInput = document.getElementById('attachments');
fileInput.addEventListener('change', handleFileSelect);

