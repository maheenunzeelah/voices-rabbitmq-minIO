from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import os
# from audioReceiver import val
# Initialize minioClient with an endpoint and access/secret keys.
def getMinioClient(access,secret):
       return Minio(
              'localhost:9000',
              access_key=access,
              secret_key=secret,
              secure=False
       )

if __name__=='__main__':
       minioClient = getMinioClient('MaheenUnzeelah','Cryptography')
     
       if(not minioClient.bucket_exists('testbucket')):
              try:
                     minioClient.make_bucket('testbucket')
              except ResponseError as err:
                     raise

       #Adding files in the bucket
       try:
              with open(val,'rb') as testfile:
                     print(val)
                     statdata = os.stat(val)
                     minioClient.put_object(
                            'testbucket',
                            'audio.wav',
                            testfile,
                            statdata.st_size
                     )
       except ResponseError as err:
              raise