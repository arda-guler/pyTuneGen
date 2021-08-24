#!/usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------
#  NOTE FREQUENCY TABLE
#-------------------------

# 3rd octave
c3 = 131
c_3 = 139
d3 = 147
d_3 = 156
e3 = 165
f3 = 175
f_3 = 185
g3 = 196
g_3 = 208
a3 = 220
a_3 = 233
b3 = 247

# 4th octave
c4 = 262
c_4 = 277
d4 = 294
d_4 = 311
e4 = 330
f4 = 349
f_4 = 370
g4 = 392
g_4 = 415
a4 = 440
a_4 = 466
b4 = 494

# 5th octave
c5 = 523
c_5 = 554
d5 = 587
d_5 = 622
e5 = 659
f5 = 698
f_5 = 740
g5 = 784
g_5 = 831
a5 = 880.00
a_5 = 932
b5 = 988

# scales

full_notes = {"C3":c3, "C#3":c_3, "D3":d3, "D#3":d_3, "E3":e3, "F3":f3, "F#3":f_3, "G3":g3, "G#3":g_3, "A3":a3, "A#3":a_3, "B3":b3,
              "C4":c4, "C#4":c_4, "D4":d4, "D#4":d_4, "E4":e4, "F4":f4, "F#4":f_4, "G4":g4, "G#4":g_4, "A4":a4, "A#4":a_4, "B4":b4,
              "C5":c5, "C#5":c_5, "D5":d5, "D#5":d_5, "E5":e5, "F5":f5, "F#5":f_5, "G5":g5, "G#5":g_5, "A5":a5, "A#5":a_5, "B5":b5}

c_major = {"C3":c3, "D3":d3, "E3":e3, "F3":f3, "G3":g3, "A3":a3, "B3":b3,
           "C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "B4":b4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "B5":b5}

f_major = {"C3":c3, "D3":d3, "E3":e3, "F3":f3, "G3":g3, "A3":a3, "A#3":a_3,
           "C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "A#5":a_5}

d_major = {"C#3":c_3, "D3":d3, "E3":e3, "F#3":f_3, "G3":g3, "A3":a3, "B3":b3,
           "C#4":c_4, "D4":d4, "E4":e4, "F#4":f_4, "G4":g4, "A4":a4, "B4":b4,
           "C#5":c_5, "D5":d5, "E5":e5, "F#5":f_5, "G5":g5, "A5":a5, "B5":b5}

g_major = {"C3":c3, "D3":d3, "E3":e3, "F#3":f_3, "G3":g3, "A3":a3, "B3":b3,
           "C4":c4, "D4":d4, "E4":e4, "F#4":f_4, "G4":g4, "A4":a4, "B4":b4,
           "C5":c5, "D5":d5, "E5":e5, "F#5":f_5, "G5":g5, "A5":a5, "B5":b5}

c_minor = {"C3":c3, "D3":d3, "D#3":d_3, "F3":f3, "G3":g3, "G#3":g_3, "A#3":a_3,
           "C4":c4, "D4":d4, "D#4":d_4, "F4":f4, "G4":g4, "G#4":g_4, "A#4":a_4,
           "C5":c5, "D5":d5, "D#5":d_5, "F5":f5, "G5":g5, "G#5":g_5, "A#5":a_5}

d_minor = {"C3":c3, "D3":d3, "E3":e3, "F3":f3, "G3":g3, "A3":a3, "A#3":a_3,
           "C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "A#5":a_5}

g_minor = {"C3":c3, "D3":d3, "D#3":d_3, "F3":f3, "G3":g3, "A3":a3, "A#3":a_3,
           "C4":c4, "D4":d4, "D#4":d_4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "D#4":d_5, "F4":f5, "G4":g5, "A4":a5, "A#4":a_5}

f_minor = {"C3":c3, "C#3":c_3, "D#3":d_3, "F3":f3, "G3":g3, "G#3":g_3, "A#3":a_3,
           "C4":c4, "C#4":c_4, "D#4":d_4, "F4":f4, "G4":g4, "G#4":g_4, "A#4":a_4,
           "C5":c5, "C#5":c_5, "D#5":d_5, "F5":f5, "G5":g5, "G#5":g_5, "A#5":a_5}

scales = {"Full Notes":full_notes, "C Major":c_major, "F Major":f_major, "D Major":d_major, "G Major":g_major,
          "C Minor":c_minor, "D Minor":d_minor, "G Minor":g_minor, "F Minor":f_minor}

#-------------------------
#       BPM PRESETS
#-------------------------

bpm_slowest = 10
bpm_slow = 15
bpm_slowish = 30
bpm_normal = 60
bpm_fastish = 120
bpm_fast = 160
bpm_fastest = 180

bpms = [bpm_slowest, bpm_slow, bpm_slowish, bpm_normal, bpm_fastish, bpm_fast, bpm_fastest]

#-------------------------
#  DURATIONS AND REPEATS
#-------------------------

note_durations = {"1/8": 1/8, "1/4":1/4, "1/2": 1/2, "1":1, "2":2, "4":4}
bar_repeats = [2, 4]
