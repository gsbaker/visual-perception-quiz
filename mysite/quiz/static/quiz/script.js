function updateProgress(progressBarElement, progressBarMessageElement, progress) {
  progressBarElement.style.width = progress.percent + "%";
  progressBarMessageElement.innerHTML = Math.round((progress.current / progress.total) * 100) + "%";
}


let bar1 = document.getElementById("progress-bar-1");
let barMessage1 = document.getElementById("progress-bar-1-message");
for (let i = 0; i < 11; i ++) {
    setTimeout(updateProgress, 80 * i, bar1, barMessage1, {
        percent: 8.2 * i,
        current: 8.2 * i,
        total: 100
    })
}

let bar2 = document.getElementById("progress-bar-2");
let barMessage2 = document.getElementById("progress-bar-2-message");
for (let i = 0; i < 11; i ++) {
    setTimeout(updateProgress, 80 * i, bar2, barMessage2, {
        percent: 2.8 * i,
        current: 2.8 * i,
        total: 100
    })
}