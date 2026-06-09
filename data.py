# data.py

# ==========================================
# DỮ LIỆU APP 03: CHECKLIST HỆ THỐNG MỚI
# ==========================================
CHECKLIST_DATA = {
    "Linux Ubuntu 24.04": [
        {"danh_muc": "1. Cấu hình cơ bản", "items": [
            {"stt": "1", "muc": "Cập nhật kernel", "cmd": "sudo apt update && sudo apt upgrade -y ( lưu ý: Override local changes to /etc/pam.d/common-*? [yes/no] no)", "row_idx": 5},
            {"stt": "2", "muc": "Kiểm tra hostname", "cmd": "hostname -f", "row_idx": 6},
            {"stt": "3", "muc": "Kiểm tra IP tĩnh", "cmd": "ip -br a", "row_idx": 7},
            {"stt": "4", "muc": "Default Gateway và DNS (10.31.100.30) được cấu hình chính xác.", "cmd": "ip route; nslookup google.com", "row_idx": 8},
            {"stt": "5", "muc": "Hostname đã được khai báo trong file /etc/hosts.", "cmd": "cat /etc/hosts", "row_idx": 9},
            {"stt": "6", "muc": "Hệ điều hành đã được cập nhật đầy đủ các package.", "cmd": "apt list --upgradable", "row_idx": 10},
            
        ]},
        {"danh_muc": "2. SSH Hardening", "items": [
            {"stt": "7", "muc": "Tạo một file cấu hình cho /run/sshd", "cmd": "sudo echo \"d /run/sshd 0755 root root -\" | sudo tee /etc/tmpfiles.d/sshd.conf", "row_idx": 12},
            {"stt": "8", "muc": "Kiểm tra sshd (Nếu lỗi chạy tiếp lệnh thứ 2)", "cmd": "sudo sshd -t,\nsystemd-tmpfiles --create /etc/tmpfiles.d/sshd.conf", "row_idx": 13},
            {"stt": "9", "muc": "PermitRootLogin = no", "cmd": "grep PermitRootLogin /etc/ssh/sshd_config", "row_idx": 14},
            {"stt": "10", "muc": "MaxAuthTries = 4", "cmd": "grep MaxAuthTries /etc/ssh/sshd_config", "row_idx": 15},
            {"stt": "11", "muc": "LoginGraceTime = 60", "cmd": "grep LoginGraceTime /etc/ssh/sshd_config", "row_idx": 16},
            {"stt": "12", "muc": "X11Forwarding = no", "cmd": "grep X11Forwarding /etc/ssh/sshd_config", "row_idx": 17},
            {"stt": "13", "muc": "AllowAgentForwarding = no", "cmd": "grep AllowAgentForwarding /etc/ssh/sshd_config", "row_idx": 18},
            {"stt": "14", "muc": "MaxSessions = 3", "cmd": "grep MaxSessions /etc/ssh/sshd_config", "row_idx": 19},
            {"stt": "15", "muc": "Chỉ sử dụng các Cipher và Key Exchange (KEX) Algorithm mạnh", "cmd": "grep -E 'KexAlgorithms|Ciphers|MACs' /etc/ssh/sshd_config", "row_idx": 20},          
            {"stt": "16", "muc": "PermitEmptyPasswords = no", "cmd": "grep PermitEmptyPasswords /etc/ssh/sshd_config", "row_idx": 21},
            {"stt": "17", "muc": "UsePAM = yes", "cmd": "grep 'UsePAM' /etc/ssh/sshd_config", "row_idx": 22},
            {"stt": "18", "muc": "GSSAPIAuthentication = no", "cmd": "grep GSSAPIAuthentication /etc/ssh/sshd_config", "row_idx": 23},
            {"stt": "19", "muc": "HostbasedAuthentication = no / IgnoreRhosts = yes", "cmd": "grep -E 'HostbasedAuthentication|IgnoreRhosts' /etc/ssh/sshd_config", "row_idx": 24},
            {"stt": "20", "muc": "LogLevel = VERBOSE", "cmd": "grep LogLevel /etc/ssh/sshd_config", "row_idx": 25},
            {"stt": "21", "muc": "MaxStartups = 10:30:60", "cmd": "grep MaxStartups /etc/ssh/sshd_config", "row_idx": 26},
            {"stt": "22", "muc": "ClientAliveInterval = 900", "cmd": "grep -E 'ClientAliveInterval|ClientAliveCountMax' /etc/ssh/sshd_config", "row_idx": 27},
            {"stt": "23", "muc": "Cấu hình SSH đã được kiểm tra cú pháp (syntax check)", "cmd": "sudo sshd -t", "row_idx": 28},
            
        ]},
        {"danh_muc": "3. Password Policy", "items": [
            {"stt": "24", "muc": "minlen = 14 trong pwquality.conf", "cmd": "grep minlen /etc/security/pwquality.conf", "row_idx": 30},
            {"stt": "25", "muc": "Chính sách mật khẩu yêu cầu ký tự hoa, thường, số, đặc biệt.", "cmd": "grep -E 'dcredit|ucredit|ocredit|lcredit' /etc/security/pwquality.conf", "row_idx": 31},
            {"stt": "26", "muc": "Lưu lịch sử 5 mật khẩu gần nhất bằng pam_pwhistory", "cmd": "grep pam_pwhistory /etc/pam.d/common-password", "row_idx": 32},
            {"stt": "27", "muc": "Mật khẩu được lưu trữ bằng thuật toán băm SHA-512.", "cmd": "grep sha512 /etc/pam.d/common-password", "row_idx": 33},
            {"stt": "28", "muc": "pwquality.conf: difok=2, maxrepeat=3, maxsequence=3, dictcheck=1", "cmd": "grep -E 'difok|maxrepeat|maxsequence|dictcheck' /etc/security/pwquality.conf", "row_idx": 34},
            {"stt": "29", "muc": "faillock.conf: deny=5, unlock_time=900 (15 phút)", "cmd": "grep -E 'deny|unlock_time' /etc/security/faillock.conf", "row_idx": 35},
            {"stt": "30", "muc": "faillock.conf: even_deny_root", "cmd": "grep 'even_deny_root' /etc/security/faillock.conf", "row_idx": 36},
        ]},
        {"danh_muc": "4. Xác thực RADIUS", "items": [
            {"stt": "31", "muc": "Máy chủ RADIUS được cấu hình chính xác", "cmd": "cat /etc/pam_radius_auth.conf", "row_idx": 38},
            {"stt": "32", "muc": "PAM common-auth được cấu hình theo đúng thứ tự xác thực", "cmd": "cat /etc/pam.d/common-auth", "row_idx": 39},
            {"stt": "33", "muc": "Tham số KbdInteractiveAuthentication = yes", "cmd": "grep KbdInteractiveAuthentication /etc/ssh/sshd_config", "row_idx": 40},
            {"stt": "34", "muc": "Kiểm tra đăng nhập bằng tài khoản RADIUS thành công.", "cmd": "Thử SSH bang user RADIUS", "row_idx": 41},
        ]},
        {"danh_muc": "5. Firewall (Iptables)", "items": [
            {"stt": "35", "muc": "iptables đang hoạt động với các rule được cấu hình đúng", "cmd": "sudo iptables -L -n -v", "row_idx": 43},
            {"stt": "36", "muc": "INPUT default policy là ACCEPT, có rule reject ở cuối", "cmd": "sudo iptables -L INPUT -n | tail -5", "row_idx": 44},
            {"stt": "37", "muc": "FORWARD default DROP", "cmd": "sudo iptables -L FORWARD -n | tail -3", "row_idx": 45},
            {"stt": "38", "muc": "SSH chỉ được phép từ VPN range và system terminal", "cmd": "sudo iptables -L INPUT -n | grep 10.31.100.18", "row_idx": 46},
            {"stt": "39", "muc": "Port 9100 chỉ được phép từ Prometheus Server", "cmd": "sudo iptables -L INPUT -n | grep 9100", "row_idx": 47},
            {"stt": "40", "muc": "iptables-persistent hoạt động, rule được giữ sau reboot", "cmd": "sudo systemctl status netfilter-persistent", "row_idx": 48},
        ]},
        {"danh_muc": "6. Fail2ban", "items": [
            {"stt": "41", "muc": "Dịch vụ fail2ban đang chạy và hoạt động bình thường.", "cmd": "sudo systemctl status fail2ban", "row_idx": 50},
            {"stt": "42", "muc": "Jail SSH được kích hoạt (bantime=3600, maxretry=4).", "cmd": "sudo fail2ban-client status sshd", "row_idx": 51},
            {"stt": "43", "muc": "Danh sách ignoreip đã bao gồm IP system terminal", "cmd": "sudo fail2ban-client get sshd ignoreip", "row_idx": 52},
        ]},
        {"danh_muc": "7. NTP", "items": [
            {"stt": "44", "muc": "NTP Server được cấu hình là ntp.vngdc.local", "cmd": "cat /etc/systemd/timesyncd.conf", "row_idx": 54},
            {"stt": "45", "muc": "NTP đang đồng bộ thành công", "cmd": "timedatectl timesync-status", "row_idx": 55},
            {"stt": "46", "muc": "Timezone được cấu hình là Asia/Ho_Chi_Minh", "cmd": "timedatectl | grep zone", "row_idx": 56},
        ]},
        {"danh_muc": "8. Logging & Monitoring", "items": [
            {"stt": "47", "muc": "rsyslog được cấu hình để forward log về Syslog Server", "cmd": "grep syslog.vngdc.local /etc/rsyslog.conf", "row_idx": 58},
            {"stt": "48", "muc": "Thư mục lưu log của máy chủ tồn tại trên Syslog Server", "cmd": "Kiểm tra trên syslog server 10.31.100.20", "row_idx": 59},
            {"stt": "49", "muc": "Wazuh agent đang hoạt động", "cmd": "systemctl status wazuh-agent", "row_idx": 60},
            {"stt": "50", "muc": "node_exporter đang hoạt động và phản hồi /metrics", "cmd": "curl http://localhost:9100/metrics | head -5", "row_idx": 61},
            {"stt": "51", "muc": "Target hiển thị trạng thái Healthy/UP trên Prometheus", "cmd": "Kiểm tra trên Prometheus UI", "row_idx": 62},
        ]},
        {"danh_muc": "9. Dịch vụ không cần thiết", "items": [
            {"stt": "52", "muc": "ModemManager disabled", "cmd": "systemctl is-enabled ModemManager", "row_idx": 64},
            {"stt": "53", "muc": "thermald disabled", "cmd": "systemctl is-enabled thermald", "row_idx": 65},
            {"stt": "54", "muc": "apport disabled", "cmd": "systemctl is-enabled apport", "row_idx": 66},
        ]},
        {"danh_muc": "10. Crontab va Scripts", "items": [
            {"stt": "55", "muc": "Script backup_iptables.sh tồn tại", "cmd": "ls -la /opt/dc_script/backup_iptables.sh", "row_idx": 68},
            {"stt": "56", "muc": "Script free_mem.sh tồn tại", "cmd": "ls -la /opt/dc_script/free_mem.sh", "row_idx": 69},
            {"stt": "57", "muc": "Crontab entries có (netfilter-persist, free_mem, clear audit)", "cmd": "sudo cat /etc/crontab", "row_idx": 70},
            {"stt": "58", "muc": "Iptables.save tồn tại và áp dụng các rule", "cmd": "sudo iptables-save", "row_idx": 71},
        ]},
        {"danh_muc": "11. Sudo Hardening", "items": [
            {"stt": "59", "muc": "Defaults use_pty", "cmd": "sudo grep 'use_pty' /etc/sudoers /etc/sudoers.d/ 2>/dev/null", "row_idx": 73},
            {"stt": "60", "muc": "Defaults logfile=/var/log/sudo.log", "cmd": "sudo grep 'logfile' /etc/sudoers /etc/sudoers.d/ 2>/dev/null", "row_idx": 74},
            {"stt": "61", "muc": "Không có NOPASSWD trong sudoers", "cmd": "sudo grep -rP 'NOPASSWD' /etc/sudoers /etc/sudoers.d/ 2>/dev/null | wc -l", "row_idx": 75},
        ]},
        {"danh_muc": "12. File Permissions", "items": [
            {"stt": "62", "muc": "/etc/shadow và /etc/gshadow: permissions = 640, owner = root:shadow", "cmd": "stat -c '%n %a %U:%G' /etc/shadow /etc/gshadow", "row_idx": 77},
            {"stt": "63", "muc": "/etc/passwd và /etc/group: permissions = 644, owner = root:root", "cmd": "stat -c '%n %a %U:%G' /etc/passwd /etc/group", "row_idx": 78},
            {"stt": "64", "muc": "/etc/security/opasswd: permissions = 600", "cmd": "stat -c '%n %a %U:%G' /etc/security/opasswd 2>/dev/null || echo 'file not exist'", "row_idx": 79},
        ]},
    ],
    
    "Windows Server 2022": [
        {"danh_muc": "1. Cấu hình cơ bản", "items": [
            {"stt": "1", "muc": "Hostname đúng quy ước đặt tên", "cmd": "hostname", "row_idx": 5},
            {"stt": "2", "muc": "IP tĩnh đã được cấu hình", "cmd": "Get-NetIPConfiguration", "row_idx": 6},
            {"stt": "3", "muc": "DNS server được cấu hình chính xác", "cmd": "Get-DnsClientServerAddress -AddressFamily IPv4", "row_idx": 7},
            {"stt": "4", "muc": "Timezone = SE Asia Standard Time (UTC+7)", "cmd": "Get-TimeZone", "row_idx": 8},
            {"stt": "5", "muc": "Windows Update đầy đủ, không còn bản cập nhật đang chờ", "cmd": "Get-WindowsUpdate", "row_idx": 9},
            {"stt": "6", "muc": "VMware Tools / QEMU Guest Agent đang chạy", "cmd": "Get-Service VMTools", "row_idx": 10},
        ]},
        {"danh_muc": "2. Password & Lockout Policy", "items": [
            {"stt": "7", "muc": "Độ dài mật khẩu tối thiểu = 14 ký tự", "cmd": "net accounts | findstr /i minimum", "row_idx": 12},
            {"stt": "8", "muc": "Chính sách độ phức tạp mật khẩu đang bật", "cmd": "net accounts hoặc secpol.msc", "row_idx": 13},
            {"stt": "9", "muc": "Lịch sử mật khẩu lưu tối thiểu 5 lần gần nhất", "cmd": "net accounts | findstr /i history", "row_idx": 14},
            {"stt": "10", "muc": "Thời hạn mật khẩu tối đa = 90 ngày", "cmd": "net accounts | findstr /i maximum", "row_idx": 15},
            {"stt": "11", "muc": "Ngưỡng khoá tài khoản = 5 lần đăng nhập sai", "cmd": "net accounts | findstr /i threshold", "row_idx": 16},
            {"stt": "12", "muc": "Thời gian khoá tài khoản ≥ 30 phút", "cmd": "net accounts | findstr /i duration", "row_idx": 17},
        ]},
        {"danh_muc": "3. Windows Firewall", "items": [
            {"stt": "13", "muc": "Windows Firewall – profile Domain đang bật", "cmd": "Get-NetFirewallProfile", "row_idx": 19},
            {"stt": "14", "muc": "Windows Firewall – profile Private đang bật", "cmd": "Get-NetFirewallProfile", "row_idx": 20},
            {"stt": "15", "muc": "Windows Firewall – profile Public đang bật", "cmd": "Get-NetFirewallProfile", "row_idx": 21},
        ]},
        {"danh_muc": "4. TLS & Protocol", "items": [
            {"stt": "16", "muc": "SSL 2.0 đã bị vô hiệu hoá hoàn toàn", "cmd": "Kiểm tra registry SCHANNEL Protocols", "row_idx": 23},
            {"stt": "17", "muc": "SSL 3.0 đã bị vô hiệu hoá hoàn toàn", "cmd": "Kiểm tra registry SCHANNEL Protocols", "row_idx": 24},
            {"stt": "18", "muc": "TLS 1.0 đã bị vô hiệu hoá hoàn toàn", "cmd": "Kiểm tra registry SCHANNEL Protocols", "row_idx": 25},
            {"stt": "19", "muc": "TLS 1.1 đã bị vô hiệu hoá hoàn toàn", "cmd": "Kiểm tra registry SCHANNEL Protocols", "row_idx": 26},
            {"stt": "20", "muc": "TLS 1.2 đang được bật", "cmd": "Kiểm tra registry SCHANNEL Protocols", "row_idx": 27},
            {"stt": "21", "muc": "SMBv1 đã bị tắt hoàn toàn", "cmd": "(Get-SmbServerConfiguration).EnableSMB1Protocol", "row_idx": 28},
            {"stt": "22", "muc": "SMBv2/v3 vẫn đang bật", "cmd": "(Get-SmbServerConfiguration).EnableSMB2Protocol", "row_idx": 29},
        ]},
        {"danh_muc": "5. Security Features", "items": [
            {"stt": "23", "muc": "UAC đang bật (EnableLUA = 1)", "cmd": "Kiểm tra registry EnableLUA", "row_idx": 31},
            {"stt": "24", "muc": "Tài khoản Guest đã bị vô hiệu hoá", "cmd": "Get-LocalUser Guest", "row_idx": 32},
            {"stt": "25", "muc": "AutoRun và AutoPlay đã bị tắt hoàn toàn", "cmd": "Kiểm tra registry NoDriveTypeAutoRun", "row_idx": 33},
            {"stt": "26", "muc": "Windows Defender Antivirus đang bật", "cmd": "Get-MpComputerStatus", "row_idx": 34},
        ]},
        {"danh_muc": "6. Audit & Logging", "items": [
            {"stt": "27", "muc": "Audit Logon/Logoff = Success + Failure", "cmd": "auditpol /get /category:Logon/Logoff", "row_idx": 36},
            {"stt": "28", "muc": "Audit Account Logon = Success + Failure", "cmd": "auditpol /get /category:Account Logon", "row_idx": 37},
            {"stt": "29", "muc": "Audit Account Management = Success", "cmd": "auditpol /get /category:Account Management", "row_idx": 38},
            {"stt": "30", "muc": "Audit Policy Change = Success", "cmd": "auditpol /get /category:Policy Change", "row_idx": 39},
            {"stt": "31", "muc": "Audit System Events = Success + Failure", "cmd": "auditpol /get /category:System", "row_idx": 40},
            {"stt": "32", "muc": "PowerShell Module Logging đang bật", "cmd": "Kiểm tra registry EnableModuleLogging", "row_idx": 41},
            {"stt": "33", "muc": "PowerShell ScriptBlock Logging đang bật", "cmd": "Kiểm tra registry EnableScriptBlockLogging", "row_idx": 42},
            {"stt": "34", "muc": "Kích thước Security Event Log ≥ 1 GB", "cmd": "wevtutil gl Security", "row_idx": 43},
        ]},
        {"danh_muc": "7. Logging & Monitoring", "items": [
            {"stt": "35", "muc": "Dịch vụ NXLog đang chạy và forward log", "cmd": "Get-Service nxlog", "row_idx": 45},
            {"stt": "36", "muc": "Wazuh Agent đang hoạt động", "cmd": "Get-Service WazuhSvc", "row_idx": 46},
            {"stt": "37", "muc": "Windows Exporter đang lắng nghe trên port 9182", "cmd": "Get-NetTCPConnection -LocalPort 9182", "row_idx": 47},
            {"stt": "38", "muc": "Target hiển thị trạng thái UP trên Prometheus", "cmd": "Kiểm tra trên Prometheus UI", "row_idx": 48},
        ]},
        {"danh_muc": "8. RDP Configuration", "items": [
            {"stt": "39", "muc": "RDP bật và yêu cầu NLA", "cmd": "Kiểm tra registry fDenyTSConnections", "row_idx": 50},
            {"stt": "40", "muc": "RDP đang dùng port không mặc định (4095)", "cmd": "Get-NetTCPConnection -LocalPort 4095", "row_idx": 51},
        ]},
        {"danh_muc": "9. NTP", "items": [
            {"stt": "41", "muc": "NTP Server được đồng bộ về server nội bộ", "cmd": "w32tm /query /source", "row_idx": 53},
            {"stt": "42", "muc": "Thời gian chính xác (sai lệch < 5 phút)", "cmd": "w32tm /resync /force", "row_idx": 54},
        ]},
    ],
    
    "Juniper JunOS": [
        {"danh_muc": "1. Cấu hình cơ bản", "items": [
            {"stt": "1", "muc": "Hostname đúng quy ước đặt tên", "cmd": "show system host-name", "row_idx": 5},
            {"stt": "2", "muc": "Management IP được cấu hình chính xác", "cmd": "show interfaces me0 | grep inet", "row_idx": 6},
            {"stt": "3", "muc": "Login banner cảnh báo đã được cấu hình", "cmd": "show system login message", "row_idx": 7},
            {"stt": "4", "muc": "Phiên bản JunOS phù hợp", "cmd": "show version", "row_idx": 8},
        ]},
        {"danh_muc": "2. Xác thực & Tài khoản", "items": [
            {"stt": "5", "muc": "RADIUS Server được cấu hình chính xác", "cmd": "show system radius-server", "row_idx": 10},
            {"stt": "6", "muc": "Thứ tự xác thực đúng: RADIUS → Local password", "cmd": "show system authentication-order", "row_idx": 11},
            {"stt": "7", "muc": "Tài khoản local admin tồn tại", "cmd": "show system login user", "row_idx": 12},
            {"stt": "8", "muc": "Kiểm tra đăng nhập bằng RADIUS thành công", "cmd": "Thử SSH bằng user RADIUS", "row_idx": 13},
            {"stt": "9", "muc": "Idle timeout được cấu hình = 15 phút", "cmd": "show system login idle-timeout", "row_idx": 14},
        ]},
        {"danh_muc": "3. Chính sách mật khẩu", "items": [
            {"stt": "10", "muc": "Độ dài mật khẩu tối thiểu = 14 ký tự", "cmd": "show system login password minimum-length", "row_idx": 16},
            {"stt": "11", "muc": "Cấu hình lockout sau 5 lần sai, khoá 30 phút", "cmd": "show system login retry-options", "row_idx": 17},
        ]},
        {"danh_muc": "4. SSH & Quản trị từ xa", "items": [
            {"stt": "12", "muc": "Telnet đã bị vô hiệu hoá hoàn toàn", "cmd": "show system services", "row_idx": 19},
            {"stt": "13", "muc": "FTP đã bị vô hiệu hoá hoàn toàn", "cmd": "show system services", "row_idx": 20},
            {"stt": "14", "muc": "SSH chỉ sử dụng protocol version 2", "cmd": "show system services ssh | grep protocol", "row_idx": 21},
            {"stt": "15", "muc": "Root login qua SSH bị từ chối", "cmd": "show system services ssh | grep root-login", "row_idx": 22},
            {"stt": "16", "muc": "Firewall filter MGMT-ACCESS trên me0", "cmd": "show interfaces me0 | grep filter", "row_idx": 23},
        ]},
        {"danh_muc": "5. Bảo vệ Control Plane", "items": [
            {"stt": "17", "muc": "Firewall filter PROTECT-RE áp dụng trên lo0", "cmd": "show interfaces lo0 | grep filter", "row_idx": 25},
            {"stt": "18", "muc": "Nội dung filter PROTECT-RE định nghĩa đúng", "cmd": "show firewall filter PROTECT-RE", "row_idx": 26},
        ]},
        {"danh_muc": "6. NTP", "items": [
            {"stt": "19", "muc": "NTP Server trỏ về server nội bộ", "cmd": "show ntp associations", "row_idx": 28},
            {"stt": "20", "muc": "NTP đang đồng bộ thành công", "cmd": "show system uptime | grep clock", "row_idx": 29},
            {"stt": "21", "muc": "Timezone được cấu hình là Asia/Ho_Chi_Minh", "cmd": "show system time-zone", "row_idx": 30},
        ]},
        {"danh_muc": "7. Syslog", "items": [
            {"stt": "22", "muc": "Log được forward về Syslog Server tập trung", "cmd": "show system syslog host", "row_idx": 32},
            {"stt": "23", "muc": "Audit log xác thực được lưu local", "cmd": "show system syslog file auth-log", "row_idx": 33},
        ]},
        {"danh_muc": "8. SNMP", "items": [
            {"stt": "24", "muc": "Không tồn tại community mặc định", "cmd": "show snmp community", "row_idx": 35},
            {"stt": "25", "muc": "SNMPv3 cấu hình authentication + privacy", "cmd": "show snmp v3 usm local-engine user", "row_idx": 36},
        ]},
        {"danh_muc": "9. Bảo mật Layer 2", "items": [
            {"stt": "26", "muc": "Spanning Tree Protocol đang được bật", "cmd": "show spanning-tree bridge", "row_idx": 38},
            {"stt": "27", "muc": "Các port không sử dụng đã bị disable", "cmd": "show interfaces terse | grep down", "row_idx": 39},
            {"stt": "28", "muc": "DHCP Snooping đang bật trên VLAN", "cmd": "show dhcp snooping binding", "row_idx": 40},
            {"stt": "29", "muc": "Storm Control được cấu hình", "cmd": "show storm-control interface", "row_idx": 41},
        ]},
    ],

    "Aruba AOS-CX": [
        {"danh_muc": "1. Cấu hình cơ bản", "items": [
            {"stt": "1", "muc": "Hostname đúng quy ước đặt tên", "cmd": "show system | grep Hostname", "row_idx": 5},
            {"stt": "2", "muc": "Management IP được cấu hình chính xác", "cmd": "show interface mgmt", "row_idx": 6},
            {"stt": "3", "muc": "Login banner cảnh báo đã được cấu hình", "cmd": "show running-config | section banner", "row_idx": 7},
            {"stt": "4", "muc": "Phiên bản AOS-CX phù hợp", "cmd": "show version", "row_idx": 8},
        ]},
        {"danh_muc": "2. Xác thực & Tài khoản", "items": [
            {"stt": "5", "muc": "RADIUS Server được cấu hình chính xác", "cmd": "show radius-server detail", "row_idx": 10},
            {"stt": "6", "muc": "Thứ tự xác thực AAA đúng: RADIUS → Local", "cmd": "show running-config | section aaa", "row_idx": 11},
            {"stt": "7", "muc": "Tài khoản local admin tồn tại", "cmd": "show users detail", "row_idx": 12},
            {"stt": "8", "muc": "Kiểm tra đăng nhập bằng RADIUS thành công", "cmd": "Thử SSH bằng user RADIUS", "row_idx": 13},
        ]},
        {"danh_muc": "3. Chính sách mật khẩu", "items": [
            {"stt": "9", "muc": "Độ dài mật khẩu tối thiểu = 14 ký tự", "cmd": "show running-config | section password-configuration", "row_idx": 15},
            {"stt": "10", "muc": "Yêu cầu độ phức tạp mật khẩu", "cmd": "show running-config | section password-configuration", "row_idx": 16},
            {"stt": "11", "muc": "Khoá tài khoản sau 5 lần đăng nhập sai", "cmd": "show running-config | section aaa", "row_idx": 17},
            {"stt": "12", "muc": "Lịch sử mật khẩu lưu tối thiểu 5 lần", "cmd": "show running-config | section password-configuration", "row_idx": 18},
        ]},
        {"danh_muc": "4. SSH & Quản trị từ xa", "items": [
            {"stt": "13", "muc": "Telnet đã bị vô hiệu hoá hoàn toàn", "cmd": "show running-config | grep telnet", "row_idx": 20},
            {"stt": "14", "muc": "Quản trị qua HTTPS; HTTP management tắt", "cmd": "show running-config | grep web-management", "row_idx": 21},
            {"stt": "15", "muc": "Danh sách IP được phép SSH đã whitelist", "cmd": "show running-config | section ssh server", "row_idx": 22},
            {"stt": "16", "muc": "Session timeout = 15 phút", "cmd": "show running-config | grep session timeout", "row_idx": 23},
        ]},
        {"danh_muc": "5. NTP", "items": [
            {"stt": "17", "muc": "NTP Server trỏ về server nội bộ", "cmd": "show ntp associations", "row_idx": 25},
            {"stt": "18", "muc": "NTP đang đồng bộ thành công", "cmd": "show ntp status", "row_idx": 26},
            {"stt": "19", "muc": "Timezone UTC+7", "cmd": "show system | grep timezone", "row_idx": 27},
        ]},
        {"danh_muc": "6. Syslog", "items": [
            {"stt": "20", "muc": "Log được forward về Syslog Server", "cmd": "show logging | grep host", "row_idx": 29},
        ]},
        {"danh_muc": "7. SNMP", "items": [
            {"stt": "21", "muc": "Không còn tồn tại SNMP community mặc định", "cmd": "show running-config | grep community", "row_idx": 31},
            {"stt": "22", "muc": "SNMPv3 đã được cấu hình", "cmd": "show snmpv3 users", "row_idx": 32},
        ]},
        {"danh_muc": "8. Bảo mật Layer 2", "items": [
            {"stt": "23", "muc": "Spanning Tree Protocol đang bật", "cmd": "show spanning-tree", "row_idx": 34},
            {"stt": "24", "muc": "BPDU Guard cấu hình trên access port", "cmd": "show spanning-tree detail", "row_idx": 35},
            {"stt": "25", "muc": "DHCP Snooping đang bật trên VLAN", "cmd": "show dhcp-snooping", "row_idx": 36},
            {"stt": "26", "muc": "Dynamic ARP Inspection đang bật", "cmd": "show arp inspection", "row_idx": 37},
            {"stt": "27", "muc": "Các port không sử dụng đã bị shutdown", "cmd": "show interface brief | grep down", "row_idx": 38},
            {"stt": "28", "muc": "Storm Control được cấu hình", "cmd": "show interface brief", "row_idx": 39},
        ]},
        {"danh_muc": "9. Lưu cấu hình", "items": [
            {"stt": "29", "muc": "Cấu hình đã được lưu (không có dấu *)", "cmd": "show running-config", "row_idx": 41},
        ]},
    ],

    "FortiGate": [
        {"danh_muc": "1. Thông tin đăng nhập & Truy cập", "items": [
            {"stt": "1", "muc": "Mật khẩu mặc định của admin đã thay đổi", "cmd": "Thử đăng nhập bằng mật khẩu mặc định", "row_idx": 5},
            {"stt": "2", "muc": "Admin chỉ đăng nhập từ Trusted Hosts", "cmd": "show system admin", "row_idx": 6},
            {"stt": "3", "muc": "Quản trị qua HTTPS; HTTP bị tắt", "cmd": "show system interface", "row_idx": 7},
            {"stt": "4", "muc": "Admin timeout = 15 phút", "cmd": "show system global | grep admintimeout", "row_idx": 8},
            {"stt": "5", "muc": "MFA đã bật cho tài khoản admin", "cmd": "show system admin", "row_idx": 9},
        ]},
        {"danh_muc": "2. Chính sách mật khẩu", "items": [
            {"stt": "6", "muc": "Password policy đang bật", "cmd": "show system password-policy", "row_idx": 11},
            {"stt": "7", "muc": "Độ dài mật khẩu tối thiểu = 14 ký tự", "cmd": "show system password-policy", "row_idx": 12},
            {"stt": "8", "muc": "Yêu cầu độ phức tạp mật khẩu", "cmd": "show system password-policy", "row_idx": 13},
            {"stt": "9", "muc": "Mật khẩu hết hạn sau 90 ngày", "cmd": "show system password-policy", "row_idx": 14},
            {"stt": "10", "muc": "Khoá tài khoản sau 5 lần sai, khoá 30 phút", "cmd": "show system global | grep admin-lockout", "row_idx": 15},
        ]},
        {"danh_muc": "3. Mã hoá & TLS", "items": [
            {"stt": "11", "muc": "Strong Crypto đang bật", "cmd": "show system global | grep strong-crypto", "row_idx": 17},
            {"stt": "12", "muc": "ssl-static-key-ciphers đã tắt", "cmd": "show system global | grep ssl-static-key", "row_idx": 18},
            {"stt": "13", "muc": "DH parameters ≥ 2048-bit", "cmd": "show system global | grep dh-params", "row_idx": 19},
            {"stt": "14", "muc": "HTTPS quản trị dùng TLS 1.2 trở lên", "cmd": "Kiểm tra thông tin kết nối", "row_idx": 20},
        ]},
        {"danh_muc": "4. NTP", "items": [
            {"stt": "15", "muc": "NTP Server trỏ về server nội bộ", "cmd": "show system ntp | grep server", "row_idx": 22},
            {"stt": "16", "muc": "NTP đang đồng bộ thành công", "cmd": "get system status | grep time", "row_idx": 23},
            {"stt": "17", "muc": "Timezone = GMT+7 (Asia/Ho_Chi_Minh)", "cmd": "show system global | grep timezone", "row_idx": 24},
        ]},
        {"danh_muc": "5. Logging", "items": [
            {"stt": "18", "muc": "Syslog forward đang bật và trỏ đúng", "cmd": "show log syslogd setting", "row_idx": 26},
            {"stt": "19", "muc": "Log severity ở mức information trở lên", "cmd": "show log syslogd setting", "row_idx": 27},
            {"stt": "20", "muc": "Forward traffic logging đang bật", "cmd": "show log syslogd filter", "row_idx": 28},
            {"stt": "21", "muc": "Admin events logging đang bật", "cmd": "show log eventfilter | grep admin", "row_idx": 29},
        ]},
        {"danh_muc": "6. Bảo mật interface quản trị", "items": [
            {"stt": "22", "muc": "Interface WAN không cho quản trị", "cmd": "show system interface WAN", "row_idx": 31},
            {"stt": "23", "muc": "Local-In Policy giới hạn IP", "cmd": "show firewall local-in-policy", "row_idx": 32},
            {"stt": "24", "muc": "USB firmware installation đã tắt", "cmd": "show system global | grep usb-mode", "row_idx": 33},
        ]},
        {"danh_muc": "7. IPS & Security Profiles", "items": [
            {"stt": "25", "muc": "IPS đang bật trong security policy", "cmd": "show ips global", "row_idx": 35},
            {"stt": "26", "muc": "IPS signature cập nhật trong 7 ngày", "cmd": "diagnose autoupdate status", "row_idx": 36},
            {"stt": "27", "muc": "Antivirus profile đang áp dụng outbound", "cmd": "show antivirus profile", "row_idx": 37},
        ]},
        {"danh_muc": "8. Firmware & Backup", "items": [
            {"stt": "28", "muc": "Firmware không có CVE nghiêm trọng", "cmd": "Kiểm tra FortiGuard PSIRT", "row_idx": 39},
            {"stt": "29", "muc": "File backup cấu hình được mã hoá", "cmd": "Xác nhận với team quản trị", "row_idx": 40},
            {"stt": "30", "muc": "Hostname đúng quy ước", "cmd": "get system status", "row_idx": 41},
        ]},
    ],
}


# ==========================================
# DỮ LIỆU APP 04: ĐÁNH GIÁ HỆ THỐNG HIỆN TẠI
# ==========================================
AUDIT_DATA = {
    "Linux Ubuntu 24.04": [
        {"danh_muc": "1. SSH Hardening", "items": [
            {"stt": "1", "nguy_co": "Cao", "muc": "grep PermitRootLogin /etc/ssh/sshd_config", "expected": "no", "row_idx": 5},
            {"stt": "2", "nguy_co": "Cao", "muc": "grep MaxAuthTries /etc/ssh/sshd_config", "expected": "4", "row_idx": 6},
            {"stt": "3", "nguy_co": "Trung bình", "muc": "grep LoginGraceTime /etc/ssh/sshd_config", "expected": "60", "row_idx": 7},
            {"stt": "4", "nguy_co": "Trung bình", "muc": "grep X11Forwarding /etc/ssh/sshd_config", "expected": "no", "row_idx": 8},
            {"stt": "5", "nguy_co": "Trung bình", "muc": "grep MaxSessions /etc/ssh/sshd_config", "expected": "3", "row_idx": 9},
            {"stt": "6", "nguy_co": "Trung bình", "muc": "grep AllowAgentForwarding /etc/ssh/sshd_config", "expected": "no", "row_idx": 10},
            {"stt": "7", "nguy_co": "Cao", "muc": "grep -E 'KexAlgorithms|Ciphers|MACs' /etc/ssh/sshd_config", "expected": "Ciphers mạnh", "row_idx": 11},
            {"stt": "8", "nguy_co": "Cao", "muc": "grep PermitEmptyPasswords /etc/ssh/sshd_config", "expected": "no", "row_idx": 12},
            {"stt": "9", "nguy_co": "Cao", "muc": "grep UsePAM /etc/ssh/sshd_config", "expected": "yes", "row_idx": 13},
            {"stt": "10", "nguy_co": "Trung bình", "muc": "grep GSSAPIAuthentication /etc/ssh/sshd_config", "expected": "no", "row_idx": 14},
            {"stt": "11", "nguy_co": "Trung bình", "muc": "grep HostbasedAuthentication /etc/ssh/sshd_config", "expected": "no", "row_idx": 15},
            {"stt": "12", "nguy_co": "Trung bình", "muc": "grep LogLevel /etc/ssh/sshd_config", "expected": "VERBOSE", "row_idx": 16},
            {"stt": "13", "nguy_co": "Cao", "muc": "grep MaxStartups /etc/ssh/sshd_config", "expected": "10:30:60", "row_idx": 17},
            {"stt": "14", "nguy_co": "Trung bình", "muc": "grep ClientAliveInterval /etc/ssh/sshd_config", "expected": "900", "row_idx": 18},
        ]},
        {"danh_muc": "2. Password Policy", "items": [
            {"stt": "15", "nguy_co": "Cao", "muc": "grep minlen /etc/security/pwquality.conf", "expected": "14", "row_idx": 20},
            {"stt": "16", "nguy_co": "Cao", "muc": "Yêu cầu độ phức tạp mật khẩu", "expected": "-1 cho mỗi loại", "row_idx": 21},
            {"stt": "17", "nguy_co": "Trung bình", "muc": "grep pam_pwhistory /etc/pam.d/common-password", "expected": "remember=5", "row_idx": 22},
            {"stt": "18", "nguy_co": "Cao", "muc": "grep sha512 /etc/pam.d/common-password", "expected": "sha512", "row_idx": 23},
            {"stt": "19", "nguy_co": "Trung bình", "muc": "grep -E 'difok|maxrepeat|maxsequence|dictcheck' /etc/security/pwquality.conf", "expected": "difok=2, maxrepeat=3, maxsequence=3, dictcheck=1", "row_idx": 24},
            {"stt": "20", "nguy_co": "Cao", "muc": "grep -E 'deny|unlock_time' /etc/security/faillock.conf", "expected": "deny=5, unlock_time=900", "row_idx": 25},
            {"stt": "21", "nguy_co": "Cao", "muc": "grep 'even_deny_root' /etc/security/faillock.conf", "expected": "even_deny_root (có dòng này)", "row_idx": 26},
        ]},
        {"danh_muc": "3. Xác thực RADIUS", "items": [
            {"stt": "22", "nguy_co": "Cao", "muc": "cat /etc/pam_radius_auth.conf", "expected": "Cấu hình IP Radius", "row_idx": 28},
            {"stt": "23", "nguy_co": "Cao", "muc": "grep KbdInteractiveAuthentication /etc/ssh/sshd_config", "expected": "yes", "row_idx": 29},
            {"stt": "24", "nguy_co": "Cao", "muc": "cat /etc/pam.d/common-auth", "expected": "RADIUS trước, local fallback", "row_idx": 30},
            {"stt": "25", "nguy_co": "Cao", "muc": "Thử SSH bang user RADIUS", "expected": "Thành công", "row_idx": 31},
        ]},
        {"danh_muc": "4. Firewall", "items": [
            {"stt": "26", "nguy_co": "Cao", "muc": "sudo iptables -L -n -v", "expected": "Hoạt động và có rule", "row_idx": 33},
            {"stt": "27", "nguy_co": "Cao", "muc": "sudo iptables -L INPUT -n", "expected": "policy DROP/REJECT", "row_idx": 34},
            {"stt": "28", "nguy_co": "Cao", "muc": "sudo iptables -L FORWARD -n", "expected": "policy DROP", "row_idx": 35},
            {"stt": "29", "nguy_co": "Cao", "muc": "sudo iptables -L INPUT -n | grep 22", "expected": "Whitelist IP rõ ràng", "row_idx": 36},
            {"stt": "30", "nguy_co": "Cao", "muc": "systemctl is-enabled netfilter-persistent", "expected": "enabled", "row_idx": 37},
        ]},
        {"danh_muc": "5. Fail2ban", "items": [
            {"stt": "31", "nguy_co": "Cao", "muc": "systemctl is-active fail2ban", "expected": "active", "row_idx": 39},
            {"stt": "32", "nguy_co": "Cao", "muc": "fail2ban-client status sshd", "expected": "bantime=3600, maxretry=4", "row_idx": 40},
        ]},
        {"danh_muc": "6. NTP", "items": [
            {"stt": "33", "nguy_co": "Trung bình", "muc": "timedatectl timesync-status", "expected": "ntp.vngdc.local", "row_idx": 42},
            {"stt": "34", "nguy_co": "Thấp", "muc": "timedatectl | grep zone", "expected": "Asia/Ho_Chi_Minh", "row_idx": 43},
        ]},
        {"danh_muc": "7. Logging", "items": [
            {"stt": "35", "nguy_co": "Cao", "muc": "grep '@' /etc/rsyslog.conf", "expected": "Gửi log về Server", "row_idx": 45},
            {"stt": "36", "nguy_co": "Cao", "muc": "systemctl is-active wazuh-agent", "expected": "active", "row_idx": 46},
            {"stt": "37", "nguy_co": "Trung bình", "muc": "systemctl is-active node_exporter", "expected": "active", "row_idx": 47},
            {"stt": "38", "nguy_co": "Trung bình", "muc": "Kiểm tra Prometheus UI", "expected": "UP", "row_idx": 48},
        ]},
        {"danh_muc": "8. Dịch vụ không cần thiết", "items": [
            {"stt": "39", "nguy_co": "Trung bình", "muc": "systemctl is-enabled ModemManager", "expected": "disabled", "row_idx": 50},
            {"stt": "40", "nguy_co": "Thấp", "muc": "systemctl is-enabled thermald", "expected": "disabled", "row_idx": 51},
            {"stt": "41", "nguy_co": "Trung bình", "muc": "systemctl is-enabled apport", "expected": "disabled", "row_idx": 52},
        ]},
        {"danh_muc": "9. Scripts & Crontab", "items": [
            {"stt": "42", "nguy_co": "Trung bình", "muc": "ls /opt/dc_script/", "expected": "Đầy đủ file bash", "row_idx": 54},
            {"stt": "43", "nguy_co": "Trung bình", "muc": "cat /etc/crontab", "expected": "Có đủ 3 entry", "row_idx": 55},
        ]},
        {"danh_muc": "10. Sudo Hardening", "items": [
            {"stt": "44", "nguy_co": "Cao", "muc": "sudo grep 'use_pty' /etc/sudoers /etc/sudoers.d/ 2>/dev/null", "expected": "Defaults use_pty", "row_idx": 57},
            {"stt": "45", "nguy_co": "Cao", "muc": "sudo grep -rP 'NOPASSWD' /etc/sudoers /etc/sudoers.d/ 2>/dev/null | wc -l", "expected": "0 (không có NOPASSWD)", "row_idx": 58},
            {"stt": "46", "nguy_co": "Trung bình", "muc": "sudo grep 'logfile' /etc/sudoers /etc/sudoers.d/ 2>/dev/null", "expected": "Defaults logfile=/var/log/sudo.log", "row_idx": 59},
        ]},
        {"danh_muc": "11. File Permissions", "items": [
            {"stt": "47", "nguy_co": "Cao", "muc": "stat -c '%n %a %U:%G' /etc/shadow /etc/gshadow", "expected": "640 root:shadow", "row_idx": 61},
            {"stt": "48", "nguy_co": "Trung bình", "muc": "stat -c '%n %a %U:%G' /etc/passwd /etc/group", "expected": "644 root:root", "row_idx": 62},
            {"stt": "49", "nguy_co": "Cao", "muc": "stat -c '%n %a %U:%G' /etc/security/opasswd 2>/dev/null", "expected": "600 root:root", "row_idx": 63},
        ]},
    ],
    
    "Windows Server 2022": [
        {"danh_muc": "1. Password & Lockout", "items": [
            {"stt": "1", "nguy_co": "Cao", "muc": "net accounts | minimum password length", "expected": "14", "row_idx": 5},
            {"stt": "2", "nguy_co": "Cao", "muc": "Độ phức tạp mật khẩu", "expected": "Yes", "row_idx": 6},
            {"stt": "3", "nguy_co": "Trung bình", "muc": "net accounts | password history", "expected": "5", "row_idx": 7},
            {"stt": "4", "nguy_co": "Trung bình", "muc": "net accounts | maximum password age", "expected": "90", "row_idx": 8},
            {"stt": "5", "nguy_co": "Cao", "muc": "net accounts | lockout threshold", "expected": "5", "row_idx": 9},
            {"stt": "6", "nguy_co": "Cao", "muc": "net accounts | lockout duration", "expected": "30", "row_idx": 10},
        ]},
        {"danh_muc": "2. Windows Firewall", "items": [
            {"stt": "7", "nguy_co": "Cao", "muc": "Get-NetFirewallProfile", "expected": "True cho cả 3 profile", "row_idx": 12},
        ]},
        {"danh_muc": "3. TLS & Protocol", "items": [
            {"stt": "8", "nguy_co": "Cao", "muc": "Kiểm tra registry SSL 2.0", "expected": "Enabled = 0", "row_idx": 14},
            {"stt": "9", "nguy_co": "Cao", "muc": "Kiểm tra registry SSL 3.0", "expected": "Enabled = 0", "row_idx": 15},
            {"stt": "10", "nguy_co": "Cao", "muc": "Kiểm tra registry TLS 1.0", "expected": "Enabled = 0", "row_idx": 16},
            {"stt": "11", "nguy_co": "Trung bình", "muc": "Kiểm tra registry TLS 1.1", "expected": "Enabled = 0", "row_idx": 17},
            {"stt": "12", "nguy_co": "Cao", "muc": "Kiểm tra registry TLS 1.2", "expected": "Enabled = 1", "row_idx": 18},
            {"stt": "13", "nguy_co": "Cao", "muc": "(Get-SmbServerConfiguration).EnableSMB1Protocol", "expected": "False", "row_idx": 19},
        ]},
        {"danh_muc": "4. Security Features", "items": [
            {"stt": "14", "nguy_co": "Cao", "muc": "Kiểm tra registry EnableLUA", "expected": "1", "row_idx": 21},
            {"stt": "15", "nguy_co": "Cao", "muc": "Get-LocalUser Guest", "expected": "False", "row_idx": 22},
            {"stt": "16", "nguy_co": "Trung bình", "muc": "Kiểm tra registry NoDriveTypeAutoRun", "expected": "0xFF (255)", "row_idx": 23},
            {"stt": "17", "nguy_co": "Cao", "muc": "Get-MpComputerStatus", "expected": "True", "row_idx": 24},
        ]},
        {"danh_muc": "5. Audit Logging", "items": [
            {"stt": "18", "nguy_co": "Cao", "muc": "auditpol /get /category:Logon/Logoff", "expected": "Success and Failure", "row_idx": 26},
            {"stt": "19", "nguy_co": "Cao", "muc": "auditpol /get /category:Account Logon", "expected": "Success and Failure", "row_idx": 27},
            {"stt": "20", "nguy_co": "Cao", "muc": "auditpol /get /category:Account Management", "expected": "Success", "row_idx": 28},
            {"stt": "21", "nguy_co": "Cao", "muc": "Kiểm tra registry EnableScriptBlockLogging", "expected": "1", "row_idx": 29},
            {"stt": "22", "nguy_co": "Trung bình", "muc": "wevtutil gl Security", "expected": "1073741824", "row_idx": 30},
        ]},
        {"danh_muc": "6. Logging & Monitoring", "items": [
            {"stt": "23", "nguy_co": "Cao", "muc": "Get-Service nxlog", "expected": "Running; log mới lên syslog", "row_idx": 32},
            {"stt": "24", "nguy_co": "Cao", "muc": "Get-Service WazuhSvc", "expected": "Running", "row_idx": 33},
            {"stt": "25", "nguy_co": "Trung bình", "muc": "Get-NetTCPConnection -LocalPort 9182", "expected": "Listen state", "row_idx": 34},
        ]},
        {"danh_muc": "7. NTP", "items": [
            {"stt": "26", "nguy_co": "Trung bình", "muc": "w32tm /query /source", "expected": "IP NTP nội bộ", "row_idx": 36},
            {"stt": "27", "nguy_co": "Thấp", "muc": "Get-TimeZone", "expected": "SE Asia Standard Time", "row_idx": 37},
        ]},
    ],

    "Juniper JunOS": [
        {"danh_muc": "1. Xác thực", "items": [
            {"stt": "1", "nguy_co": "Cao", "muc": "show system radius-server", "expected": "IP RADIUS được cấu hình", "row_idx": 5},
            {"stt": "2", "nguy_co": "Cao", "muc": "show system authentication-order", "expected": "radius password", "row_idx": 6},
            {"stt": "3", "nguy_co": "Trung bình", "muc": "show system login idle-timeout", "expected": "15", "row_idx": 7},
        ]},
        {"danh_muc": "2. Chính sách mật khẩu", "items": [
            {"stt": "4", "nguy_co": "Cao", "muc": "show system login password minimum-length", "expected": "14", "row_idx": 9},
            {"stt": "5", "nguy_co": "Cao", "muc": "show system login retry-options", "expected": "tries=5, lockout-period=30", "row_idx": 10},
        ]},
        {"danh_muc": "3. SSH & Quản trị", "items": [
            {"stt": "6", "nguy_co": "Cao", "muc": "show system services | grep telnet", "expected": "Không có kết quả", "row_idx": 12},
            {"stt": "7", "nguy_co": "Cao", "muc": "show system services ssh | grep protocol", "expected": "v2", "row_idx": 13},
            {"stt": "8", "nguy_co": "Cao", "muc": "show system services ssh | grep root-login", "expected": "deny", "row_idx": 14},
            {"stt": "9", "nguy_co": "Trung bình", "muc": "show system login message", "expected": "Có nội dung WARNING", "row_idx": 15},
            {"stt": "10", "nguy_co": "Cao", "muc": "show interfaces me0 | grep filter", "expected": "MGMT-ACCESS", "row_idx": 16},
        ]},
        {"danh_muc": "4. Control Plane", "items": [
            {"stt": "11", "nguy_co": "Cao", "muc": "show interfaces lo0 | grep filter", "expected": "PROTECT-RE", "row_idx": 18},
        ]},
        {"danh_muc": "5. NTP", "items": [
            {"stt": "12", "nguy_co": "Trung bình", "muc": "show ntp associations", "expected": "IP NTP nội bộ", "row_idx": 20},
            {"stt": "13", "nguy_co": "Thấp", "muc": "show system time-zone", "expected": "Asia/Ho_Chi_Minh", "row_idx": 21},
        ]},
        {"danh_muc": "6. Syslog", "items": [
            {"stt": "14", "nguy_co": "Cao", "muc": "show system syslog host", "expected": "IP syslog server được cấu hình", "row_idx": 23},
        ]},
        {"danh_muc": "7. SNMP", "items": [
            {"stt": "15", "nguy_co": "Cao", "muc": "show snmp community", "expected": "Kết quả trống", "row_idx": 25},
            {"stt": "16", "nguy_co": "Cao", "muc": "show snmp v3 usm local-engine user", "expected": "Có user với auth+priv", "row_idx": 26},
        ]},
        {"danh_muc": "8. Layer 2", "items": [
            {"stt": "17", "nguy_co": "Trung bình", "muc": "show spanning-tree bridge", "expected": "STP enabled", "row_idx": 28},
            {"stt": "18", "nguy_co": "Trung bình", "muc": "show interfaces terse | grep down", "expected": "Các port disable", "row_idx": 29},
            {"stt": "19", "nguy_co": "Trung bình", "muc": "show dhcp snooping binding", "expected": "Active", "row_idx": 30},
        ]},
    ],
    
    "Aruba AOS-CX": [
        {"danh_muc": "1. Xác thực", "items": [
            {"stt": "1", "nguy_co": "Cao", "muc": "show radius-server detail", "expected": "IP RADIUS được cấu hình", "row_idx": 5},
            {"stt": "2", "nguy_co": "Cao", "muc": "show running-config | section aaa", "expected": "group radius local", "row_idx": 6},
        ]},
        {"danh_muc": "2. Chính sách mật khẩu", "items": [
            {"stt": "3", "nguy_co": "Cao", "muc": "show running-config | section password", "expected": "minimum-length 14", "row_idx": 8},
            {"stt": "4", "nguy_co": "Cao", "muc": "Yêu cầu độ phức tạp mật khẩu", "expected": "min-upper/lower/digit/special = 1", "row_idx": 9},
            {"stt": "5", "nguy_co": "Cao", "muc": "show running-config | section aaa authentication", "expected": "limit=5, lockout=1800", "row_idx": 10},
        ]},
        {"danh_muc": "3. SSH & Quản trị", "items": [
            {"stt": "6", "nguy_co": "Cao", "muc": "show running-config | grep telnet", "expected": "Không có telnet-server enable", "row_idx": 12},
            {"stt": "7", "nguy_co": "Cao", "muc": "show running-config | grep web-management", "expected": "Chỉ https, không có http", "row_idx": 13},
            {"stt": "8", "nguy_co": "Trung bình", "muc": "show running-config | section banner", "expected": "Có nội dung WARNING", "row_idx": 14},
            {"stt": "9", "nguy_co": "Trung bình", "muc": "show running-config | grep session timeout", "expected": "15", "row_idx": 15},
        ]},
        {"danh_muc": "4. NTP", "items": [
            {"stt": "10", "nguy_co": "Trung bình", "muc": "show ntp associations", "expected": "IP NTP nội bộ", "row_idx": 17},
            {"stt": "11", "nguy_co": "Thấp", "muc": "show system | grep timezone", "expected": "7 (UTC+7)", "row_idx": 18},
        ]},
        {"danh_muc": "5. Syslog", "items": [
            {"stt": "12", "nguy_co": "Cao", "muc": "show logging | grep host", "expected": "IP syslog server được cấu hình", "row_idx": 20},
        ]},
        {"danh_muc": "6. SNMP", "items": [
            {"stt": "13", "nguy_co": "Cao", "muc": "show running-config | grep community", "expected": "Kết quả trống", "row_idx": 22},
            {"stt": "14", "nguy_co": "Cao", "muc": "show snmpv3 users", "expected": "Có user với auth+priv", "row_idx": 23},
        ]},
        {"danh_muc": "7. Layer 2", "items": [
            {"stt": "15", "nguy_co": "Trung bình", "muc": "show spanning-tree", "expected": "STP enabled; bpdu-guard enabled", "row_idx": 25},
            {"stt": "16", "nguy_co": "Trung bình", "muc": "show dhcp-snooping", "expected": "Active", "row_idx": 26},
            {"stt": "17", "nguy_co": "Trung bình", "muc": "show arp inspection", "expected": "Active", "row_idx": 27},
            {"stt": "18", "nguy_co": "Trung bình", "muc": "show interface brief | grep down", "expected": "Các port shutdown", "row_idx": 28},
        ]},
        {"danh_muc": "8. Lưu cấu hình", "items": [
            {"stt": "19", "nguy_co": "Cao", "muc": "show running-config", "expected": "Không có dấu *", "row_idx": 30},
        ]},
    ],

    "FortiGate": [
        {"danh_muc": "1. Thông tin đăng nhập", "items": [
            {"stt": "1", "nguy_co": "Cao", "muc": "Thử đăng nhập bằng mật khẩu mặc định", "expected": "Phải bị từ chối", "row_idx": 5},
            {"stt": "2", "nguy_co": "Cao", "muc": "show system admin → trusthost", "expected": "Có whitelist IP quản trị", "row_idx": 6},
            {"stt": "3", "nguy_co": "Cao", "muc": "show system interface", "expected": "Không có http", "row_idx": 7},
            {"stt": "4", "nguy_co": "Trung bình", "muc": "show system global | grep admintimeout", "expected": "15", "row_idx": 8},
        ]},
        {"danh_muc": "2. Chính sách mật khẩu", "items": [
            {"stt": "5", "nguy_co": "Cao", "muc": "show system password-policy", "expected": "enable", "row_idx": 10},
            {"stt": "6", "nguy_co": "Cao", "muc": "show system password-policy | min-length", "expected": "14", "row_idx": 11},
            {"stt": "7", "nguy_co": "Trung bình", "muc": "show system password-policy | expire-day", "expected": "90", "row_idx": 12},
            {"stt": "8", "nguy_co": "Cao", "muc": "show system global | admin-lockout", "expected": "threshold=5, duration=1800", "row_idx": 13},
        ]},
        {"danh_muc": "3. Mã hoá & TLS", "items": [
            {"stt": "9", "nguy_co": "Cao", "muc": "show system global | strong-crypto", "expected": "enable", "row_idx": 15},
            {"stt": "10", "nguy_co": "Cao", "muc": "show system global | ssl-static-key", "expected": "disable", "row_idx": 16},
            {"stt": "11", "nguy_co": "Trung bình", "muc": "show system global | dh-params", "expected": "≥ 2048", "row_idx": 17},
        ]},
        {"danh_muc": "4. NTP", "items": [
            {"stt": "12", "nguy_co": "Trung bình", "muc": "show system ntp", "expected": "IP NTP nội bộ", "row_idx": 19},
            {"stt": "13", "nguy_co": "Thấp", "muc": "show system global | timezone", "expected": "45 (SE Asia)", "row_idx": 20},
        ]},
        {"danh_muc": "5. Logging", "items": [
            {"stt": "14", "nguy_co": "Cao", "muc": "show log syslogd setting", "expected": "enable; IP syslog server", "row_idx": 22},
            {"stt": "15", "nguy_co": "Cao", "muc": "show log syslogd filter", "expected": "enable", "row_idx": 23},
            {"stt": "16", "nguy_co": "Cao", "muc": "show log eventfilter", "expected": "enable", "row_idx": 24},
        ]},
        {"danh_muc": "6. Bảo mật interface", "items": [
            {"stt": "17", "nguy_co": "Cao", "muc": "show system interface WAN", "expected": "Chỉ ping", "row_idx": 26},
            {"stt": "18", "nguy_co": "Cao", "muc": "show firewall local-in-policy", "expected": "Có policy restrict IP", "row_idx": 27},
            {"stt": "19", "nguy_co": "Trung bình", "muc": "show system global | usb-mode", "expected": "disable", "row_idx": 28},
        ]},
        {"danh_muc": "7. IPS & Security", "items": [
            {"stt": "20", "nguy_co": "Cao", "muc": "show ips global", "expected": "enable; signature enabled", "row_idx": 30},
            {"stt": "21", "nguy_co": "Cao", "muc": "diagnose autoupdate status", "expected": "Last update trong 7 ngày", "row_idx": 31},
        ]},
        {"danh_muc": "8. Firmware", "items": [
            {"stt": "22", "nguy_co": "Cao", "muc": "Kiểm tra FortiGuard PSIRT advisory", "expected": "Không có CVSS ≥ 7.0 chưa vá", "row_idx": 33},
            {"stt": "23", "nguy_co": "Trung bình", "muc": "Kiểm tra trên backup server", "expected": "File .conf mã hoá, lưu an toàn", "row_idx": 34},
        ]},
    ],
}