# C.Q.B.v2

## 📦 Installation Guide

Follow these steps to set up the project locally.

### 1. Clone the Repository

To get started, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/Abeltodoanything/lounge-lizard.git 
```
Then navigate into the project directory:
```bash
cd lounge-lizard
```
### 2. Install uv with this command

```bash
pip install uv
```
### 5. Create a .env
Before running the code, make a .env file and add your BASE_URL and your API_KEY. The file should contain two lines.
```bash
 BASE_URL={url}
 API_KEY={API Key}
 ```
For api keys i recomend https://openrouter.ai

### 4. Run the code with uv
```bash
uv run main.py
```