import boto3

def list_certificates():
    # Create an ACM client
    acm_client = boto3.client('acm')

    # List all certificates in ACM
    response = acm_client.list_certificates()

    # Extract and print certificate information
    for certificate in response['CertificateSummaryList']:
        certificate_arn = certificate['CertificateArn']
        certificate_details = acm_client.describe_certificate(CertificateArn=certificate_arn)

        print(f"Certificate ARN: {certificate_arn}")
        print(f"Domain Name: {certificate_details['Certificate']['DomainName']}")
        print(f"Certificate Status: {certificate_details['Certificate']['Status']}")
        print(f"Issuer: {certificate_details['Certificate']['Issuer']}")
        print(f"Not Before: {certificate_details['Certificate']['NotBefore']}")
        print(f"Not After: {certificate_details['Certificate']['NotAfter']}")
        print("\n")

if __name__ == "__main__":
    list_certificates()
