# CI-CD_Book-Review-API
CI/CD with Azure – Structured Project-Based Roadmap
A small REST API where users can add and fetch book reviews. We'll test it, build it, and deploy it using Azure Pipelines.

✅ Phase 1: Fundamentals + Setup

Objective: Understand basic CI/CD, set up your environment, and get Azure DevOps ready.

 1- Create a free Azure DevOps account
 
 2- Install Git, VS Code, and set up a GitHub repo
 
 3- Clone a sample REST API app (can be Python, Node.js, or .NET—let me know your preference!)
 
 4- Understand core CI/CD concepts:
 
      a- What is CI/CD
      
      b- Difference between CI and CD
      
      c- Importance of automated testing
      
- Deliverable: Run the app locally, commit it to GitHub, and connect your repo to Azure DevOps.

✅ Phase 2: Setup CI Pipeline

Objective: Create a build pipeline that runs tests automatically on push.

 1- Write unit tests (using pytest for Python or Jest for Node.js)
 
 2- Create your first azure-pipelines.yml file
 
 3- Set up a build pipeline in Azure Pipelines
 
 4- Add tasks for:
 
     a- Installing dependencies
     
     b- Running tests
     
     c- Checking code quality (e.g. with flake8 or eslint)

- Deliverable: Every push triggers a pipeline that runs tests and code checks.

✅ Phase 3: Add Code Coverage + Reporting

Objective: Make your pipeline more test-focused and measurable.

 Add code coverage tools (coverage.py, nyc, or coverlet)

 Publish test results in Azure DevOps

 Configure email or Slack alerts for failed builds/tests

Deliverable: Pipeline publishes test results and coverage on every commit.

✅ Phase 4: Continuous Deployment (CD)

Objective: Automatically deploy to Azure Web App after a successful build.

 Set up a resource group and Azure App Service

 Add Azure credentials to your pipeline (via Service Connection)

 Add deployment steps to azure-pipelines.yml

 Use staging and production environments (if possible)

Deliverable: App is deployed automatically after tests pass.

✅ Phase 5: Interview Readiness & Real-World Simulations
Objective: Get confident with real-world CI/CD questions and debugging.

 Practice interview questions:

How do you ensure high test coverage?

What do you do when a pipeline fails?

How would you handle flaky tests?

 Simulate a failed build and fix it

 Add one integration test to your pipeline

 Optional: Add Docker + container deployment (if time allows)

Deliverable: Be ready to walk an interviewer through your whole pipeline.
