# CI & CD

**Continuous Integration (CI)** is a software development practice where members of a team integrate their work frequently, usually multiple times a day.

Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible.
The primary objectives of CI are to provide rapid feedback, find and address bugs quicker, improve software quality, and reduce the time it takes to validate and release new software updates. 

CI typically involves:

- Frequent code commits by developers.
- Automated testing to ensure changes do not introduce errors or regressions.
- Reporting tools to notify developers of the build and test results.

CI is often combined with Continuous Delivery (CD) to streamline the code changes further through to production.

**Continuous Delivery (CD)** is a software development practice in which code changes are automatically built, tested, and prepared for a release to production. The main goal of Continuous Delivery is to accelerate the feedback loop with customers and ensure that the software can be reliably released at any time.

- Ensures that the software can be released at any time.
- It emphasizes the automation of the entire software delivery process, from integration, testing, and build to deployment.
- However, the actual deployment to production might be manual, requiring a human intervention.

- **Continuous Deployment**: 
- Extends Continuous Delivery by automatically deploying every change directly to production, without human intervention, once it has passed all stages of your production pipeline.

Every merged change that passes all stages of production is released to the customers. There's no explicit approval required.

Key aspects of Continuous Delivery include:

1. **Automated Testing**: Ensuring that all changes are automatically tested to ensure software quality is maintained.

2. **Environment Consistency**: Ensuring that testing and staging environments closely replicate the production environment to catch environment-specific issues.

3. **Infrastructure as Code (IaC)**: Treating infrastructure setup and configuration the same way as source code, with revisions and versioning, enabling automated and consistent environment setups.


### Github action

- go to Action -> create new workflow -> select django: github creates for us a yml file
- edit the created yml file to:

```yml
name: Django CI

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      max-parallel: 1
      matrix:
        python-version: [3.9]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test
```

1. **Name of the Workflow**:
   ```yaml
   name: Django CI
   ```
   This gives a name to the workflow. It's primarily used for display purposes in the GitHub Actions UI. This workflow is named "Django CI".

2. **Event Triggers**:
   ```yaml
   on:
     push:
       branches: [ "master" ]
     pull_request:
       branches: [ "master" ]
   ```
   This section determines when the workflow will run:
   - It triggers on `push` events but only for the `master` branch.
   - It also triggers on `pull_request` events, again only for the `master` branch.

3. **Jobs**:
   ```yaml
   jobs:
     build:
   ```
   Here, the workflow defines a single job named `build`. Jobs run in parallel by default unless specified otherwise.

4. **Runtime Environment**:
   ```yaml
   runs-on: ubuntu-latest
   ```
   This job will run on the latest version of the Ubuntu virtual environment provided by GitHub Actions.

5. **Strategy**:
   ```yaml
   strategy:
     max-parallel: 1
     matrix:
       python-version: [3.9]
   ```
   - `max-parallel: 1` means only one job should run at a time. This setting is redundant in this specific context since the matrix only has one version of Python defined.
   - `matrix` sets up a build matrix. This can be used to run the job on multiple versions of a dependency, in this case, Python. Here, it's set to only run on Python 3.9.

6. **Steps**:
   This section defines a list of steps that the job will run. They are executed in the order they are listed:

   - **Checkout Repository**:
     ```yaml
     - uses: actions/checkout@v3
     ```
     This step checks out the repository using the `actions/checkout` action at its v3 version. It's necessary so that the workflow can access the content of the repository.

    - **Setup Python**:
     ```yaml
     - name: Set up Python ${{ matrix.python-version }}
       uses: actions/setup-python@v3
       with:
         python-version: ${{ matrix.python-version }}
     ```
     This step sets up a Python environment using the specified version from the matrix (Python 3.9 in this case) using the `actions/setup-python` action.

        - **Install Dependencies**:
     ```yaml
     - name: Install Dependencies
       run: |
         python -m pip install --upgrade pip
         pip install -r requirements.txt
     ```
     This step installs the required dependencies for the Django project. First, it upgrades `pip`, and then it installs packages specified in `requirements.txt`.

    - **Run Django Tests**:
     ```yaml
     - name: Run Tests
       run: |
         python manage.py test
     ```
     This step runs the Django tests using the `manage.py test` command.