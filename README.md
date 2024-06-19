# Hands Up Detection Service

This project provides a FastAPI-based service that detects if both hands are above the head in an uploaded image. 

The service uses the MediaPipe Pose detection model for solving this task.
It is wrapped in a Docker container for easy deployment and testing.

**Note:** This implementation covers only the main case for detecting hands above the head. Possible edge cases are shared at the end of this document.

<br>

## Running the Application Locally

1. Create a directory for the project and navigate into it:
   ```sh
   mkdir hands_up_detection
   cd hands_up_detection
   ```

2. Clone the repository:
    ```sh
   git clone https://github.com/maryia-galetskaya/test_task_incode.git
   ```

3. Build the Docker image:
    ```sh
    docker build -t fastapi-app .
    ```

4. Run the Docker container:
    ```sh
    docker run -p 8000:8000 fastapi-app
    ```

5. The application will be available at http://127.0.0.1:8000
### Utilizing the API
You can utilize the interactive documentation provided by FastAPI to use the API.

1. Open your browser and go to http://127.0.0.1:8000/docs.
2. Use the `/detect_hands/` endpoint to upload your image and test the API.

The interactive documentation allows you to upload an image directly and see the response from the server.

<br>

## Running Tests
To run the tests inside the Docker container:

1. Ensure the Docker image is built:
    ```sh
    docker build -t fastapi-app .
    ```

2. Run the tests:
    ```sh
    docker run --rm -v $(pwd):/app fastapi-app pytest
    ```

<br>
<br>

## Edge Cases

Here are some possible edge cases not covered by the current implementation:

1. Images with multiple people.
2. Images where some objects obscure the main landmarks.
3. Images with poor lighting or low resolution.
4. Images that are flipped or turned 90 degrees.
5. Images where the head is tilted 90 degrees.
6. Images taken from different perspectives (e.g., from the side or back).

These edge cases require additional handling and are not included in the basic implementation provided.