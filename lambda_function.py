import json
import post_message as pm

def lambda_handler(event, context):
    pm.post_message()
