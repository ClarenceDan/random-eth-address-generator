from eth_keys import keys
import secrets

def main():
    with open("output.txt", "w") as file:
        for i in range(100):
            # Generate a secure random private key
            private_key_bytes = secrets.token_bytes(32)
            private_key = keys.PrivateKey(private_key_bytes)

            # Derive the public key and Ethereum address from the private key
            public_key = private_key.public_key
            address = public_key.to_checksum_address()

            # Write the private key and address to the file
            file.write(f"{private_key}:{address}\n")

    print("Keys and addresses have been written to output.txt")

if __name__ == "__main__":
    main()
