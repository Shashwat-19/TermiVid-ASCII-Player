# 🤝 Contributing to TermiVid ASCII Player

We welcome contributions from developers who are passionate about terminal applications and ASCII art!  
Whether you're fixing bugs, adding features, or improving performance, your contributions help make TermiVid better.

---

## 📝 Contribution Guidelines

- **Code Style**: Follow [PEP 8](https://peps.python.org/pep-0008/) and use `black` for formatting  
- **Testing**: Maintain >90% test coverage for new code  
- **Documentation**: Update docstrings and README for new features  
- **Performance**: Profile code changes that affect playback performance  
- **Compatibility**: Ensure changes work across supported Python versions (3.7+)  

---

## 🚀 How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/TermiVid.git
   cd TermiVid
2. **Set Up Development Environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```
3. **Create Feature Branch**
```
git checkout -b feature/your-feature-name
```
4 **Make Your Changes**
- Follow PEP 8 coding standards
- Add tests for new functionality
- Update documentation as needed
5. **Run Tests**
```
pytest tests/
python -m flake8 src/
```
6. **Commit and Push**
```
git commit -m "Add: Brief description of changes"
git push origin feature/your-feature-name
```
---
### 🎯 Types of Contributions Welcome
- **🐛 Bug Fixes** — Fix playback issues, memory leaks, or display problems
- ✨ **New Features** — Add codec support, new ASCII charsets, or playback features
- ⚡ **Performance** — Optimize frame processing, memory usage, or startup time
- 🎨 **Visual Improvements** — Enhance ASCII conversion algorithms or display quality
- 📚 **Documentation** — Improve guides, API docs, or code comments
- 🧪 **Testing** — Add test coverage or improve existing tests
- 🔧 **DevOps** — Improve build process, CI/CD, or deployment scripts
---
### 🛠️ Development Setup
```
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests with coverage
pytest --cov=src tests/

# Format code
black src/ tests/

# Type checking
mypy src/
```