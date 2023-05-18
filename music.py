from pydub import AudioSegment
import random

# Define the beat pattern
kick = AudioSegment.from_file("kick.wav")
snare = AudioSegment.from_file("snare.wav")
hihat = AudioSegment.from_file("hihat.wav")
beat = kick + snare + hihat

# Create the beat track
track = AudioSegment.silent(duration=4000)
for i in range(16):
    if random.random() < 0.5:
        track = track.overlay(beat, position=i*250)

# Export the beat as an mp3 file
track.export("beat2.mp3", format="mp3")