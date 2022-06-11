while(True):

# Detect Faces in image
    faces = rekognition.search_faces_by_image(
        CollectionId='...', Image={'Bytes':image}, ...)

    #Show name and Confidence
    for matches in faces['FaceMatches']:

        if 'ExternalImageId' in matches['Face'].keys():
            name = matches['Face']['ExternalImageId']
            confidence = matches['Face']['Confidence']

            cv2.putText(...)
