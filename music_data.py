import requests

music_data = {
    "Shiiva Raw - Castle": {
        "beat_times": [1.9, 2.3, 2.5, 2.8, 3.1, 3.6, 4.1, 4.5, 5.3, 5.7, 6.0, 6.5, 6.8, 7.1, 7.6, 8.2, 8.4, 8.8, 9.2, 9.4, 10.2, 10.4, 11.0, 11.4, 11.8, 12.2, 12.5, 12.8, 13.1, 13.4, 14.2, 14.6, 15.0, 15.3, 15.8, 16.4, 16.9, 17.5, 17.9, 18.2, 18.5, 18.8, 19.2, 19.5, 19.9, 20.9, 21.1, 21.5, 22.1, 22.9, 23.2, 23.6, 24.2, 24.7, 25.0, 25.3, 26.1, 26.6, 27.2, 27.6, 28.0, 28.7, 29.0, 29.4, 29.7, 30.0, 30.7, 31.2, 31.5, 31.8, 32.2, 33.1, 33.7, 34.1, 34.5, 34.9, 35.3, 35.7, 36.3, 36.5, 37.2, 38.2, 38.6, 39.1, 39.4, 39.6, 40.2, 40.8, 41.2, 41.7, 42.4, 42.6, 43.0, 43.5, 43.8, 44.1, 44.7, 45.2, 45.6, 45.9, 46.3, 46.9, 47.1, 47.4, 48.0, 48.3, 48.8, 49.1, 49.5, 50.1, 50.7, 51.2, 51.5, 51.7, 52.1, 52.5, 52.8, 53.3, 53.6, 53.9, 54.2, 54.7, 55.3, 55.6, 56.0, 56.5, 57.1, 57.7, 58.1, 58.5, 58.9, 59.2, 59.8, 60.4, 60.7, 61.0, 61.3, 61.8, 62.3, 62.5, 63.0, 63.4, 63.6, 64.2, 64.5, 65.2, 65.7, 66.1, 66.3, 66.5, 67.2, 67.8, 68.2, 69.0, 69.4, 69.8, 70.4, 71.0, 71.4, 72.0, 72.5, 72.8, 73.0, 73.4, 73.9, 74.2, 74.7, 75.0, 75.3, 76.0, 76.6, 76.9, 77.5, 77.9, 78.5, 78.7, 79.3, 79.5, 79.9, 80.9, 81.3, 81.7, 81.9, 82.3, 82.5, 83.1, 83.4, 83.7, 84.1, 84.5, 84.9, 85.2, 86.0, 86.3, 86.8, 87.0, 87.4, 87.7, 88.1, 88.4, 88.8, 89.0, 89.6, 89.8, 90.2, 90.6, 91.0, 91.5, 91.7, 92.0, 92.3, 92.6, 92.8, 93.1, 93.5, 93.8, 94.2, 94.7, 94.9, 95.5, 96.0, 96.5, 97.0, 97.5, 97.8, 98.2, 98.8, 99.0, 99.3, 99.9, 100.2, 100.4, 100.7, 101.0, 101.4, 101.8, 102.0, 102.5, 103.1, 104.0, 104.4, 104.7, 105.3, 105.8, 106.6, 106.9, 107.2, 107.5, 107.9, 108.3, 108.5, 108.7, 109.0, 109.6, 110.0, 110.5, 110.7, 111.1, 111.7, 111.9, 112.3, 112.8, 113.2, 113.7, 114.1, 114.4, 114.9, 115.2, 115.5, 116.1, 116.4, 116.8, 117.2, 117.8, 118.3, 118.5, 118.8, 119.2, 119.5, 120.0],
        "filename": "music/default/Shiiva Raw - Castle.mp3",
        "duration": 120
    },
    "Serebro - Malo Tebya Hardstyle Remix": {
        "beat_times": [1.7, 2.0, 2.4, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3, 4.7, 5.0, 5.3, 5.7, 6.0, 6.3, 6.7, 7.0, 7.3, 7.6, 8.0, 8.3, 8.6, 9.0, 9.3, 9.6, 10.0, 10.3, 10.6, 11.0, 11.3, 11.6, 12.0, 12.3, 12.6, 12.9, 13.3, 13.6, 13.9, 14.3, 14.6, 14.9, 15.3, 15.6, 15.9, 16.3, 16.6, 16.9, 17.2, 17.6, 17.9, 18.2, 18.6, 18.9, 19.2, 19.6, 19.9, 20.2, 20.5, 20.9, 21.2, 21.5, 21.9, 22.2, 22.5, 22.8, 23.2, 23.5, 23.8, 24.2, 24.5, 24.8, 25.2, 25.5, 25.8, 26.1, 26.5, 26.8, 27.1, 27.5, 27.8, 28.1, 28.5, 28.8, 29.1, 29.5, 29.8, 30.1, 30.4, 30.8, 31.1, 31.4, 31.8, 32.1, 32.4, 32.8, 33.1, 33.4, 33.8, 34.1, 34.4, 34.7, 35.1, 35.4, 35.7, 36.1, 36.4, 36.7, 37.1, 37.4, 37.7, 38.1, 38.4, 38.7, 39.0, 39.4, 39.7, 40.0, 40.4, 40.7, 41.0, 41.4, 41.7, 42.0, 42.4, 42.7, 43.0, 43.3, 43.7, 44.0, 44.3, 44.7, 45.0, 45.3, 45.7, 46.0, 46.3, 46.6, 47.0, 47.3, 47.6, 47.9, 48.3, 48.6, 48.9, 49.3, 49.6, 49.9, 50.3, 50.6, 50.9, 51.3, 51.6, 51.9, 52.2, 52.6, 52.9, 53.2, 53.6, 53.9, 54.2, 54.6, 54.9, 55.2, 55.6, 55.9, 56.2, 56.5, 56.9, 57.2, 57.5, 57.9, 58.2, 58.5, 58.9, 59.2, 59.5, 59.9, 60.2, 60.5, 60.9, 61.2, 61.5, 61.8, 62.2, 62.5, 62.8, 63.2, 63.5, 63.8, 64.2, 64.5, 64.8, 65.1, 65.5, 65.8, 66.1, 66.5, 66.8, 67.1, 67.5, 67.8, 68.1, 68.4, 68.8, 69.1, 69.4, 69.8, 70.1, 70.4, 70.8, 71.1, 71.4, 71.7, 72.1, 72.4, 72.7, 73.1, 73.4, 73.7, 74.1, 74.4, 74.7, 75.0, 75.4, 75.7, 76.0, 76.4, 76.7, 77.0, 77.4, 77.7, 78.0, 78.3, 78.7, 79.0, 79.3, 79.7, 80.0, 80.3, 80.7, 81.0, 81.3, 81.7, 82.0, 82.3, 82.6, 83.0, 83.3, 83.6, 84.0, 84.3, 84.6, 85.0, 85.3, 85.6, 85.9, 86.3, 86.6, 86.9, 87.3, 87.6, 87.9, 88.3, 88.6, 88.9, 89.3, 89.6, 89.9, 90.2, 90.6, 90.9, 91.2, 91.6, 91.9, 92.2, 92.6, 92.9, 93.2, 93.6, 93.9, 94.2, 94.6, 94.9, 95.2, 95.5, 95.9, 96.2, 96.5, 96.9, 97.2, 97.5, 97.8, 98.2, 98.5, 98.8, 99.2, 99.5, 99.8, 100.1, 100.5, 100.8, 101.1, 101.5, 101.8, 102.1, 102.5, 102.8, 103.1, 103.5, 103.8, 104.1, 104.4, 104.8, 105.1, 105.4, 105.8, 106.1, 106.4, 106.8, 107.1, 107.4, 107.8, 108.1, 108.4, 108.7, 109.1, 109.4, 109.7, 110.1, 110.4, 110.7, 111.1, 111.4, 111.7, 112.1, 112.4, 112.7, 113.0, 113.4, 113.7, 114.0, 114.4, 114.7, 115.0, 115.4, 115.7, 116.0, 116.4, 116.7, 117.0, 117.3, 117.7, 118.0, 118.3, 118.7, 119.0, 119.3, 119.7, 120.0, 120.3, 120.7, 121.0, 121.3, 121.6, 122.0, 122.3, 122.6, 122.9, 123.3, 123.6, 123.9, 124.3, 124.6, 124.9, 125.3, 125.6, 125.9, 126.3, 126.6, 126.9, 127.2, 127.6, 127.9, 128.2, 128.6, 128.9, 129.2, 129.6, 129.9, 130.2, 130.5, 130.9, 131.2, 131.5, 131.9, 132.2, 132.5, 132.9, 133.2, 133.5, 133.9, 134.2, 134.5, 134.8, 135.2, 135.5, 135.8, 136.2, 136.5, 136.8, 137.2, 137.5, 137.8, 138.2, 138.5, 138.8, 139.1, 139.5, 139.8, 140.1, 140.5, 140.8, 141.1, 141.5, 141.8, 142.1, 142.5, 142.8, 143.1, 143.4, 143.8, 144.1, 144.4, 144.8, 145.1, 145.4, 145.8, 146.1, 146.4, 146.8, 147.1, 147.4, 147.7, 148.1, 148.4, 148.7, 149.0, 149.4, 149.7, 150.0, 150.4, 150.7, 151.0, 151.3, 151.7, 152.0, 152.3, 152.7, 153.0, 153.3, 153.7, 154.0, 154.3, 154.7, 155.0, 155.3, 155.7, 156.0, 156.3, 156.6, 157.0, 157.3, 157.6, 158.0, 158.3, 158.6, 158.9, 159.3, 159.6, 159.9, 160.3, 160.6, 160.9, 161.2, 161.5, 161.8, 162.1, 162.4, 162.7, 163.1, 163.4, 163.7, 164.0],
        "filename": "music/default/Serebro - Malo Tebya Hardstyle Remix.mp3",
        "duration": 165
    }
}

url = "http://127.0.0.1:5000"
data = requests.get(url, params={"action": "get music data"}).json()
music_data.update(data[0])
for i in range(data[1]):
    with open(data[0][list(data[0].keys())[i]]["filename"].replace('"', ""), "wb") as f:
        f.write(requests.get("http://127.0.0.1:5000", params={"action": "get music files", "num": i}).content)

