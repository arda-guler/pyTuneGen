from midiutil import MIDIFile
from pytunegen.tunegen import TuneGen
from pytunegen.constants import full_notes
import math

tunegen = TuneGen()

print(f"Seed: {tunegen.randseed}")
print(f"BPM: {str(tunegen.bpm_current)}")
print("Time Signature:", tunegen.time_sig_display)
print(f"Chord: {tunegen.chord_current_name}")
print(f"Length: {tunegen.music_length} bars")

music = tunegen.generate()

exportMIDI = MIDIFile(1)
exportMIDI.addTempo(0, 0, tunegen.bpm_current)

time = 0
for bar in music:
    for note in bar.notes:
        if not note.silence:
            midi_note = int((12/math.log(2)) * math.log(note.pitch/27.5) + 21)
            # addNote(track, channel, pitch, time, duration, volume)
            exportMIDI.addNote(0, 0, midi_note, time, note.duration, 100)
            time += note.duration
        else:
            time += note.duration

with open(str(tunegen.randseed) + ".mid", "wb") as export_file:
    exportMIDI.writeFile(export_file)
    
