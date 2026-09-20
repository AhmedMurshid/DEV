"""Portfolio copy grounded in Ahmed's supplied resume. Edit here to update the site."""
PROFILE = {
    'name': 'Ahmed Abdullahi', 'title': 'Database & Cloud Engineer',
    'email': 'ahmed.abdullahione@gmail.com', 'location': 'Louisville, Kentucky',
    'github': 'https://github.com/AhmedMurshid',
    'linkedin': 'https://www.linkedin.com/in/ahmed-murshid/',
}
PROJECTS = [
    {
        'slug': 'multi-database-operations', 'number': '01', 'category': 'DATABASE ENGINEERING', 'theme': 'database',
        'title': 'One platform. Many data sources.', 'name': 'Multi-Database Operations Platform',
        'summary': 'A unified workspace for querying databases, ingesting files and APIs, and automating ETL workflows.',
        'tags': ['Python', 'SQL', 'ETL', 'APIs'],
        'nodes': ['Databases · Files · APIs', 'Connection & source routing', 'SQL execution · ETL', 'Rendered query results'],
        'challenge': 'Working across different database engines, file formats, and APIs requires consistent connection handling, routing, and reusable transformation workflows.',
        'approach': 'Built a database operations platform spanning Oracle, PostgreSQL, MySQL, MariaDB, SQL Server, SQLite, CSV, JSON, Excel, and API-based sources.',
        'work': ['Developed connection management and multi-source SQL execution.', 'Built file and API ingestion with source-routing workflows.', 'Implemented query output rendering and error handling.', 'Created reusable ETL, transformation, scheduling, and automation workflows.'],
        'result': 'A common operations layer for database, file, and API sources, with reusable workflows for querying and transforming data.',
    },
    {
        'slug': 'ai-google-slides-maker', 'number': '02', 'category': 'BACKEND DEVELOPMENT', 'theme': 'backend',
        'title': 'From a prompt to a presentation.', 'name': 'AI Google Slides Maker',
        'summary': 'A deployed Django application connecting structured content, the Google Slides API, and containerized infrastructure.',
        'tags': ['Django', 'Docker', 'Linux', 'Cloudflare'],
        'nodes': ['Prompt · Slide & scene JSON', 'Django backend', 'Google Slides API', 'Generated presentation'],
        'challenge': 'Turning a prompt and structured slide content into a presentation requires reliable backend processing, API integration, and a deployable application.',
        'approach': 'Built and deployed a Django application that converts user prompts and structured slide and scene JSON into Google Slides presentations.',
        'work': ['Integrated Google Slides API workflows into the backend.', 'Handled prompts and structured slide and scene JSON.', 'Managed Docker deployment and Linux hosting.', 'Configured domain routing and Cloudflare.'],
        'result': 'A deployed backend application that connects presentation generation with containerized hosting and domain routing.',
    },
    {
        'slug': 'rocket-launch-weather', 'number': '03', 'category': 'DATA & MACHINE LEARNING', 'theme': 'data',
        'title': 'Better signals for launch conditions.', 'name': 'Rocket Launch Weather ML Capstone',
        'summary': 'A machine learning capstone evaluating weather conditions and predicting suitability for a safe rocket launch.',
        'tags': ['Python', 'H2O AutoML', 'Scikit-learn'],
        'nodes': ['Weather data', 'Data preparation', 'Train & compare models', 'Predictive evaluation'],
        'challenge': 'Weather conditions influence launch suitability. The capstone explored how prepared weather data and machine learning models could support that classification task.',
        'approach': 'Developed a Python machine learning solution using H2O AutoML and Scikit-learn to prepare weather data, train models, and evaluate predictive performance.',
        'work': ['Prepared weather data for machine learning.', 'Trained and compared models with H2O AutoML and Scikit-learn.', 'Evaluated predictive performance for launch-condition suitability.'],
        'result': 'A capstone workflow covering data preparation, model comparison, and evaluation. This academic project is not an operational launch-safety system.',
    },
]
EXPERTISE = [
    {'number': '01', 'title': 'Database engineering', 'description': 'Production support, performance troubleshooting, patching, validation, and access management for business-critical databases.', 'tags': 'Oracle RAC / Multitenant / PDB / PostgreSQL / SQL Server'},
    {'number': '02', 'title': 'Cloud & data', 'description': 'Cloud database operations, ETL, and BigQuery dashboards that turn audit and usage data into operational visibility.', 'tags': 'GCP / BigQuery / AlloyDB / AWS / ETL'},
    {'number': '03', 'title': 'Automation', 'description': 'Repeatable workflows for database validation, auditing, job execution, monitoring, and reporting.', 'tags': 'Python / SQL / PL/SQL / Bash'},
    {'number': '04', 'title': 'Backend development', 'description': 'Django applications, API integrations, containerized deployments, Linux hosting, and domain routing.', 'tags': 'Django / Docker / APIs / Linux / Cloudflare'},
    {'number': '05', 'title': 'Security & reliability', 'description': 'Database access controls, auditing, query activity monitoring, and compliance-related operational support.', 'tags': 'Access management / Auditing / Monitoring / UAT'},
]
EXPERIENCE = [
    {'role': 'Database Platform Engineer', 'company': 'UPS', 'date': 'Aug 2025 — Present', 'description': 'Supporting business-critical enterprise databases across healthcare applications, Worldport sortation, warehouse operations, and logistics platforms.'},
    {'role': 'Database Analyst Co-op', 'company': 'UPS', 'date': 'Sep 2023 — Aug 2025', 'description': 'Part of a progression at UPS spanning production database support, automation, controlled changes, and operational reporting.'},
    {'role': 'ISM Intern', 'company': 'UPS', 'date': 'May 2023 — Aug 2023', 'description': 'The start of my enterprise technology journey at UPS, followed by a database analyst co-op and a platform engineering role.'},
    {'role': 'IT Student Help Desk Technician', 'company': 'University of Louisville', 'date': 'Oct 2022 — May 2023', 'description': 'Supported students, faculty, and staff with hardware, software, account access, operating system imaging, and classroom technology.'},
]
