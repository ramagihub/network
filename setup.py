from setuptools import setup, find_packages

list_requirements:list[str] = []
def get_requirement()-> list[str]:
    try:
        with open('requirements.txt') as file:
            lines= file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement != '' and requirement != '-e .':
                    list_requirements.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')
    return list_requirements
requirements = get_requirement()
print(requirements)
setup(version='0.2.0',
      author_email='',
      packages=find_packages(),
      install_requires=get_requirement(),
      )
