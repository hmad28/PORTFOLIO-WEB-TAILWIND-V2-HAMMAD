from base64 import b64encode

# Load and read the uploaded HTML file
file_path = "index.php"
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Encode the HTML content in Base64
encoded_html = b64encode(html_content.encode("utf-8")).decode("utf-8")

# Create a simple HTML + JavaScript wrapper that decodes and renders the HTML
output_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Encrypted Page</title>
</head>
<body>
    <script>
        const encoded = "{encoded_html}";
        const decoded = atob(encoded);
        document.write(decoded);
    </script>
</body>
</html>
"""

# Save the encrypted HTML wrapper to a new file
output_path = "encrypted_index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output_html)

output_path
