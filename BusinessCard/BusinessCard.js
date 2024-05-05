const mainImage = document.getElementById('image');
const Instagram = document.getElementById('instagram');
const Website = document.getElementById('website')
const imageWidth = mainImage.clientWidth;
const imageHeight = mainImage.clientHeight;
const containerWidth = mainImage.parentNode.clientWidth;
const containerHeight = mainImage.parentNode.clientHeight
Instagram.style.top = `${(imageHeight / 2)+115}px`;
Instagram.style.marginTop = `-${Instagram.clientHeight / 2}px`;
Instagram.style.height = `${Instagram.clientHeight}px`;
Instagram.style.fontSize = `${containerWidth * 0.02}px`;

Website.style.top = `${(imageHeight / 2)+115}px`;
Website.style.marginTop = `-${Website.clientHeight / 2}px`;
Website.style.height = `${Website.clientHeight}px`;
Website.style.fontSize = `${containerWidth * 0.02}px`;