let choices_ul = document.getElementById("id_choices");
let choices_lis = choices_ul.getElementsByTagName("li");
for (let i = 0; i < choices_lis.length; i ++) {
    choices_lis[i].classList.add("choice-li");
}