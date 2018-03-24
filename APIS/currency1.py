import requests

def main():
    res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR,GBP,CHF,CAD,TRY")
    if res.status_code != 200:
        raise Exception("ERROR: API isteiği başarısız.")
    data = res.json()
    base = data["base"]
    rate_EUR = data["rates"]["EUR"]
    rate_CHF = data["rates"]["CHF"]
    rate_CAD = data["rates"]["CAD"]
    rate_TRY = data["rates"]["TRY"]
    print(f"1 {base} is equal to {rate_EUR} EUR")
    print()
    print(f"1 {base} is equal to {rate_CHF} CHF")
    print()
    print(f"1 {base} is equal to {rate_CAD} CAD")
    print()
    print(f"1 {base} is equal to {rate_TRY} TRY")
    print()


if __name__ == "__main__":
    main()
