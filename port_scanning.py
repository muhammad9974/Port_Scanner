import socket
from datetime import datetime

# Function to perform a port scan on a given host and range of ports
def port_scan(target_ip, start_port, end_port):
    # Print a banner with the current time and target information
    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Scan Started at: {datetime.now()}")
    print("-" * 50)
    
    # Loop through the range of ports
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for each connection attempt
        result = sock.connect_ex((target_ip, port))  # Try connecting to the port
        
        # Check the result of the connection attempt
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        
        # Close the socket after each check
        sock.close()

    print("-" * 50)
    print(f"Scan Completed at: {datetime.now()}")
    print("-" * 50)

# Main function to get user input and call the port_scan function
if __name__ == "__main__":
    print("Welcome to the Port Scanner!")
    
    # Get target IP from the user
    target_ip = input("Enter the IP address to scan: ")
    
    # Get port range from the user
    try:
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
        
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535.")
        else:
            # Perform the port scan
            port_scan(target_ip, start_port, end_port)
    except ValueError:
        print("Please enter valid numeric port values.")
