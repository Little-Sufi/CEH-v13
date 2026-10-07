# Lab 04: Shodan - Internet Connected Device Search

[⬅️ Previous](Lab-03-Easy-Track-theHarvester.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Intermediate-Track-Amass.md)

---

## 🎯 Lab Objective
Find exposed infrastructure without actively scanning the target.

## 🌐 Direct Lab Access
- Shodan Website: https://www.shodan.io
- Shodan CLI Docs: https://cli.shodan.io

---

## 🛠️ Installation & Setup
```bash
# Install via pip
pip3 install shodan

# Initialize with your API key (get from https://account.shodan.io)
shodan init <YOUR_SHODAN_API_KEY>
```

---

## 📝 Command Reference

### Basic Searches
```bash
# Search by organization
shodan search "org:TargetCorp"

# Search by product
shodan search "product:Apache"

# Search by port
shodan search "port:3389"

# Search by country
shodan search "country:US"
```

### Advanced Searches
```bash
# Exposed RDP with screenshots
shodan search "port:3389 has_screenshot:true"

# Exposed CCTV cameras
shodan search "webcam"

# Exposed MongoDB
shodan search "product:MongoDB port:27017"

# Exposed Elasticsearch
shodan search "product:Elastic port:9200"

# Exposed Redis
shodan search "product:Redis port:6379"

# Exposed Jenkins
shodan search "product:Jenkins port:8080"

# Exposed SSH with weak auth
shodan search "port:22"
```

### Host Information
```bash
# Get info about specific IP
shodan host 192.168.1.10

# Save search results
shodan search --limit 100 "org:TargetCorp" > shodan_results.txt
```

---

## 🔗 Additional Resources
- Shodan Search Examples: https://www.shodan.io/search/examples
- Censys: https://censys.io
- ZoomEye: https://www.zoomeye.org

---

[⬅️ Previous](Lab-03-Easy-Track-theHarvester.md) | 
## 🧪 Hands-On Step-by-Step Exercise
1. **Querying via CLI**: Set up your Shodan API key in Kali:
   ```bash
   shodan init [YOUR_API_KEY]
   ```
2. **Search Exposed Devices**: Search for exposed industrial systems or network devices:
   ```bash
   shodan search port:502 country:"US" (Finds Modbus SCADA devices in the US)
   shodan search "default password" port:3389 (Exposed RDP systems)
   ```
3. **Filter and Export**: Export the results to a JSON file for analysis:
   ```bash
   shodan download --limit 100 target_data "port:80 os:Windows"
   ```

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Intermediate-Track-Amass.md)
