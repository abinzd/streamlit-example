<!DOCTYPE html>
<html>
<head>
  <title>Random Quote Generator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 50px;
    }

    h1 {
      color: #333;
    }

    .quote {
      margin-top: 30px;
      font-size: 20px;
    }

    button {
      margin-top: 20px;
      padding: 10px 20px;
      font-size: 16px;
      background-color: #333;
      color: #fff;
      border: none;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Random Quote Generator</h1>
  <div class="quote">
    <p id="quoteText">Click the button to generate a random quote.</p>
  </div>
  <button id="generateButton" onclick="generateQuote()">Generate Quote</button>

  <script>
    // Array of quotes
    var quotes = [
      "The only way to do great work is to love what you do. - Steve Jobs",
      "Innovation distinguishes between a leader and a follower. - Steve Jobs",
      "Stay hungry, stay foolish. - Steve Jobs",
      "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
      "The best way to predict the future is to create it. - Peter Drucker",
      "Believe you can and you're halfway there. - Theodore Roosevelt",
      "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
      "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
    ];

    // Function to generate a random quote
    function generateQuote() {
      var randomNumber = Math.floor(Math.random() * quotes.length);
      document.getElementById("quoteText").innerHTML = quotes[randomNumber];
    }
  </script>
</body>
</html>
