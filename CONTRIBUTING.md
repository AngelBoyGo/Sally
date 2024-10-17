# Contributing to Sally - Heart Disease Risk Assessment Tool

We are excited that you are interested in contributing to Sally! This document provides guidelines and instructions to help you submit a pull request (PR) successfully.

## Getting Started

1. **Fork the Repository:**
   - Go to the main repository on GitHub.
   - Click the **Fork** button in the top-right corner to create your own copy of the repository.

2. **Clone the Forked Repository:**
   - On your machine, open the terminal or command prompt.
   - Run the following command to clone your forked repository:
     ```bash
     git clone https://github.com/YOUR_USERNAME/sally_project.git
     cd sally_project
     ```

3. **Set the Original Repository as Upstream:**
   - Add the original repository to keep your fork in sync with the latest changes.
     ```bash
     git remote add upstream https://github.com/ORIGINAL_OWNER/sally_project.git
     ```

4. **Create a New Branch:**
   - Create a branch for your changes.
     ```bash
     git checkout -b feature/new-feature-name
     ```

## Making Changes

1. **Implement Your Changes:**
   - Add your code or make the required fixes/improvements.
   - Ensure your code follows the existing style and structure of the project.

2. **Test Your Changes:**
   - Run the application locally to confirm everything works as expected.
     ```bash
     python app.py
     ```

3. **Add and Commit Changes:**
   - Stage your changes and commit them with a meaningful commit message:
     ```bash
     git add .
     git commit -m "Add feature or fix description"
     ```

4. **Push Your Changes to GitHub:**
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/new-feature-name
     ```

## Submitting a Pull Request

1. **Open a Pull Request:**
   - Go to your forked repository on GitHub.
   - Click the **Compare & Pull Request** button.

2. **Provide Details:**
   - Give your PR a descriptive title and include a summary of the changes you made.
   - Link any related issues if applicable.

3. **Submit the Pull Request:**
   - Click the **Create Pull Request** button to submit your PR.

4. **Wait for Review:**
   - A project maintainer will review your PR and may suggest changes. Please address feedback promptly.

## Keeping Your Fork in Sync

1. **Fetch the Latest Changes from Upstream:**
   ```bash
   git fetch upstream
Merge Changes into Your Branch:

bash
Copy code
git merge upstream/main
Resolve Any Conflicts and Push the Changes:

bash
Copy code
git push origin feature/new-feature-name
Code of Conduct
Please be respectful to other contributors and maintainers. We aim to foster an inclusive and friendly community. For more details, refer to our Code of Conduct.

License
By contributing to Sally, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
