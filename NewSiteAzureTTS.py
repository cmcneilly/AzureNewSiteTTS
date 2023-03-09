#https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech?tabs=script%2Cwindowsinstall&pivots=programming-language-python

import azure.cognitiveservices.speech as speechsdk
import csv

#https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt-tts#voice-styles-and-roles
languageCode = 'en-US'
ssmlGender = 'MALE'
voicName = 'en-US-GuyNeural'
speakingRate = '+5%'
pitch = '-1%'
voiceStyle = 'newscast'

azureKey = '4a23316f4bcd426b8373d1c030471cca'
azureRegion = 'eastus'

with open('VoiceNewSite.csv', "r") as recording:
    recording_reader = csv.DictReader(recording, delimiter=',')
    for row in recording_reader:
        audioOuputFile1920 = "W_6" + row['Store'] + "1920.wav"
        audioOuputFile1921 = "W_6" + row['Store'] + "1921.wav"
        audioOuputFile1922 = "W_6" + row['Store'] + "1922.wav"
        audioOuputFile1927 = "W_6" + row['Store'] + "1927.wav"
        audioOuputFile1930 = "W_6" + row['Store'] + "1930.wav"
        audioOuputFile1931 = "W_6" + row['Store'] + "1931.wav"
        audioOuputFile1932 = "W_6" + row['Store'] + "1932.wav"
        audioOuputFile1980 = "W_6" + row['Store'] + "1980.wav"
        site = row['Store']
        city = row['City']
        state = row['State']
        #
        head1 = f'<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="{languageCode}">'
        head2 = f'<voice name="{voicName}">'
        head3 = f'<mstts:express-as style="{voiceStyle}">'
        head4 = f'<prosody rate="{speakingRate}" pitch="{pitch}">'
        head5 = f'<break time="100ms"/>'
        tail = '</prosody></mstts:express-as></voice></speak>'
        #
        ssml1920 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "RV Outdoor Info" + tail
        ssml1921 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "Retail Parts" + tail
        ssml1922 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "OEM Parts" + tail
        ssml1927 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "Rollover" + tail
        ssml1930 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "Sales" + tail
        ssml1931 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "Service" + tail
        ssml1932 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "Mobile Service" + tail
        ssml1980 = head1 + head2 + head3 + head4 + city + " " + state + head5 + "BDC Management" + tail
        print('Processing Site',site)

        #
        speech_config = speechsdk.SpeechConfig(subscription=azureKey, region=azureRegion)
        audio_config1920 = speechsdk.AudioConfig(filename=audioOuputFile1920)
        audio_config1921 = speechsdk.AudioConfig(filename=audioOuputFile1921)
        audio_config1922 = speechsdk.AudioConfig(filename=audioOuputFile1922)
        audio_config1927 = speechsdk.AudioConfig(filename=audioOuputFile1927)
        audio_config1930 = speechsdk.AudioConfig(filename=audioOuputFile1930)
        audio_config1931 = speechsdk.AudioConfig(filename=audioOuputFile1931)
        audio_config1932 = speechsdk.AudioConfig(filename=audioOuputFile1932)
        audio_config1980 = speechsdk.AudioConfig(filename=audioOuputFile1980)
        #
        # Set file format to be 8khz-8bit-mono-mulaw
        # https://docs.microsoft.com/en-us/dotnet/api/microsoft.cognitiveservices.speech.speechsynthesisoutputformat?view=azure-dotnet
        speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff8Khz8BitMonoMULaw)
        #
        synthesizer1920 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1920)
        synthesizer1920.speak_ssml_async(ssml1920)
        synthesizer1921 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1921)
        synthesizer1921.speak_ssml_async(ssml1921)
        synthesizer1922 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1922)
        synthesizer1922.speak_ssml_async(ssml1922)
        synthesizer1927 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1927)
        synthesizer1927.speak_ssml_async(ssml1927)
        synthesizer1930 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1930)
        synthesizer1930.speak_ssml_async(ssml1930)
        synthesizer1931 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1931)
        synthesizer1931.speak_ssml_async(ssml1931)
        synthesizer1932 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1932)
        synthesizer1932.speak_ssml_async(ssml1932)
        synthesizer1980 = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config1980)
        synthesizer1980.speak_ssml_async(ssml1980)