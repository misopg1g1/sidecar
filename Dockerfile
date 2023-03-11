FROM python:3.9
EXPOSE 3010
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "entrypoint:app", "--host", "0.0.0.0", "--port", "3001","--workers", "4"]
