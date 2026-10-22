from http.server import BaseHTTPRequestHandler
import json
import pandas as pd

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        
        try:
            df = pd.read_csv('Hasil_Sumatera Utara_cafe_enrich_FINAL.csv')
            data_json = df.to_dict(orient='records')
            self.wfile.write(json.dumps(data_json).encode('utf-8'))
        except Exception as e:
            error_msg = {"error": str(e)}
            self.wfile.write(json.dumps(error_msg).encode('utf-8'))
        return
