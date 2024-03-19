import pygame
import keyboard
import time

class oP1UM:
    def __init__(self):
        self.playlist = ["Playboi Carti – Stop Breathing.mp3", "Playboi Carti – Rockstar Made.mp3", "Playboi Carti – Sky.mp3"]
        self.cur_index = 0
        self.is_playing = False
        self.paused_time = 0
        self.paused = False

        pygame.mixer.init()

    def play_song(self):
        if not self.is_playing:
            if self.paused:
                pygame.mixer.music.unpause()
                print("Resuming:", self.playlist[self.cur_index], "from", self.paused_time, "seconds")
            else:
                pygame.mixer.music.load(self.playlist[self.cur_index])
                pygame.mixer.music.play()
                print("Playing:", self.playlist[self.cur_index])
            self.is_playing = True
            self.paused = False

    def stop_song(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            print("Stopping:", self.playlist[self.cur_index])
            self.is_playing = False
            self.paused = False

    def pause_song(self):
        if self.is_playing and not self.paused:
            self.paused_time = pygame.mixer.music.get_pos() / 1000
            pygame.mixer.music.pause()
            print("Pausing:", self.playlist[self.cur_index], "at", self.paused_time, "seconds")
            self.paused = True

    def resume_song(self):
        if self.is_playing and self.paused:
            pygame.mixer.music.unpause()
            print("Resuming:", self.playlist[self.cur_index], "from", self.paused_time, "seconds")
            self.paused = False

    def next_song(self):
        self.stop_song()
        self.cur_index = (self.cur_index + 1) % len(self.playlist)
        self.play_song()

    def prev_song(self):
        self.stop_song()
        self.cur_index = (self.cur_indexq - 1) % len(self.playlist)
        self.play_song()

def main():
    player = oP1UM()

    keyboard.add_hotkey('p', player.play_song)
    keyboard.add_hotkey('s', player.stop_song)
    keyboard.add_hotkey('space', player.pause_song)
    keyboard.add_hotkey('r', player.resume_song)
    keyboard.add_hotkey('n', player.next_song)
    keyboard.add_hotkey('b', player.prev_song)

    print("Press 'p' to play, 's' to stop, 'space' to pause, 'r' to resume, 'n' for next song, 'b' for previous song, 'q' to quit ")

    while True:
        if keyboard.is_pressed('q'):
            pygame.mixer.quit()
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()