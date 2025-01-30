schemaVersion: "2.2"
description: "Install HTTPD on CentOS Stream, Ubuntu 20.04, and Amazon Linux 2 (no installation for Windows)."
mainSteps:
  - action: "aws:runShellScript"
    name: "InstallHttpdLinux"
    inputs:
      runCommand:
        - "#!/bin/bash"
        - 'OS=$(cat /etc/os-release | grep -w NAME | cut -d "=" -f 2 | tr -d \")'
        - 'if [[ "$OS" == "CentOS Stream" ]]; then'
        - '    yum install -y httpd'
        - '    systemctl enable httpd'
        - '    systemctl start httpd'
        - 'elif [[ "$OS" == "Ubuntu" ]]; then'
        - '    apt update && apt install -y apache2'
        - '    systemctl enable apache2'
        - '    systemctl start apache2'
        - 'elif [[ "$OS" == "Amazon Linux" ]]; then'
        - '    yum install -y httpd'
        - '    systemctl enable httpd'
        - '    systemctl start httpd'
        - 'else'
        - '    echo "Unsupported OS or no action needed for Windows"'
        - 'fi'
  - action: "aws:runPowerShellScript"
    name: "SkipWindowsHttpd"
    precondition:
      StringEquals:
        - "platformType"
        - "Windows"
    inputs:
      runCommand:
        - Write-Host "HTTPD installation is not required for Windows"
