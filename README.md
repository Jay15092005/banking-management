# Bank Management System

A simple banking system application with both console and web interfaces.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Configure the application:
   
   Option 1: Using TOML configuration (recommended)
   - The application uses a `config.toml` file for configuration
   - You can edit this file to change database settings and application parameters

   ```toml
   [database]
   host = "your_database_host"
   user = "your_database_user"
   password = "your_database_password"
   name = "your_database_name"
   ```

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

The `config.toml` file provides the following configuration sections:

- `[database]` - Database connection settings
- `[application]` - General application information
- `[features]` - Enable/disable specific features
- `[settings]` - Application parameters like limits
- `[ui]` - User interface customization

## Deployment on Streamlit Community Cloud

This application is designed to be easily deployed on Streamlit Community Cloud.

### Steps for Deployment:

1. Create a GitHub repository with your code

2. Set up secrets in Streamlit Community Cloud:
   - Go to your app dashboard in Streamlit Community Cloud
   - Navigate to the "Secrets" section
   - Add your database credentials and other configuration settings:

   ```toml
   [database]
   host = "your_database_host"
   user = "your_database_user"
   password = "your_database_password"
   name = "your_database_name"
   
   [application]
   name = "Bank Management System"
   ```

3. Deploy your app:
   - Connect your GitHub repository to Streamlit Community Cloud
   - Select the `Streamlit.py` as the main file to run
   - Deploy!

The application is designed to first look for secrets in Streamlit's secrets management system
for production deployment, then fall back to local configuration files for development.

### Secrets Management

For local development:
- Use `.streamlit/secrets.toml` file (not committed to version control)
- This file will only be used during local development

For Streamlit deployment:
- Configure secrets through the Streamlit Community Cloud dashboard
- These will be securely stored and available to your application when deployed
