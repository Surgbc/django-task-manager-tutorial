# Django Task Manager Tutorial

A hands-on Django course that teaches web development by building a complete Task Management System from scratch.

## 🎯 What You'll Build

By the end of this tutorial, you'll have created a full-featured Task Management System with:

- **User Authentication**: Registration, login, logout, profiles
- **Task Management**: Create, read, update, delete tasks
- **Advanced Features**: Categories, priorities, due dates, search
- **File Attachments**: Upload and manage task-related files
- **REST API**: JSON API for mobile apps and integrations
- **Professional UI**: Responsive design with Bootstrap
- **Testing Suite**: Comprehensive unit and integration tests
- **Production Deployment**: Live application on cloud platform

## 📚 Course Structure

This tutorial follows a **progressive building approach** - each chapter adds new functionality to the same project. You can follow along by checking out the commits for each chapter.

### Part I: Foundation
- **Chapter 1**: Development Environment & Project Setup
- **Chapter 2**: Django Fundamentals & First Views  
- **Chapter 3**: Database Models & Admin
- **Chapter 4**: User Authentication

### Part II: Core Functionality  
- **Chapter 5**: Task CRUD Operations
- **Chapter 6**: Advanced Task Features
- **Chapter 7**: User Interface & Experience
- **Chapter 8**: Forms & Validation

### Part III: Advanced Features
- **Chapter 9**: File Uploads & Attachments
- **Chapter 10**: API & Integration
- **Chapter 11**: Testing & Quality Assurance
- **Chapter 12**: Deployment & Production

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ installed
- Basic command line knowledge
- Text editor (VS Code recommended)
- Git installed

### Quick Start
```bash
# Clone this repository
git clone https://github.com/surgbc/django-task-manager-tutorial.git
cd django-task-manager-tutorial

# Check out the starting point
git checkout chapter-1-start

# Follow the course instructions from Chapter 1
```

## 📖 How to Use This Repository

### Following Along with the Course

1. **Start at the beginning**: `git checkout chapter-1-start`
2. **Work through exercises**: Follow the course materials
3. **Check your progress**: Compare with `git checkout chapter-1-complete`
4. **Move to next chapter**: `git checkout chapter-2-start`

### Git Branches and Tags

- `main`: Latest complete version
- `chapter-X-start`: Starting point for each chapter
- `chapter-X-complete`: Completed chapter with all exercises
- `solution-X.Y`: Individual exercise solutions

### Branch Strategy
```bash
# Start a chapter
git checkout chapter-1-start

# Work on exercises
git add .
git commit -m "Complete exercise 1.1: Setup development environment"

# Compare with official solution
git diff chapter-1-complete
```

## 🛠️ Development Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements/development.txt
```

### 3. Set Up Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see your application!

## 📋 Project Milestones

Each major milestone is tagged for easy reference:

- `v0.1.0`: Basic project setup and first views
- `v0.2.0`: User authentication system complete
- `v0.3.0`: Core task management functionality
- `v0.4.0`: Advanced UI and user experience
- `v0.5.0`: File uploads and attachments
- `v1.0.0`: Production-ready application with API

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 📊 Project Statistics

| Feature | Status | Chapter |
|---------|--------|---------|
| Project Setup | ✅ Complete | 1-2 |
| User Authentication | ✅ Complete | 4 |
| Task CRUD | ✅ Complete | 5 |
| Advanced Features | ✅ Complete | 6-7 |
| File Uploads | ✅ Complete | 9 |
| REST API | ✅ Complete | 10 |
| Testing | ✅ Complete | 11 |
| Deployment | ✅ Complete | 12 |

## 🤝 Contributing

This is an educational repository. If you find issues or have suggestions:

1. Check existing issues
2. Create a new issue with details
3. For major changes, discuss first

## 📝 License

This tutorial project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Course Companion

This repository accompanies the **"Django Web Development: A Project-Based Approach"** course. For the complete learning experience:

- 📖 **Course Textbook**: Comprehensive explanations and theory
- 💻 **This Repository**: Hands-on code and exercises  
- 🎥 **Video Tutorials**: Step-by-step guidance (coming soon)
- 💬 **Community Forum**: Get help and discuss with other learners

## 🔗 Related Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Happy Learning! 🎉**

*Build something amazing with Django!*