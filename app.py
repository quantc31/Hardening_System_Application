# app.py
from flask import Flask, render_template, request, send_file
import openpyxl
import io
import os
from data import CHECKLIST_DATA, AUDIT_DATA # Import data từ file data.py

app = Flask(__name__)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_DIR = os.path.join(CURRENT_DIR, "templates_excel")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checklist', methods=['GET'])
def checklist_view():
    # Lấy tham số type từ URL (mặc định là Ubuntu)
    device_type = request.args.get('type', 'Linux Ubuntu 24.04')
    data = CHECKLIST_DATA.get(device_type, [])
    types = list(CHECKLIST_DATA.keys())
    return render_template('checklist.html', data=data, types=types, selected_type=device_type)

@app.route('/export_checklist', methods=['POST'])
def export_checklist():
    device_type = request.form.get('device_type')
    hostname = request.form.get('hostname', '')
    ip_address = request.form.get('ip_address', '')
    check_date = request.form.get('check_date', '')
    inspector = request.form.get('inspector', '')

    # Load template Excel File 03
    template_path = os.path.join(EXCEL_DIR, "03_Checklist_Hệ thống mới.xlsx")
    wb = openpyxl.load_workbook(template_path)
    ws = wb[device_type]

    # === GHI THÔNG TIN CHUNG (APP 03) ===
    ws['A2'] = f"Hostname: {hostname}"
    ws['D2'] = f"IP Address: {ip_address}"
    if check_date:
        parts = check_date.split('-')
        if len(parts) == 3: check_date = f"{parts[2]}/{parts[1]}/{parts[0]}"
    ws['E2'] = f"Ngày kiểm tra: {check_date}"
    ws['F2'] = f"Người kiểm tra: {inspector}"

    # Đếm số lượng
    total_items = 0
    pass_items = 0
    fail_items = 0
    na_items = 0

    for cat in CHECKLIST_DATA.get(device_type, []):
        for item in cat['items']:
            row = item['row_idx']
            result = request.form.get(f"result_{row}")
            note = request.form.get(f"note_{row}", '')

            # Ghi kết quả và ghi chú vào Excel
            ws.cell(row=row, column=5, value=result)
            ws.cell(row=row, column=6, value=note)

            total_items += 1
            if result == "PASS": pass_items += 1
            elif result == "FAIL": fail_items += 1
            elif result == "N/A": na_items += 1

    # Xóa các sheet thừa (chỉ giữ sheet của device_type và sheet hướng dẫn)
    for sheet_name in list(wb.sheetnames):
        if sheet_name != device_type and sheet_name not in ["Hướng dẫn"]:
            wb.remove(wb[sheet_name])

    # Tính % = pass / (pass + fail + na)
    if total_items > 0:
        compliance_rate = pass_items / total_items
    else:
        compliance_rate = 0

    # Đánh giá Đạt/Không đạt
    if compliance_rate == 1.0:
        status_text = "ĐẠT YÊU CẦU"
    else:
        status_text = "CHƯA ĐẠT - CẦN XỬ LÝ"

    # Ghi đè thẳng số liệu vào vùng Tổng kết ở cuối file Excel
    # (Shine nhớ chỉnh lại column=... cho đúng với cột trong file Excel của bạn nhé)
    for r in range(ws.max_row, 1, -1):
        cell_val = str(ws.cell(row=r, column=1).value or "").strip()
        if "Tổng số mục kiểm tra" in cell_val: ws.cell(row=r, column=4, value=total_items)
        elif "Số mục PASS" in cell_val: ws.cell(row=r, column=4, value=pass_items)
        elif "Số mục FAIL" in cell_val: ws.cell(row=r, column=4, value=fail_items)
        elif "Số mục N/A" in cell_val: ws.cell(row=r, column=4, value=na_items)
        elif "Tỷ lệ tuân thủ" in cell_val: 
            ws.cell(row=r, column=4, value=compliance_rate)
            ws.cell(row=r, column=4).number_format = '0.00%' # Ép định dạng %
        elif "Trạng thái tổng thể" in cell_val: 
            ws.cell(row=r, column=4, value=status_text)
            break

    # Xuất file
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    
    filename = f"Checklist_{device_type}_{hostname}.xlsx"
    return send_file(buffer, as_attachment=True, download_name=filename, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# app.py (Bổ sung phần App 04)

@app.route('/audit', methods=['GET'])
def audit_view():
    device_type = request.args.get('type', 'Linux Ubuntu 24.04')
    data = AUDIT_DATA.get(device_type, [])
    types = list(AUDIT_DATA.keys())
    return render_template('audit.html', data=data, types=types, selected_type=device_type)

@app.route('/export_audit', methods=['POST'])
def export_audit():
    device_type = request.form.get('device_type')
    hostname = request.form.get('hostname', '')
    ip_address = request.form.get('ip_address', '')
    audit_date = request.form.get('audit_date', '')
    assessor = request.form.get('assessor', '')
    approver = request.form.get('approver', '')

    # Load template Excel File 04
    template_path = os.path.join(EXCEL_DIR, "04_Đánh giá hệ thống hiện tại.xlsx")
    wb = openpyxl.load_workbook(template_path)
    ws = wb[device_type]

    # === GHI THÔNG TIN CHUNG (APP 04) ===
    # A2 đại diện cho ô merge A, B, C
    ws['A2'] = f"Thiết bị / Hostname: {hostname}"
    ws['D2'] = f"IP Address: {ip_address}"
    # Đổi định dạng ngày sang dd/mm/yyyy trước khi ghi
    if audit_date:
        parts = audit_date.split('-')
        if len(parts) == 3: audit_date = f"{parts[2]}/{parts[1]}/{parts[0]}"
    ws['F2'] = f"Ngày đánh giá: {audit_date}"
    ws['H2'] = f"Người đánh giá: {assessor}"
    ws['I2'] = f"Người phê duyệt: {approver}"

    total_items = 0
    pass_items = 0
    fail_items = 0
    na_items = 0
    high_risk_fails = 0

    # Lấy data từ Form và đẩy vào Excel
    for cat in AUDIT_DATA.get(device_type, []):
        for item in cat['items']:
            row = item['row_idx']
            
            actual = request.form.get(f"actual_{row}")
            result = request.form.get(f"result_{row}")
            remed = request.form.get(f"remediation_{row}")
            duedate = request.form.get(f"duedate_{row}")

            # Chỉnh sửa format ngày tháng (từ YYYY-MM-DD sang DD/MM/YYYY)
            if duedate:
                date_parts = duedate.split('-')
                if len(date_parts) == 3:
                    duedate = f"{date_parts[2]}/{date_parts[1]}/{date_parts[0]}"

            # Ghi vào Excel: Cột F (Actual), G (Result), H (Remediation), I (Due date)
            ws.cell(row=row, column=6, value=actual)
            ws.cell(row=row, column=7, value=result)
            ws.cell(row=row, column=8, value=remed)
            ws.cell(row=row, column=9, value=duedate)

            # Tính toán %
            total_items += 1
            if result == "PASS": pass_items += 1
            elif result == "FAIL": fail_items += 1
            elif result == "N/A": na_items += 1

    # Tính % = pass / (pass + fail + na)
    if total_items > 0:
        compliance_rate = pass_items / total_items
    else:
        compliance_rate = 0

    # Phân loại trạng thái
    if compliance_rate >= 0.90:
        status_text = "ĐẠT YÊU CẦU"
    elif compliance_rate >= 0.80:
        status_text = "CHẤP NHẬN ĐƯỢC - CẦN CẢI THIỆN"
    else:
        status_text = "KHÔNG ĐẠT - RỦI RO CAO"

    # Tự động dò dòng và ghi kết quả tổng hợp vào Excel
    for r in range(ws.max_row, 1, -1):
        cell_val = str(ws.cell(row=r, column=1).value or "").strip()
        if "Tổng số mục đánh giá" in cell_val: ws.cell(row=r, column=5, value=total_items)
        elif "Số mục PASS" in cell_val: ws.cell(row=r, column=5, value=pass_items)
        elif "Số mục FAIL" in cell_val: ws.cell(row=r, column=5, value=fail_items)
        elif "Số mục N/A" in cell_val: ws.cell(row=r, column=5, value=na_items)
        elif "FAIL – Nguy cơ Cao" in cell_val: ws.cell(row=r, column=5, value=high_risk_fails)
        elif "Tỷ lệ tuân thủ" in cell_val: 
            ws.cell(row=r, column=5, value=compliance_rate)
            ws.cell(row=r, column=5).number_format = '0.00%'
        elif "Trạng thái:" in cell_val:
            ws.cell(row=r, column=5, value=status_text)
            break

    # Xóa các sheet thừa
    for sheet_name in list(wb.sheetnames):
        if sheet_name != device_type and sheet_name not in ["Tổng quan"]:
            wb.remove(wb[sheet_name])

    # Xuất file
    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    filename = f"Audit_{device_type}_{hostname}.xlsx"
    return send_file(buffer, as_attachment=True, download_name=filename, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True, port=5000)