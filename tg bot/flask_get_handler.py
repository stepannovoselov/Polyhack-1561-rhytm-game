from flask import Flask, request, send_file
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def handle_get_request():
    query_params = request.args
    if query_params.get("action") == "get music data":
        respone = {}
        for song_name in os.listdir("custom music/"):
            if song_name.endswith(".mp3"):
                song_name = song_name.replace(".mp3", "")

                with open(f"custom music/{song_name}.txt", encoding="UTF-8") as f:
                    splitted = f.read().split("\n")
                    respone[song_name] = {}
                    respone[song_name]["beat_times"] = eval(splitted[0])
                    respone[song_name]["filename"] = "music/custom/" + splitted[1].replace('"', "")
                    respone[song_name]["duration"] = eval(splitted[2])
        return [respone, len(respone.keys())]

    elif query_params.get("action") == "get music files":
        N = int(query_params.get("num"))
        result = send_file("custom music/" + [i for i in os.listdir("custom music/") if i.endswith(".mp3")][N], as_attachment=True)
        #os.remove("custom music/" + [i for i in os.listdir("custom music/") if i.endswith(".mp3")][N])
        #os.remove("custom music/" + [i for i in os.listdir("custom music/") if i.endswith(".txt")][N])
        return result


def keep_alive():
    app.run()