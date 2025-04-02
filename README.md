# Bank Management System

A simple banking system application with both console and web interfaces.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Configure the application for local development:
   
   Option 1: Using Streamlit secrets (recommended)
   - Create a `.streamlit/secrets.toml` file in the root directory
   - Copy the structure from `.streamlit/secrets.example.toml`
   - Add your database credentials and other settings

   Option 2: Using environment variables (.env file)
   - Create a `.env` file in the root directory
   - Add the following environment variables:
   ```
   DB_HOST=your_database_host
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_NAME=your_database_name
   ```

3. Run the application:
   - Console interface: `python main.py`
   - Web interface: `streamlit run Streamlit.py`

## Features

- User registration and login
- Deposit and withdraw funds
- Check account balance
- Transfer money between accounts
- Transaction tracking

## Configuration Options

The secrets configuration provides the following sections:

- `[database]` - Database connection settings
- `[application]` - General application information
- `[features]` - Enable/disable specific features
- `[settings]` - Application parameters like limits
- `[ui]` - User interface customization

## Deployment on Streamlit Community Cloud

### Step 1: Prepare Your Repository

1. Make sure your code is in a GitHub repository
2. Ensure your repository has these files:
   - Streamlit.py (main application file)
   - requirements.txt (correctly formatted without merge conflicts)
   - Other necessary Python files (database.py, Bank.py, etc.)
3. Add `.streamlit/secrets.toml` to your `.gitignore` file

### Step 2: Deploy to Streamlit Community Cloud

1. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
2. Log in with your GitHub account
3. Click "New app"
4. Select your repository, branch, and main file (Streamlit.py)
5. Click "Advanced settings"
6. In the "Secrets" section, copy and paste the contents of your `.streamlit/secrets.example.toml` file (with real credentials)
7. Click "Deploy!"

### Step 3: Troubleshooting Deployment Issues

If you encounter deployment errors:

1. Check the error logs in the Streamlit Community Cloud dashboard
2. Verify that your requirements.txt file is properly formatted
3. Make sure your database credentials are correct in the secrets
4. If code changes are needed, update your GitHub repository and the app will automatically redeploy

For more information, see [Streamlit Secrets Management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).
