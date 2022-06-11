
#request
$ aws rekognition create-collection
--collection-id trainers

#response
{
    "CollectionArn":"aws:rekognition:us-west-2:416159072693:collection/Trainers",
    "FaceModelVersion": "3.0",
    "StatusCode": 200
}

#Request

$ aws rekognition index-faces \
--collection-id trainers \
-- image "S3Object={Bucket=hands-on-rekognition,Name=John.jpg" \
--external-image-id Johnaws rekognition index-faces \
--collection-id Trainers \
--image "S3Object={Bucket=us-west-2-aws-training,Name=awsu-spl/spl-202/faces/John.jpg}" \
--external-image-id John

#Response = parameters
