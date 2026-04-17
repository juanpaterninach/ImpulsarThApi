#import boto3
#from ..config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET, AWS_REGION

#s3 = boto3.client(
#    "s3",
 #   aws_access_key_id=AWS_ACCESS_KEY,
 #   aws_secret_access_key=AWS_SECRET_KEY,
 #   region_name=AWS_REGION
#)

#def subir_archivo(file, nombre_archivo):

 #   s3.upload_fileobj(
  #      file,
  #      AWS_BUCKET,
  #      nombre_archivo,
  #      ExtraArgs={"ACL": "public-read"}
  #  )

#    url = f"https://{AWS_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{nombre_archivo}"

 #   return url
