from fastapi.testclient import TestClient
import app
client = TestClient(app.app)
health = client.get('/health')
assert health.status_code == 200 and health.json()['ok'] is True
page = client.get('/')
assert page.status_code == 200 and 'AI Video Studio' in page.text
print('OK: health endpoint and mobile web page are available.')
if not health.json()['ffmpeg']:
    print('WARNING: FFmpeg not found; MP4 export requires FFmpeg.')
