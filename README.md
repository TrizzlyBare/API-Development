# 🧩 FastAPI Double API - Dockerized

โครงงานตัวอย่างสำหรับสร้าง API 2 ตัว โดยใช้ภาษา Python + FastAPI และ deploy ด้วย Docker Compose  
ระบบนี้เหมาะสำหรับเรียนรู้การทำงานร่วมกันของหลาย API (Microservices) แบบง่ายๆ

---

## 📋 รายละเอียดตามเงื่อนไข

| เงื่อนไข                                            | สถานะ                                        |
| --------------------------------------------------- | -------------------------------------------- |
| ✅ สร้าง API 2 ตัว                                  | ใช้ FastAPI สำหรับ API1 และ API2             |
| ✅ Listen ที่ port ใดก็ได้                          | API1: `5055`, API2: `6066`                   |
| ✅ API1 request ต่อไปยัง API2 แล้วส่งกลับไปยัง User | ทำผ่าน `/proxy`                              |
| ✅ มีการ Print logs ทั้ง API1 และ API2              | ใช้ `logging` ทั้งคู่                        |
| ✅ endpoint และคำตอบอะไรก็ได้                       | `/proxy` → `/hello`, ตอบ `"Hello from API2"` |
| ✅ Deploy บน `docker-compose.yml`                   | ใช้ `docker-compose up --build`              |
| ✅ ส่งงานผ่าน GitHub/GitLab public                  | ✅ โปรเจกต์พร้อม push ขึ้น repo ได้เลย       |
| ✅ เขียน README.md บอกวิธี deploy และทดสอบ          | ✔️ ตามนี้ครับ                                |

---

## 🧠 คำอธิบายโปรเจกต์

ระบบนี้ประกอบด้วย 2 APIs:

- **API1 (port 5055):** รับ request จากผู้ใช้ → forward ไปยัง API2 → ตอบกลับผลลัพธ์
- **API2 (port 6066):** ตอบข้อความ `Hello from API2 on port 6066!`

ระบบนี้ deploy ได้ในไม่กี่วินาทีด้วย Docker Compose และสามารถนำไปต่อยอดได้ง่าย เช่นเพิ่ม DB, Auth, หรือ AI module

---

## 🛠️ เทคโนโลยีที่ใช้

- Python 3.10
- FastAPI
- Uvicorn
- Docker
- Docker Compose

---

## 🚀 วิธี Deploy และทดสอบ

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-deploy-api.git
cd ai-deploy-api
```

> 📝 เปลี่ยน `your-username` เป็นชื่อ GitHub ของคุณ

---

### 2. รันด้วย Docker Compose

```bash
docker-compose up --build
```

ระบบจะสร้าง container 2 ตัว:

- `api1` → Listen บน port `5055`
- `api2` → Listen บน port `6066`

---

### 3. ทดสอบ API

#### ➤ เรียก API1 (ซึ่งจะ request ไป API2 อัตโนมัติ):

```bash
curl http://localhost:5055/proxy
```

📤 คำตอบที่ได้:

```json
{
  "api1": "Success",
  "api2_response": {
    "message": "Hello from API2 on port 6066!"
  }
}
```

#### ➤ หรือเรียก API2 ตรงๆ:

```bash
curl http://localhost:6066/hello
```

📤 คำตอบ:

```json
{
  "message": "Hello from API2 on port 6066!"
}
```

---

## 🐳 Ports

| Service | Port | Endpoint |
| ------- | ---- | -------- |
| API1    | 5055 | `/proxy` |
| API2    | 6066 | `/hello` |

---

## 🪵 Logging

เมื่อรัน `docker-compose`, จะเห็น log แบบนี้ใน console:

```
api1  | INFO:     API1: Received request from user.
api1  | INFO:     API1: Forwarded request to API2.
api2  | INFO:     API2: Received request from API1.
```

---

## 🔓 การเปิด Public Repo

1. Push โปรเจกต์ขึ้น GitHub หรือ GitLab
2. ตั้งค่า repository เป็น **public**
3. ส่งลิงก์ให้ผู้ตรวจเช็คได้ทันที เช่น:
   ```
   https://github.com/your-username/ai-deploy-api
   ```

---

## 📁 โครงสร้างโฟลเดอร์

```
ai-deploy-api/
├── api1/
│   ├── main.py
│   └── Dockerfile
├── api2/
│   ├── main.py
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📌 หมายเหตุเพิ่มเติม

- หากต้องการเปลี่ยน port → แก้ `main.py`, `Dockerfile` และ `docker-compose.yml` ให้ตรงกัน
- หากต้องการเปลี่ยน endpoint เช่น `/proxy` → `/fetch`, ก็เปลี่ยนใน `api1/main.py`

---

## 🙋 Support

ต้องการให้เพิ่มฟีเจอร์อื่น เช่น AI, DB, Auth, หรือสอน deploy ขึ้น Cloud → ทักมาได้ครับ!
