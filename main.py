from urllib.request import Request, urlopen
import time
import argparse

REQUEST_COUNT = 10
TIMEOUT = 30

def meansure_speed(url: str) -> None:
    total_bytes = 0
    total_time = 0.0
    
    for req_number in range(1, REQUEST_COUNT + 1):
        start_time = time.perf_counter()
        
        request = Request(url=url, headers={"User-Agent": "InternetTestSpeed/1.0"})
        with urlopen(request, timeout=TIMEOUT) as res:
            data = res.read()
        
        elapsed_time = time.perf_counter() - start_time
        downloaded_bytes = len(data)
        
        total_bytes += downloaded_bytes
        total_time += elapsed_time
        
        print(
            f"Request {req_number}/{REQUEST_COUNT}: "
            f"{elapsed_time:.3f} секунд, "
            f"{downloaded_bytes / 1024:.2f} Килобайт"
        )
        average_time = total_time / REQUEST_COUNT
        total_megabytes = total_bytes / (1024 * 1024)
        speed_mbps = (total_bytes * 8) / total_time / 1_000_000
        
        print("\n---Результат---")
        print(f"Средняя скорость ответа: {average_time:.3f}")
        print(f"Скачано мегабайт: {total_megabytes:.3f}")
        print(f"Скорость интернета: {speed_mbps:.3f}")
            
def main():
    parser = argparse.ArgumentParser(
        description="Измерение скорости скачивание с использованием HTTP."
    )
    parser.add_argument("url", help="Адрес сайта для скачивания файла или страницы")
    args = parser.parse_args()
    
    try:
        meansure_speed(args.url)
    except Exception as err:
        print(f"Ошибка: {err}")

if __name__ == "__main__":
    main()