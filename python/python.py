import time
import requests

# anlik kuru api ile cek
def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()['price'])
    else:
        print("kur degeri cekilirken hata ile karsilasildi.")
        return None

# belirtilen zaman araliginin basinda ve sonunda fiyat cekilir ve if conditionu ile yorum yazilir
def monitor_price(interval=10):
    old_price = get_btc_price()
    if old_price is None:
        return

    with open("btc_kur_log.txt", "w") as log_file:
        while True:
            time.sleep(interval)  # intervale gore sleep yapilir
            new_price = get_btc_price()
            if new_price is None:
                continue

            if new_price > old_price:
                log_entry = "Kur {} seviyesinden {} seviyesine yukseldi\n".format(old_price,new_price)
            elif new_price < old_price:
                log_entry = "Kur {} seviyesinden {} seviyesine ind\ni".format(old_price,new_price)
            else:
                log_entry = "kurda herhangi bir degisiklik olmadi {}\n".format(new_price)

            log_file.write(log_entry)
            log_file.flush()  # girdiyi output dosyasina flush eder
            old_price = new_price  # dongu devamliligi

if __name__ == "__main__":
    monitor_price()

