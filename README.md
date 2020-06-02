# Render Blender 3D scenes in the cloud (using Docker)

A simple web app that renders a [Blender](http://www.blender.org/) 3D scene with custom text.

Run with `docker run -p 8080:8080 gcr.io/as-a-service-dev/render`

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://deploy.cloud.run)

**Note:** This fork has been modified for a specifc Cloud Run demo: 
* You must send a POST request with a Cloud Pub/Sub payload
* You can't choose a Blender model, only the Outrun model is used
* Images are written to Cloud Storage instead of the HTTP response
* Replace `<YOUR-GCS-BUCKET>` with your GCS bucket name

Many thanks to the [original author](https://github.com/as-a-service/render)!

## API

### URL parameters:

* `text`: The text to render, defaults to `HELLO`.

Example: `/?text=HELLO`

## Running the server locally

* Build with `docker build . -t render`
* Start with `docker run -p 8080:8080 render`
* Open in your browser at `http://localhost:8080/?text=Hey`
