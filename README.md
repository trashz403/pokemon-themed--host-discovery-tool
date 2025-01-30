# Jigglypuff Scanner 🎶

Jigglypuff Scanner is a fun and slightly chaotic network scanning tool that plays *Jigglypuff's* song while scanning your target network. It uses `nmap` for scanning and `pygame` for music playback, making your reconnaissance activities a little more... musical! 🎤🎶

## Features
- Plays *Jigglypuff.mp3* before starting the scan 🎵
- Supports multiple scan types using `nmap`
  - TCP SYN Scan
  - TCP ACK Ping
  - UDP Scan
  - ICMP Address Mask Request
  - ICMP Timestamp Request
  - ICMP Echo Request
  - In-depth Scan (combines multiple scans)
- Fancy colored ASCII art for aesthetic appeal ✨

## Requirements
Make sure you have the following installed:
- Python 3.x
- `pygame` (`pip install pygame`)
- `termcolor` (`pip install termcolor`)
- `nmap` (`pip install python-nmap`)
- `nmap` must be installed on your system (Linux: `sudo apt install nmap` / Windows: Install from [nmap.org](https://nmap.org/download.html))

## Usage
1. Ensure `jigglypuff.mp3` is in the same directory as the script.
2. Run the script:
   ```bash
   python jigglypuff_scanner.py
   ```
3. Enter the target IP or range (e.g., `192.168.1.0/24`).
4. Select a scan type (1-7).
5. Enjoy the music while waiting for results! 🎶

## Disclaimer
This tool is meant for educational and legal penetration testing purposes **only**. Unauthorized scanning can be illegal and unethical. Use responsibly! 🛑

## License
MIT License. Feel free to modify and share, but don't use it for malicious purposes!

---

**Author:** Niranjan M Sanil

