import random
from django.core.mail import send_mail

def get_otp(firstname, email):
    otp_code = random.randint(100000, 999999)
    
    subject = 'Homedine Password Reset OTP'

    message = f"""
                Hey {firstname},

                We received a request to reset your Homedine account password.

                Your OTP for password reset is: {otp_code}

                If you did not request a password reset, please ignore this email.
                Do not share this OTP with anyone.

                Thanks,
                Team Homedine
                """

    html_message = f"""
                        <html>
                            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                                <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e2e2e2; border-radius: 10px;">
                                    <h2 style="color: #E74C3C; text-align: center;">
                                        Password Reset Request
                                    </h2>

                                    <p>Hi {firstname},</p>

                                    <p>
                                        We received a request to reset your <strong>Homedine</strong> account password.
                                        Please use the OTP below to proceed with resetting your password:
                                    </p>

                                    <h1 style="font-size: 48px; color: #E74C3C; text-align: center; margin: 20px 0;">
                                        {otp_code}
                                    </h1>

                                    <p style="font-size: 15px;">
                                        This OTP is valid for a short time.  
                                        <strong>Do not share this code with anyone</strong>.
                                    </p>

                                    <p>
                                        If you did not request a password reset, you can safely ignore this email.
                                        Your account will remain secure.
                                    </p>

                                    <p style="text-align: center; margin-top: 30px; font-size: 14px; color: #888;">
                                        — Team Homedine<br>
                                        Making your kitchen smarter 🍽️✨
                                    </p>
                                </div>
                            </body>
                        </html>
                        """

    send_mail(
        subject=subject,
        message=message,
        from_email='homedine57@gmail.com',
        recipient_list=[email],
        fail_silently=False,
        html_message=html_message
    )

    return otp_code
