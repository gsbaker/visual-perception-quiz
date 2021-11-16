let choices_ul = document.getElementById("id_choices");
let choices_lis = choices_ul.getElementsByTagName("li");
for (let i = 0; i < choices_lis.length; i ++) {
    choices_lis[i].classList.add("choice-li");
}


function updateProgress(progressBarElement, progressBarMessageElement, progress) {
  progressBarElement.style.width = progress.percent + "%";
  progressBarMessageElement.innerHTML = Math.round((progress.current / progress.total) * 100) + "%";
}


var question = '{{ current_question|escapejs }}';
console.log(question);


setTimeout(() => generateProgress(), 1000);


function generateProgress() {
    let bar1 = document.getElementById("progress-bar-1");
    let barMessage1 = document.getElementById("progress-bar-1-message");
    for (let i = 0; i < 11; i ++) {
        setTimeout(updateProgress, 80 * i, bar1, barMessage1, {
            percent: 2.0 * i,
            current: 2.0 * i,
            total: 100
        })
    }

    let bar2 = document.getElementById("progress-bar-2");
    let barMessage2 = document.getElementById("progress-bar-2-message");
    for (let i = 0; i < 11; i ++) {
        setTimeout(updateProgress, 80 * i, bar2, barMessage2, {
            percent: 8.2 * i,
            current: 8.2 * i,
            total: 100
        })
    }

    let bar3 = document.getElementById("progress-bar-3");
    let barMessage3 = document.getElementById("progress-bar-3-message");
    for (let i = 0; i < 11; i ++) {
        setTimeout(updateProgress, 80 * i, bar3, barMessage3, {
            percent: 0.6 * i,
            current: 0.6 * i,
            total: 100
        })
    }

    let bar4 = document.getElementById("progress-bar-4");
    let barMessage4 = document.getElementById("progress-bar-4-message");
    for (let i = 0; i < 11; i ++) {
        setTimeout(updateProgress, 80 * i, bar4, barMessage4, {
            percent: 0.2 * i,
            current: 0.2 * i,
            total: 100
        })
    }
}

