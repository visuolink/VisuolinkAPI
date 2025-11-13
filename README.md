# 🪢 VisuoLink

A robust FastAPI-based authentication backend for the VisuoLink ecosystem. Deployed on Render using Uvicorn, this API provides secure user authentication, registration, and data management for VisuoLink's gesture-based control applications across desktop and mobile platforms.

---

## 🌐 Live API

**Interactive API Docs (Swagger):** [visuolinkapi.onrender.com/docs](https://visuolinkapi.onrender.com/docs)  
**Alternative Docs (ReDoc):** [visuolinkapi.onrender.com/redoc](https://visuolinkapi.onrender.com/redoc)

---

## 🚀 Features

- 👤 **User Management** - Registration, login, and profile management
- 🔒 **Password Security** - Bcrypt password hashing
- 📊 **PostgreSQL Database** - Reliable data persistence with SQLAlchemy ORM
- ⚡ **Fast & Async** - Asynchronous request handling with FastAPI
- 🛡️ **Input Validation** - Pydantic models for request/response validation
- 🔒 Minimal system permissions required
- 🌍 **CORS Enabled** - Cross-origin resource sharing for web/mobile clients
- 📝 **Auto-Generated Docs** - Interactive API documentation (Swagger UI & ReDoc)
- ☁️ **Cloud Deployed** - Production-ready deployment on Render

---

## 📦 Project Structure

```
VisuolinkAPI/
├── app/
│   ├── __init__.py
│   ├── main.py              
│   ├── utils.py           
│   ├── database.py          
│   ├── models.py
│   ├── schemas.py
│   ├── routers/      
├── requirements.txt    
└── README.md   
```
---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI server)
- **Database:** PostgreSQL
- **Validation:** Pydantic v2
- **ORM:** SQLAlchemy 
- **Deployment:** Render
- **IDE:** VS Code

---

## 🧪 Setup & Run Locally

1. **Clone the repository**

   ```bash
   git clone [https://github.com/visuolink/VisuolinkAPI.git]
   cd VisuolinkAPI
   ```

2. **Open in IDE(vs code)**

   - Open the project from `File > Open`

3. **Run the App**

   - Open the terminal and start the venv
   - Run Command **uvicorn main:app --reload**

---

## 🧩 Contribution

Contributions are welcome!  
If you find a bug or want to improve the app:

1. Fork this repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a Pull Request

---

## 👨‍💻 Author

- **Sumit0ubey** – [GitHub Profile](https://github.com/Sumit0ubey)

---

## 🙏 Acknowledgments

- FastAPI team for the amazing framework
- Render for reliable cloud hosting
- SQLAlchemy and Pydantic communities
- All contributors and testers

---

> 📌 **Disclaimer:**  
> This project is intended for **educational purposes only**. All content, including code and assets, is shared to help student/developers learn and grow. Any resemblance to other apps, icons, or designs is purely coincidental. Please do not use this project for commercial purposes without proper permissions.

---

## 📌 Tags

`python` `fastapi ` `api` `render` `pydantic` `uvicorn` `postgresql` `sqlalchemy`
