#!/usr/bin/python
# -*- coding: utf-8 -*-

from pytunegen.tunegen import TuneGen
from pytunegen.constants import full_notes
from midiutil import MIDIFile
import math

class MIDIgen():
    """MIDI Exporter"""
    
    def __init__(self, seed = None, music_length = 50,
                 chord = None, bpm = None, time_sig = None,
                 note_jump_limit = 2.2, silence_percent = 1,
                 non_repeat_percent = 65):
    
        self.tunegen = TuneGen(seed, music_length, chord, bpm,
                               time_sig, note_jump_limit,
                               silence_percent, non_repeat_percent)
        self.music = self.tunegen.generate()

    def export(self, export_filename = None):

        self.exportMIDI = MIDIFile(1)
        self.exportMIDI.addTempo(0, 0, self.tunegen.bpm_current)

        time = 0
        for bar in self.music:
            for note in bar.notes:
                if not note.silence:
                    midi_note = int((12/math.log(2)) * math.log(note.pitch/27.5) + 21)
                    # addNote(track, channel, pitch, time, duration, volume)
                    self.exportMIDI.addNote(0, 0, midi_note, time, note.duration, 100)
                    time += note.duration
                else:
                    time += note.duration

        if not export_filename:
            export_filename = str(self.tunegen.randseed) + ".mid"
        elif not export_filename[-4:] == ".mid":
            export_filename = export_filename + ".mid"

        with open(export_filename, "wb") as export_file:
            self.exportMIDI.writeFile(export_file)
