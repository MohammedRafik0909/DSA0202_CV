import cv2

video_path = 'C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/WhatsApp Video 2023-05-16 at 12.38.37 PM.mp4'
cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

output_path = 'C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/rev_video.mp4'
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

while total_frames > 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    total_frames -= 1

cap.release()
out.release()

print('Reversal complete. Reversed video saved to:', output_path)
