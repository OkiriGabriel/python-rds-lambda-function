import boto3  
import datetime  
import time  
import sys

db_instance='instance01'  
region='us-east-1'

def lambda_handler(event, context):  
    try: 
        date=time.strftime("-%d-%m-%Y")
        snapshot_name = db_instance+date
        source = boto3.client('rds', region_name=region)
        global db_instance
        source.delete_db_instance(DBInstanceIdentifier=db_instance,SkipFinalSnapshot=False,FinalDBSnapshotIdentifier=snapshot_name)
    except Exception as e:
        raise e
    print '[main] End'
