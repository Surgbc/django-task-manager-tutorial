# Course Guide: Following the Django Tutorial

## How to Use This Repository

This repository is designed to accompany the **"Django Web Development: A Project-Based Approach"** course. Each commit represents a step in the learning process.

## Git Workflow for Students

### Chapter 1: Development Environment & Project Setup

```bash
# Start with this commit (already done)
git checkout f644a17  # Initial project setup

# Follow Chapter 1 exercises:
# - Exercise 1.1: Python and Django Installation (done on your machine)
# - Exercise 1.2: Create Django Project (this commit)
# - Exercise 1.3: Git Repository Setup (this commit)
# - Exercise 1.4: Development Tools Configuration (next commit)
```

### Following Along

1. **Read the course material** for the chapter
2. **Try the exercises yourself** first
3. **Compare with the commits** to check your work
4. **Move to the next chapter** when ready

### Branch Strategy

- `master`: Complete progression of the course
- `chapter-X-start`: Starting point for each chapter (coming soon)
- `chapter-X-complete`: Completed chapter with all exercises (coming soon)

## Course Structure

### Part I: Foundation
- ✅ **Chapter 1**: Development Environment & Project Setup
- 🔄 **Chapter 2**: Django Fundamentals & First Views (next)
- 📋 **Chapter 3**: Database Models & Admin
- 👤 **Chapter 4**: User Authentication

### Part II: Core Functionality  
- 📝 **Chapter 5**: Task CRUD Operations
- ⚡ **Chapter 6**: Advanced Task Features
- 🎨 **Chapter 7**: User Interface & Experience
- 📋 **Chapter 8**: Forms & Validation

### Part III: Advanced Features
- 📎 **Chapter 9**: File Uploads & Attachments
- 🔗 **Chapter 10**: API & Integration
- 🧪 **Chapter 11**: Testing & Quality Assurance
- 🚀 **Chapter 12**: Deployment & Production

## Commit Messages Format

Each commit follows this pattern:
```
type: brief description

- Detailed explanation of changes
- What was implemented
- Why it was implemented this way

Course: Chapter X, Exercise X.Y
```

## Getting Help

If you get stuck:
1. Check the commit history: `git log --oneline`
2. Compare your code with the repository
3. Read the course materials again
4. Ask questions in the course forum

## Development Commands Quick Reference

```bash
# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Django commands
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser

# Git commands
git status
git log --oneline
git diff
```

Happy learning! 🎓