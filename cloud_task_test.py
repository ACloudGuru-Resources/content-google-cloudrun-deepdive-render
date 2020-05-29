from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2
from sys import argv
import base64

# Create a client.
client = tasks_v2.CloudTasksClient()

project = 'acg-cloudrun'
queue = 'render2'
location = 'europe-west1'
url = 'https://render-pubsub-shsx3fvwgq-ew.a.run.app'
msg = argv[1].encode()

payload = '{"message": {"data": "' + base64.b64encode(msg).decode('utf-8') + '"}}'
converted_payload = payload.encode()

# Construct the fully qualified queue name.
parent = client.queue_path(project, location, queue)

# Construct the request body.
task = {
        'http_request': {  
            'headers': {'Content-Type': 'application/json'},
            'http_method': 'POST',
            'url': url,
            'oidc_token': {
                'service_account_email': 'testbot2@acg-cloudrun.iam.gserviceaccount.com'
            },
            'body': converted_payload
        }
}

# Use the client to build and send the task.
response = client.create_task(parent, task)

print('Created task {}'.format(response.name))
