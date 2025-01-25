# Hand Tracking Camera using OpenCVs
This project demonstrates hand tracking using a camera and OpenCV. The application captures video from a webcam and uses computer vision techniques to detect and track hands in real-time.

## Features

- Real-time hand detection and tracking
- Visualizes hand landmarks
- Supports multiple hand tracking

## Requirements

- Python 3.x
- OpenCV
- Mediapipe

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/axeltanjung/handtracking.git
    cd handtracking
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python mediapipe
    ```

## Usage

Run the hand tracking script:
```bash
python hand_tracking.py
```

## How It Works

The application uses the Mediapipe library to detect and track hands. OpenCV is used to capture video from the webcam and display the results.

1. Capture video from the webcam.
2. Use Mediapipe to detect hands and extract landmarks.
3. Draw the landmarks and connections on the video frame.
4. Display the processed video in real-time.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [Mediapipe](https://mediapipe.dev/)
