
function main(){
    (function(){
        emailjs.init("eAaiCLhfnHUAWEnNa"); // Replace with your EmailJS user ID
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            event.preventDefault();
            // Collect form data
            var formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };
            // Send the form data
            emailjs.send("3dserviceemail", "template_biaflkd", formData)
                .then(function(response) {
                    console.log('Success!', response.status, response.text);
                    alert('Message sent successfully!');
                }, function(error) {
                    console.log('Failed!', error);
                    alert('Message sending failed!');
                });
        });
    })();
}
