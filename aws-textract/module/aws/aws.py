import os
import boto3
import trp

class aws:

    def sessionAWS(awsProfile, awsRegion):
        session = boto3.Session(profile_name=awsProfile, region_name=awsRegion)
        return session
    

    def awsTextract(awsProfile, awsRegion, bucketName, formImage):

        session = aws.sessionAWS(awsProfile, awsRegion)
        textractmodule = session.client('textract')
        
        response = textractmodule.analyze_document(
            Document={
                'S3Object': {
                    'Bucket': bucketName,
                    'Name': formImage
                }   
            },
            FeatureTypes=["FORMS"]
        )

        # print(response)
        doc = trp.Document(response)
        print ('------------- Print Form detected text ------------------------------')
        for page in doc.pages:
            for field in page.form.fields:
                print("Key: {}, Value: {}".format(field.key, field.value))