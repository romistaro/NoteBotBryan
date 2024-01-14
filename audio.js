start = document.getElementById("start");
stop = document.getElementById("stop");

if (navigator.mediaDevices.getUserMedia) {
    let onSuccess = function(stream) {
        const mediaRecorder = new MediaRecorder(stream);
    }
}
