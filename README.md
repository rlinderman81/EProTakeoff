# Lighting Takeoff MVP

Minimal proof‑of‑concept that detects lighting fixtures on MEP plans
and returns an automated take‑off.

## Stack
* **Backend** – FastAPI + YOLOv8  
* **Frontend** – React (Vite) + Tailwind  
* **Model** – `ultralytics` YOLOv8 (you must supply a trained checkpoint at `backend/models/light_yolov8.pt`)

---

## Quick Start

### 1. Clone / download

```bash
unzip takeoff_mvp.zip && cd takeoff_mvp
```

### 2. Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be live at <http://localhost:8000>.

### 3. Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Vite dev server runs on <http://localhost:5173>.

### 4. Upload & Detect

1. Choose a plan (image/PDF)  
2. Click **Run Detection**  
3. See light count + bounding box data

---

## Exporting to Excel

Not included in MVP – easiest path is using `pandas.ExcelWriter`
on the backend. Add an endpoint like `/export` that returns an
`.xlsx` built from the `detections` dictionary.

## Next Steps

* Training a robust lighting‑symbol detector  
* Auto‑scaling & unit conversion  
* Revision comparison & overlay  
* Area / linear take‑offs  
* Export filters & grouping
