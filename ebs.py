import boto3
import csv

# Initialize a session using boto3
session = boto3.Session(region_name="us-east-1")
ec2 = session.client("ec2")

# Fetch EBS volumes in "available" state
volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes']

# Prepare the CSV data
csv_file_path = "ebs_volumes_available_us_east_1.csv"
csv_headers = ["Volume ID", "Volume Size (GiB)", "Creation Date"]

with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)  # Write headers
    
    for volume in volumes:
        writer.writerow([
            volume['VolumeId'],
            volume['Size'],
            volume['CreateTime'].strftime('%Y-%m-%d %H:%M:%S')  # Format datetime to string
        ])

print(f"CSV file created: {csv_file_path}")

