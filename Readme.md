# Facebook Auto Poster 🤖

A Python script that uses Selenium to automate logging into a Facebook account and publishing a post. This project is built for educational purposes to demonstrate browser automation.

---

## ✨ Features

-   🔐 **Secure Login**: Safely handles credentials using a `.env` file to keep them out of the source code.
-   🚦 **Manual Intervention**: Intelligently pauses the script to allow the user to manually solve CAPTCHAs or dismiss popups.
-   ✍️ **Automated Posting**: Automatically navigates to the post creation dialog and publishes predefined text content.
-   ⚙️ **Auto Driver Management**: Uses `webdriver-manager` to seamlessly download and manage the correct ChromeDriver.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,selenium" />
</p>

-   **Scripting Language**: **Python**
-   **Browser Automation**: **Selenium WebDriver**

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   Google Chrome Browser

### Installation

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/jyrjanon/Facebook_Blog_Autoposter.git](https://github.com/jyrjanon/Facebook_Blog_Autoposter.git)
    cd Facebook_Blog_Autoposter
    ```

2.  **Install Required Packages**
    It's recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

    # Install dependencies
    pip install selenium webdriver-manager python-dotenv
    ```

3.  **Set Up Environment Variables**
    Create a `.env` file in the root of the project and add your Facebook credentials:
    ```env
    FACEBOOK_EMAIL="your-email@example.com"
    FACEBOOK_PASSWORD="your-secret-password"
    ```

---

## 🏃 How to Run

1.  Execute the script from your terminal:
    ```bash
    python main.py
    ```
2.  The script will open Chrome, navigate to Facebook, and log you in.
3.  **Wait for the prompt in your terminal!** Manually solve any puzzles and close popups in the browser.
4.  Once the main feed is visible, press **Enter** in the terminal to resume the automation.

---

## ⚠️ Disclaimer

This script is intended for educational purposes only. Automating social media accounts may violate their Terms of Service. Please use this project responsibly and at your own risk.

## Future Improvements

- Add support for scheduling multiple posts.
- Improve error handling for failed logins.
- Add support for posting images.

## Future Scalability

- Automated AI generated Captions and Description
