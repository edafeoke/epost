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
