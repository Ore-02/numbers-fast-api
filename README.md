# Number Classification API

## 📌 Overview
This is a FastAPI-based API that takes a number as input and returns interesting mathematical properties about it, along with a fun fact retrieved from the [Numbers API](http://numbersapi.com/).

## 🚀 Features
- Determines if the number is **prime**.
- Checks if the number is **perfect**.
- Identifies if the number is an **Armstrong number**.
- Classifies the number as **odd** or **even**.
- Computes the **sum of its digits**.
- Retrieves a **fun fact** about the number.
- Returns responses in **JSON format**.
- Handles **invalid inputs** with appropriate HTTP status codes.
- Supports **CORS (Cross-Origin Resource Sharing)**.

## 📡 API Endpoint
### **GET /api/classify-number?number=371**
#### ✅ **Success Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### ❌ **Error Response (400 Bad Request)**
```json
{
    "number": "invalid",
    "error": true,
    "message": "Invalid input. Please enter a valid integer."
}
```

## 🛠️ Tech Stack
- **FastAPI** (Python framework for building APIs)
- **Uvicorn** (ASGI server for running FastAPI)
- **Requests** (For fetching data from Numbers API)
- **Git & GitHub** (Version control & repository hosting)
- **AWS EC2** (For deployment)

## 🛠️ Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/Ore-02/numbers-fast-api.git
cd numbers-fast-api
```

### 2️⃣ **Set Up a Virtual Environment**
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the API Locally**
```sh
uvicorn main:app --reload
```

## 🌍 Deployment to AWS EC2
To deploy this API to an EC2 instance:
1. **Launch an Ubuntu EC2 instance**
2. **Install dependencies on the instance**
3. **Run the FastAPI app with Uvicorn**
4. **Configure a reverse proxy (e.g., Nginx)**
5. **Set up a domain or use the public IP**
6. **Ensure the API is accessible via a public URL**

## 📖 License
This project is open-source and available under the [MIT License](LICENSE).

## 🙌 Acknowledgments
- **FastAPI** for making API development fast and easy.
- **Numbers API** for providing fun facts about numbers.

## 📞 Contact
For any questions, feel free to reach out:
- GitHub: [Ore-02](https://github.com/Ore-02)
- Email: ayandeleoluwafemi@gmail.com

