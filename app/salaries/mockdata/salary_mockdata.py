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


seniority = [
    'Junior',
    'Mid-Junior',
    'Mid',
    'Mid-Senior',
    'Senior'
]

english_level = [
    "A1",
    "A2",
    "B1",
    "B2",
    "C1",
    "C2"
]


def all_technologies():
    return technologies


def all_titles():
    return titles


def all_seniority():
    return seniority


def all_english_levels():
    return english_level


def salary_mokedata():
    """
    Salary Mockdata

    Calculate the amount of salary you will receive.
    """
    total_salary = 50000*round(random.uniform(0.18, 1.35), 2)

    data = {
        "bottom": total_salary*round(random.uniform(0.78, 0.92), 2),
        "average": total_salary,
        "top": total_salary*round(random.uniform(1.16, 1.08), 2),
    }
    return data
