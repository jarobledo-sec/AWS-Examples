# AWS s3 module is imported
Import-Module AWS.Tools.S3

# https://docs.aws.amazon.com/powershell/v5/reference/
# set region
$region = "eu-west-3"
Set-DefaultAWSRegion -Region $region

# name of the bucket is requested
$bucketName = Read-Host -Prompt 'Enter the S3 bucket name'

# region and bucket name varibles are displayed
Write-Host "AWS Region: $region"
Write-Host "S3 Bucket: $bucketName"

# create a function to verify the existence of a bucket with that name
function BucketExists {
    $bucket = Get-S3Bucket -BucketName $bucketName -ErrorAction SilentlyContinue
    return $null -ne $bucket
}

if (-not (BucketExists)){
    Write-Host "Bucket does not exists..."
    New-S3Bucket -BucketName $bucketName # -Region $region
} else {
    Write-Host "Bucket already exists..."
} 

# create a new file
$fileName = 'myfile.txt'
$fileContent = 'Hello World!'
Set-Content -Path $fileName -Value $fileContent

# upload objects
Write-S3Object -BucketName $bucketName -File $fileName -Key $fileName # -Region $region

