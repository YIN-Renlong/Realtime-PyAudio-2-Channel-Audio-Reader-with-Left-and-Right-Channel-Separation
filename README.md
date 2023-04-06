# Realtime PyAudio Read 2-Channel and Left-Right

This script allows you to read and process live audio input from a stereo source, outputting both the combined stereo signal and the separate left and right channels. The script uses the PyAudio library and requires Python 3.

## Installation

1. Clone this repository or download the `realtime_pyaudio_read_2_channel_and_left_right.py` file.

## Usage

1. Install PyAudio library: `pip install pyaudio`
2. Run the program: `python realtime_pyaudio_read_2_channel_and_left_right.py`
3. Choose the audio device you want to use by entering its index number
4. The program will start a live audio stream and print the stereo channel data, left channel data, and right channel data in real-time
5. Press `Ctrl+C` to stop the live audio stream

## Example of output

Stereo channel data:
[[535 320]
 [481 263]
 [433 214]
 ...
 [118 -69]
 [ 91 -47]
 [ 72 -11]]
Left channel data:
[535 481 433 ... 118  91  72]
Right channel data:
[320 263 214 ... -69 -47 -11]

## License

This script is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Credits

This script was created by [[YIN Renlong](https://github.com/YIN-Renlong)].
