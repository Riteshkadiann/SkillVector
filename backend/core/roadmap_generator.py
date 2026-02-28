from typing import List, Dict
from utils.skill_taxonomy import get_resources, SKILL_TO_CATEGORY

SKILL_DURATION = {
    "machine learning":3,"deep learning":3,"cybersecurity":3,"cyber security":3,
    "system design":3,"distributed systems":3,"kubernetes":3,"network security":3,
    "penetration testing":3,"data science":3,"aws":2,"gcp":2,"azure":2,"docker":2,
    "postgresql":2,"mongodb":2,"nlp":2,"computer vision":2,"tensorflow":2,"pytorch":2,
    "data structures":2,"algorithms":2,"react":2,"nextjs":2,"django":2,"spark":2,
    "kafka":2,"terraform":2,"microservices":2,"ruby on rails":2,"rails":2,
    "scalability":2,"version control systems":1,"version control":1,
}

def _get_duration(skill: str) -> int:
    s = skill.lower().strip()
    if s in SKILL_DURATION:
        return SKILL_DURATION[s]
    cat = SKILL_TO_CATEGORY.get(s, "")
    if cat in ("cybersecurity","ml_ai","system_design","data_engineering"):
        return 2
    return 1


# ─── Every resource set: 3 items, NO "Ask ChatGPT" (that's in the project) ───
SKILL_RESOURCES = {
    "bash":                    ["Bash Official Docs", "Bash on Exercism.io", "The Linux Command Line (free book)"],
    "shell scripting":         ["Bash Official Docs", "Bash on Exercism.io", "The Linux Command Line (free book)"],
    "linux":                   ["OverTheWire Bandit Wargames", "Linux Journey (linuxjourney.com)", "Ryan's Linux Tutorial"],
    "linux terminal":          ["OverTheWire Bandit Wargames", "Linux Journey (linuxjourney.com)", "Ryan's Linux Tutorial"],
    "scalability":             ["Designing Data-Intensive Applications (Kleppmann)", "ByteByteGo by Alex Xu", "High Scalability Blog"],
    "version control":         ["Pro Git Book (free at git-scm.com)", "GitHub Skills (skills.github.com)", "Atlassian Git Tutorials"],
    "version control systems": ["Pro Git Book (free at git-scm.com)", "GitHub Skills (skills.github.com)", "Atlassian Git Tutorials"],
    "svn":                     ["SVN Book (svnbook.red-bean.com)", "Atlassian SVN Guide", "TortoiseSVN Docs"],
    "git":                     ["Pro Git Book (free)", "GitHub Skills", "Oh My Git! interactive game"],
    "github":                  ["GitHub Skills (skills.github.com)", "GitHub Docs", "GitHub Actions Quickstart"],
    "python":                  ["Real Python (realpython.com)", "Python.org Official Docs", "LeetCode Python Track"],
    "javascript":              ["javascript.info", "MDN Web Docs", "FreeCodeCamp JS Course"],
    "typescript":              ["TypeScript Handbook (typescriptlang.org)", "Total TypeScript by Matt Pocock", "Execute Program"],
    "java":                    ["Baeldung.com", "Java Docs (oracle.com)", "CodeWithMosh Java Course"],
    "c#":                      ["Microsoft C# Docs", "C# Corner", "Tim Corey YouTube Channel"],
    "c++":                     ["learncpp.com", "cppreference.com", "The Cherno C++ YouTube Series"],
    "go":                      ["Tour of Go (go.dev/tour)", "Go by Example", "Boot.dev Go Course"],
    "rust":                    ["The Rust Book (doc.rust-lang.org)", "Rustlings exercises", "Jon Gjengset YouTube"],
    "ruby":                    ["Ruby Docs", "The Odin Project Ruby", "Ruby Koans"],
    "rails":                   ["Rails Guides (guides.rubyonrails.org)", "GoRails.com", "The Odin Project Rails"],
    "ruby on rails":           ["Rails Guides (guides.rubyonrails.org)", "GoRails.com", "The Odin Project Rails"],
    "vba":                     ["Excel VBA – Chandoo.org", "Excel Macro Mastery", "ExcelJet VBA Reference"],
    ".net":                    ["Microsoft .NET Docs", "C# Corner", "Scott Hanselman .NET YouTube"],
    "asp.net":                 ["ASP.NET Core Docs", "Tim Corey YouTube", "Traversy Media ASP.NET"],
    "react":                   ["React Official Docs (react.dev)", "Scrimba React Course", "Jack Herrington YouTube"],
    "nextjs":                  ["Next.js Docs (nextjs.org/docs)", "Next.js Learn (nextjs.org/learn)", "Vercel Blog"],
    "vue":                     ["Vue.js Docs (vuejs.org)", "Vue Mastery", "Traversy Media Vue"],
    "angular":                 ["Angular Docs (angular.io)", "Angular University", "Academind Angular Course"],
    "svelte":                  ["Svelte Docs (svelte.dev)", "Svelte Tutorial (svelte.dev/tutorial)", "Fireship Svelte"],
    "node.js":                 ["Node.js Docs", "The Odin Project Node", "Academind NodeJS Course"],
    "express":                 ["Express.js Docs", "FreeCodeCamp Express Tutorial", "Traversy Media Express"],
    "express.js":              ["Express.js Docs", "FreeCodeCamp Express Tutorial", "Traversy Media Express"],
    "django":                  ["Django Docs (djangoproject.com)", "Django Girls Tutorial", "TestDriven.io Django"],
    "flask":                   ["Flask Docs (flask.palletsprojects.com)", "Flask Mega-Tutorial by Grinberg", "CoreySchafer Flask YT"],
    "fastapi":                 ["FastAPI Docs (fastapi.tiangolo.com)", "TestDriven.io FastAPI", "ArjanCodes FastAPI YT"],
    "graphql":                 ["GraphQL.org Docs", "Apollo GraphQL Tutorials", "Fireship GraphQL"],
    "rest api":                ["RESTful API Design – restfulapi.net", "Postman Learning Center", "HTTP Cats (for fun + learning)"],
    "rest apis":               ["RESTful API Design – restfulapi.net", "Postman Learning Center", "HTTP Cats (for fun + learning)"],
    "rest":                    ["RESTful API Design – restfulapi.net", "Postman Learning Center", "Phil Sturgeon API Design"],
    "postgresql":              ["PostgreSQL Docs", "pgExercises.com", "Use The Index, Luke (use-the-index-luke.com)"],
    "mysql":                   ["MySQL Docs", "SQLZoo", "PlanetScale MySQL for Developers"],
    "mongodb":                 ["MongoDB University (university.mongodb.com)", "MongoDB Docs", "Traversy Media MongoDB"],
    "redis":                   ["Redis Docs (redis.io/docs)", "Redis University", "TryRedis (try.redis.io)"],
    "sql":                     ["SQLZoo (sqlzoo.net)", "Mode Analytics SQL Tutorial", "LeetCode SQL 50 Problems"],
    "database design":         ["CMU Database Systems (free lectures)", "Designing Data-Intensive Applications", "Database Design – freeCodeCamp YT"],
    "relational databases":    ["CMU Database Systems (free lectures)", "PostgreSQL Docs", "SQLZoo"],
    "nosql":                   ["MongoDB University", "Redis University", "AWS DynamoDB Docs"],
    "aws":                     ["AWS Skill Builder (skillbuilder.aws)", "AWS Free Tier Tutorials", "A Cloud Guru AWS CCP"],
    "ec2":                     ["AWS EC2 Docs", "AWS EC2 Tutorial – Adrian Cantrill", "Linux Server Hardening Guide"],
    "s3":                      ["AWS S3 Docs", "S3 Hosting Guide", "AWS S3 + CloudFront Tutorial"],
    "gcp":                     ["Google Cloud Skills Boost", "GCP YouTube Channel", "Coursera GCP Fundamentals"],
    "google cloud":            ["Google Cloud Skills Boost", "GCP YouTube Channel", "Coursera GCP Fundamentals"],
    "azure":                   ["Microsoft Learn (learn.microsoft.com)", "AZ-900 Study Guide", "John Savill Azure YT"],
    "docker":                  ["Docker Docs (docs.docker.com)", "Play with Docker (labs.play-with-docker.com)", "TechWorld with Nana Docker YT"],
    "kubernetes":              ["Kubernetes Docs (kubernetes.io)", "KodeKloud K8s Course", "TechWorld with Nana K8s YT"],
    "terraform":               ["Terraform Docs (developer.hashicorp.com)", "HashiCorp Learn", "KodeKloud Terraform"],
    "ci/cd":                   ["GitHub Actions Docs", "GitLab CI/CD Docs", "CircleCI University"],
    "github actions":          ["GitHub Actions Docs", "GitHub Actions Marketplace", "Fireship GitHub Actions"],
    "machine learning":        ["fast.ai Practical ML (fast.ai)", "Coursera ML Specialization – Andrew Ng", "Kaggle ML Courses"],
    "deep learning":           ["fast.ai Deep Learning (fast.ai)", "DeepLearning.AI Specialization", "d2l.ai Book (free)"],
    "nlp":                     ["Hugging Face NLP Course (huggingface.co/course)", "Stanford CS224N (free lectures)", "Speech & Language Processing – Jurafsky"],
    "computer vision":         ["fast.ai Computer Vision", "Stanford CS231n (free lectures)", "OpenCV Python Tutorial"],
    "pytorch":                 ["PyTorch Docs + Tutorials (pytorch.org)", "Andrej Karpathy Neural Networks YT", "Zero to Mastery PyTorch"],
    "tensorflow":              ["TensorFlow Docs (tensorflow.org)", "DeepLearning.AI TF Dev Certificate", "Kaggle TF Tutorials"],
    "scikit-learn":            ["Scikit-learn Docs", "Kaggle ML Course", "Hands-On ML by Aurélien Géron"],
    "pandas":                  ["Pandas Docs (pandas.pydata.org)", "Kaggle Pandas Course", "Effective Pandas – Matt Harrison"],
    "numpy":                   ["NumPy Docs (numpy.org)", "CS231n NumPy Tutorial", "Scientific Python Lectures (scipy-lectures.org)"],
    "feature engineering":     ["Feature Engineering for ML – Alice Zheng (book)", "Kaggle Feature Engineering Course", "Towards Data Science Articles"],
    "model deployment":        ["FastAPI + MLflow Deployment Guide", "BentoML Docs", "AWS SageMaker Docs"],
    "etl":                     ["dbt Docs (docs.getdbt.com)", "Apache Airflow Docs", "FreeCodeCamp Data Engineering YT"],
    "data structures":         ["NeetCode 150 (neetcode.io)", "CLRS Algorithms Book", "CS50 by Harvard (cs50.harvard.edu)"],
    "algorithms":              ["NeetCode.io", "AlgoExpert", "Abdul Bari Algorithms YT"],
    "oop":                     ["Refactoring.Guru", "Head First Design Patterns (book)", "ArjanCodes OOP YT"],
    "operating systems":       ["Operating Systems: Three Easy Pieces (ostep.org – free)", "MIT 6.004", "Neso Academy OS YT"],
    "system design":           ["Designing Data-Intensive Applications (Kleppmann)", "ByteByteGo by Alex Xu", "Grokking System Design"],
    "microservices":           ["Microservices.io Patterns", "Sam Newman – Building Microservices (book)", "Chris Richardson Microservices"],
    "cybersecurity":           ["TryHackMe Beginner Path (tryhackme.com)", "CompTIA Security+ Study Guide", "OWASP Learning Gateway"],
    "network security":        ["CompTIA Network+ Study Guide", "Professor Messer Security+ YT", "Cybrary Network Security"],
    "penetration testing":     ["TryHackMe", "Hack The Box Academy", "TCM Security Practical Ethical Hacking"],
    "owasp":                   ["OWASP Top 10 Docs (owasp.org)", "PortSwigger Web Security Academy (free)", "OWASP Testing Guide"],
    "collaboration":           ["Atlassian Teamwork Blog", "Crucial Conversations (book)", "Google re:Work Team Guides"],
    "communication":           ["Toastmasters (toastmasters.org)", "Crucial Conversations (book)", "HBR Communication Articles"],
    "leadership":              ["Leaders Eat Last – Simon Sinek", "The Manager's Path (book)", "Harvard ManageMentor"],
    "agile":                   ["Scrum Guide (scrumguides.org)", "Agile Manifesto (agilemanifesto.org)", "Mountain Goat Software"],
    "documentation":           ["Divio Documentation System", "Google Dev Docs Style Guide", "Write the Docs Community"],
    # ── Security & Operations ─────────────────────────────────────────────────
    "access control":          ["ASIS International (asisonline.org)", "Security Industry Association Docs", "TryHackMe Physical Security Room"],
    "surveillance":            ["ASIS Security Management Magazine", "CCTV Training – IPVM (ipvm.com)", "Security Guard College Online"],
    "patrolling":              ["Security Guard Training Manual – Ontario", "ASIS International", "Ontario Security Guard License Study Guide"],
    "incident reporting":      ["Security Guard Training Manual – Ontario", "Effective Incident Reports – ASIS", "Ontario Security Guard License Study Guide"],
    "verbal de-escalation":    ["CPI Crisis Prevention Institute (crisisprevention.com)", "Verbal Judo by George Thompson (book)", "Ontario MCSCS De-escalation Resources"],
    "de-escalation":           ["CPI Crisis Prevention Institute (crisisprevention.com)", "Verbal Judo by George Thompson (book)", "Ontario MCSCS Resources"],
    "conflict resolution":     ["CPI Crisis Prevention Institute", "Crucial Conversations (book)", "Ontario Security Guard License Study Guide"],
    "emergency response":      ["St. John Ambulance Canada", "Ontario OHSA Resources", "Red Cross First Aid Certification"],
    "first aid":               ["St. John Ambulance Canada (sja.ca)", "Red Cross First Aid", "Ontario First Aid Requirements – OHSA"],
    "cpr":                     ["St. John Ambulance Canada (sja.ca)", "Red Cross CPR Course", "Heart & Stroke Foundation Canada"],
    "whmis":                   ["CCOHS WHMIS 2015 (ccohs.ca)", "Ontario WHMIS Training – IHSA", "SafetyDriven WHMIS Course"],
    "aoda":                    ["AccessON (ontario.ca/aoda)", "Ontario AODA Training Resources", "ARCH Disability Law Centre"],
    "ohsa":                    ["Ontario OHSA (ontario.ca/ohsa)", "IHSA Safety Training (ihsa.ca)", "WSIB Ontario"],
    "radio communication":     ["APCO International Training", "Security Radio Procedures Guide", "Ontario Security Guard License Study Guide"],
    "situational awareness":   ["ASIS International", "Left of Bang by Patrick Van Horne (book)", "Security Management Magazine"],
    "concierge":               ["Concierge Alliance of America", "Les Clefs d'Or Canada", "LinkedIn Learning Hospitality Courses"],
    "hospitality":             ["AHLA Hospitality Training (ahla.com)", "Cornell eCornell Hospitality Courses", "LinkedIn Learning Hospitality"],
    "property services":       ["BOMA Canada (bomacanada.ca)", "Real Property Institute of Canada", "LinkedIn Learning Facilities Management"],
    "digital signage":         ["Digital Signage Federation (digitalsignagefederation.org)", "Screenly Docs", "LinkedIn Learning Digital Signage"],
    "interpersonal communication": ["Toastmasters (toastmasters.org)", "Crucial Conversations (book)", "Coursera Communication Skills"],
    "organizational aptitude": ["Getting Things Done by David Allen (book)", "Coursera Time Management", "LinkedIn Learning Organizational Skills"],
    "multi-tasking":           ["Getting Things Done by David Allen", "LinkedIn Learning Productivity", "Coursera Work Smarter, Not Harder"],
    "customer service":        ["LinkedIn Learning Customer Service", "Coursera Customer Service Fundamentals", "Help Scout Academy (helpscout.com/academy)"],
    "microsoft word":          ["Microsoft Learn (learn.microsoft.com)", "GCFGlobal Word Tutorial (gcfglobal.org)", "LinkedIn Learning Word"],
    "microsoft excel":         ["Microsoft Learn Excel", "ExcelJet (exceljet.net)", "Chandoo.org Excel Training"],
    "excel":                   ["ExcelJet (exceljet.net)", "Chandoo.org Excel Training", "Microsoft Learn Excel"],
    "outlook":                 ["Microsoft Learn Outlook", "GCFGlobal Outlook Tutorial", "LinkedIn Learning Outlook"],
    "scheduling":              ["Calendly Best Practices", "LinkedIn Learning Time Management", "Coursera Project Scheduling"],
    "documentation":           ["Divio Documentation System", "Google Dev Docs Style Guide", "Write the Docs Community"],
    "building compliance":     ["BOMA Canada (bomacanada.ca)", "Ontario Building Code (ontario.ca)", "LinkedIn Learning Facilities Compliance"],
    "front-of-house":          ["AHLA Front Office Operations Course", "LinkedIn Learning Hospitality", "Cornell eCornell Hotel Management"],
    "security protocols":      ["ASIS International (asisonline.org)", "Ontario Security Guard License Study Guide", "Security Management Magazine"],
    "log management":          ["Security Guard Training Manual", "ASIS Incident Documentation Guide", "Ontario MCSCS Resources"],
    "id verification":         ["Identity Verification Best Practices – ASIS", "Jumio Identity Verification Guide", "Security Guard Training Manual"],

    "pytest":                  ["pytest Docs (docs.pytest.org)", "Real Python pytest Guide", "Brian Okken – Python Testing with pytest"],
    "jest":                    ["Jest Docs (jestjs.io)", "Testing Library Docs", "Kent C. Dodds Testing Course"],
    "postman":                 ["Postman Learning Center", "REST API Testing with Postman", "Valentin Despa Postman YT"],
    "application development": ["The Pragmatic Programmer (book)", "Clean Code by Robert Martin", "Refactoring.Guru"],
    "web development":         ["The Odin Project (free)", "FreeCodeCamp", "MDN Web Docs"],
    "web services":            ["RESTful Web Services – O'Reilly (book)", "Postman Learning Center", "MDN HTTP Docs"],
    "software deployment":     ["The DevOps Handbook", "GitHub Actions Docs", "DigitalOcean Deployment Tutorials"],
    "full-stack development":  ["The Odin Project (free)", "Full Stack Open (fullstackopen.com)", "Traversy Media"],
}

# ─── Unique, specific, impressive projects for every skill ────────────────────
SPECIFIC_PROJECTS = {
    # ── Shell / Linux ─────────────────────────────────────────────────────────
    "bash":               "Write a Bash automation script that monitors a directory for new files, logs changes with timestamps, and sends a desktop alert. Add error handling and make it run as a cron job.",
    "shell scripting":    "Write a Bash automation script that monitors a directory for new files, logs changes with timestamps, and sends a desktop alert. Add error handling and make it run as a cron job.",
    "linux":              "Set up a Linux VPS from scratch: configure UFW firewall, create a non-root sudo user, install Nginx, set up SSL with Let's Encrypt, and enable automatic security updates.",
    "linux terminal":     "Complete OverTheWire Bandit levels 0–20 — each level teaches a real Linux concept. Write a cheatsheet documenting every command you used.",

    # ── Version Control ───────────────────────────────────────────────────────
    "version control systems": "Take an existing project and implement a full Git workflow: feature branches, pull request template, commit message convention (Conventional Commits), branch protection rules, and a CHANGELOG.md.",
    "version control":         "Take an existing project and implement a full Git workflow: feature branches, pull request template, commit message convention (Conventional Commits), branch protection rules, and a CHANGELOG.md.",
    "svn":                     "Migrate a small project from SVN to Git: preserve commit history, set up a .gitignore, document the migration steps in a README, and add a GitHub Actions CI pipeline.",
    "git":                     "Master advanced Git: practice interactive rebase, cherry-pick, bisect for bug hunting, and stash. Write a team Git workflow guide with diagrams.",
    "github":                  "Build a fully automated GitHub repository: README with badges, GitHub Actions CI (lint + test + build), issue templates, PR templates, and a GitHub Pages documentation site.",

    # ── Scalability / Architecture ────────────────────────────────────────────
    "scalability":        "Take a slow API endpoint in one of your existing projects, profile it, add database indexes, implement Redis caching, and document the before/after latency with benchmarks. Write a blog post on what you learned.",
    "system design":      "Design a URL shortener from scratch: write a 2-page design doc covering architecture diagram, database schema, caching strategy, rate limiting, and capacity estimates. Present it like a real interview.",
    "microservices":      "Refactor a monolith into 3 microservices (auth, data, API gateway) with Docker Compose, inter-service HTTP calls, and shared logging. Document every architectural decision in an ADR.",
    "distributed systems":"Build a simplified distributed key-value store in Python with consistent hashing, node replication, and failure detection. Benchmark reads/writes under load.",

    # ── Cloud ─────────────────────────────────────────────────────────────────
    "aws":                "Deploy a full-stack app to AWS: EC2 behind an Application Load Balancer, RDS PostgreSQL, S3 for file storage, CloudFront CDN, Route 53 domain, and SSL cert via ACM. Document the architecture.",
    "ec2":                "Launch an EC2 instance, harden it (disable root login, configure SSH keys, UFW firewall), install Nginx as a reverse proxy, and set up a systemd service for auto-restart on crash.",
    "s3":                 "Build a file upload service: pre-signed URLs for direct browser-to-S3 uploads, lifecycle rules to move old files to Glacier, and a CloudFront CDN in front. Show before/after load time.",
    "azure":              "Deploy a containerized .NET or Node.js app to Azure App Service with CI/CD from GitHub Actions, Azure Key Vault for secrets, and Application Insights for monitoring.",
    "gcp":                "Deploy a containerized FastAPI app to Cloud Run (serverless), connect it to Cloud SQL, set up Cloud Logging, and configure a CI/CD pipeline via Cloud Build.",
    "google cloud":       "Deploy a containerized FastAPI app to Cloud Run (serverless), connect it to Cloud SQL, set up Cloud Logging, and configure a CI/CD pipeline via Cloud Build.",
    "docker":             "Dockerize a full-stack app (React frontend + FastAPI backend + PostgreSQL). Use Docker Compose for local dev, multi-stage builds to minimize image size, and health checks.",
    "kubernetes":         "Deploy a 3-tier app on Minikube: Deployment, Service, Ingress, ConfigMap, and Secret. Add a HorizontalPodAutoscaler. Write a runbook explaining each component.",
    "terraform":          "Provision a full AWS environment with Terraform: VPC, EC2, RDS, S3 bucket with versioning, and IAM roles. Store state in S3 with DynamoDB locking. No manual console clicks.",
    "ci/cd":              "Build a production-grade GitHub Actions pipeline: lint → unit tests → integration tests → Docker build → push to ECR → deploy to EC2. Add Slack notifications on failure.",

    # ── Languages ─────────────────────────────────────────────────────────────
    "python":             "Build a CLI job scraper in Python that hits a public jobs API, filters by keywords, ranks results by skill match, and exports a report to CSV — use argparse, requests, and pandas.",
    "javascript":         "Build a vanilla JS offline-capable Kanban board: drag-and-drop, localStorage persistence, keyboard shortcuts, and a dark mode toggle — zero frameworks, zero dependencies.",
    "typescript":         "Migrate an existing JavaScript project to strict TypeScript. Eliminate all implicit `any` types, add Zod for runtime validation, and write a migration guide in the README.",
    "java":               "Build a thread-safe in-memory task queue in Java using concurrency primitives (BlockingQueue, ExecutorService). Write JUnit tests proving thread safety under concurrent load.",
    "c#":                 "Build a .NET Web API with Entity Framework Core, JWT authentication, role-based authorization, input validation with FluentValidation, and full Swagger documentation.",
    "c++":                "Implement a memory-safe dynamic array (like std::vector) from scratch in C++ with RAII, move semantics, and iterator support. Write unit tests with GoogleTest.",
    "go":                 "Build a concurrent web scraper in Go: goroutines for parallel fetching, channels for result aggregation, rate limiting with a semaphore, and graceful shutdown on SIGINT.",
    "rust":               "Build a CLI file encryption tool in Rust using AES-256-GCM. Implement key derivation with Argon2, file chunking for large files, and a progress bar with indicatif.",
    "ruby":               "Build a Ruby CLI tool that parses a GitHub user's public repos, calculates their top languages, and generates a Markdown report — use the GitHub API and httparty gem.",
    "rails":              "Build a multi-user Rails blog with Devise authentication, role-based access (admin/editor/reader), image uploads via Active Storage + S3, and full test coverage with RSpec.",
    "ruby on rails":      "Build a multi-user Rails blog with Devise authentication, role-based access (admin/editor/reader), image uploads via Active Storage + S3, and full test coverage with RSpec.",
    "vba":                "Build an Excel VBA macro suite that: cleans messy CSV imports, generates a pivot table summary, emails a formatted report via Outlook, and runs on a daily schedule.",
    ".net":               "Build a .NET 8 Web API with Entity Framework, CQRS pattern using MediatR, FluentValidation, Serilog structured logging, and a GitHub Actions CI pipeline.",
    "asp.net":            "Build an ASP.NET Core MVC app with Identity authentication, SQLite database, CRUD operations, model validation, and deploy it to Azure App Service.",

    # ── Web Frameworks ────────────────────────────────────────────────────────
    "react":              "Build a real-time GitHub profile dashboard: search any username, display repos sorted by stars, live activity feed using polling, and a dark mode — deploy to Vercel.",
    "nextjs":             "Build a personal portfolio + blog with Next.js App Router: MDX blog posts, ISR for dynamic content, OpenGraph image generation, sitemap.xml, and Lighthouse score > 95.",
    "vue":                "Build a personal finance tracker with Vue 3 Composition API: add/categorize expenses, chart spending by month with Chart.js, export to CSV, and persist data with Pinia.",
    "django":             "Build a multi-user task management API with Django REST Framework: JWT auth, nested serializers, filtering/ordering/pagination, and 90%+ test coverage with pytest-django.",
    "flask":              "Build a URL shortener with Flask: custom short codes, click analytics (country, referrer, timestamp), rate limiting per IP, and a simple admin dashboard.",
    "fastapi":            "Build an async FastAPI job board API: JWT auth, async SQLAlchemy with PostgreSQL, background tasks for email notifications, Redis caching, and auto-generated Swagger docs.",
    "node.js":            "Build a real-time collaboration tool with Node.js + Socket.io: multiple rooms, user presence indicators, message history from Redis, and graceful reconnection handling.",
    "express":            "Build a production-ready Express.js REST API: middleware stack (helmet, cors, rate-limit, morgan), Joi validation, structured error handling, and Jest integration tests.",
    "express.js":         "Build a production-ready Express.js REST API: middleware stack (helmet, cors, rate-limit, morgan), Joi validation, structured error handling, and Jest integration tests.",
    "graphql":            "Add a GraphQL layer to an existing REST API using Apollo Server: queries, mutations, subscriptions, DataLoader for N+1 prevention, and query depth limiting.",

    # ── Databases ─────────────────────────────────────────────────────────────
    "postgresql":         "Design a normalized e-commerce schema (users, products, orders, reviews). Write 10 complex queries using window functions, CTEs, and full-text search. Add indexes and measure query plan improvements.",
    "mysql":              "Insert 1 million rows into a test table, benchmark 5 slow queries, add appropriate indexes, re-benchmark, and document the exact performance gains in a README.",
    "mongodb":            "Build a product catalog API with MongoDB Atlas: complex aggregation pipeline for analytics (top products by revenue, category trends), text search index, and Atlas Search.",
    "redis":              "Add Redis caching to 3 slow endpoints in an existing project. Implement cache invalidation on write, measure latency before/after, and add a cache hit-rate metric to a dashboard.",
    "sql":                "Solve 30 LeetCode SQL problems (Easy → Hard). Write a blog post or Notion doc explaining window functions, CTEs, and subqueries with real examples from the problems you solved.",
    "database design":    "Design a database for a hospital system: patients, doctors, appointments, prescriptions, billing. Apply 3NF normalization, write an ER diagram, and justify every design decision.",
    "relational databases":"Design a normalized relational schema for a social network (users, posts, comments, likes, followers). Write queries for a news feed, trending posts, and mutual friends.",
    "nosql":              "Compare MongoDB vs Redis vs DynamoDB for 3 different use cases. Build a small proof-of-concept for each, document query patterns, and write a trade-off analysis.",

    # ── ML / AI / Data ────────────────────────────────────────────────────────
    "machine learning":   "Build an end-to-end ML pipeline: data cleaning → EDA → feature engineering → train 3 models → compare with cross-validation → deploy best model as a FastAPI endpoint with input validation.",
    "deep learning":       "Train a CNN on CIFAR-10: experiment with dropout, batch normalization, and learning rate scheduling. Log all experiments to Weights & Biases and write a report comparing results.",
    "nlp":                "Fine-tune a HuggingFace BERT model for sentiment analysis on a real dataset (IMDB or Yelp reviews). Deploy it as an API, evaluate precision/recall/F1, and write a model card.",
    "computer vision":    "Build a real-time object detection app with YOLO running on webcam input. Add custom class fine-tuning on a dataset you label yourself with Roboflow.",
    "pytorch":            "Implement a transformer from scratch following Andrej Karpathy's 'Neural Networks: Zero to Hero' series. Train it on a small text dataset and generate coherent text.",
    "tensorflow":         "Build and deploy a TensorFlow.js model that classifies hand gestures in the browser using the webcam — zero server, runs entirely client-side.",
    "scikit-learn":       "Build an ML project comparing 5 classifiers (Logistic Regression, Random Forest, SVM, KNN, XGBoost) on a real dataset. Use GridSearchCV for tuning, SHAP for explainability.",
    "pandas":             "Analyze the NYC Taxi dataset (1M+ rows): clean messy data, engineer features, answer 5 business questions with charts, and write a Jupyter notebook formatted like a data science portfolio piece.",
    "numpy":              "Implement linear regression, logistic regression, k-means clustering, and a 2-layer neural network from scratch using only NumPy. Benchmark against scikit-learn equivalents.",
    "feature engineering":"Take a Kaggle competition dataset, apply 10 feature engineering techniques (encoding, scaling, interaction terms, target encoding), measure impact on model AUC, and document each technique.",
    "model deployment":   "Deploy an ML model as a FastAPI service: versioned endpoints, input schema validation with Pydantic, model loading from MLflow registry, health check endpoint, and a Docker image.",
    "etl":                "Build an ETL pipeline with Apache Airflow: extract from a public API daily, transform with pandas, load to PostgreSQL, add data quality checks, and email alerts on failure.",

    # ── CS Fundamentals ───────────────────────────────────────────────────────
    "data structures":    "Implement stack, queue, singly/doubly linked list, BST, AVL tree, heap, and hash map from scratch in Python — no built-ins. Write unit tests for each, then solve 20 LeetCode problems using them.",
    "algorithms":         "Complete NeetCode Blind 75 (neetcode.io). For every pattern you learn (sliding window, two pointers, dynamic programming, etc.), write a one-page explanation with a diagram. Make it a public Notion doc.",
    "oop":                "Refactor a messy procedural Python script into clean OOP following SOLID principles. Apply at least 3 design patterns (Factory, Observer, Strategy). Write before/after comparison.",
    "operating systems":  "Build a simple Unix shell in C: parse commands, handle pipes (|), input/output redirection (>, <), background processes (&), and Ctrl+C signal handling. Add a brief README explaining each system call.",

    # ── Security ──────────────────────────────────────────────────────────────
    "cybersecurity":      "Complete TryHackMe 'Pre-Security' + 'Jr Penetration Tester' path. Write a professional writeup for 3 rooms explaining vulnerability, exploitation steps, and how to fix it as a developer.",
    "network security":   "Set up a home lab: pfSense firewall, VLANs, Wireshark packet capture, and an IDS with Suricata. Document a simulated attack and detection flow.",
    "penetration testing":"Complete 5 HackTheBox 'Starting Point' machines. Write a professional penetration test report for each: scope, findings, CVSS score, evidence, and remediation steps.",
    "owasp":              "Audit one of your own web apps against the OWASP Top 10. Fix every finding, document the vulnerable code vs. fixed code, and write a security report as if presenting to a CTO.",

    # ── DevOps / Deployment ───────────────────────────────────────────────────
    "software deployment": "Set up a complete deployment pipeline: code push → GitHub Actions CI (tests pass) → Docker image built and pushed to DockerHub → auto-deployed to a DigitalOcean droplet via SSH. Zero manual steps.",
    "ci/cd":               "Build a production-grade GitHub Actions pipeline: lint → unit tests → integration tests → Docker build → push to registry → deploy to cloud. Add Slack notifications and rollback on failure.",

    # ── Web / Frontend ────────────────────────────────────────────────────────
    "web development":     "Build a fully responsive personal portfolio site from scratch (HTML/CSS/JS — no frameworks): smooth scroll, dark mode, animated skill bars, a working contact form via Formspree, and Lighthouse score > 90.",
    "web services":        "Build a RESTful web service that consumes 2 external APIs (weather + news), aggregates the data, and exposes a unified endpoint with caching, error handling, and API key management via environment variables.",
    "front-end development":"Build a complex interactive UI component (data table with sort/filter/pagination, or a multi-step form wizard) using only vanilla JS. No frameworks. Document the component API like a real design system.",
    "application development":"Build a complete CRUD app from scratch with authentication, authorization, input validation, error handling, logging, and tests. Document the architecture in a README with diagrams.",
    "full-stack development": "Build a full-stack app (React frontend + FastAPI backend + PostgreSQL): user auth, real-time updates via WebSockets, deployed on a VPS with Nginx + SSL. Write a 1-page architecture doc.",

    # ── Soft skills ───────────────────────────────────────────────────────────
    "communication":      "Record a 5-minute Loom video walking through one of your technical projects as if presenting to a hiring manager. Post it as a LinkedIn article explaining the problem, solution, and what you learned.",
    "leadership":         "Find an open-source project on GitHub with 'good first issue' tags. Fix 2 bugs, open a PR with a clear description, respond to review comments professionally, and get it merged.",
    "collaboration":      "Contribute to a real open-source project: review an existing PR and leave constructive feedback, open a well-documented bug report, and fix a documented issue. Show the full collaboration thread.",
    "agile":              "Run a real 2-week sprint on one of your own projects using GitHub Projects: write user stories, estimate with story points, hold a retrospective, and document velocity. Treat it like a real job.",
    "documentation":      "Write complete documentation for one of your projects: README, API docs with Swagger/OpenAPI examples, architecture decision records (ADRs), and a getting-started guide that a stranger could follow.",
    # ── Security & Hospitality ────────────────────────────────────────────────
    "access control":          "Create a professional 1-page Access Control Procedures document for a hypothetical building: entry/exit protocols, visitor log process, key/card issuance, and emergency lockdown steps. Format it as a real site SOP.",
    "surveillance":            "Write a mock CCTV Monitoring Report for a 4-hour shift: time-stamped observations, 2 simulated incidents (suspicious activity + unauthorized access attempt), escalation steps taken, and outcome. Format like a real security report.",
    "patrolling":              "Design a Patrol Schedule and Checklist for a 3-floor office building: checkpoint locations, inspection criteria, shift handover notes, and a daily log template. Present it as a real site document.",
    "incident reporting":      "Write 3 professional Incident Reports for different scenarios: slip-and-fall, unauthorized access, and a fire alarm activation. Use formal security report language — include time, location, persons involved, action taken, and follow-up.",
    "verbal de-escalation":    "Research the CPI Crisis Prevention Model and write a 1-page guide on verbal de-escalation techniques. Include 3 real-world scenario role-plays (agitated visitor, trespasser, medical emergency) with the exact language you would use.",
    "de-escalation":           "Research the CPI Crisis Prevention Model and write a 1-page guide on verbal de-escalation techniques. Include 3 real-world scenario role-plays with the exact language you would use in each situation.",
    "conflict resolution":     "Write a professional Conflict Resolution Procedure for a security site: stages of escalation, communication techniques at each stage, when to call for backup, and post-incident documentation steps.",
    "emergency response":      "Create an Emergency Response Quick Reference Card (one page, laminated-format) covering: fire evacuation, medical emergency, unauthorized intruder, and power failure. Include radio call scripts for each scenario.",
    "first aid":               "Complete or refresh your Standard First Aid & CPR Level C certification. Write a 1-page First Aid Incident Response Checklist for a workplace, covering the 5 most common workplace injuries and the correct response protocol.",
    "cpr":                     "Complete or refresh your CPR Level C certification via St. John Ambulance or Red Cross. Practice the full sequence on a mannequin. Write out the full BLS (Basic Life Support) protocol in your own words as a reference card.",
    "whmis":                   "Complete the CCOHS free WHMIS 2015 online course (ccohs.ca). Create a WHMIS reference sheet listing all 9 hazard pictograms, what they mean, and 2 real workplace examples of each.",
    "aoda":                    "Complete the AODA online training (ontario.ca). Write a short reflection: 3 specific ways a concierge or security guard would apply AODA principles in their daily role, with real examples.",
    "ohsa":                    "Study the Ontario OHSA worker rights and responsibilities. Write a 1-page OHSA Rights & Responsibilities Summary covering: right to refuse unsafe work, reporting procedure, and employer duties — formatted as a real workplace handout.",
    "radio communication":     "Study the phonetic alphabet and 10-code radio protocol. Practice by writing out 5 realistic security radio transmissions using proper format (unit ID, location, situation, action). Record yourself saying them if possible.",
    "situational awareness":   "Read the core concepts of 'Left of Bang' (color code awareness system). Apply it by writing a detailed observation log for a real public space you visit: people, behaviors, anomalies, and your assessment — like a real security professional.",
    "concierge":               "Create a Concierge Welcome Package for a hypothetical luxury office building: building overview, amenities guide, local dining/transit recommendations, emergency contacts, and FAQs. Format it as a real tenant-facing document.",
    "hospitality":             "Write a Guest Experience Standard Operating Procedure for a front-of-house role: greeting protocol, handling complaints, escalation steps, and follow-up communication. Include email templates for common guest requests.",
    "property services":       "Create a monthly Property Inspection Checklist for an office building: lobby, washrooms, fitness centre, parking, exterior. Include severity rating for each item and the work order escalation path.",
    "digital signage":         "Learn a free digital signage tool (Screenly OSE or Canva Display). Create 3 professional building announcement slides — an event notice, a policy update, and a seasonal message — at screen-appropriate dimensions.",
    "interpersonal communication": "Record a 3-minute video introducing yourself professionally as if greeting a key executive tenant. Then write a formal follow-up email after a tenant complaint, demonstrating professional tone, empathy, and resolution.",
    "organizational aptitude": "Take one real week of tasks (personal or work) and manage them in Notion or Trello: prioritize by urgency/importance matrix, set deadlines, and write an end-of-week review. Screenshot the board as your portfolio artifact.",
    "multi-tasking":           "Document a real or simulated shift scenario where you manage 3 simultaneous demands (phone call + visitor + delivery). Write a time-log showing how you prioritized each, and what communication you used to manage all three.",
    "customer service":        "Write a Customer Service Excellence Guide for a security/concierge hybrid role: greeting standards, complaint handling with the HEART model (Hear, Empathize, Apologize, Resolve, Thank), and a self-assessment checklist.",
    "microsoft excel":         "Build a real Excel workbook for a security site: visitor log with auto-formatting, incident tracker with dropdown severity, and a monthly summary dashboard with charts. Use formulas, conditional formatting, and data validation.",
    "excel":                   "Build a real Excel workbook for a security site: visitor log with auto-formatting, incident tracker with dropdown severity, and a monthly summary dashboard with charts. Use formulas, conditional formatting, and data validation.",
    "microsoft word":          "Create a complete Security Site Document Package in Word: daily activity log template, incident report form, handover briefing template, and visitor register — all professionally formatted with headers, tables, and your name/logo.",
    "building compliance":     "Research the Ontario Building Code and BOMA standards for commercial properties. Write a Building Compliance Checklist for a property manager covering fire safety, accessibility, elevator compliance, and signage requirements.",
    "front-of-house":          "Design a Front-of-House Operations Manual for a premier office lobby: daily opening/closing checklist, visitor greeting protocol, phone etiquette script, and appearance standards — formatted as an onboarding document for new staff.",
    "scheduling":              "Build a 2-week staff scheduling template in Excel or Google Sheets for a 3-person concierge team: shift coverage, break times, cross-training notes, and an availability tracker. Add conditional formatting for overtime.",
    "security protocols":      "Write a Site-Specific Security Protocol document for a hypothetical office building: access control procedures, CCTV monitoring schedule, incident response flowchart, and guard communication protocol.",

}


def _get_micro_project(skill: str) -> str:
    s = skill.lower().strip()
    if s in SPECIFIC_PROJECTS:
        return SPECIFIC_PROJECTS[s]
    # Partial match on first word(s)
    for key, proj in SPECIFIC_PROJECTS.items():
        if s.startswith(key) or key.startswith(s):
            return proj
    # Category-based fallback — still specific, uses the skill name
    cat = SKILL_TO_CATEGORY.get(s, "")
    if cat == "cybersecurity":
        return f"Complete a TryHackMe room focused on {skill}. Write a professional writeup covering the vulnerability, exploitation, and how to remediate it as a developer."
    elif cat == "ml_ai":
        return f"Train a {skill} model on a real Kaggle dataset. Log experiments, evaluate with proper metrics (not just accuracy), and deploy the best model as a REST API endpoint."
    elif cat == "cloud_devops":
        return f"Provision {skill} infrastructure using code (Terraform or CloudFormation). Deploy a real app on it, set up monitoring, and document the architecture with a diagram."
    elif cat == "web_frameworks":
        return f"Build a production-ready CRUD API using {skill}: authentication, input validation, error handling, structured logging, and at least 80% test coverage."
    elif cat == "databases":
        return f"Design a real-world schema using {skill} for an app of your choice. Write 10 queries of increasing complexity, add indexes, measure query plan improvements with EXPLAIN."
    elif cat == "programming_languages":
        return f"Build a CLI tool in {skill} that solves a real problem you have. Add argument parsing, error handling, logging, and unit tests. Write a README that explains installation and usage."
    elif cat == "computer_science":
        return f"Implement core {skill} concepts from scratch without using built-in libraries. Write unit tests proving correctness, then solve 10 LeetCode problems that require this knowledge."
    elif cat == "testing":
        return f"Add comprehensive {skill} tests to one of your existing projects. Aim for 80%+ coverage, include edge cases and failure paths, and set up coverage reporting in your CI pipeline."
    elif cat == "soft_skills":
        return f"Apply {skill} in a real setting: contribute to a team project, open-source repo, or run a mock sprint. Document the outcome and write a reflection on what improved."
    # Universal fallback
    return (
        f"Learn {skill} using the resources above, then build a small but complete project that demonstrates it. "
        f"Focus on one real use case, handle errors properly, and write a README explaining what you built and why."
    )


def _get_resources(skill: str) -> List[str]:
    s = skill.lower().strip()
    # Use local curated list first
    if s in SKILL_RESOURCES:
        return SKILL_RESOURCES[s]
    for key in SKILL_RESOURCES:
        if key in s or s.startswith(key.split()[0]):
            return SKILL_RESOURCES[key]
    # Category fallback — real resources, no "Ask ChatGPT" here
    cat = SKILL_TO_CATEGORY.get(s, "")
    if cat == "cybersecurity":
        return ["TryHackMe (tryhackme.com)", "PortSwigger Web Security Academy (free)", "OWASP Docs (owasp.org)"]
    elif cat == "ml_ai":
        return ["fast.ai (fast.ai)", "Kaggle Courses (kaggle.com/learn)", "Papers with Code (paperswithcode.com)"]
    elif cat == "cloud_devops":
        return ["Official Cloud Provider Docs", "KodeKloud", "TechWorld with Nana YT"]
    elif cat == "programming_languages":
        return [f"{skill.title()} Official Docs", f"{skill.title()} on Exercism.io", "LeetCode"]
    elif cat == "databases":
        return [f"{skill.title()} Official Docs", "SQLZoo (sqlzoo.net)", "CMU Database Systems (free)"]
    elif cat == "soft_skills":
        return ["Coursera Professional Skills Courses", "LinkedIn Learning", "HBR Articles (hbr.org)"]
    return [f"{skill.title()} Official Documentation", "YouTube tutorials", "Coursera or Udemy"]


def _get_duration(skill: str) -> int:
    s = skill.lower().strip()
    if s in SKILL_DURATION:
        return SKILL_DURATION[s]
    cat = SKILL_TO_CATEGORY.get(s, "")
    if cat in ("cybersecurity", "ml_ai", "system_design", "data_engineering"):
        return 2
    return 1


def generate_roadmap(priority_skills: List[Dict], weeks: int = 8) -> List[Dict]:
    roadmap = []
    current_week = 1
    for item in priority_skills:
        if current_week > weeks:
            break
        skill    = item["skill"]
        duration = _get_duration(skill)
        end_week = min(current_week + duration - 1, weeks)
        week_label = f"Week {current_week}" if current_week == end_week else f"Week {current_week}–{end_week}"

        roadmap.append({
            "week":             week_label,
            "skill":            skill,
            "importance_score": item.get("importance_score", 0),
            "resources":        _get_resources(skill),
            "micro_project":    _get_micro_project(skill),
            "duration_weeks":   duration,
            "completed":        False,
        })
        current_week = end_week + 1
    return roadmap
