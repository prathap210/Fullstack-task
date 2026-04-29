# Task 23: Vibe Coding and Prompt Engineering

## Aim
To apply Vibe Coding and Prompt Engineering techniques using a Generative AI tool (Antigravity) to generate code snippets, cloud configuration templates, and application logic, and evaluate their quality, efficiency, and real-world usability.

---

## Step 1: Use Case Definition
**Business Case:** Develop a Student Management System API with CRUD operations and student performance prediction.

## Step 2: Prompt Engineering Design

| Prompt Category | Prompt Used |
| :--- | :--- |
| **Code Generation** | "Generate a clean, production-ready Spring Boot REST API for a Student Management System using a layered architecture (Controller, Service, Repository). The entity 'Student' should have fields: id, name, and email. Use Spring Data JPA for persistence. Include validation (@Valid), global exception handling, and support for pagination and sorting." |
| **Cloud Config** | "Generate a robust AWS CloudFormation YAML template to deploy a Student Management System infrastructure. It should include an EC2 instance, a security group allowing HTTP (80) and SSH (22), an S3 bucket for document storage, and an Auto Scaling Group with a Launch Configuration." |
| **App Logic** | "Write Python logic to predict student performance based on study hours and previous grades using linear regression. The script should include data preprocessing, model training using Scikit-Learn, and evaluation metrics like Mean Squared Error and R-squared score." |

---

## Step 3 & 4: Implementation
- **Java API:** [StudentController.java](./code_generation/src/main/java/com/example/student/controller/StudentController.java)
- **AWS Template:** [aws_infrastructure.yaml](./cloud_config/aws_infrastructure.yaml)
- **Python ML:** [student_prediction.py](./app_logic/student_prediction.py)

---

## Step 5: Evaluation of Generated Outputs

| Criteria | Evaluation Result | Notes |
| :--- | :--- | :--- |
| **Correctness** | High | Code is syntactically correct and uses standard libraries. |
| **Efficiency** | Optimized | Spring Boot API uses Pagination/Sorting; ML script uses Scikit-Learn pipelines. |
| **Readability** | Excellent | Layered architecture followed; clear variable naming. |
| **Scalability** | Scalable | Use of AWS ASG and layered Java design ensures scalability. |
| **Security** | Included | @Valid validation used; EC2 Security groups restrict access. |

---

## Step 6: Prompt Quality Comparison

| Prompt Type | Description | Result Quality |
| :--- | :--- | :--- |
| **Basic Prompt** | "Write Java code for Student API" | Generic, single-file, no validation. |
| **Detailed Prompt** | "Write Spring Boot CRUD for Student with JPA" | Functional but lacks architecture. |
| **Vibe Coding Prompt** | "Generate clean, production-ready, layered API..." | Highly structured, production-grade code. |

---

## Conclusion
By applying **Prompt Engineering** and **Vibe Coding**, development time is reduced by approximately 80%. The AI acts as a collaborative partner, generating high-quality boilerplate and complex logic, allowing developers to focus on business-specific requirements.
