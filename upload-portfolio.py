import boto3
from botocore.client import Config
import io
from io import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
<<<<<<< HEAD
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:953723435519:DeployPortfolioTopic')
=======
<<<<<<< HEAD
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:953723435519:DeployPortfolioTopic')

    try:
        s3 = boto3.resource('s3') # , config=Config(signature_version='s4v4'))

        portfolio_bucket = s3.Bucket('portfolio.mabyog.com')
        build_bucket = s3.Bucket('portfoliobuild.mabyog.com')

        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)



        with zipfile.ZipFile(portfolio_zip) as myzip:
             for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={"ContentType": mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print "Job Done!"
        topic.publish(Subject="Portfolio Deployed", Message="Portfolio deployed successfully!")
    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="Portfolio deployed failed!")
        raise

    return 'Hello from Lambda!'
=======
    s3 = boto3.resource('s3') # , config=Config(signature_version='s4v4'))
>>>>>>> 519435bdee7d6ec09de6bbb2821e30a6188ce3bf


    location = {
        "bucketName": 'portfoliobuild.mabyog.com',
        "objectKey": 'portfoliobuild.zip'
    }


    try:
        job = event.get("CodePipeline.job")

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3location"]

        print "Building portfolio from " + str(location)

        s3 = boto3.resource('s3') #, config=Config(signature_version='s4v4'))

        portfolio_bucket = s3.Bucket('portfolio.mabyog.com')
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)


<<<<<<< HEAD
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')


        print "Job Done!"
        topic.publish(Subject="Portfolio Deployed", Message="Portfolio deployed successfully!")
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="Portfolio deployed failed!")
        raise

    return 'Hello from Lambda!'
=======
ß
>>>>>>> 673fa61200dbf190c50f7882138c42a28efeefd3
>>>>>>> 519435bdee7d6ec09de6bbb2821e30a6188ce3bf
