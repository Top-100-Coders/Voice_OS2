import tkinter as tk
import time
import sounddevice as sd
import numpy as np
import threading
import wavio as wv
import subprocess 
import back_end

#main window
class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice OS")
        self.root.minsize(300, 250)  # Set minimum window size

        self.microphone_icon = tk.PhotoImage(file="microphone-342.png")  # Replace with your microphone icon path

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        self.microphone_label = tk.Label(self.frame, image=self.microphone_icon)
        self.microphone_label.pack(anchor=tk.CENTER, padx=10, pady=5)

        self.start_button = tk.Button(self.frame, text="Start", command=self.start_stop_action)
        self.start_button.pack(anchor=tk.CENTER, padx=10, pady=5)

        self.label = tk.Label(self.frame, text="")
        self.label.pack(anchor=tk.CENTER)

        self.is_running = False
        self.audio_thread = None

    def start_stop_action(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(text="Stop")
            self.label.config(text="Recording")
            self.audio_thread = threading.Thread(target=self.record_audio)
            self.audio_thread.start()
        else:
            self.is_running = False
            self.start_button.config(text="Start")
            self.label.config(text="")
            if self.audio_thread and self.audio_thread.is_alive():
                self.audio_thread.join()

    def record_audio(self):
        audio_data = []
        while self.is_running: 
            data = sd.rec(int(44100 * 5), samplerate=44100, channels=2, dtype=np.int16) 
            audio_data.extend(data)
            sd.wait()
        wv.write("recording1.wav", audio_data, 44100, sampwidth=2) # sampwidth ?
        
        ques = back_end.transcrpt("recording1.wav") 
        command=back_end.chat(ques)
        # print(command)
        try: 
            if command=="ls": 
                command="dir"
            subprocess.run(command, shell=True, check=True) # what is subprocess? parameters?
        except subprocess.CalledProcessError as e:  
            print(f"Command execution failed: {e}")

     
#main func
def main():
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
