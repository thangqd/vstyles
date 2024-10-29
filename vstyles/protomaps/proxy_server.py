from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>')
def proxy(url):
    # Fetch the PMTiles file
    target_url = f'https://demo-bucket.protomaps.com/{url}'
    response = requests.get(target_url)

    # Create a new response object with CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    return Response(response.content, status=response.status_code, headers=headers)

if __name__ == '__main__':
    app.run(port=5000)
