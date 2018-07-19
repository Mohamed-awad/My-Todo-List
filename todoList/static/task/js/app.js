
$(document).ready(function () {

  $('.box').on("click", function() {
    if (this.checked) {
        this.setAttribute("checked", "checked");
        var x = document.getElementsByName(this.id)[0];
        var y = x.textContent;
        x.innerHTML = '<del>' + y + '</del>';
    } else {
      this.removeAttribute("checked");
      var x = document.getElementsByName(this.id)[0];
        var y = x.textContent;
        x.innerHTML = y
    }
  });
})
