$ aws rekognition starrt-face-search
--videos "S3Object={Bucket=...,Name=trainers.mp4}"
--collection-id trainers

# time passing searching

$ aws rekognition get-face-search --job-id...