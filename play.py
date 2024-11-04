import mido
import time

# Replace 'Your MIDI Port' with the actual name of your MIDI output port
port_name = 'Your MIDI Port'

# A minor chord notes (MIDI note numbers)
A = 57    # A3
C = 60    # C4
E = 64    # E4

# MIDI CC number and value for Filter Frequency
cc_number = 102  # Filter Frequency CC
cc_value = 80    # Desired value for the Filter Frequency (0-127)

# Open the MIDI output port
with mido.open_output(port_name) as port:
    # Send a MIDI CC message to change the Filter Frequency
    port.send(mido.Message('control_change', control=cc_number, value=cc_value))

    # Send 'note on' messages to play the chord
    port.send(mido.Message('note_on', note=A, velocity=64))
    port.send(mido.Message('note_on', note=C, velocity=64))
    port.send(mido.Message('note_on', note=E, velocity=64))

    # Hold the notes for 1 second
    time.sleep(1)

    # Send 'note off' messages to release the chord
    port.send(mido.Message('note_off', note=A, velocity=64))
    port.send(mido.Message('note_off', note=C, velocity=64))
    port.send(mido.Message('note_off', note=E, velocity=64))