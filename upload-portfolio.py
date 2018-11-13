import boto3
from botocore.client import Config
import io
from io import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
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

    return 'Hello from Lambda!'

ß
