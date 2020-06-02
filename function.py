from subprocess import call
from google.cloud import storage
import base64

def render(request):

    envelope = request.get_json()
    if not envelope:
        msg = 'no Pub/Sub message received'
        print(f'error: {msg}')
        return f'Bad Request: {msg}', 400

    if not isinstance(envelope, dict) or 'message' not in envelope:
        msg = 'invalid Pub/Sub message format'
        print(f'error: {msg}')
        return f'Bad Request: {msg}', 400

    text = 'HELLO'
    pubsub_message = envelope['message']
    if isinstance(pubsub_message, dict) and 'data' in pubsub_message:
        text = base64.b64decode(pubsub_message['data']).decode('utf-8').strip()

    location = '/tmp/renders/'
    suffix = 'tempfile'
    filename = location + suffix + '0001.png'
    blender_file = "models/outrun.blend"

    # This script changes the text, it is run inside our 3D software. 
    blender_expression = "import bpy; bpy.data.objects['Text'].data.body = '%s'" % text
    # Render 3D image
    call('blender -b %s --python-expr "%s" -o %s%s -f 1' % (blender_file, blender_expression, location, suffix), shell=True)

    # upload file to GCS
    client = storage.Client()
    bucket = client.get_bucket('<YOUR-GCS-BUCKET>')
    blobname = text + '.png'
    blob = bucket.blob(blobname)
    blob.upload_from_filename(filename)

    #returns a public url
    return blob.public_url
