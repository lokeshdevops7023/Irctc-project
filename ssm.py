import boto3
import json

# Initialize the SSM client
ssm_client = boto3.client('ssm')

def update_document_with_local_content(doc_name, file_path):
    try:
        # Read the updated content from the local file
        with open(file_path, 'r') as file:
            updated_content = file.read()

        # Debug: Print the content to check if it's well-formed
        print("Updated Document Content: ")
        print(updated_content)

        # Check if the content is valid JSON
        try:
            json.loads(updated_content)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format: {e}")
            return

        # Update the document with the new content
        updated_doc = ssm_client.update_document(
            Name=doc_name,
            Content=updated_content,
            DocumentVersion="$LATEST"  # Use $LATEST to refer to the latest version
        )

        # Get the new version of the document
        new_version = updated_doc["DocumentDescription"]["LatestVersion"]
        print(f"Updated document to version: {new_version}")

        # Set the new version as the default version
        ssm_client.update_document_default_version(
            Name=doc_name,
            DocumentVersion=new_version
        )
        print(f"Set version {new_version} as the default for document '{doc_name}'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace with your document name and the path to the updated file
    document_name = "ssm-Updatefcc-test-verify-ec2-alarms-automation"
    local_file_path = "/Users/saicandy/Downloads/demo.json"  # Path to your local updated file

    update_document_with_local_content(document_name, local_file_path)

