# COPYRIGHT (C) <2023> <YIN RENLONG>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pyaudio
import numpy as np

def get_audio_devices():
    pa = pyaudio.PyAudio()
    device_count = pa.get_device_count()
    devices = []
    for i in range(device_count):
        device_info = pa.get_device_info_by_index(i)
        devices.append((i, device_info["name"], device_info["maxInputChannels"]))
    pa.terminate()
    return devices

def choose_audio_device():
    devices = get_audio_devices()
    print("Available audio devices:")
    for i, device_name, channels in devices:
        print(f"{i}: {device_name} ({channels} channels)")

    chosen_device = int(input("Enter the index of the device you want to use: "))
    return chosen_device

def callback(in_data, frame_count, time_info, status):
    audio_data = np.frombuffer(in_data, dtype=np.int16).reshape(-1, 2)
    left_channel = audio_data[:, 0]
    right_channel = audio_data[:, 1]

    print("Stereo channel data:")
    print(audio_data)
    print("Left channel data:")
    print(left_channel)
    print("Right channel data:")
    print(right_channel)

    return (None, pyaudio.paContinue)

def main():
    chosen_device = choose_audio_device()

    pa = pyaudio.PyAudio()
    stream = pa.open(
        input_device_index=chosen_device,
        format=pyaudio.paInt16,
        channels=2,
        rate=44100,
        input=True,
        frames_per_buffer=1024,
        stream_callback=callback
    )

    print("Starting live audio stream...")
    stream.start_stream()

    try:
        while stream.is_active():
            pass
    except KeyboardInterrupt:
        print("Stopping live audio stream...")

    stream.stop_stream()
    stream.close()
    pa.terminate()

if __name__ == "__main__":
    main()
