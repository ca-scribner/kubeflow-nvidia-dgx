FROM python:3.9

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY gpu_distributed_worker.py /main.py
COPY gpu_distributed_utilities.py /gpu_distributed_utilities.py

ENTRYPOINT ["python", "/main.py"]
