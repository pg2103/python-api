## Step 1: Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone git@github.com:pg2103/python-api.git
cd python-api

```

## Step 2: Create a Virtual Environment

This keeps the project dependencies isolated from your main system.

```bash
python -m venv venv

```

## Step 3: Activate the Environment

This step depends on which **Operating System** you are using:

| Operating System | Command |
| --- | --- |
| **Windows** | `venv\Scripts\activate` |
| **macOS / Linux** | `source venv/bin/activate` |

> **Note:** Once activated, you should see `(venv)` appear at the start of your terminal prompt.

## Step 4: Install Dependencies

Now, pull in all the libraries the project needs:

```bash
pip install -r requirements.txt

```

## Step 5: Run the Application

The final step is to actually execute the code. Usually, Python APIs have a main entry point. Look for a file named `app.py`
Try running:

```bash
python app.py

```

---
