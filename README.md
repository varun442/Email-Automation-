# Email Automation for Job Applications

An automated system for sending personalized job application emails with resume attachments.

## Setup

1. Clone the repository
```bash
git clone <repository-url>
cd email-automation
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
- Copy `.env.example` to `.env`
- Update the values in `.env` with your email credentials
```bash
cp .env.example .env
```

5. Prepare your data
- Place your resume PDF in the data directory
- Create recipients CSV using `createcsv.py`
- CSV should have columns: Name, Email

6. Run the system
```bash
python send_emails.py
```

## Features
- Personalized emails with first name
- Resume attachment
- Rate limiting to avoid spam filters
- Activity logging
- Environment variable configuration

## Requirements
- Python 3.8+
- Gmail account with App Password
- PDF resume file
- CSV file with recipient information

## File Structure
```
email-automation/
├── send_emails.py          # Main email script
├── create_recipients_csv.py # CSV creation script
├── requirements.txt        # Project dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Notes
- Emails are sent with a 1-minute delay to avoid spam filters
- All activities are logged in `email_log.txt`
- Uses Gmail's SMTP server