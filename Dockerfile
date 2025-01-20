FROM python:3.12.4-slim

ENV PROVIDER=ollama
ENV MAX_OUTPUT_TOKENS=4000
ENV TEMPERATURE=0.7
ENV INSTALL_OLLAMA=true
ENV OLLAMA_URL=http://localhost:11434
ENV OLLAMA_MODEL=llama3.2:1b
ENV OPENAI_API_KEY=
ENV OPENAI_MODEL=

WORKDIR /app

COPY requirements.txt requirements.txt
COPY /src ./src
COPY __main__.py __main__.py
COPY start.sh start.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

RUN chmod +x start.sh
CMD ["./start.sh"]


