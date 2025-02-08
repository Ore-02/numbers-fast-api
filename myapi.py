from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def check_perfect_sum(num):
    if num <= 0:
        return False 
    half_num = num // 2
    divisor = [n for n in range(1, half_num + 1) if num % n == 0]
    return sum(divisor) == num
    
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def check_armstrong(num):
    digits = [int(d) for d in str(abs(num))]
    power = len(digits)
    total = sum(d ** power for d in digits)
    if total == num:
           return True
    return False

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

def digit_sum(num):
    digits = [int(d) for d in str(abs(num))]
    total = sum(d for d in digits)
    return total

@app.get("/api/classify-number")
async def classify_number(number: str):
    
    try:
        num = float(number)  # Convert to float first
        if num != int(num):  # If it's a float, return error
            return {"number": number,"error": True},400
        num = int(num)  # Convert safely to integer
    except ValueError:
        return {"number": number,"error": True},400

    try:
        response = requests.get(f"http://numbersapi.com/{num}?json")
        response_json = response.json()
        fun_fact = response_json.get("text", "No fact available.")
    except Exception:
        fun_fact = "No fact available."
    
    json_format = {
    "number": number,
    "is_prime": False,
    "is_perfect": False,
    "properties": [],
    "digit_sum": digit_sum(number), # sum of its digits
    "fun_fact": fun_fact
    }
    
    if check_perfect_sum(number) is True:
        json_format["is_perfect"] = True
    
    if check_prime(number) is True:
        json_format["is_prime"] = True
        
    if check_armstrong(number) is True:
        json_format["properties"].append("armstrong")
    
    if is_odd(number) is True:
        json_format["properties"].append("odd")
    else:
        json_format["properties"].append("even")

    
    return json_format