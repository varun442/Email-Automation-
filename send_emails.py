import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import time
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email configuration from environment variables
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')

# File paths
RESUME_PATH = "./data/Varun_Savai_Resume_saia.pdf"
CSV_PATH = "./data/recipients.csv"
LOG_FILE = "./data/email_log.txt"

def log_activity(message):
    """Log activities with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

def create_email_content(recipient_first_name):
    """Create email subject and body"""
    subject = "Software Development at Saia - Atlanta-based Full Stack Engineer | MS CS from GSU"
    
    body = f"""Hi {recipient_first_name},

I know we haven't been introduced yet, but I'll take just 60 seconds of your time. I'm Varun Savai, an Atlanta-based software engineer with 2+ years of experience and a recent MS in Computer Science from Georgia State University.

I'm deeply aligned with Saia's commitment to doing things the right way and delivering innovative logistics solutions. After reviewing your requirements, I'm excited about three specific areas where my experience directly matches your needs:

1. Full Stack Development & Code Quality
- Engineered responsive front-end components using ReactJS/JavaScript at Alien Attorney (Atlanta), improving workflow efficiency by 60%
- Developed microservices using Core Java and Spring Boot at LTIMindtree, reducing processing time by 40%
- Implemented comprehensive TDD & BDD testing frameworks, achieving 40% reduction in discrepancies

2. Cloud & DevOps Architecture
- Streamlined CI/CD pipelines using GitHub Actions and Docker, achieving 99% deployment success rate
- Implemented Kafka-based monitoring system processing 10,000+ daily transactions
- Strong experience with AWS, Kubernetes, and automated testing/monitoring tools

3. Relevant Project Experience
- SaaS AI Course Generator (courseaii.vercel.app)
  * Built high-performance platform using NextJS/ReactJS serving 1,000+ MAUs
  * Integrated multiple APIs and PostgreSQL for robust data management
  * Demonstrated ability to deliver production-ready, scalable solutions

Being based in Atlanta, I'm particularly excited about the opportunity to contribute to a local industry leader like Saia. My experience with both technical implementation and collaborative development would allow me to hit the ground running with your team.

Would you be open to a brief conversation about how my skills could contribute to Saia's continued success? I'm available at your convenience and can be reached at (862)-410-4910 or varunsavaigsu@gmail.com.

Best regards,
Varun Savai
Portfolio: https://varunsavai.vercel.app/

P.S. I've also applied through your careers portal (Job ID JR10369-2024) and am locally available for immediate start. If you're not the appropriate contact for this position, I would greatly appreciate if you could forward my profile to the relevant hiring manager."""
    
    return subject, body

def send_email(recipient_name, recipient_email):
    """Send email to a recipient"""
    try:
        # Get recipient's first name
        first_name = recipient_name.split()[0]
        
        # Create message
        msg = MIMEMultipart()
        subject, body = create_email_content(first_name)
        
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add body
        msg.attach(MIMEText(body, 'plain'))
        
        # Add resume
        with open(RESUME_PATH, 'rb') as f:
            resume = MIMEApplication(f.read(), _subtype='pdf')
            resume.add_header('Content-Disposition', 'attachment', filename=os.path.basename(RESUME_PATH))
            msg.attach(resume)
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
        success_msg = f"Successfully sent email to {recipient_name} ({recipient_email})"
        print(success_msg)
        log_activity(success_msg)
        return True
    
    except Exception as e:
        error_msg = f"Failed to send email to {recipient_name} ({recipient_email}): {str(e)}"
        print(error_msg)
        log_activity(error_msg)
        return False

def main():
    # Verify files exist
    if not os.path.exists(RESUME_PATH):
        print(f"Error: Resume file not found at {RESUME_PATH}")
        return
    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV file not found at {CSV_PATH}")
        return
    
    # Read the CSV file
    try:
        df = pd.read_csv(CSV_PATH)
        print(f"Found {len(df)} recipients in CSV file")
        log_activity(f"Starting email campaign to {len(df)} recipients")
        
        # Send emails with delays to avoid spam filters
        for index, row in df.iterrows():
            success = send_email(row['Name'], row['Email'])
            if success and index < len(df) - 1:  # Don't wait after the last email
                print(f"Waiting 1 minute before sending next email...")
                time.sleep(60)  # 2 minutes delay
        
        log_activity("Email campaign completed")
        print("Email campaign completed! Check email_log.txt for details.")
        
    except Exception as e:
        error_msg = f"Error in main execution: {str(e)}"
        print(error_msg)
        log_activity(error_msg)

if __name__ == "__main__":
    main()