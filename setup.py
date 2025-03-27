from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Sanuja Chakraborty',
    author_email='sanujachakraorty123@gmail.com',
    install_requires=["google-genai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)