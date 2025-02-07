from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def check_perfect_sum(num):
    half_num = int(num/2)
    divisor = []
    for n in range(1,half_num+1):
        if num % n == 0:
            divisor.append(n)
    if sum(divisor) == num:
        return True
    return False
    
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def check_armstrong(num):
    digits = [int(d) for d in str(num)]
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
    digits = [int(d) for d in str(num)]
    total = sum(d for d in digits)
    return total

def is_valid_integer(value: str) -> bool:
    """Check if the value is a valid integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="The number to classify")):
    
    if not is_valid_integer(number):
        return {"number": number, "error": True}
    
    number = int(number) 

    response = requests.get(f"http://numbersapi.com/{number}?json")
    response_json = response.json()
    
    json_format = {
    "number": number,
    "is_prime": False,
    "is_perfect": False,
    "properties": [],
    "digit_sum": digit_sum(number), # sum of its digits
    "fun_fact": response_json["text"]
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