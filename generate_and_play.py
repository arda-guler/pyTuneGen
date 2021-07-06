#!/usr/bin/python
# -*- coding: utf-8 -*-

from synthesizer import Player, Synthesizer, Waveform
from pytunegen.tunegen import TuneGen
from pytunegen.constants import *
import time

# initialize the player
player = Player()
player.open_stream()
synth1 = Synthesizer(osc1_waveform = Waveform.sine, osc1_volume=1.0,
    use_osc2=True, osc2_waveform=Waveform.square, osc2_volume=0.3)

# initialize the tune generator
tunegen = TuneGen(None)

# print the generator details
print(f"Seed: {tunegen.randseed}")
print(f"BPM: {str(tunegen.bpm_current)}")
print(f"Scale: {str(tunegen.scale)}/4")
print(f"Chord: {tunegen.chord_current_name}")
print(f"Length: {music_length} bars")

tune_group = tunegen.generate()

for group in tune_group:
    print(str(group.note_names))
    print(str(group.durations))
    print(f"Bar Repeat: {group.bar_repeat}\n")
    for tune in group.tunes:
        if not tune.silence:
            player.play_wave(synth1.generate_constant_wave(tune.note, tune.duration * 60/tunegen.bpm_current))
        else:
            time.sleep(tune.duration * 60/tunegen.bpm_current)
