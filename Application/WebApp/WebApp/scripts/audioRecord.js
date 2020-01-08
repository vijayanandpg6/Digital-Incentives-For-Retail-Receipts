var onFail = function (e) {
    console.log('Rejected!', e);
};

var onSuccess = function (s) {
    var context = new (window.AudioContext || window.webkitAudioContext)()
    var mediaStreamSource = context.createMediaStreamSource(s);
    recorder = new Recorder(mediaStreamSource);
    recorder.record();

    // audio loopback
    // mediaStreamSource.connect(context.destination);
}

window.URL = window.URL || window.webkitURL;
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;

var recorder;
var audio = document.querySelector('audio');

function startRecording() {
    document.getElementById("recordingLogo").style.display = "block";
    if (navigator.getUserMedia) {
        navigator.getUserMedia({ audio: true }, onSuccess, onFail);
    } else {
        console.log('navigator.getUserMedia not present');
    }
}

function stopRecording() {
    document.getElementById("recordingLogo").style.display = "none";
    recorder.stop();
    recorder.exportWAV(function (s) {

        audio.src = window.URL.createObjectURL(s);
    });
}
