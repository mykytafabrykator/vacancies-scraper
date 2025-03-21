# flake8: noqa
from pathlib import Path
import uuid
from datetime import date

WORK_UA_URL = "https://work.ua/jobs-"
ROBOTA_UA_URL = "https://robota.ua/zapros/"

BASE_DIR = Path(__file__).resolve().parent

SCRAPING_DATA_PATH = BASE_DIR / "vacancies_scraper" / "data"
ANALYSIS_DATA_PATH = BASE_DIR / "vacancies_analysis" / "data"

ID = f"{uuid.uuid4().hex[:8]}"

SCRAPING_OUTPUT_FILE = SCRAPING_DATA_PATH / f"{date.today()}-{ID}-vacancies.csv"
ANALYSIS_OUTPUT_FILE = ANALYSIS_DATA_PATH / f"{date.today()}-{ID}-stats.csv"

TECHNOLOGIES_TO_ANALYZE = [
    # Programming languages
    "python", "java", "javascript", "typescript", "c++", "go", "rust", "kotlin", "swift", "php", "dart", "ruby", "scala",

    # Frameworks (BE & API)
    "django", "flask", "fastapi", "spring boot", "spring framework", "express", "nestjs", "graphql", "grpc", "laravel",

    # Frameworks (FE)
    "react", "angular", "vue", "vue.js", "nextjs", "nuxtjs", "svelte", "jquery", "react-native", "redux", "material ui",

    # DevOps / Cloud
    "docker", "docker compose", "docker swarm", "kubernetes", "helm", "terraform", "ansible", "jenkins",
    "azure devops", "github actions", "gitlab ci", "circleci", "travisci", "vagrant", "prometheus", "grafana",
    "nginx", "apache", "cloudformation", "aws", "gcp", "azure", "openstack", "cloudwatch", "google kubernetes engine",

    # DB
    "postgresql", "mysql", "mariadb", "sqlite", "mongodb", "mongodb atlas", "redis", "neo4j", "hbase", "elasticsearch",

    # Queues / brokers
    "rabbitmq", "kafka", "apache kafka", "confluent", "celery",

    # Machine Learning / Data Science
    "tensorflow", "pytorch", "sklearn", "scipy", "pandas", "numpy", "matplotlib", "seaborn", "jupyter", "opencv",

    # Other technologies
    "html", "css", "tailwind", "bootstrap", "sass", "webpack", "vite", "babel",
    "websockets", "rest", "jwt", "oauth", "serverless", "microservices", "microfrontends",
    "ssr", "pwa", "web scraping", "scrapy", "beautifulsoup",

    # QA / testing
    "pytest", "jest", "mocha", "chai", "selenium", "puppeteer", "robot framework", "supertest",

    # Blockchain
    "solidity", "web3", "ethereum", "ipfs", "truffle",

    # Other instruments
    "git", "github", "gitlab", "bitbucket", "vscode", "figma", "storybook", "styled components", "uikit", "pm2",

    # Cloud instruments
    "aws lambda", "google cloud functions", "azure functions", "fargate", "rancher", "datadog", "google analytics",

    # Integration
    "stripe", "twilio", "sendgrid", "firebase", "mongodb compass", "docker hub", "markdown",

    # Visuals / 3D
    "d3.js", "three.js", "recharts", "rxjs", "socket.io",

    # Mobile
    "flutter", "flutterflow", "swiftui", "ionic", "fastlane",

    # Other
    "bash scripting", "bash commands", "consul", "logstash", "apache beam", "google data studio"
]
