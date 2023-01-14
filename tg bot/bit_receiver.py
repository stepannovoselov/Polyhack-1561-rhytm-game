import librosa


def get_beat_seconds(audio_file, threshold=0.5):
    y, sr = librosa.load(audio_file)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_seconds = librosa.frames_to_time(beat_frames, sr=sr)
    strong_beats = [beat for beat in beat_seconds if beat > threshold]
    return strong_beats


def format_arr(arr):
    arr = [round(x, 1) for x in arr]

    arr = list(set(arr))
    arr.sort()

    for i in range(len(arr)):
        if len(arr) > i + 1:
            if arr[i + 1] - arr[i] < 0.2:
                arr.pop(i + 1)
        else:
            break

    return arr


def main_song_handler(name):
    return format_arr(get_beat_seconds(name))
