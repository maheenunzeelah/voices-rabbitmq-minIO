import pika
import fileuploader
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import os
import json


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

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

global val
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    val=json.loads(body)
    stri=json.dumps(val)
    print(stri)
    with open(val["path"],'r') as testfile:
         print(testfile)
         statdata = os.stat(val["path"])
         minioClient.put_object(
            'testbucket',
            val["filename"],
            testfile,
            statdata.st_size
                     )
    #    except ResponseError as err:
    #           raise



channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()