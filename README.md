# Hand Gesture Drag & Drop

A computer vision project that allows users to drag and drop virtual rectangles using hand gestures captured through a webcam. Built with OpenCV and CVZone for real-time hand tracking and gesture recognition.

## Features

- **Real-time Hand Tracking**: Detects and tracks hand landmarks using MediaPipe through CVZone
- **Gesture-based Interaction**: Drag rectangles by bringing index and middle fingers close together
- **Multiple Objects**: Interact with 5 draggable rectangles simultaneously
- **Visual Feedback**: Semi-transparent overlay shows draggable objects with stylized corners
- **Cross-platform Camera Support**: Robust camera initialization with fallback options

## Demo

The application creates 5 purple rectangles that can be dragged around the screen using hand gestures. When your index finger and middle finger are close together (pinch gesture), you can drag any rectangle by positioning your index finger over it.

## Requirements

### Python Dependencies

```bash
pip install opencv-python
pip install cvzone
pip install numpy
pip install mediapipe
```

### System Requirements

- Python 3.7 or higher
- Webcam or external camera
- Windows, Linux, or macOS

## Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/naakaarafr/Hand-Gesture-Drag-Drop.git
   cd Hand-Gesture-Drag-Drop
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install opencv-python cvzone numpy mediapipe
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage

1. **Start the application**: Run `python main.py`
2. **Position yourself**: Sit in front of your camera with good lighting
3. **Hand positioning**: Keep your hand visible in the camera frame
4. **Drag gesture**: 
   - Bring your index finger and middle finger close together (less than 50 pixels apart)
   - Position your index finger over any rectangle
   - Move your hand to drag the rectangle around the screen
5. **Exit**: Press 'q' to quit the application

## How It Works

### Hand Detection
- Uses CVZone's HandDetector with 80% confidence threshold
- Tracks hand landmarks in real-time using MediaPipe
- Focuses on index finger (landmark 8) and middle finger (landmark 12) positions

### Gesture Recognition
- Calculates Euclidean distance between index and middle fingertips
- Distance < 50 pixels triggers "grab" mode
- Index finger position becomes the cursor for dragging

### Object Interaction
- 5 rectangles initialized at positions: [150,150], [400,150], [650,150], [900,150], [1150,150]
- Each rectangle (200x200 pixels) can be independently dragged
- Collision detection checks if cursor is within rectangle bounds

### Visual Rendering
- Creates overlay with semi-transparent rectangles
- Uses alpha blending for smooth visual integration
- Stylized corners using CVZone's cornerRect function

## Configuration

### Adjustable Parameters

```python
# In main.py, you can modify:

# Hand detection sensitivity
detector = HandDetector(detectionCon=0.8)  # 0.5-1.0 range

# Grab threshold distance
if length < 50:  # Adjust this value (pixels)

# Rectangle size
size=[200, 200]  # [width, height] in pixels

# Rectangle color
colorR = (255, 0, 255)  # BGR color values

# Transparency
alpha = 0.5  # 0.0 (transparent) to 1.0 (opaque)
```

### Camera Settings
The application includes robust camera initialization:
- Primary: DirectShow (Windows)
- Fallback 1: Default camera
- Fallback 2: V4L2 (Linux)

## Troubleshooting

### Camera Issues
- **No camera detected**: Check if camera is connected and not used by other applications
- **Poor performance**: Ensure good lighting and clean camera lens
- **Camera permission**: Grant camera access permission to the application

### Performance Issues
- **Low FPS**: Close other camera applications, reduce system load
- **Hand detection problems**: Ensure hand is fully visible with contrasting background
- **Gesture not working**: Check finger distance threshold, ensure clear hand visibility

### Common Errors
```python
# If you get import errors:
pip install --upgrade cvzone opencv-python

# If camera fails to initialize:
# Try different camera indices (0, 1, 2...)
cap = cv2.VideoCapture(1)  # Try different numbers
```

## Project Structure

```
Hand-Gesture-Drag-Drop/
│
├── main.py              # Main application file
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── screenshots/         # Demo images (optional)
```

## Technical Details

### Libraries Used
- **OpenCV**: Computer vision and image processing
- **CVZone**: Simplified hand tracking and UI elements
- **NumPy**: Numerical operations and array handling
- **MediaPipe**: (Dependency of CVZone) Hand landmark detection

### Key Components
1. **DragRect Class**: Manages individual draggable rectangles
2. **Hand Detection Loop**: Continuous hand tracking and gesture recognition
3. **Collision Detection**: Determines rectangle-cursor interaction
4. **Visual Rendering**: Blends original camera feed with virtual objects

## Future Enhancements

- [ ] Add more gesture types (open palm, fist, etc.)
- [ ] Implement object snapping to grid
- [ ] Add color-coded rectangles
- [ ] Save/load rectangle positions
- [ ] Multi-hand support
- [ ] Touch-free menu navigation
- [ ] Object rotation with gestures

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

- Built with [CVZone](https://github.com/cvzone/cvzone) by Computer Vision Zone
- Hand tracking powered by [MediaPipe](https://mediapipe.dev/)
- Computer vision using [OpenCV](https://opencv.org/)

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the configuration options
3. Create an issue in the repository with detailed error information

---

**Note**: This project requires a working camera and adequate lighting for optimal performance. Hand gestures should be performed clearly and within the camera's field of view.
