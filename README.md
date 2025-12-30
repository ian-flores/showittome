# `showittome`

> **A security demonstration of supply chain attacks in data science environments**

## Warning

**This repository contains intentionally malicious code for educational purposes only.**

This project demonstrates how a supply chain attack could steal credentials from a user's environment. The code is designed to illustrate security vulnerabilities, not to be used for actual attacks.

**Do not:**
- Use this code against systems you do not own or have explicit permission to test
- Deploy the credential-stealing R package in any production environment
- Use this for any malicious purpose

**This code is provided solely to:**
- Educate data professionals about supply chain attack risks
- Demonstrate why credential security matters
- Show how easily malicious code can hide in innocuous-looking packages

## Context

### Purpose

People adjacent to data science (data engineers, data scientists, data analysts, business analysts) are usually not familiar with the concepts of supply chain attacks or securing their credentials. The purpose of this repository is to showcase an example of how an attacker could steal unencrypted SSH keys from someone's environment using an R package with very little dependencies and sending it to a Flask API to be stored and processed.

### How the Attack Works

1. **Victim installs the R package** - The package appears harmless with minimal dependencies (only `httr`)
2. **Victim calls `grabber()`** - The function scans `~/.ssh/` for `.pem` private key files
3. **Keys are exfiltrated** - Private keys, filenames, and IP address are sent via POST to an attacker-controlled server
4. **Attacker receives credentials** - The Flask API logs the stolen keys for later use

This demonstrates why you should:
- Never install packages from untrusted sources
- Always review package code before installation
- Encrypt your SSH private keys with passphrases
- Use SSH agents instead of storing raw keys

### License

**All of the code hereby included is protected under the [Hippocratic License Version 2.1](LICENSE.md).**

This license permits use for educational and defensive security purposes while prohibiting use that violates human rights or causes harm.

## Infrastructure

### R Package

The R package is contained in the `R_pkg` directory. It contains one function, `grabber()`, that looks at all of the credentials files in the `~/.ssh/` folder and sends the private keys via a POST request to a server. It has one R package dependency, the `httr` package.

#### Installation (for educational review only)

```r
# Do NOT install this on any system with real credentials
# For code review only:
devtools::install_local("R_pkg")
```

### Python API

The Python API is contained in the `Python_API` directory. It contains the Flask API and the Docker Compose files to deploy the API.

#### Flask API

The Flask API is contained within the `Python_API/api` directory. The API has one POST endpoint at `/showittome` that returns a 200 code. If there is a GET request the API will deny the request so the API is not visible by visiting the website's endpoint in a browser. The connections to the API are handled by a `Gunicorn` server.

#### Running the API (isolated environment only)

```bash
cd Python_API
docker-compose up --build
```

The API will be available at `http://localhost/showittome` (POST only).

#### Docker Compose

The `docker-compose.yaml` file brings up two services to serve the API. The first service is the API itself and the second service is an Nginx proxy to handle the connections to the `Gunicorn` server.

## Protecting Yourself

If you're a data professional, here's how to protect against this type of attack:

1. **Encrypt your SSH keys** - Always use a passphrase when generating keys
2. **Use SSH agents** - Don't leave unencrypted keys on disk
3. **Audit packages** - Review source code before installing, especially from unknown sources
4. **Use virtual environments** - Isolate package installations
5. **Monitor network traffic** - Watch for unexpected outbound connections
6. **Check package popularity** - Be wary of new packages with few downloads

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## Acknowledgements

Docker configuration adapted from: https://github.com/realpython/orchestrating-docker

## Responsible Disclosure

If you discover a security vulnerability in this demonstration code or have concerns about its potential misuse, please open an issue or contact the maintainer directly.
