const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo')

//Mobile Menu
menu.addEventListener('click', function(){
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
});


function Home() {
    window.location.href = "3Dhtml.html";
}
function Pictures() {
    window.location.href = "3DPictures.html";
}
function Links() {
    window.location.href = "3DLinks.html";
}
function Specials() {
    window.location.href = "Halloween.html";
}
function About() {
    window.location.href = "3DAbout.html";
}
function Order() {
    window.location.href = "3DOrder.html";
}


function Submitbutton(){
    var fullName = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phoneNumber = document.getElementById("phoneNumber").value;
    var printname = document.getElementById("printname").value;
    var printlink = document.getElementById("printlink").value;
    var description = document.getElementById("description").value;
    var printSize = document.getElementById("printSize").value;
    var printColors = document.getElementById("printColors").value;
    //firstname = (fullName.split(" ")[0]);
    //lastname = (fullName.split(" ")[1]);

    console.log("Full Name:", fullName);
    console.log("Email:", email);
    console.log("Phone Number:", phoneNumber);
    console.log("Print Name:", printname);
    console.log("Print link:", printlink);
    console.log("Description:", description);
    console.log("Print Size:", printSize);
    console.log("Print Colors:", printColors);

    //if every spot needs to be filled out
    if (fullName == "" || email == "" || phoneNumber == "" || printname == "" || description == "" || printSize == "" || printColors == ""){
        alert("You're missing some information. Please double check the informetion entered before clicking submit again.");
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
            emailjs.init("eAaiCLhfnHUAWEnNa"); //EmailJS public key
            
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
                    //Cwindow.location.href = 'OrderSucesspage.html';
                }, function(error) {
                    console.log('Failed!', error);
                    //window.location.href = 'OrderErrorpage.html';
                });
            });
        })();
    }
}
    
    