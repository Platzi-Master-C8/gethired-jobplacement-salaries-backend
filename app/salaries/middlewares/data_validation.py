

# Mockdata

titles = [
    "developer",
    "fullstack",
    "backend",
    "frontend",
    "desktop",
    "enterprise",
    "mobile",
    "devops specialist",
    "system administrator",
    "database administrator",
    "designer",
    "embedded applications",
    "data scientist",
    "machine learning specialist",
    "student",
    "engineer",
    "engineering manager",
    "data",
    "business analyst",
    "qa",
    "test",
    "product manager",
    "academic researcher",
    "site reliability",
    "educator",
    "game",
    "graphics",
    "senior executive",
    "scientist",
    "marketing",
    "sales professional"
]


technologies = [
    "javascript",
    "html",
    "css",
    "python",
    "sql",
    "java",
    "nodejs",
    "typescript",
    "c#",
    "bash/shell",
    "c++",
    "php",
    "c",
    "powershell",
    "go",
    "kotlin",
    "rust",
    "ruby",
    "dart",
    "assembly",
    "swift",
    "r",
    "vba",
    "matlab",
    "groovy",
    "objective-c",
    "scala",
    "perl",
    "haskell",
    "delphi",
    "clojure",
    "elixir",
    "lisp",
    "julia",
    "f#",
    "erlang",
    "apl",
    "crystal",
    "cobol",
    "mysql",
    "postgresql",
    "sqlite",
    "mongodb",
    "microsoft sql server",
    "redis",
    "mariadb",
    "firebase",
    "elasticsearch",
    "oracle",
    "dynamodb",
    "cassandra",
    "ibm db2",
    "couchbase",
    "aws",
    "google cloud platform",
    "microsoft azure",
    "heroku",
    "digitalocean",
    "ibm cloud or watson",
    "oracle cloud infrastructure",
    "react.js",
    "jquery",
    "express",
    "angular",
    "vue.js",
    "asp.net core",
    "flask",
    "asp.net",
    "django",
    "spring",
    "angular.js",
    "laravel",
    "ruby on rails",
    "gatsby",
    "fastapi",
    "symfony",
    "svelte",
    "drupal",
    ".net framework",
    "numpy",
    ".net core / .net 5",
    "pandas",
    "tensorflow",
    "react native",
    "flutter",
    "keras",
    "qt",
    "torch/pytorch",
    "cordova",
    "apache spark",
    "hadoop",
    "git",
    "docker",
    "yarn",
    "kubernetes",
    "unity 3d",
    "ansible",
    "terraform",
    "xamarin",
    "unreal engine",
    "puppet",
    "deno",
    "chef",
    "flow",
    "pulumi"
]

annual_salary_by_technology = [
    {"clojure": 95000},
    {"f#": 81037},
    {"elixir": 80077},
    {"erlang": 80077},
    {"perl": 80000},
    {"ruby": 80000},
    {"scala": 77832},
    {"rust": 77530},
    {"go": 75669},
    {"lisp": 75669},
    {"apl": 75631},
    {"groovy": 75002},
    {"crystal": 72400},
    {"bash/shell": 71340},
    {"powershell": 68824},
    {"haskell": 67021},
    {"julia": 65228},
    {"objective-c": 64859},
    {"python": 59454},
    {"r": 59454},
    {"typescript": 59172},
    {"swift": 58910},
    {"c#": 58368},
    {"sql": 56228},
    {"assembly": 55211},
    {"kotlin": 55071},
    {"nodejs": 54672},
    {"c++": 54049},
    {"javascript": 54049},
    {"vba": 53825},
    {"c": 53184},
    {"html": 52980},
    {"css": 52980},
    {"cobol": 52340},
    {"java": 51888},
    {"delphi": 46704},
    {"matlab": 43948},
    {"php": 38916},
    {"dart": 32986},
    {"pulumi": 109824},
    {"terraform": 90482},
    {"chef": 90000},
    {"puppet": 76000},
    {"kubernetes": 75000},
    {"ansible": 72000},
    {"deno": 64859},
    {"docker": 63469},
    {"yarn": 57696},
    {"git": 56798},
    {"flow": 51887},
    {"xamarin": 51704},
    {"unreal engine": 49228},
    {"unity 3d": 45396},
    {"apache spark": 67464},
    {".net core / .net 5": 62520},
    {"hadoop": 60624},
    {".net framework": 59185},
    {"numpy": 54049},
    {"pandas": 54049},
    {"torch/pytorch": 52869},
    {"qt": 51888},
    {"tensorflow": 50000},
    {"keras": 45396},
    {"react native": 44160},
    {"cordova": 39192},
    {"flutter": 32429},
    {"ruby on rails": 77556},
    {"svelte": 62520},
    {"asp.net core": 60744},
    {"gatsby": 60129},
    {"react.js": 58128},
    {"asp.net": 56220},
    {"flask": 54876},
    {"fastapi": 54049},
    {"spring": 51888},
    {"drupal": 51429},
    {"vue.js": 50000},
    {"angular.js": 49450},
    {"angular": 48852},
    {"express": 47850},
    {"jquery": 45797},
    {"symfony": 45396},
    {"django": 45379},
    {"laravel": 29196},
    {"aws": 66810},
    {"microsoft azure": 64630},
    {"google cloud platform": 55600},
    {"ibm cloud or watson": 52942},
    {"oracle cloud infrastructure": 51888},
    {"digitalocean": 51704},
    {"heroku": 45000},
    {"dynamodb": 80936},
    {"elasticsearch": 67021},
    {"cassandra": 64930},
    {"redis": 64548},
    {"ibm db2": 64044},
    {"couchbase": 63018},
    {"postgresql": 59454},
    {"microsoft sql server": 58167},
    {"sqlite": 51704},
    {"oracle": 48644},
    {"mariadb": 45678},
    {"mongodb": 45401},
    {"mysql": 43404},
    {"firebase": 37834}
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
    return salary_up


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
    return salary_up


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
        return max(salary_up)


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
