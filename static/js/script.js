// ========== function-to-animate-contant ==========

var myVar;
function myFunction() {
  myVar = setTimeout(showPage,  50  );
}
function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}