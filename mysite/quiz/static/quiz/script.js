function updateProgress(progressBarElement, progressBarMessageElement, progress) {
  progressBarElement.style.width = progress.percent + "%";
  progressBarMessageElement.innerHTML = (progress.current / progress.total) * 100 + "%";
}


let bar = document.getElementById("progress-bar");
let barMessage = document.getElementById("progress-bar-message");
for (let i = 0; i < 11; i ++) {
    setTimeout(updateProgress, 500 * i, bar, barMessage, {
        percent: 10 * i,
        current: 10 * i,
        total: 100
    })
}
