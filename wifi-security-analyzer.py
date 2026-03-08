import subprocess

networks = []


result = subprocess.run(
    ['netsh','wlan','show','network','mode=bssid'],
    capture_output=True,
    text=True
)

output =  result.stdout

lines = output.split("\n")

for line in lines:
    if "SSID" in line and "BSSID" not in line:
        parts = line.split(":")
        ssid = parts[1].strip()
    if "Authentication" in line:
        parts = line.split(":")
        auth = parts[1].strip()
    if "Signal" in line:
        parts = line.split(":")
        signal = parts[1].strip()
        
        network = {
            "ssid": ssid,
            "auth": auth,
            "signal": signal
        }


networks.append(network)

for network in networks :
    print("SSID: " , network["ssid"])
    print("Authentication: " , network["auth"])
    print("Signal: " , network["signal"])
    print("-----------------------------")
