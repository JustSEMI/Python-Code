import serial
import time
import subprocess
import psutil  # untuk ambil CPU usage

# PORT Arduino
PORT = "/dev/ttyUSB0"
BAUD = 9600

def get_cpu_temp():
    try:
        cpu_temp = subprocess.check_output(
            "sensors | grep 'Package id 0:' | awk '{print $4}' | tr -d '+°C'",
            shell=True
        ).decode().strip()
        return float(cpu_temp)
    except:
        return None

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)  # CPU usage %

def main():
    try:
        ser = serial.Serial(PORT, BAUD)
        time.sleep(2)

        while True:
            cpu_temp = get_cpu_temp()
            cpu_usage = get_cpu_usage()

            if cpu_temp is None:
                data = f"CPU: N/A | {cpu_usage:.1f}%"
            else:
                if cpu_temp > 80:
                    data = f"CPU: {cpu_temp:.1f}C | {cpu_usage:.1f}%"
                else:
                    data = f"CPU: {cpu_temp:.1f}C | {cpu_usage:.1f}%"

            ser.write((data + "\n").encode())
            print("Kirim:", data)

    except KeyboardInterrupt:
        print("\nProgram berhenti")
    finally:
        if "ser" in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    main()
