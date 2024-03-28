from django.shortcuts import render
from django.http import JsonResponse
import cv2
import numpy as np
from pyzbar.pyzbar import decode 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

def index(request):
    return render(request, 'index.html')


def gen_frames():
    global scanning
    cap = cv2.VideoCapture(0)
    scanning = False
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            if scanning:
                decoded_objects = decode(frame)
                for obj in decoded_objects:
                    # Draw a rectangle around the barcode
                    (x, y, w, h) = obj.rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Extract barcode data
                    barcode_data = obj.data.decode("utf-8")
                    print(barcode_data)  # Print barcode data to the console
            ret, buffer = cv2.imencode('.jpg', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@gzip.gzip_page
def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')



def start_scan(request):
    global scanning
    scanning = True
    return HttpResponse('Barcode scanning started.')

def stop_scan(request):
    global scanning
    scanning = False
    return HttpResponse('Barcode scanning stopped.')

def scan(request):

    return render(request , 'scan.html')