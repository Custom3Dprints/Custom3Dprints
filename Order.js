function Submitbutton(){
    var fullName = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phoneNumber = document.getElementById("phoneNumber").value;
    var printname = document.getElementById("printname").value;
    var printlink = document.getElementById("printlink").value;
    var description = document.getElementById("description").value;
    var printSize = document.getElementById("printSize").value;
    var printColors = document.getElementById("printColors").value;
    
    console.log("Full Name:", fullName);
    console.log("Email:", email);
    console.log("Phone Number:", phoneNumber);
    console.log("Print Name:", printname);
    console.log("Print link:", printlink);
    console.log("Description:", description);
    console.log("Print Size:", printSize);
    console.log("Print Colors:", printColors);

    //if every spot needs to be filled out
    if (fullName == "" || email == "" || phoneNumber == "" || printname == "" || printlink == "" || description == "" || printSize == "" || printColors == ""){
        alert("You're missing some information. Please double check the informetion imputted before clicking submit again.");
        return false;
    }
    else{
        return true;
    }
}

//Emialjs
function main() {
    let noBlanks = Submitbutton();
    
    if (noBlanks == true){
        //Email me
        (function(){
            emailjs.init("eAaiCLhfnHUAWEnNa"); // Replace with your EmailJS user ID
    
            document.getElementById('contact-form').addEventListener('submit', function(event) {
                event.preventDefault();
                // Collect form data
                var formData = {
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    phoneNumber: document.getElementById('phoneNumber').value,
                    printname: document.getElementById('printname').value,
                    printlink: document.getElementById('printlink').value,
                    description: document.getElementById('description').value,
                    printSize: document.getElementById('printSize').value,
                    printColors: document.getElementById('printColors').value
                };
            
                // Send the form data
                emailjs.send("3dserviceemail", "template_biaflkd", formData)
                    .then(function(response) {
                        console.log('Success!', response.status, response.text);
                        window.location.href = 'OrderSucesspage.html';
                    }, function(error) {
                        console.log('Failed!', error);
                        //window.location.href = 'OrderErrorpage.html';
                        //wait 4 seconds setTimer(function, 4000){}
                        //window.location.href = 'Order.html';
                    });
            });
        })();

        //Email customer
        (function(){
            emailjs.init("eAaiCLhfnHUAWEnNa"); // Replace with your EmailJS user ID
    
            document.getElementById('contact-form').addEventListener('submit', function(event) {
                event.preventDefault();
                // Collect form data
                var formData = {
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    phoneNumber: document.getElementById('phoneNumber').value,
                    printname: document.getElementById('printname').value,
                    printlink: document.getElementById('printlink').value,
                    description: document.getElementById('description').value,
                    printSize: document.getElementById('printSize').value,
                    printColors: document.getElementById('printColors').value
                };
            
                // Send the form data
                emailjs.send("3dserviceemail", "template_1l2bole", formData)
                    .then(function(response) {
                        console.log('Success!', response.status, response.text);
                        //window.location.href = 'OrderSucesspage.html';
                    }, function(error) {
                        console.log('Failed!', error);
                        //window.location.href = 'OrderErrorpage.html';
                    });
            });
        })();
    }
}

