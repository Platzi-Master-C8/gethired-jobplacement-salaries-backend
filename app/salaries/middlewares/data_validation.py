import random

# Mockdata

titles = [
    "Developer",
    "Fullstack",
    "Backend",
    "Frontend",
    "Desktop",
    "Enterprise",
    "Mobile",
    "Devops Specialist",
    "System Administrator",
    "Database Administrator",
    "Designer",
    "Embedded Applications",
    "Data Scientist",
    "Machine Learning Specialist",
    "Student",
    "Engineer",
    "Engineering Manager",
    "Data",
    "Business Analyst",
    "Qa",
    "Test",
    "Product Manager",
    "Academic Researcher",
    "Site Reliability",
    "Educator",
    "Game",
    "Graphics",
    "Senior Executive",
    "Scientist",
    "Marketing",
    "Sales Professional"
]


technologies = [
    "Javascript",
    "Html",
    "Css",
    "Python",
    "Sql",
    "Java",
    "Nodejs",
    "Typescript",
    "C#",
    "Bash Shell",
    "C++",
    "Php",
    "C",
    "Powershell",
    "Go",
    "Kotlin",
    "Rust",
    "Ruby",
    "Dart",
    "Assembly",
    "Swift",
    "R",
    "Vba",
    "Matlab",
    "Groovy",
    "Objective-c",
    "Scala",
    "Perl",
    "Haskell",
    "Delphi",
    "Clojure",
    "Elixir",
    "Lisp",
    "Julia",
    "F#",
    "Erlang",
    "Apl",
    "Crystal",
    "Cobol",
    "Mysql",
    "Postgresql",
    "Sqlite",
    "Mongodb",
    "Microsoft Sql Server",
    "Redis",
    "Mariadb",
    "Firebase",
    "Elasticsearch",
    "Oracle",
    "Dynamodb",
    "Cassandra",
    "Ibm Db2",
    "Couchbase",
    "Aws",
    "Google Cloud Platform",
    "Microsoft Azure",
    "Heroku",
    "Digitalocean",
    "Ibm Cloud or Watson",
    "Oracle Cloud Infrastructure",
    "React.js",
    "Jquery",
    "Express",
    "Angular",
    "Vue.js",
    "Asp.net Core",
    "Flask",
    "Asp.net",
    "Django",
    "Spring",
    "Angular.js",
    "Laravel",
    "Ruby on Rails",
    "Gatsby",
    "Fastapi",
    "Symfony",
    "Svelte",
    "Drupal",
    ".net Framework",
    "Numpy",
    ".net Core",
    ".net 5",
    "Pandas",
    "Tensorflow",
    "React Native",
    "Flutter",
    "Keras",
    "Qt",
    "Torch",
    "Pytorch",
    "Cordova",
    "Apache Spark",
    "Hadoop",
    "Git",
    "Docker",
    "Yarn",
    "Kubernetes",
    "Unity 3d",
    "Ansible",
    "Terraform",
    "Xamarin",
    "Unreal Engine",
    "Puppet",
    "Deno",
    "Chef",
    "Flow",
    "Pulumi"
]

annual_salary_by_technology = [
    {"Clojure": 95000},
    {"F#": 81037},
    {"Elixir": 80077},
    {"Erlang": 80077},
    {"Perl": 80000},
    {"Ruby": 80000},
    {"Scala": 77832},
    {"Rust": 77530},
    {"Go": 75669},
    {"Lisp": 75669},
    {"Apl": 75631},
    {"Groovy": 75002},
    {"Crystal": 72400},
    {"Bash Shell": 71340},
    {"Powershell": 68824},
    {"Haskell": 67021},
    {"Julia": 65228},
    {"Objective-c": 64859},
    {"Python": 59454},
    {"R": 59454},
    {"Typescript": 59172},
    {"Swift": 58910},
    {"C#": 58368},
    {"Sql": 56228},
    {"Assembly": 55211},
    {"Kotlin": 55071},
    {"Nodejs": 54672},
    {"C++": 54049},
    {"Javascript": 54049},
    {"Vba": 53825},
    {"C": 53184},
    {"Html": 52980},
    {"Css": 52980},
    {"Cobol": 52340},
    {"Java": 51888},
    {"Delphi": 46704},
    {"Matlab": 43948},
    {"Php": 38916},
    {"Dart": 32986},
    {"Pulumi": 109824},
    {"Terraform": 90482},
    {"Chef": 90000},
    {"Puppet": 76000},
    {"Kubernetes": 75000},
    {"Ansible": 72000},
    {"Deno": 64859},
    {"Docker": 63469},
    {"Yarn": 57696},
    {"Git": 56798},
    {"Flow": 51887},
    {"Xamarin": 51704},
    {"Unreal Engine": 49228},
    {"Unity 3d": 45396},
    {"Apache Spark": 67464},
    {".net Core": 62520},
    {".net 5": 62520},
    {"Hadoop": 60624},
    {".net Framework": 59185},
    {"Numpy": 54049},
    {"Pandas": 54049},
    {"Torch": 52869},
    {"Pytorch": 52869},
    {"Qt": 51888},
    {"Tensorflow": 50000},
    {"Keras": 45396},
    {"React Native": 44160},
    {"Cordova": 39192},
    {"Flutter": 32429},
    {"Ruby on Rails": 77556},
    {"Svelte": 62520},
    {"Asp.net Core": 60744},
    {"Gatsby": 60129},
    {"React.js": 58128},
    {"Asp.net": 56220},
    {"Flask": 54876},
    {"Fastapi": 54049},
    {"Spring": 51888},
    {"Drupal": 51429},
    {"Vue.js": 50000},
    {"Angular.js": 49450},
    {"Angular": 48852},
    {"Express": 47850},
    {"Jquery": 45797},
    {"Symfony": 45396},
    {"Django": 45379},
    {"Laravel": 29196},
    {"Aws": 66810},
    {"Microsoft Azure": 64630},
    {"Google Cloud Platform": 55600},
    {"Ibm Cloud or Watson": 52942},
    {"Oracle Cloud Infrastructure": 51888},
    {"Digitalocean": 51704},
    {"Heroku": 45000},
    {"Dynamodb": 80936},
    {"Elasticsearch": 67021},
    {"Cassandra": 64930},
    {"Redis": 64548},
    {"Ibm Db2": 64044},
    {"Couchbase": 63018},
    {"Postgresql": 59454},
    {"Microsoft Sql Server": 58167},
    {"Sqlite": 51704},
    {"Oracle": 48644},
    {"Mariadb": 45678},
    {"Mongodb": 45401},
    {"Mysql": 43404},
    {"Firebase": 37834}
]

annual_salary_by_title = [
    {}
]


def all_technologies():
    return technologies


def all_titles():
    return titles


def salary_by_language(level):
    """
    Returns a salary increase for English level
    """
    if level == "A1" or level == "A2":
        salary_up = 1000
    elif level == "B1" or level == "B2":
        salary_up = 2000
    else:
        salary_up = 4000
    return salary_up*round(random.uniform(0.78, 1.12), 2)


def salary_by_seniority(seniority):
    """
    Returns a salary increase by seniority.
    """
    if seniority == 1:
        salary_up = 500
    elif seniority == 2:
        salary_up = 1000
    elif seniority == 3:
        salary_up = 2500
    elif seniority == 4:
        salary_up = 4000
    else:
        salary_up = 0
    return salary_up*round(random.uniform(0.95, 1.02), 2)


def salary_by_technologies(technology):
    """
    Filters by technology and returns a value in USD.
    """
    salary_up = []
    tech = []
    for select_tech in technology:
        select_tech_name = dict(select_tech)
        tech.append(select_tech_name["name"])
        if tech == []:
            salary_up = 0
            return salary_up

    for salary_tech in annual_salary_by_technology:
        for salary_tech_name, salary_tech_value in salary_tech.items():
            for tech_salary in tech:
                if salary_tech_name == tech_salary:
                    salary_up.append(salary_tech_value)

    if salary_up == []:
        salary_up = 0
        return salary_up
    else:
        return max(salary_up)*round(random.uniform(0.80, 1.06), 2)


def salary_by_knowledge(dataquery):
    """
    Salary by Knowledge

    Calculate the amount of salary you will receive.
    """
    total_salary = []
    total_salary.append(salary_by_language(dataquery["english_level"]))
    total_salary.append(salary_by_seniority(dataquery["seniority"]))
    total_salary.append(salary_by_technologies(dataquery["technologies"]))

    total_salary = sum(total_salary)
    data = {
        "bottom": total_salary*0.77,
        "average": total_salary,
        "top": total_salary*1.23,
    }
    return data
