# Hindi to Telugu Learner

A modern web application to help users translate Hindi text and speech to Telugu, designed for students, professionals, and everyday users. The app features:

- Text translation from Hindi to Telugu
- Real-time speech-to-text and translation
- Category-based quick examples (Hello, Office, Food, Student)
- Beautiful, responsive UI with sidebar navigation

## Features
- Translate Hindi text to Telugu instantly
- Speak in Hindi and get Telugu translation
- Real-time translation mode for live conversations
- Example phrases for common scenarios

## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask or FastAPI recommended)

## Getting Started

### Frontend
1. Open `frontend/index.html` in your browser to use the app.
2. Customize styles in `frontend/style.css` and logic in `frontend/app.js`.

### Backend
1. Run the backend server from the `backend/app.py` file:
   ```bash
   python app.py
   ```
2. Ensure required Python packages are installed (Flask, SpeechRecognition, etc.).

### Connecting Frontend & Backend
- The frontend sends translation requests to the backend API.
- Update API endpoints in `app.js` as needed.

## Folder Structure
```
hindi-telugu-app/
  frontend/        # Main web app UI
  backend/         # Python backend API
```

## License
MIT

## Author
Made with ❤️ by the Hindi-Telugu App Team
