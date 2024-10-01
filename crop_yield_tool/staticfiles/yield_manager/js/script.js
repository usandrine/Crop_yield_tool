// script.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is linked and working!");

    // Example of a basic interactive feature:
    const cropButtons = document.querySelectorAll('.btn');

    cropButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            alert('Navigating to crop details!');
        });
    });
});
