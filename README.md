# vectrum
vector self drive code


1. install python3
2. python3 -m pip install --user anki_vector (install sdk)
3. python3 -m pip install --user --upgrade anki_vector (update sdk)
4. python3 -m anki_vector.configure
5. Download Python example scripts that use the Vector SDK


# AWS:
image match(r2d2):
- S3 bucket
- S3 folder1
- lambda1 to poll s3 for new images
- lambda1 above publishes to SNS topic
- lambda2 subscribes to the SNS topic and triggers image match job
- response1 to be sent to r2d2 local program

# Local:
- r2d2 program to capture image from vector and upload to s3 folder1
- r2d2 to poll or wait to receive response1
- r2d2 to start yoda program with the response inference

