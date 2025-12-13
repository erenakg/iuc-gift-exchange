#!/usr/bin/env python3
"""Basit script: db.sqlite3'te verilen e-posta için EmailVerification kayıtlarını ve
proje log dosyasını yazdırır. Kullanım:

  python scripts/check_email_verifications.py altan.tari@ogr.iuc.edu.tr

"""
import os
import sys
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / 'db.sqlite3'
LOG_PATH = PROJECT_ROOT / 'django-error.log'

def print_log_tail(path, lines=200):
    if not path.exists():
        print(f"Log dosyası bulunamadı: {path}")
        return
    print(f"\n--- Son {lines} satır: {path} ---\n")
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        all_lines = f.readlines()
        for l in all_lines[-lines:]:
            print(l.rstrip())

def query_verifications(db_path, email):
    if not db_path.exists():
        print(f"Veritabanı dosyası bulunamadı: {db_path}")
        return

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    q = '''
    SELECT ev.code, ev.created_at, ev.expires_at, ev.is_used, ev.ip_address, u.email
    FROM landing_emailverification ev
    JOIN auth_user u ON ev.user_id = u.id
    WHERE u.email = ?
    ORDER BY ev.created_at DESC
    '''

    cur.execute(q, (email,))
    rows = cur.fetchall()
    if not rows:
        print(f"{email} için EmailVerification kaydı bulunamadı.")
    else:
        print(f"{email} için {len(rows)} kayıt bulundu:\n")
        for r in rows:
            print(f"- code={r['code']} created_at={r['created_at']} expires_at={r['expires_at']} is_used={r['is_used']} ip={r['ip_address']}")

    conn.close()

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python scripts/check_email_verifications.py email@domain.com")
        sys.exit(1)

    email = sys.argv[1]
    print(f"Proje kökü: {PROJECT_ROOT}")
    print(f"Veritabanı: {DB_PATH}")

    query_verifications(DB_PATH, email)

    print_log_tail(LOG_PATH, lines=200)

if __name__ == '__main__':
    main()
