FROM python:3.9.5
MAINTAINER Ashni Damaria <ashni.damaria@gmail.com>
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
ADD . /app
# Install dependencies
RUN pip install -r requirements.txt
# Expose port
ENV PORT 8080
# Run the application:
CMD ["uvicorn", "api:app", "--host", "0.0.0.0","--port","80"]
