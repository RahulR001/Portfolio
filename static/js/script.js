// ========== function-to-animate-contant ==========

var myVar;
function myFunction() {
  myVar = setTimeout(showPage,  200  );
}
function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}