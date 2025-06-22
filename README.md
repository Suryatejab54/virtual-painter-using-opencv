🎨 Virtual Painter Using OpenCV and Hand Tracking
This interactive Python project transforms your webcam into a gesture-controlled drawing board. No touchscreen or stylus needed—just your fingers! Powered by OpenCV and a custom hand tracking module, this app detects hand gestures in real-time to switch tools, draw, and erase on a virtual canvas.

🛠 Features
✋ Hand Gesture Control: Use two fingers to toggle between brush and selection modes; one finger to draw.

🎨 Color Selection: Select red, green, purple, or black (eraser) by waving near virtual buttons.

🖌️ Smooth Drawing: Draw fluid strokes on a transparent canvas, with adjustable brush and eraser thickness.

📸 Canvas Blending: Overlays your art directly onto the webcam feed using masking and bitwise ops.

💾 Expandable: Add more gestures, tools, or even save your art with just a keystroke!

📂 File Structure
├── images/         # Virtual button images (top menu bar)
├── i.py            # Main Python script
├── handtracking.py # Hand detection module using Mediapipe
└── README.md       # Project documentation
▶️ Getting Started
Clone the repo:

bash
git clone https://github.com/Suryatejab54/virtual-painter-using-opencv.git
cd virtual-painter-using-opencv
Install the required libraries:

bash
pip install opencv-python mediapipe numpy
Run the project:

bash
python i.py
🔍 Suggestions for Extension
Save and load previous drawings

Add a live brush preview

Implement gesture-based brush thickness control

Integrate with a web application for shared sketching sessions
