function sing(song, words) {
  const synth = new Tone.Synth().toDestination();
  let total_duration = 0;
  for (let i = 0; i < song.length; i++) {
    total_duration += song[i][1];
    synth.triggerAttackRelease(song[i][0], song[i][1], total_duration);
  }

  var word_list = words.split(" ");
  let word_count = word_list.length;
  if (song.length < word_list.length) {
    word_count = song.length;
  }

  (function printWord(i) {
    setTimeout(function () {
      if (word_list[i]) {
        let color = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
        $("#words").append(
          "<span style='color:" + color + "'>" + word_list[i] + "</span> "
        );
      }
      if (--i) printWord(i);
    }, song[song.length-i][1] * 1000);
  })(word_count);
}
