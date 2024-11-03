class NoteHashtable:
    def __init__(self):
        self.table = {}
        self.populate_table()

    def populate_table(self):
        # Note: Frequencies for the 4th and 5th octaves are included
        notes_frequencies = {
            'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13,
            'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'G4': 392.00,
            'G#4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'B4': 493.88,
            'C5': 523.25, 'C#5': 554.37, 'D5': 587.33, 'D#5': 622.25,
            'E5': 659.25, 'F5': 698.46, 'F#5': 739.99, 'G5': 783.99,
            'G#5': 830.61, 'A5': 880.00, 'A#5': 932.33, 'B5': 987.77,
            'C6': 1046.50
        }
        # Reverse the mapping
        for note, frequency in notes_frequencies.items():
            self.table[round(frequency, 2)] = note

    def get_note_from_frequency(self, frequency):
        # Round the frequency to two decimal places
        return self.table.get(round(frequency, 2), "Frequency not found")

# Example usage
"""
frequency_to_note = NoteHashtable()
print(frequency_to_note.get_note_from_frequency(440.0))  # Output: A4
print(frequency_to_note.get_note_from_frequency(523.25))  # Output: C5
print(frequency_to_note.get_note_from_frequency(300.0))   # Output: Frequency not found
"""

#Check if frequency is correct
def note_to_frequency(note, octave):
    a4 = 440.0
    notes = {
        'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F': -4, 'F#': -3,
        'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2
    }

    if note in notes:
        semitone_distance = notes[note] + (octave - 4) * 12
        frequency = a4 * (2 ** (semitone_distance / 12))
        return round(frequency, 2)
    else:
        return None

# Example Usage
"""print(note_to_frequency('A', 4))  # Output: 440.0
print(note_to_frequency('C', 5))  # Output: 523.25
"""