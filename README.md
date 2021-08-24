# pyTuneGen
Generates music tunes using Python. Sometimes it isn't terrible at it.

You can customize the generation by choosing your favorite scale, a suitable bpm, an interesting time signature, or adjust some of the unorthodox variables including the randomization seed; or you can simply sit back and let the lords of random number generation do their own thing!

pyTuneGen can also export these grand works of art into MIDI files for convenient handling.

## Installation
```sh
pip install pytunegen
```

## Usage
If you want to start creating random MIDIs right away, it is this simple!
```sh
from pytunegen.midigen import MIDIgen
MIDIgen().export()
```
Although it is simple enough and does the job, the example above is extremely bare-bones and you might want to customize the kind of music generated. To acheive this, you can adjust some or all of the many parameters (this example shows all parameters):
```sh
from pytunegen.midigen import MIDIgen

midi_exporter = MIDIgen(seed=18811938, music_length=100, scale="F Minor", bpm=20, time_sig="3/8",
                        note_jump_limit=1.8, silence_percent=2, non_repeat_percent=75)
midi_exporter.export("my_MIDI_file.mid")
```
You don't have to deal with MIDI files if you want to use the generated music in Python scripts. Instead, you can use TuneGen!
TuneGen creates a list of bars, which themselves are lists of notes, with properties pitch, length and silence (bool value to show whether that note actually denotes a silence).

Here is a simple player that prints out the characteristics of the generated music, and uses the 'synthesizer' package to play it.
```sh
from synthesizer import Player, Synthesizer, Waveform
from pytunegen.tunegen import TuneGen
import time

# initialize the player
player = Player()
player.open_stream()
synth1 = Synthesizer(osc1_waveform = Waveform.sine, osc1_volume=1.0,
    use_osc2=True, osc2_waveform=Waveform.square, osc2_volume=0.3)

# initialize the tune generator
tunegen = TuneGen()

# print the generator details
print(f"Seed: {tunegen.randseed}")
print(f"BPM: {str(tunegen.bpm_current)}")
print("Time Signature:", tunegen.time_sig_display)
print(f"Scale: {tunegen.scale_current_name}")
print(f"Length: {tunegen.music_length} bars")

music = tunegen.generate()

for bar in music:
    print(str(bar.note_names))
    print(str(bar.durations))
    print(f"Bar Repeat: {bar.bar_repeat}\n")
    for note in bar.notes:
        if not note.silence:
            player.play_wave(synth1.generate_constant_wave(note.pitch, note.duration * 60/tunegen.bpm_current))
        else:
            time.sleep(note.duration * 60/tunegen.bpm_current)
```
