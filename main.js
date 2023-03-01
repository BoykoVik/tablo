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
  slides[slideIndex-1].style.display = "flex";
  setTimeout(showSlides, 2000);
}

var dayIndex = 0;
showDays();

function showDays() {
  var i;
  var days = document.getElementsByClassName("aday");
  for (i = 0; i < days.length; i++) {
    days[i].style.display = "none";
  }
  dayIndex++;
  if (dayIndex > days.length) {dayIndex = 1}
  days[dayIndex-1].style.display = "flex";
  setTimeout(showDays, 10000);
}