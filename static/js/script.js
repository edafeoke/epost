$(document).ready(function() {
    // Handle email form submission
    $('#compose-form').submit(function(e) {
        e.preventDefault();

        $.ajax({
            url: '/compose',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#compose-form')[0].reset();
                $('#compose-message').text(response.message);
            }
        });
    });
});
