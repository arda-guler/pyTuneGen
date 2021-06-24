function sing(song, words) {
  const synth = new Tone.Synth().toDestination();
  let total_duration = 0;
  for (let i = 0; i < song.length; i++) {
    total_duration += song[i][1];
    synth.triggerAttackRelease(song[i][0], song[i][1], total_duration);
  }

  var list = words.split(" ");
  (function printWord(i) {
    setTimeout(function () {
      if (list[i]) {
        let color = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
        $("#words").append(
          "<span style='color:" + color + "'>" + list[i] + "</span> "
        );
      }
      if (--i) printWord(i);
    }, (total_duration * 1000) / list.length);
  })(list.length);
}
