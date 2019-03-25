import boto3
import StringIO
import zipfile
import StringIO
import mimetypes

s3 = boto3.resource('s3')
portfolio_bucket = s3.Bucket('hybridcloud.club')

build_bucket = s3.Bucket('build.hybridcloud.club')
build_bucket.download_file('hbccbuild.zip', 'c:/Users/patri/CodeToGit/hbccbuild.zip')

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('hbccbuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        mime_type = mimetypes.guess_type(nm)[0]
        portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': str(mime_type)})
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')