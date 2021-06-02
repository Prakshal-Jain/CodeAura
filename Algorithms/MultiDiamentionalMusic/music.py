import sys
from pydub.playback import play
from pydub import AudioSegment

def stereo(inputFilename, outputFilename="output.wav", volume_left=0, volume_right=100):
    left_channel = AudioSegment.from_wav(inputFilename)
    if(left_channel.channels != 1):
        left_channel = left_channel.split_to_mono()[0]
    sampleArr = left_channel.get_array_of_samples()
    arrRight = []
    arrLeft = []
    size = len(sampleArr)
    counter = 0
    while(counter < size):
        # print(int((1 - volume_left/100)*sampleArr[counter]), sampleArr[counter])
        arrLeft.append((int((volume_left/100)*sampleArr[counter]).to_bytes(2,'little',signed = True)))
        arrRight.append((int((volume_right/100)*sampleArr[counter]).to_bytes(2,'little',signed = True)))
        counter += 1

    stereo_sound = AudioSegment.from_mono_audiosegments(left_channel._spawn(arrLeft), left_channel._spawn(arrRight))
    file_handle = stereo_sound.export(outputFilename, format="wav")

stereo("input.wav", volume_left=30, volume_right=70)
