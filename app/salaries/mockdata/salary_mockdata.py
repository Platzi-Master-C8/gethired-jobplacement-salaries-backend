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


seniority = {
    "title": 'Seniority levels',
    "texts": [
        {"level": 'Junior', "description": '0-3 years of experience. Some knowledge of the language and technology stack.'},
        {"level": 'Junior-Mid', "description": 'Between junior and Mid-level'},
        {"level": 'Mid', "description": '1-3 years of experience. Good working knowledge of the language and technology stack.'},
        {"level": 'Mid-Senior', "description": 'Between Mid-level and Senior'},
        {"level": 'Senior', "description": '3+ years of experience. Mastery of the language and tech stack.'},
    ],
    "infoLink": 'https://medium.com/javascript-scene/what-is-the-difference-between-a-junior-and-a-senior-developer-63c1594d7a98',
}

english_level = {
    "title": 'English Levels accordingly to CEFR',
    "texts": [
        {"level": 'A1', "description": 'Can understand and use familiar everyday expressions and very basic phrases.'},
        {"level": 'A2', "description": 'Can understand sentences and frequently used expressions.'},
        {"level": 'B1', "description": 'Can deal with most situations likely to arise while travelling.'},
        {"level": 'B2', "description": 'Can interact with a degree of fluency with native speakers.'},
        {"level": 'C1', "description": 'Can use language effectively for social, academic and professional purposes.'},
        {"level": 'C2', "description": 'Can understand with ease virtually everything heard or read.'}
    ],
    "infoLink": 'https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages',
}


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
