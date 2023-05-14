from trolleybus import Trolleybus

if __name__ == "__main__":    trolleybuses = [
    Trolleybus(), Trolleybus(100, 45, "Naukova", 50, 21, 13),
    Trolleybus.getInstance(), Trolleybus.getInstance()
]
for trolleybus in trolleybuses:
    print(trolleybus)
