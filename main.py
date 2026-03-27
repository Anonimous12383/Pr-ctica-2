import requests 

def main():
    print("Proyecto funcionando 🚀")
    r = requests.get("https://api.github.com")
    print(r.status_code)

if __name__ == "__main__":
    main()