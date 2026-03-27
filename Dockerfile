FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt || pip install pytest aiohttp playwright pytest-asyncio pyyaml
RUN python -m playwright install chromium
CMD ["python", "toolbox.py"]
