# ─── Master Skill Taxonomy ────────────────────────────────────────────────────
# This is a SUPPLEMENT to free-form NLP extraction — not a filter.
# Skills NOT in this taxonomy can still be detected and shown.

SKILL_TAXONOMY = {
    "programming_languages": [
        "python","javascript","typescript","java","c#","c++","c","go","rust",
        "kotlin","swift","php","ruby","scala","r","matlab","perl","bash",
        "shell scripting","powershell","dart","elixir","haskell","lua","vba",
    ],
    "web_frameworks": [
        "react","angular","vue","nextjs","nuxtjs","svelte","django","flask",
        "fastapi","express","express.js","node.js","nestjs","spring boot","spring",
        "rails","ruby on rails","laravel","asp.net",".net","graphql",
        "rest api","rest apis","rest","grpc","websockets","tailwind css","bootstrap",
        "material ui","jquery","backbone.js",
        "web development","web services","front-end development","frontend development",
        "backend development","full-stack development","application development",
        "software development","software deployment","apis","api development",
        "api integration","web application","web applications",
    ],
    "databases": [
        "postgresql","mysql","mongodb","redis","sqlite","oracle","cassandra",
        "elasticsearch","dynamodb","firebase","supabase","cockroachdb","neo4j",
        "influxdb","mariadb","mssql","database design","database optimization",
        "query optimization","orm","prisma","sqlalchemy","sequelize","sql",
        "databases","relational databases","relational database",
        "relational database management systems","rdbms","nosql",
    ],
    "cloud_devops": [
        "aws","ec2","s3","lambda","rds","cloudfront","iam","vpc","eks","ecs",
        "sqs","sns","api gateway","gcp","google cloud","bigquery","cloud run",
        "azure","azure functions","azure devops","docker","kubernetes","terraform",
        "ansible","pulumi","ci/cd","github actions","jenkins","gitlab ci","circleci",
        "linux","nginx","apache","microservices","serverless","prometheus","grafana",
        "datadog","cloudwatch","linux terminal","software deployment",
    ],
    "ml_ai": [
        "machine learning","deep learning","nlp","natural language processing",
        "computer vision","tensorflow","pytorch","scikit-learn","keras","pandas",
        "numpy","matplotlib","seaborn","plotly","hugging face","transformers",
        "openai api","langchain","llm","rag","vector database","xgboost",
        "lightgbm","random forest","data analysis","data visualization",
        "feature engineering","model deployment","mlflow","cuda",
    ],
    "data_engineering": [
        "spark","apache spark","hadoop","kafka","apache kafka","airflow","dbt",
        "snowflake","databricks","data pipeline","etl","elt","data warehouse",
        "data lake","data modeling","data quality",
    ],
    "cybersecurity": [
        "cybersecurity","cyber security","network security","application security",
        "appsec","penetration testing","ethical hacking","vulnerability assessment",
        "owasp","owasp top 10","sast","dast","threat modeling","incident response",
        "siem","firewall","ids","ips","vpn","ssl","tls","encryption","cryptography",
        "pki","zero trust","security audit","devsecops","soc","burp suite","nmap",
        "metasploit","wireshark","identity management","oauth","jwt","saml",
        "compliance","gdpr","hipaa","iso 27001","soc2",
    ],
    "system_design": [
        "system design","software architecture","microservices architecture",
        "distributed systems","api design","database design","scalability",
        "high availability","fault tolerance","caching","message queues",
        "event-driven architecture","design patterns","solid principles",
        "clean architecture","domain-driven design","ddd","cqrs","event sourcing",
    ],
    "computer_science": [
        "data structures","algorithms","oop","object-oriented programming",
        "functional programming","concurrency","multithreading","operating systems",
        "computer networks","memory management","big o notation","recursion",
        "dynamic programming","version control systems","version control",
    ],
    "mobile": [
        "react native","flutter","android","ios","swift","kotlin","xamarin",
        "expo","mobile development",
    ],
    "testing": [
        "unit testing","integration testing","end-to-end testing","jest","pytest",
        "selenium","cypress","playwright","tdd","test-driven development","bdd",
        "mocking","performance testing","load testing","k6","jmeter",
    ],
    "tools": [
        "git","github","gitlab","bitbucket","jira","confluence","figma","postman",
        "insomnia","vscode","intellij","pycharm","jupyter","tableau","power bi",
        "excel","notion","slack","vim","tmux","ssh","svn","subversion",
    ],
    "operations_security": [
        "access control", "surveillance", "cctv", "patrolling", "patrol",
        "crowd management", "traffic management", "incident reporting",
        "incident report", "daily activity logs", "conflict resolution",
        "verbal de-escalation", "de-escalation", "emergency response",
        "emergency services", "safety compliance", "radio communication",
        "situational awareness", "physical stamina", "loss prevention",
        "security guard", "security license", "ontario security guard license",
        "concierge", "hospitality", "property services", "tenant relations",
        "guest services", "customer service", "public interaction",
        "event coordination", "amenities management", "lobby operations",
        "access cards", "digital signage", "work orders",
        "first aid", "cpr", "cpr level c", "standard first aid",
        "whmis", "aoda", "ohsa", "fall protection",
        "ppe", "g2 license", "driver's license", "drivers license",
        "microsoft word", "microsoft excel", "microsoft outlook",
        "word", "excel", "outlook", "powerpoint",
        "scheduling", "multi-tasking", "prioritization",
        "interpersonal communication", "interpersonal skills",
        "organizational skills", "organizational aptitude",
        "report writing", "log management", "id verification",
        "building compliance", "front-of-house", "pet policy",
        "event support", "tenant satisfaction", "property management",
        "janitorial coordination", "security protocols", "site protocols",
        "crowd control", "unauthorized access", "suspicious activity",
        "vehicle movement", "pedestrian management", "barricades",
        "move-in coordination", "delivery management",
    ],
    "soft_skills": [
        "communication","leadership","teamwork","collaboration","agile","scrum",
        "kanban","project management","problem solving","critical thinking",
        "time management","mentoring","presentation","technical writing",
        "documentation","adaptability","attention to detail",
    ],
}

CATEGORY_PRIORITY = {
    "cybersecurity":         1,
    "programming_languages": 2,
    "system_design":         2,
    "computer_science":      2,
    "cloud_devops":          3,
    "ml_ai":                 3,
    "web_frameworks":        3,
    "databases":             4,
    "data_engineering":      4,
    "mobile":                5,
    "testing":               5,
    "tools":                 6,
    "operations_security":   3,
    "soft_skills":           7,
}

SKILL_TO_CATEGORY = {}
for _cat, _skills in SKILL_TAXONOMY.items():
    for _skill in _skills:
        SKILL_TO_CATEGORY[_skill.lower()] = _cat

ALL_SKILLS = []
for _skills in SKILL_TAXONOMY.values():
    ALL_SKILLS.extend(_skills)

def get_skill_priority(skill: str) -> int:
    cat = SKILL_TO_CATEGORY.get(skill.lower(), "unknown")
    return CATEGORY_PRIORITY.get(cat, 5)

def is_soft_skill(skill: str) -> bool:
    return SKILL_TO_CATEGORY.get(skill.lower(), "") == "soft_skills"

# ─── Curated Learning Resources ───────────────────────────────────────────────
SKILL_RESOURCES = {
    "python":           ["Python.org Official Docs","Real Python","LeetCode Python Track"],
    "javascript":       ["javascript.info","MDN Web Docs","FreeCodeCamp JS Course"],
    "typescript":       ["TypeScript Handbook","Total TypeScript by Matt Pocock","Execute Program"],
    "java":             ["Java Docs","Baeldung.com","CodeWithMosh Java Course"],
    "c#":               ["Microsoft C# Docs","C# Corner","Tim Corey YouTube"],
    "go":               ["Tour of Go","Go by Example","Boot.dev Go Course"],
    "rust":             ["The Rust Book","Rustlings","Jon Gjengset YouTube"],
    "ruby":             ["Ruby Docs","The Odin Project Ruby","Ruby Koans"],
    "rails":            ["Rails Guides","GoRails.com","Odin Project Rails"],
    "ruby on rails":    ["Rails Guides","GoRails.com","Odin Project Rails"],
    "react":            ["React Official Docs","Scrimba React Course","Jack Herrington YouTube"],
    "nextjs":           ["Next.js Docs","Next.js Learn Course","Vercel Blog"],
    "node.js":          ["Node.js Docs","The Odin Project Node","Academind NodeJS Course"],
    "express":          ["Express.js Docs","FreeCodeCamp Express Tutorial","Traversy Media Express"],
    "express.js":       ["Express.js Docs","FreeCodeCamp Express Tutorial","Traversy Media Express"],
    "fastapi":          ["FastAPI Docs","TestDriven.io FastAPI","ArjanCodes FastAPI YT"],
    "django":           ["Django Docs","Django Girls Tutorial","TestDriven.io Django"],
    "flask":            ["Flask Docs","Flask Mega-Tutorial by Grinberg","CoreySchafer Flask YT"],
    "graphql":          ["GraphQL.org Docs","Apollo GraphQL Tutorials","Fireship GraphQL"],
    "rest api":         ["RESTful API Design Guide","Postman Learning Center","Phil Sturgeon API Design"],
    "rest apis":        ["RESTful API Design Guide","Postman Learning Center","Phil Sturgeon API Design"],
    ".net":             ["Microsoft .NET Docs","C# Corner",".NET on YouTube by Scott Hanselman"],
    "asp.net":          ["ASP.NET Core Docs","Tim Corey YouTube","Traversy Media ASP.NET"],
    "postgresql":       ["PostgreSQL Docs","pgExercises.com","Use The Index, Luke"],
    "mysql":            ["MySQL Docs","SQLZoo MySQL","PlanetScale MySQL for Devs"],
    "mongodb":          ["MongoDB University","MongoDB Docs","Traversy Media MongoDB Course"],
    "redis":            ["Redis Docs","Redis University","TryRedis Interactive Tutorial"],
    "sql":              ["SQLZoo","Mode Analytics SQL Tutorial","LeetCode SQL 50"],
    "database design":  ["Database Design – freeCodeCamp YT","CMU Database Systems Course","DDIA Book"],
    "aws":              ["AWS Free Tier + Tutorials","AWS Skill Builder","A Cloud Guru AWS CCP"],
    "ec2":              ["AWS EC2 Docs","EC2 Tutorial – TechWithLucy","Linux Server Setup Guide"],
    "s3":               ["AWS S3 Docs","S3 Static Hosting Guide","AWS S3 + CloudFront Tutorial"],
    "gcp":              ["Google Cloud Skills Boost","GCP YouTube Channel","Coursera GCP Fundamentals"],
    "azure":            ["Microsoft Learn Azure","AZ-900 Prep Guide","John Savill Azure Masterclass YT"],
    "docker":           ["Docker Docs","Play with Docker","TechWorld with Nana Docker YT"],
    "kubernetes":       ["Kubernetes Docs","KodeKloud K8s Course","TechWorld with Nana K8s YT"],
    "terraform":        ["Terraform Docs","HashiCorp Learn","KodeKloud Terraform"],
    "ci/cd":            ["GitHub Actions Docs","GitLab CI/CD Docs","FreeCodeCamp CI/CD Tutorial"],
    "linux":            ["Linux Command Line Book","OverTheWire Bandit","Ryan's Linux Tutorial"],
    "svn":              ["SVN Book (svnbook.red-bean.com)","Atlassian SVN Tutorial","YouTube SVN to Git Migration"],
    "machine learning": ["fast.ai Practical ML","Coursera ML Specialization (Andrew Ng)","Kaggle ML Courses"],
    "deep learning":    ["fast.ai Deep Learning","DeepLearning.AI Specialization","d2l.ai Book"],
    "nlp":              ["Hugging Face NLP Course","Stanford CS224N","Speech & Language Processing (Jurafsky)"],
    "computer vision":  ["fast.ai CV","Stanford CS231n","OpenCV Python Tutorial"],
    "pytorch":          ["PyTorch Docs","PyTorch Tutorials","Andrej Karpathy Neural Networks YT"],
    "tensorflow":       ["TensorFlow Docs","DeepLearning.AI TF Dev Certificate","Kaggle TF"],
    "scikit-learn":     ["Scikit-learn Docs","Kaggle ML Course","Hands-On ML by Aurelien Geron"],
    "pandas":           ["Pandas Docs","Kaggle Pandas Course","Effective Pandas by Matt Harrison"],
    "numpy":            ["NumPy Docs","CS231n NumPy Tutorial","Scientific Python Lectures"],
    "langchain":        ["LangChain Docs","LangChain Cookbook","Alejandro AO LangChain YT"],
    "openai api":       ["OpenAI API Docs","OpenAI Cookbook","Fireship OpenAI Course"],
    "cybersecurity":    ["TryHackMe (Beginner Path)","CompTIA Security+ Study Guide","OWASP Learning Gateway"],
    "cyber security":   ["TryHackMe (Beginner Path)","CompTIA Security+ Study Guide","OWASP Learning Gateway"],
    "penetration testing": ["TryHackMe","Hack The Box","TCM Security Practical Ethical Hacking"],
    "network security": ["CompTIA Network+","Professor Messer Security+","Cybrary Network Security"],
    "owasp":            ["OWASP Top 10 Docs","PortSwigger Web Security Academy","OWASP Testing Guide"],
    "ethical hacking":  ["TCM Security Course","Hack The Box Academy","Kali Linux Revealed"],
    "encryption":       ["Cryptography I – Coursera Stanford","Practical Cryptography Book","Khan Academy Cryptography"],
    "devsecops":        ["Snyk Learn","OWASP DevSecOps Guideline","Udemy DevSecOps Bootcamp"],
    "system design":    ["Designing Data-Intensive Applications (Kleppmann)","ByteByteGo by Alex Xu","Grokking System Design"],
    "microservices":    ["Microservices.io Patterns","Sam Newman Building Microservices","Chris Richardson Microservices"],
    "distributed systems": ["DDIA Book","MIT 6.824 Distributed Systems","Martin Kleppmann YT"],
    "data structures":  ["NeetCode 150 (LeetCode)","CLRS Algorithms Book","CS50 by Harvard"],
    "algorithms":       ["NeetCode.io","AlgoExpert","Abdul Bari Algorithms YT"],
    "oop":              ["Refactoring.Guru OOP Patterns","Head First Design Patterns Book","ArjanCodes OOP YT"],
    "operating systems":["Operating Systems: Three Easy Pieces (free book)","MIT 6.004","Neso Academy OS YT"],
    "design patterns":  ["Refactoring.Guru","Head First Design Patterns","ArjanCodes YT"],
    "git":              ["Pro Git Book (free)","GitHub Skills","Oh My Git! Game"],
    "github":           ["GitHub Skills","GitHub Docs","Traversy Media Git & GitHub"],
    "postman":          ["Postman Learning Center","REST API Testing with Postman","Valentin Despa Postman YT"],
    "pytest":           ["pytest Docs","Real Python pytest Guide","Brian Okken pytest Book"],
    "jest":             ["Jest Docs","Testing Library Docs","Kent C. Dodds Testing Course"],
    "cypress":          ["Cypress Docs","Cypress Real World App","Gleb Bahmutov YT"],
    "unit testing":     ["Google Testing Blog","Martin Fowler Testing Articles","The Art of Unit Testing"],
    "vba":              ["Excel VBA Tutorial – Chandoo.org","Excel Macro Mastery","ExcelJet VBA Reference"],
    "communication":    ["Toastmasters","Crucial Conversations Book","HBR Communication Articles"],
    "leadership":       ["Leaders Eat Last – Simon Sinek","The Manager's Path Book","Harvard ManageMentor"],
    "agile":            ["Agile Manifesto","Scrum Guide (scrum.org)","Mountain Goat Software"],
    "documentation":    ["Divio Documentation System","Google Dev Docs Style Guide","Write the Docs Community"],
}

def get_resources(skill: str) -> list:
    """Return curated learning resources, with universal fallback."""
    skill_lower = skill.lower().strip()
    if skill_lower in SKILL_RESOURCES:
        return SKILL_RESOURCES[skill_lower]
    for key, resources in SKILL_RESOURCES.items():
        if key in skill_lower or skill_lower in key:
            return resources
    # Category-based fallback
    cat = SKILL_TO_CATEGORY.get(skill_lower, "")
    if cat == "cybersecurity":
        return ["TryHackMe","CompTIA Security+ Guide","OWASP Learning Gateway"]
    elif cat == "ml_ai":
        return ["fast.ai","Kaggle Courses","Papers with Code"]
    elif cat == "cloud_devops":
        return ["Official Cloud Docs","KodeKloud","TechWorld with Nana YT"]
    elif cat == "programming_languages":
        return [f"{skill.title()} Official Docs",f"{skill.title()} on Exercism.io","LeetCode"]
    elif cat == "databases":
        return [f"{skill.title()} Official Docs","SQLZoo","Database Design Book"]
    # Universal fallback
    return ["Official Documentation","Coursera or Udemy","YouTube Tutorial"]

# ─── NON-TECH SKILL TAXONOMY EXPANSION ────────────────────────────────────────
# Added so SkillVector works for security, hospitality, healthcare, legal, etc.
# These are appended to the existing taxonomy.

_NON_TECH_SKILLS = {

    "security": [
        "access control", "surveillance", "cctv", "cctv monitoring", "patrolling",
        "security patrolling", "crowd management", "crowd control", "traffic management",
        "incident reporting", "incident reports", "daily activity logs", "activity logs",
        "conflict resolution", "verbal de-escalation", "de-escalation", "emergency response",
        "safety compliance", "radio communication", "two-way radio", "situational awareness",
        "loss prevention", "access card", "access cards", "id verification",
        "security guard", "concierge security", "event security", "retail security",
        "foot patrol", "site patrol", "trespass enforcement", "unauthorized access prevention",
        "threat assessment", "report writing", "security report writing",
        "ontario security guard licence", "security guard licence", "security license",
        "first aid", "standard first aid", "cpr", "cpr level c", "first aid cpr",
        "fall protection", "whmis", "aoda", "ohsa", "health and safety",
        "ppe", "personal protective equipment", "radio", "key control",
        "physical stamina", "physical fitness", "mobile patrol",
    ],

    "hospitality_customer_service": [
        "customer service", "guest services", "client relations", "tenant relations",
        "front desk", "reception", "concierge", "hospitality", "property services",
        "event coordination", "event planning", "event support",
        "customer satisfaction", "complaint resolution", "conflict resolution",
        "interpersonal skills", "interpersonal communication", "public interaction",
        "front-of-house", "front of house", "lobby management", "building management",
        "amenity management", "digital signage", "building compliance",
        "move-in coordination", "move-out coordination", "access card management",
        "tenant satisfaction", "proactive service", "service standard",
        "multi-tasking", "multitasking", "time management", "prioritization",
        "professional demeanor", "polished demeanor",
    ],

    "healthcare_medical": [
        "patient care", "nursing", "clinical assessment", "medication administration",
        "vital signs", "ehr", "electronic health records", "phlebotomy",
        "wound care", "infection control", "triage", "healthcare",
        "bedside manner", "medical terminology", "hipaa", "patient advocacy",
        "cpr certification", "bls", "acls", "pals",
    ],

    "office_admin": [
        "microsoft word", "microsoft excel", "microsoft outlook", "microsoft office",
        "microsoft powerpoint", "ms office", "ms word", "ms excel",
        "outlook", "word", "powerpoint",
        "data entry", "scheduling", "calendar management", "file management",
        "record keeping", "administrative support", "office administration",
        "typing", "reception", "switchboard", "document management",
        "bookkeeping", "invoicing", "accounts payable", "accounts receivable",
        "quickbooks", "sage", "minute taking", "correspondence",
    ],

    "trades_technical": [
        "electrical", "plumbing", "hvac", "carpentry", "welding",
        "blueprint reading", "autocad", "cad", "site management",
        "construction management", "safety inspection", "quality control",
        "equipment operation", "forklift", "heavy equipment",
        "preventive maintenance", "troubleshooting", "mechanical",
    ],

    "retail_sales": [
        "sales", "retail", "merchandising", "inventory management", "stock management",
        "pos system", "point of sale", "cash handling", "cash register",
        "upselling", "cross-selling", "product knowledge", "store operations",
        "loss prevention", "visual merchandising", "customer retention",
        "crm", "salesforce", "hubspot", "lead generation", "cold calling",
        "b2b sales", "b2c sales", "account management",
    ],

    "finance_accounting": [
        "accounting", "financial analysis", "financial reporting", "bookkeeping",
        "accounts payable", "accounts receivable", "payroll", "tax preparation",
        "auditing", "budgeting", "forecasting", "gaap", "ifrs",
        "excel financial modeling", "financial modeling", "bloomberg",
        "cfa", "cpa", "variance analysis", "reconciliation",
    ],

    "marketing_creative": [
        "seo", "sem", "google ads", "facebook ads", "social media marketing",
        "content marketing", "email marketing", "copywriting", "content creation",
        "branding", "graphic design", "adobe photoshop", "adobe illustrator",
        "adobe premiere", "canva", "figma", "ui design", "ux design",
        "user research", "a/b testing", "google analytics", "hubspot",
        "mailchimp", "hootsuite", "wordpress", "shopify",
    ],

    "education_training": [
        "teaching", "curriculum development", "lesson planning", "classroom management",
        "instructional design", "e-learning", "lms", "moodle", "blackboard",
        "tutoring", "mentoring", "coaching", "facilitation", "training delivery",
        "needs assessment", "performance management",
    ],

    "legal": [
        "legal research", "contract drafting", "contract review", "litigation",
        "compliance", "regulatory compliance", "corporate law", "paralegal",
        "legal writing", "westlaw", "quicklaw", "due diligence",
        "intellectual property", "privacy law", "gdpr compliance",
    ],

    "logistics_supply_chain": [
        "supply chain", "logistics", "warehouse management", "inventory control",
        "procurement", "purchasing", "vendor management", "shipping",
        "receiving", "freight", "sap", "erp", "lean", "six sigma",
        "demand planning", "forecasting", "distribution", "last mile delivery",
    ],

    "certifications_licences": [
        "ontario security guard licence", "security guard license", "g2 license",
        "g license", "driver's license", "clean driver abstract",
        "first aid certification", "cpr certification", "whmis certification",
        "aoda training", "ohsa training", "fall protection certification",
        "smart serve", "food handler certificate", "servsafe",
        "forklift certification", "osha certification",
        "pmp", "scrum master", "six sigma certification",
        "aws certified", "google cloud certified", "azure certified",
    ],
}

# Append to existing taxonomy and rebuild ALL_SKILLS + SKILL_TO_CATEGORY
for _cat, _skills in _NON_TECH_SKILLS.items():
    SKILL_TAXONOMY[_cat] = _skills
    CATEGORY_PRIORITY[_cat] = 4  # medium priority
    for _s in _skills:
        SKILL_TO_CATEGORY[_s.lower()] = _cat
        ALL_SKILLS.append(_s)
