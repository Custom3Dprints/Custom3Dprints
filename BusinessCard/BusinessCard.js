const mainImage = document.getElementById('image');
const Instagram = document.getElementById('instagram');
const Website = document.getElementById('website');

function adjustLinksPosition() {
    const imageWidth = mainImage.clientWidth;
    const imageHeight = mainImage.clientHeight;
    const containerWidth = mainImage.parentNode.clientWidth;
    const containerHeight = mainImage.parentNode.clientHeight;
    // Calculate the top position based on image and container height
    const topPosition = ((containerHeight - Instagram.offsetHeight) / 2)+20;
    // Apply the top position to both links
    Instagram.style.top = `${topPosition}px`;
    Website.style.top = `${topPosition}px`;
    // Adjust font size based on container width
    const fontSize = containerWidth/18;
    Instagram.style.fontSize = `${fontSize}px`;
    Website.style.fontSize = `${fontSize}px`;
}

// Call the function initially
adjustLinksPosition();

// Add event listener for window resize
window.addEventListener('resize', adjustLinksPosition);