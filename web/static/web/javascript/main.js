var slideIndex = 0;
showSlides();
function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  $(slides[slideIndex-1]).css('z-index','-1');
  $(slides[slideIndex-1]).fadeIn(1000);
  setTimeout(showSlides, 5000);
}
