// code https://github.com/mdn/dom-examples/blob/main/web-speech-api/speech-color-changer/script.js
// sample https://mdn.github.io/dom-examples/web-speech-api/speech-color-changer/

var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechRecognitionEvent =
  SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

var recognition = new SpeechRecognition();
recognition.continuous = true;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

var recorder = document.querySelector("#recorder");
var transcript = document.querySelector("#transcript");

var chat = async function (msg) {
  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg }),
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    console.log(json);

    return json.reply;
  } catch (error) {
    console.error(error.message);
  }
};

recognition.onresult = function (event) {
  // The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
  // The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
  // It has a getter so it can be accessed like an array
  // example: event.results[0][0].transcript
  // The first [0] returns the SpeechRecognitionResult at the last position.
  // Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
  // These also have getters so they can be accessed like arrays.
  // The second [0] returns the SpeechRecognitionAlternative at position 0.
  // We then return the transcript property of the SpeechRecognitionAlternative object

  var result = [];
  for (var i = 0; i < event.results.length; ++i) {
    if (event.results[i][0].transcript.trim().length > 0) {
        result.push(event.results[i][0].transcript);
    }
  }
  transcript.value = result.join(', ') + ".";
};

recognition.onend = async function () {
    if (transcript.value.length > 0) {
        document.querySelector("#history").innerHTML += '<p>Me: ' + transcript.value + '</p>'
        reply = await chat(transcript.value);
        document.querySelector("#history").innerHTML += '<p>Echo: ' + reply + '</p>'
    }
};

recognition.onerror = function (event) {
  alert("Recognize failed");
};

recorder.onmousedown = function () {
  recorder.className = "recorder-button recording";
  recognition.start();
};
recorder.onmouseup = function () {
  recognition.stop();
  recorder.className = "recorder-button";
};
