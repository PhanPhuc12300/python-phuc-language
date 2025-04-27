import math
from mpmath import mp
from decimal import Decimal, getcontext
from datetime import date
import webbrowser
import subprocess
import sys
import base64
import os
import shutil
from pathlib import Path
import time
from datetime import datetime, timedelta
import random
import itertools
import functools
from collections import Counter, defaultdict, deque
import re
import json
import csv
import unittest
import logging
import traceback
import subprocess
import platform
def he_dieu_hanh():
    he_dieu_hanh = platform.system()
    return he_dieu_hanh
def chep_anh(ten_anh):
    with open(ten_anh, 'rb') as f:
        image_data = f.read()
        encoded_data = base64.b64encode(image_data)
    with open('bansao.jpg', 'wb') as f:
        decoded_data = base64.b64decode(encoded_data)
        f.write(decoded_data)
def tao_file(ten_file, noi_dung):
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(noi_dung)
def ngau_nhien(*ds):
    ds = list(ds)
    return random.choice(ds)
def tim_pi(so_luong):
    from mpmath import mp
    import time
    mp.dps = so_luong + 1
    pi_digits_correct = str(mp.pi)[0:]
    pi_digits_correct[:so_luong+2]
    delay = 0.1 / (so_luong / 10)
    for i in pi_digits_correct[:so_luong]:
        print(str(i),end="",flush=True)
        time.sleep(delay)
    print()
def thong_tin_windows():
  if platform.system() == "Windows":
    thong_tin_chi_tiet = platform.platform()
    phien_ban_release = platform.release()
    phien_ban_don_gian = f"Windows-{phien_ban_release}"
    thong_tin_windows = {
        "thong_tin_chi_tiet": thong_tin_chi_tiet,
        "phien_ban_don_gian": phien_ban_don_gian,
        "phien_ban_release": phien_ban_release
    }
    if thong_tin_windows:
        print("Thông tin Windows tổng hợp:")
        print(f"  Thông tin chi tiết: {thong_tin_windows['thong_tin_chi_tiet']}")
        print(f"  Phiên bản đơn giản: {thong_tin_windows['phien_ban_don_gian']}")
        print(f"  Phiên bản release: {thong_tin_windows['phien_ban_release']}")
    else:
        print("Không phải hệ điều hành Windows.")
def ngay_hien_tai():
    ngay_hien_tai = datetime.today()
    ngay_format = ngay_hien_tai.strftime("%d/%m/%Y")
    return ngay_format
def ngay_le_vn():
    ngay_hom_nay = date.today()
    nam_hien_tai = ngay_hom_nay.year
    ngay_le = [
        {"ten": "Tết Dương Lịch", "ngay": f"01/01/{nam_hien_tai}"},  # 1/1
        {"ten": "Tết Nguyên Đán", "ngay": f"10/02/{nam_hien_tai}"},  # 10 tháng 2 (Tết Nguyên Đán, có thể thay đổi)
        {"ten": "Ngày Giỗ Tổ Hùng Vương", "ngay": f"10/04/{nam_hien_tai}"},  # 10 tháng 4 (Lịch dương)
        {"ten": "Ngày Lao động", "ngay": f"01/05/{nam_hien_tai}"},  # 1 tháng 5
        {"ten": "Quốc khánh", "ngay": f"02/09/{nam_hien_tai}"},  # 2 tháng 9
        {"ten": "Ngày Giải phóng miền Nam", "ngay": f"30/04/{nam_hien_tai}"},  # 30 tháng 4
        {"ten": "Tết Trung thu", "ngay": f"10/09/{nam_hien_tai}"}  # 10 tháng 9 (Tết Trung thu)
    ]
    print("Danh sách ngày lễ quan trọng ở Việt Nam:")
    for le in ngay_le:
        print(f"{le['ten']}: {le['ngay']}")
def ping():
    system_platform = platform.system().lower()
    if system_platform == "windows":
        command = ["ping", "127.0.0.1", "-n", "1"]  # Ping 1 lần
    else:
        command = ["ping", "127.0.0.1", "-c", "1"]  # Ping 1 lần
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        # print("Kết quả ping:\n", result.stdout)
        if result.returncode == 0:
            if system_platform == "windows":
                match = re.search(r'time[=<](\d+)ms', result.stdout)
                if not match:
                    match = re.search(r'Average = (\d+)ms', result.stdout)
            else:
                match = re.search(r'time=(\d+\.\d+) ms', result.stdout)
            if match:
                ping_time = float(match.group(1))
                return str(ping_time) + " ms"
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Đã xảy ra lỗi khi thực hiện ping: {e}")
def tim_file(file_name, search_path='/'):
    matches = []
    try:
        for root, dirs, files in os.walk(search_path):
            # Kiểm tra nếu tên file có trong danh sách files
            for file in files:
                if file.lower() == file_name.lower():  # So sánh không phân biệt hoa thường
                    matches.append(os.path.join(root, file))
    except PermissionError as e:
        print(f"Không có quyền truy cập vào thư mục: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    if matches:
        print("Tìm thấy file "+file_name+" ở các vị trí:")
        for match in matches:
            print(match)
    else:
        print("Không tìm thấy file.")
def cai_thu_vien(ten_thu_vien):
    try:
        __import__(ten_thu_vien)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", ten_thu_vien])
def bcnn(a, b):
    return abs(a * b) // math.gcd(a, b)
def elaina():
    print('Elaina is the main protagonist of the light novel and anime series "Wandering Witch: The Journey of Elaina". Known as the "Ashen Witch" due to her distinctive silver hair, she embarks on a journey to explore the world, inspired by her favorite childhood book. Throughout her travels, Elaina encounters diverse cultures, people, and experiences, documenting her adventures along the way. ')
    print('Elaina is portrayed as a prodigious witch who achieved her title at the young age of fifteen. Her character is multifaceted, exhibiting traits such as curiosity, wit, and a degree of narcissism. She often prefers to observe events rather than intervene directly, leading to varied perceptions among viewers regarding her actions and decisions.')
def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
try:
    with open("python-phuc.pyp") as f:
        code = f.read()
    ##############################################
    sqrt = math.sqrt
    luy_thua = math.pow
    giai_thua = math.factorial
    ucln = math.gcd
    pi, euler = math.pi, math.e
    log, sin, cos, tan = math.log, math.sin, math.cos, math.tan
    chrome = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')
    mo_web = chrome.open
    ##############################################
    code = code.replace("neu_loi","except")
    code = code.replace("ko_lam_gi","pass")
    code = code.replace("so","int")
    code = code.replace("viet(","print(")
    code = code.replace("chay","for")
    code = code.replace("trong(","in range(")
    code = code.replace("khi","while")
    code = code.replace("nhap","import")
    code = code.replace("ds","list")
    code = code.replace("xau","str")
    code = code.replace("tach(","split(")
    code = code.replace("neu","if")
    code = code.replace("con_neu","elif")
    code = code.replace("neu_ko","else")
    code = code.replace("thu:","try:")
    code = code.replace("the(","replace(")
    code = code.replace("nhap(","input(")
    code = code.replace("tao_ham","def(")
    code = code.replace("tra_ve","return")
    code = code.replace("ko","not")
    code = code.replace("va","va")
    code = code.replace("hoac","or")
    code = code.replace("dung","break")
    code = code.replace("voi","with")
    code = code.replace("bi_danh","as")
    code = code.replace("lon_nhat(","max(")
    code = code.replace("nho_nhat(","min(")
    code = code.replace("tong(","sum(")
    code = code.replace("do_dai(","len(")
    code = code.replace("tu","from")
    code = code.replace("xoa","del")
    code = code.replace("mo(","open(")
    code = code.replace("tiep_tuc","continue")
    code = code.replace("them(","append(")
    code = code.replace("noi(","join(")
    code = code.replace("ghi(","write(")
    code = code.replace("doc(","read(")
    code = code.replace("doc_hang(","read line(")
    code = code.replace("giup(","help(")
#########################################################
    exec(code)
except FileNotFoundError:
    print("Lỗi: Không thể tìm thấy file 'python-phuc.pyp'.")
except SyntaxError as e:
    print(f"Lỗi cú pháp: {e}")
except NameError as e:
    print(f"Lỗi tên biến: {e}")
except Exception as e:
    print(f"Lỗi khác: {e}")
