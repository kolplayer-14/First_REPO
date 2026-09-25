
import os



# ==========================================
# 1. SETUP LOOKUP TABLES & VALIDATION RULES
# ==========================================
VALID_ZONES = {
    "North", "South", "East", "West", 
    "North-East", "North-West", "South-East", "South-West"
}

# Define sample messy data exactly from the case study
raw_data_content = """Project_ID,Highway_Number,Zone,Target_Length_KM,Completed_Length,Inspection_Date
PRJ001,NH-44,North,120km,45.5,12-05-2025
PRJ002,NH-2,East,85,85,2025/06/14
PRJ003,,South,150KM,N/A,18-07-2025
PRJ004,NH-8,West,200,110.25,2025-08-19
PRJ005,NH-44,North,50km,60,2025-09-01
PRJ006,NH-16,East,abc,30,14/10/2025
PRJ001,NH-44,North,120km,45.5,12-05-2025
PRJ007,NH-7,South,95,95.0,02-11-2025
PRJ008,NH-1,North,100,50,20261408
PRJ009,NH-12,East,120,40,26-08-12"""

# Write raw content to local file for emulation
file_name = "C:\\Users\\HARSHIT\\OneDrive\\Practice_Coding\\Learning\\highway_data.csv"
# dynamically check path structure to gracefully create parents or directories if needed
os.makedirs(os.path.dirname(file_name), exist_ok=True)
with open(file_name, "w") as f:
    f.write(raw_data_content.strip())

# ==========================================
# 2. THE CLEANING ENGINE (MAIN PIPELINE)
# ==========================================
def run_cleaning_pipeline(csv_path):
    final_clean_records = []
    seen_project_ids = set()  # Your dynamic tracking set for on-the-fly deduplication
    
    if not os.path.exists(csv_path):
        print(f"Error: File {csv_path} not found.")
        return []

    with open(csv_path, "r") as file:
        lines = file.readlines()
        
    # Start loop at index 1 to skip header row as planned
    for line_idx, raw_line in enumerate(lines[1:], start=1):
        row = raw_line.strip().split(',')
        
        # Skip blank lines safely
        if not row or row == [''] or len(row) < 6:
            continue
            
        # Extract variables from list indexes
        raw_prj_id = row[0]
        raw_h_num = row[1]
        raw_zone = row[2]
        raw_target_len = row[3]
        raw_completed_len = row[4]
        raw_date = row[5]
        
        # ----------------------------------------------------
        # GATE 1: Project ID Validation & Deduplication
        # ----------------------------------------------------
        project_id = raw_prj_id.strip()
        if not project_id.isalnum():
            print(f"[Line {line_idx}] Rejected: Project ID '{project_id}' is missing or not alphanumeric.")
            continue
            
        project_id = project_id.upper()
        
        # Dynamic check against your track set
        if project_id in seen_project_ids:
            print(f"[Line {line_idx}] Filtered: Project ID '{project_id}' is a duplicate record.")
            continue
            
        # ----------------------------------------------------
        # GATE 2: Highway Number Standardization
        # ----------------------------------------------------
        h_num_raw = raw_h_num.strip()
        if not h_num_raw.replace("-", "").isalnum() or h_num_raw == "":
            print(f"[Line {line_idx}] Rejected: Highway Number '{h_num_raw}' is invalid or missing.")
            continue
            
        h_num_upper = h_num_raw.upper()
        if "-" not in h_num_upper and len(h_num_upper) > 2:
            h_num_upper = h_num_upper[:2] + "-" + h_num_upper[2:]
            
        # ----------------------------------------------------
        # GATE 3: Zone Title Case & Set Lookup
        # ----------------------------------------------------
        zone_raw = raw_zone.strip()
        if len(zone_raw) > 0:
            zone_clean = zone_raw[0].upper() + zone_raw[1:].lower()
        else:
            zone_clean = ""
            
        if zone_clean not in VALID_ZONES:
            print(f"[Line {line_idx}] Rejected: Zone '{zone_raw}' does not match official lookups.")
            continue

        # ----------------------------------------------------
        # GATE 4: Target Length Conversion & "km" Removal
        # ----------------------------------------------------
        target_len_clean = raw_target_len.strip().lower().replace("km", "")
        try:
            target_length = int(target_len_clean)
        except ValueError:
            print(f"[Line {line_idx}] Rejected: Target Length '{raw_target_len}' contains corrupt text characters.")
            continue

        # ----------------------------------------------------
        # GATE 5: Completed Length & N/A to None Handling
        # ----------------------------------------------------
        comp_len_raw = raw_completed_len.strip().upper()
        if comp_len_raw in ("N/A", "NULL", "", "NONE"):
            completed_length = None
        else:
            try:
                completed_length = float(comp_len_raw)
            except ValueError:
                print(f"[Line {line_idx}] Rejected: Completed Length '{raw_completed_len}' is corrupted.")
                continue

        # ----------------------------------------------------
        # GATE 6: Logical Sanity Check (Completed <= Target)
        # ----------------------------------------------------
        if completed_length is not None and completed_length > target_length:
            print(f"[Line {line_idx}] Rejected: Logical Anomaly. Completed Length ({completed_length}) exceeds Target ({target_length}).")
            continue

        # ----------------------------------------------------
        # GATE 7: Multi-Alias Manual Date Standardization
        # ----------------------------------------------------
        date_raw = raw_date.strip()
        standardized_date = None
        year = month = day = None
        
        # Branch A: Handle Continuous 8-Digit Arrays (YYYYMMDD, YYYYDDMM, etc.)
        if len(date_raw) == 8 and date_raw.isdigit():
            if 2000 <= int(date_raw[0:4]) <= 2040:  # Year at front
                year = date_raw[0:4]
                partA, partB = date_raw[4:6], date_raw[6:8]
                if int(partA) > 12:  # YYYYDDMM
                    day, month = partA, partB
                else:  # YYYYMMDD
                    month, day = partA, partB
            elif 2000 <= int(date_raw[4:8]) <= 2040:  # Year at back
                year = date_raw[4:8]
                partA, partB = date_raw[0:2], date_raw[2:4]
                if int(partA) > 12:  # DDMMYYYY
                    day, month = partA, partB
                else:  # MMDDYYYY
                    month, day = partA, partB
            else:
                print(f"[Line {line_idx}] Rejected: Date '{date_raw}' has invalid 4-digit century position.")
                continue

            if year is not None and month is not None and day is not None:
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    standardized_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

        # Branch B: Handle Delimited Formats (using '-' or '/')
        else:
            parts = date_raw.replace('/', '-').split('-')
            if len(parts) == 3:
                p1, p2, p3 = parts[0], parts[1], parts[2]
                
                # Check 4-digit components
                if len(p1) == 4 and p1.isdigit():
                    year, month, day = p1, p2, p3
                elif len(p3) == 4 and p3.isdigit():
                    year = p3
                    if p1.isdigit() and int(p1) > 12:  # DD-MM-YYYY
                        day, month = p1, p2
                    else:  # MM-DD-YYYY
                        month, day = p1, p2
                        
                # Check 2-digit aliases (YYMMDD, YYDDMM, DDMMYY, MMDDYY)
                elif len(p1) == 2 and len(p2) == 2 and len(p3) == 2 and p1.isdigit() and p2.isdigit() and p3.isdigit():
                    if 20 <= int(p1) <= 35:  # Year at front
                        year = f"20{p1}"
                        if int(p2) > 12:  # YYDDMM
                            day, month = p2, p3
                        else:  # YYMMDD
                            month, day = p2, p3
                    elif 20 <= int(p3) <= 35:  # Year at back
                        year = f"20{p3}"
                        if int(p1) > 12:  # DDMMYY
                            day, month = p1, p2
                        else:  # MMDDYY
                            month, day = p1, p2
                else:
                    print(f"[Line {line_idx}] Rejected: Date '{date_raw}' has invalid segment configurations.")
                    continue
                
                # Final assignment check for Branch B segments
                if year is not None and month is not None and day is not None:
                    if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                        standardized_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

        # Final structural Gate for Date verification
        if not standardized_date:
            print(f"[Line {line_idx}] Rejected: Date '{date_raw}' could not be logically standardized.")
            continue

        # ----------------------------------------------------
        # GATE 8: Commitment to State Tracking
        # ----------------------------------------------------
        seen_project_ids.add(project_id)
        final_clean_records.append({
            "Project_ID": project_id,
            "Highway_Number": h_num_upper,
            "Zone": zone_clean,
            "Target_Length_KM": target_length,
            "Completed_Length": completed_length,
            "Inspection_Date": standardized_date
        })
        
    return final_clean_records

# Execute pipeline execution testing

cleaned_data = (run_cleaning_pipeline(file_name))

print("\n--- CLEANED OUTPUT DATA ---")
for record in cleaned_data:
    print(record)


#     from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class StudentRecord(BaseModel):
#     enrollment_id: int
#     name: str
#     marks: float

# @app.post("/api/v1/process-record")
# def process_data(record: StudentRecord):
#     # Simulate data engineering transformation (e.g., status classification)
#     grade = "Pass" if record.marks >= 40.0 else "Fail"
#     return {
#         "status": "success",
#         "processed_student": record.name,
#         "result": grade
#     }





# # import streamlit as st
# # import requests

# # st.title("Data Engineering Student Processing Dashboard")

# # enrollment = st.number_input("Enrollment ID", min_value=1000)
# # name = st.text_input("Student Name")
# # marks = st.slider("Marks", 0.0, 100.0, 50.0)

# # if st.button("Submit to Backend API"):
# #     payload = {"enrollment_id": enrollment, "name": name, "marks": marks}
    
# #     # POST request to FastAPI backend
# #     response = requests.post("http://127.0.0.1:8000/api/v1/process-record", json=payload)
    
# #     if response.status_code == 200:
# #         st.json(response.json())
# #     else:
# #         st.error("API Connection Failed")

      