
//  function star() {
//     let count = 100;
//     let main = document.querySelector("body");
//     let i = 0;
//     while (i < count) {
//       let star = document.createElement("i");
//       let x = Math.floor(Math.random() * window.innerWidth);
//       let y = Math.floor(Math.random() * window.innerHeight);
//       let duration = Math.random() * 10;
//       let size = Math.random() * 1;
//       star.style.left = x + 'px';
//       star.style.top = y + 'px';
//       star.style.width = 1 + size + 'px';
//       star.style.height = 1 + size + 'px';
//       star.style.animationDuration = 6 + duration + 's';
//       star.style.animationDelay = duration + 's';
//       main.appendChild(star);
//       i++
//     }
//   } star();
 
var myVar;
 
function myFunction() {

  myVar = setTimeout(showPage,  50  );

}
 
function showPage() {

  document.getElementById("loader").style.display = "none";

  document.getElementById("myDiv").style.display = "block";

}