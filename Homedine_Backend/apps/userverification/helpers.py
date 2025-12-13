import random
from django.core.mail import send_mail

def get_otp(firstname, email):
    otp_code = random.randint(100000, 999999)
    
    subject = 'Your Homedine Account OTP Verification'

    message = f"""
                Hey {firstname},

                Welcome to Homedine! Your OTP for verifying your account is: {otp_code}

                Homedine is your one-stop platform to buy and sell kitchen appliances, making your kitchen look aesthetic, organized, and absolutely mind-blowing!

                Please enter this OTP correctly to verify your account and start exploring amazing kitchen products today.

                Thank you for joining our Homedine community!
                """

    # HTML version
    html_message = f"""
                        <html>
                            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                                <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e2e2e2; border-radius: 10px;">
                                    <h2 style="color: #2E86C1; text-align: center;">Welcome to Homedine, {firstname}!</h2>
                                    <p>We’re excited to have you on board. Your OTP for verifying your account is:</p>
                                    <h1 style="font-size: 48px; color: #2E86C1; text-align: center; margin: 20px 0;">{otp_code}</h1>
                                    <p style="font-size: 16px;">
                                        Homedine is a unique platform where you can buy and sell kitchen appliances, 
                                        helping you create a kitchen that is not only functional but also aesthetic and mind-blowing.
                                    </p>
                                    <p>Please enter this OTP in the app to verify your account and start browsing amazing products!</p>
                                    <p style="text-align: center; margin-top: 30px; font-size: 14px; color: #888;">
                                        Thank you for joining the Homedine community!<br>
                                        Your dream kitchen awaits 🏡✨
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
