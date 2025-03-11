import speech_recognition as sr
import simpleaudio as sa

def play_buzzer():
    try:
        wave_obj = sa.WaveObject.from_wave_file("buzzer.wav")
        wave_obj.play()
        wave_obj2 = sa.WaveObject.from_wave_file("smutnatrombeczka.wav")
        play_obj2 = wave_obj2.play()
        play_obj2.wait_done()
    except Exception as e:
        print("Brak dzwieku, error:", e)

def listen_and_recognize(mic):
    r = sr.Recognizer()
    with mic as source:
        print("Kalibracja Mikrofonu (żeby usunac szum). Poczekaj...")
        r.adjust_for_ambient_noise(source, duration=3)  # Increase duration if needed
        print("Nasłuchuje...")
        audio = r.listen(source)

    try:
        recognized_text = r.recognize_google(audio, language="pl-PL")
        print("You said:", recognized_text)
        if "jakby" in recognized_text.lower():
            print("Wykryto 'jakby' w zdaniu!")
            play_buzzer()
    except sr.UnknownValueError:
        print("Nie zrozumiano dzwięku.")
    except sr.RequestError as e:
        print("RequestError; {0}".format(e))

if __name__ == "__main__":
    mic = sr.Microphone()
    print("Wcisnij CTRL+C zeby wyjsc")
    try:
        while True:
            listen_and_recognize(mic)
    except KeyboardInterrupt:
        print("\nWychodze...")
