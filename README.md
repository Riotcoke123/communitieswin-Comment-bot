<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>communities.win Comment Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            font-size: 28px;
            margin-bottom: 20px;
        }
        h2 {
            font-size: 24px;
            margin-bottom: 16px;
        }
        pre {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, monospace;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>communities.win Comment Bot</h1>
    <h2>Overview</h2>
    <p>This Python script automates commenting on new posts in the communities.win platform using Selenium WebDriver.</p>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3</li>
        <li>Selenium WebDriver</li>
        <li>Chrome WebDriver (chromedriver)</li>
    </ul>
    <h2>Setup</h2>
    <ol>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install selenium</code></pre>
        </li>
        <li><strong>Download Chrome WebDriver:</strong>
            <p>Download the <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads" target="_blank">Chrome WebDriver</a> that matches your Chrome browser version. Make sure it's either in your system's PATH or provide the executable path in the script (<code>webdriver.Chrome()</code>).</p>
        </li>
        <li><strong>Comments File:</strong>
            <p>Prepare a text file (<code>comments.txt</code>) containing the comments you want to post. Each comment should be on a separate line.</p>
        </li>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li><strong>Run the Script:</strong>
            <p>Execute the Python script (<code>comment_bot.py</code>).</p>
        </li>
        <li><strong>Login:</strong>
            <p>The script will open Chrome, navigate to the communities.win new posts section, and prompt you to log in. Modify the login process in the script (<code>username</code>, <code>password</code>) based on your credentials.</p>
        </li>
        <li><strong>Automated Commenting:</strong>
            <p>The bot will scroll through new posts, select a post, check if it has already commented, select a random comment from <code>comments.txt</code>, and post it if not already present. It avoids detection by simulating human behavior with random delays between actions.</p>
        </li>
        <li><strong>Logging and Error Handling:</strong>
            <p>Logs are printed in the console, including errors encountered during processing. Ensure the script runs smoothly without interruption to avoid unexpected behavior.</p>
        </li>
    </ol>
    <h2>Notes</h2>
    <ul>
        <li>Adjust the script as per changes in the website structure or to enhance functionality.</li>
        <li>Handle exceptions gracefully to maintain robustness of the automation.</li>
    </ul>
    <h2>Disclaimer</h2>
    <ul>
        <li>Use this script responsibly and adhere to communities.win policies and guidelines.</li>
        <li>Avoid excessive or spammy behavior to prevent account suspension or bans.</li>
    </ul>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
</body>
</html>
