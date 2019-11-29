FROM python:3.7-stretch
COPY ./ /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD ["dbmigrate"]
CMD ["web"]
EXPOSE 3000
