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

```
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
Stereo channel data:
[[ 58  27]
 [ 49  65]
 [ 45  98]
 ...
 [173 422]
 [207 485]
 [254 546]]
Left channel data:
[ 58  49  45 ... 173 207 254]
Right channel data:
[ 27  65  98 ... 422 485 546]
```

Left channel data input only:
```
Stereo channel data:
[[-210    0]
 [-301    0]
 [-402    0]
 ...
 [-634    0]
 [-599    0]
 [-570    0]]
Left channel data:
[-210 -301 -402 ... -634 -599 -570]
Right channel data:
[0 0 0 ... 0 0 0]
Stereo channel data:
[[-533    0]
 [-449    0]
 [-356    0]
 ...
 [-481    0]
 [-516    0]
 [-545    0]]
Left channel data:
[-533 -449 -356 ... -481 -516 -545]
Right channel data:
[0 0 0 ... 0 0 0]
```

Right channel data input only:
```
Stereo channel data:
[[   0  144]
 [   0  142]
 [   0  137]
 ...
 [   0 -919]
 [   0 -925]
 [   0 -921]]
Left channel data:
[0 0 0 ... 0 0 0]
Right channel data:
[ 144  142  137 ... -919 -925 -921]
Stereo channel data:
[[   0 -918]
 [   0 -920]
 [   0 -930]
 ...
 [   0 -643]
 [   0 -629]
 [   0 -607]]
Left channel data:
[0 0 0 ... 0 0 0]
Right channel data:
[-918 -920 -930 ... -643 -629 -607]
```

## License

This script is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Credits

This script was created by [[YIN Renlong](https://github.com/YIN-Renlong)].
