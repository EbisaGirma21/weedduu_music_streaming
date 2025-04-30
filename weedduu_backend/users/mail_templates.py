from datetime import datetime

def mail_template(name, otp_code):
    date = datetime.now().strftime("%d %B, %Y")
    return f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Arkwood Movies</title>

    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap"
      rel="stylesheet"
    />
  </head>
  <body
    style="
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background-size: cover;
      background-color: #cccccc;
      font-size: 14px;
      padding-bottom: 50px;
    "
  >
    <div
      style="
        max-width: 680px;
        border: 2px solid #e6ebf1;
        margin: 0 auto;
        padding: 45px 30px 60px;
        background-color: rgba(
          255,
          255,
          255,
          0.8
        ); /* white background with transparency */
        font-size: 14px;
        color: #434343;
        margin-top: 10px;
        margin-bottom: 25px;
      "
    >
      <header>
        <table style="width: 100%">
          <tbody>
            <tr style="height: 0; width: 100%; text-align: center">
              <img
                src="https://euvievq.stripocdn.email/content/guids/de03dfc8-c7c2-4d09-96db-f929422ec90d/images/weedduu1.png"
                alt=""
                title="Smart home logo"
                height="100"
                class="adapt-img"
                style="
                  display: block;
                  font-size: 14px;
                  border: 0;
                  outline: none;
                  text-decoration: none;
                  width: 100%;
                  object-fit: contain;
                "
              />
            </tr>
            <tr style="height: 0">
              <td style="width: 20px">
                <img alt="" src="./Arkwood_Logo.png" height="50px" />
              </td>

              <td>
                <span
                  style="
                    font-size: 24px;
                    font-weight: 600;
                    color: #000;
                    margin-left: -30px;
                    height: 100%;
                  "
                  >Weedduu App</span
                >
              </td>
              <td style="text-align: right">
                <span style="font-size: 16px; line-height: 30px; color: #000"
                  >{date}</span
                >
              </td>
            </tr>
          </tbody>
        </table>
      </header>

      <main>
        <div
          style="
            margin: 0;
            margin-top: 70px;
            padding: 92px 30px 115px;
            background: #ffffff;
            border-radius: 30px;
            text-align: center;
          "
        >
          <div style="width: 100%; max-width: 489px; margin: 0 auto">
            <p
              style="
                margin: 0;
                margin-top: 17px;
                font-size: 16px;
                font-weight: 500;
              "
            >
              Hey {name},
            </p>
            <h1
              style="
                margin: 0;
                font-size: 24px;
                font-weight: 500;
                color: #1f1f1f;
              "
            >
              Your OTP
            </h1>
            <p
              style="
                margin: 0;
                margin-top: 17px;
                font-weight: 500;
                letter-spacing: 0.56px;
              "
            >
              Thank you for joining
              <strong>Weedduu</strong>, the gospel music streaming app created
              to uplift your spirit and feed your soul. From classic gospel
              hymns to modern praise tracks, you now have access to a world of
              powerful worship music—anytime, anywhere. OTP is valid for
              <span style="font-weight: 600; color: #e6ba52">2 minutes</span>.
              Do not share this code with others
            </p>
            <p
              style="
                margin: 0;
                margin-top: 60px;
                font-size: 40px;
                font-weight: 600;
                letter-spacing: 25px;
                color: #e6ba52;
              "
            >
              {otp_code}
            </p>
          </div>
        </div>

        <p
          style="
            max-width: 400px;
            margin: 0 auto;
            margin-top: 90px;
            text-align: center;
            font-weight: 500;
            color: #8c8c8c;
          "
        >
          Need help? Ask at
          <a href="mailto:arkwood@example.com" style="text-decoration: none"
            >weedduu@example.com</a
          >
          or visit our
          <a href="" target="_blank" style="text-decoration: none"
            >Help Center</a
          >
        </p>
      </main>

      <footer
        style="
          width: 100%;
          max-width: 490px;
          margin: 20px auto 0;
          text-align: center;
          border-top: 1px solid #e6ebf1;
        "
      >
        <p
          style="
            margin: 0;
            margin-top: 40px;
            font-size: 16px;
            font-weight: 600;
            color: #434343;
          "
        >
          Weedduu App
        </p>
        <p style="margin: 0; margin-top: 8px; color: #434343">
          Address: Addis Ababa, Ethiopia.
        </p>
        <div style="margin: 0; margin-top: 16px">
          <a href="" target="_blank" style="display: inline-block">
            <img
              width="36px"
              alt="Facebook"
              src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661502815169_682499/email-template-icon-facebook"
            />
          </a>
          <a
            href=""
            target="_blank"
            style="display: inline-block; margin-left: 8px"
          >
            <img
              width="36px"
              alt="Instagram"
              src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661504218208_684135/email-template-icon-instagram"
          /></a>
          <a
            href=""
            target="_blank"
            style="display: inline-block; margin-left: 8px"
          >
            <img
              width="36px"
              alt="Twitter"
              src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661503043040_372004/email-template-icon-twitter"
            />
          </a>
          <a
            href=""
            target="_blank"
            style="display: inline-block; margin-left: 8px"
          >
            <img
              width="36px"
              alt="Youtube"
              src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661503195931_210869/email-template-icon-youtube"
          /></a>
        </div>
        <p style="margin: 0; margin-top: 16px; color: #434343">
          Copyright © 2025 Weedduu. All rights reserved.
        </p>
      </footer>
    </div>
  </body>
</html>
    '''
