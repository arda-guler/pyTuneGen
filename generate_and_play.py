#!/usr/bin/python
# -*- coding: utf-8 -*-

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
print(f"Scale: {str(tunegen.scale)}/4")
print(f"Chord: {tunegen.chord_current_name}")
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
