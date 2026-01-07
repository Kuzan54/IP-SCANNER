import requests

ascii_art = r"""
██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║
██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║
██║██║         ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

        👤 by Kuzan54
        🌐 https://github.com/Kuzan54
"""

print(ascii_art)

ip = input("\n👉 Enter an IP address: ")

print("\n📡 Scanning IP...\n")

url = f"http://ip-api.com/json/{ip}"
response = requests.get(url)
data = response.json()

if data["status"] == "success":
    print("✅ Scan successful!\n")
    print("📌 IP Address      :", data["query"])
    print("🌍 Country         :", data["country"])
    print("🏙️ City            :", data["city"])
    print("📡 ISP             :", data["isp"])
    print("🏢 Organization    :", data["org"])
    print("🧭 Latitude        :", data["lat"])
    print("🧭 Longitude       :", data["lon"])
else:
    print("❌ Error: Invalid IP address or API issue")

print("\n🔗 GitHub: https://github.com/Kuzan54")
print("⚠️ Educational purposes only")
