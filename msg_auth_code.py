import hashlib

def generate_mac(message, secret_key):
    """Generate a simple MAC using SHA-256 hash."""
    data = secret_key + message  # Combine secret key and message
    mac = hashlib.sha256(data.encode()).hexdigest()  # Generate hash
    return mac

def verify_mac(message, secret_key, received_mac):
    """Verify the MAC by comparing it with a freshly generated MAC."""
    expected_mac = generate_mac(message, secret_key)
    return expected_mac == received_mac

# Example Usage
message = "Hello, this is a secure message."
secret_key = "supersecretkey"

# Generate MAC
mac = generate_mac(message, secret_key)
print("Generated MAC:", mac)

# Verify MAC
is_valid = verify_mac(message, secret_key, mac)
print("Is the MAC valid?", is_valid)
