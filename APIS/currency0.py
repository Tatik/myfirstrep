import requests

def main():
    res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR,GBP,CHF,CAD,TRY")
    if res.status_code != 200:
        raise Exception("ERROR: API isteiği başarısız.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
