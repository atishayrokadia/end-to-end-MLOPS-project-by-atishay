import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "end-to-end-MLOPS-project-by-atishay"
AUTHOR_USER_NAME = "atishayrokadia"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "atishayrokadia2402@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Project for Practice",
    Long_description=long_description,
    Long_description_content = "text/markdown",
    url= f"https://github.com/atishayrokadia/end-to-end-MLOPS-project-by-atishay",
    project_urls={
        "Bug Tracker" : f"https://github.com/atishayrokadia/end-to-end-MLOPS-project-by-atishay/issues",
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where="src")
)