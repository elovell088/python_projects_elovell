import paramiko

def transfer_file_via_ssh(local_path, remote_path, hostname, port, username, password):
    
    ssh_client = paramiko.SSHClient()

    try:
        #Grabs the servers public key
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the server
        ssh_client.connect(hostname=hostname, port=port, username=username, password=password)

        #Creates an SFTP Client
        sftp_client = ssh_client.open_sftp()

        #Transfers the file
        sftp_client.put(local_path, remote_path)

        print(f"File transferred successfully from {local_path} to {remote_path} on {hostname}")
    except Exception as e:
        print(f"File transfer failed: {str(e)}")
    finally:
        # Close the SFTP session and SSH connection
        if ssh_client:
            ssh_client.close()

local_file_path = '/path/to/local/file.txt'
remote_file_path = '/path/to/remote/file.txt'
hostname = 'your_server_hostname'
port = 22
username = 'your_username'
password = 'your_password'

transfer_file_via_ssh(local_file_path, remote_file_path, hostname, port, username, password)
