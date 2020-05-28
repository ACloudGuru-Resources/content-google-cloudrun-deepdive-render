FROM python

RUN apt-get update && \
	apt-get install -y \
		blender

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask google-cloud-storage
CMD ["python", "invoker.py"]