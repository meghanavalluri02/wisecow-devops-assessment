@echo off
echo Generating self-signed TLS certificate for Wisecow...
echo.

REM Create directory for certificates
if not exist certs mkdir certs
cd certs

REM Generate private key and certificate
echo Creating private key...
openssl genpkey -algorithm RSA -out tls.key -pkeyopt rsa_keygen_bits:2048

echo Creating certificate signing request...
openssl req -new -key tls.key -out tls.csr -subj "/CN=wisetow.local"

echo Creating self-signed certificate...
openssl x509 -req -days 365 -in tls.csr -signkey tls.key -out tls.crt -extfile <(printf "subjectAltName=DNS:wisecow.local,IP:127.0.0.1,IP:192.168.49.2")

echo Cleaning up...
del tls.csr

echo.
echo Certificate files created:
echo   tls.crt  - Certificate
echo   tls.key  - Private key
echo.

REM Create Kubernetes TLS secret
echo Creating Kubernetes TLS secret...
kubectl create secret tls wisecow-tls ^
  --cert=tls.crt ^
  --key=tls.key ^
  --dry-run=client -o yaml | kubectl apply -f -

if %errorlevel% equ 0 (
    echo.
    echo SUCCESS! TLS secret "wisecow-tls" created in Kubernetes!
    echo.
    echo Test HTTPS access:
    echo   1. Run: kubectl port-forward service/wisecow-service 8443:80
    echo   2. Visit: https://localhost:8443
    echo   3. Click "Advanced" ^> "Proceed to localhost (unsafe)"
    echo.
    echo Note: The certificate is self-signed, so browsers show "unsafe" warning.
) else (
    echo.
    echo ERROR creating TLS secret. Check kubectl output above.
)

pause