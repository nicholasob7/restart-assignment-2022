Timestamps:
[99800, 99840, 100000, 100040, ...]

Convert into individual scene start/end times:
[(99800, 101480), (127520, 131760), ...]

Convert into clips for Amazon Elastic Transcoder:
[
    {'Key': 'trainers.mp4',
    'TimeSpan': {'StartTime': '99.8', 'Duration': '1.68'}},
    {'Key': 'trainers.mp4',
    'TimeSpan'}: {'StartTime': '127.52', 'Duration': '4.24}},
    ...
]