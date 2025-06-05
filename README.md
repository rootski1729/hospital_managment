🏥 Healthcare Backend API
A scalable and secure RESTful backend system for managing hospital operations using Django REST Framework, JWT authentication, PostgreSQL, and Docker. Designed for deployment on AWS EC2.

🚀 Features
Admin user registration and JWT-based login.

CRUD operations for Patients and Doctors.

Mapping between Patients and Doctors with validation.

Role-based access using Django’s is_staff (admin control only).

Dockerized PostgreSQL database (running on EC2).

Secure API access with permissions and validations.

🧱 Tech Stack
Python 3.10+

Django 4.x

Django REST Framework

djangorestframework-simplejwt

PostgreSQL (via Docker)

AWS EC2 (Ubuntu)

🧑‍💻 API Endpoints
🔐 Authentication (Admin Only)
Method	Endpoint	Description
POST	/api/auth/register/	Register a new admin user
POST	/api/auth/login/	Login and get JWT tokens

🧑 Patients
Method	Endpoint	Description
GET	/api/patients/	List all patients
POST	/api/patients/	Create a new patient
GET	/api/patients/<id>/	Retrieve patient details
PUT	/api/patients/<id>/	Update a patient
DELETE	/api/patients/<id>/	Delete a patient

👨‍⚕️ Doctors
Method	Endpoint	Description
GET	/api/doctors/	List all doctors
POST	/api/doctors/	Create a new doctor
GET	/api/doctors/<id>/	Retrieve doctor details
PUT	/api/doctors/<id>/	Update a doctor
DELETE	/api/doctors/<id>/	Delete a doctor

🔗 Patient-Doctor Mapping
Method	Endpoint	Description
GET	/api/mappings/	List all mappings
POST	/api/mappings/	Assign a doctor to a patient
GET	/api/mappings/<patient_id>/	Get doctors assigned to a specific patient
DELETE	/api/mappings/<id>/	Remove doctor from patient (mapping only)

🐳 Docker Setup for PostgreSQL on EC2
1. Launch Dockerized PostgreSQL
bash
Copy
Edit
docker run --name postgres-container \
  -e POSTGRES_DB=healthcare \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -d postgres
🔐 Be sure to restrict your EC2 Security Group to allow port 5432 access only from your app.
