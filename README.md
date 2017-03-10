# sample_code

## soup.py
Requires install of pip module BeautifulSoup

```
pip install beautifulsoup4
```

## install_jenkins_plugins.sh
### Requirements
#### Authentication
If your Jenkins requires authentication, you should set up public key authentication. Login from the web UI and go to http://yourserver.com/me/configure, then set your public keys in the designated text area. When connecting to the server, the CLI will look for ~/.ssh/identity, ~/.ssh/id_dsa, ~/.ssh/id_rsa and use those to authenticate itself against the server. Alternatively, the -i option can be used to explicitly specify the location of the private key.

See the middle of this guide for how to generate SSH key pair, if you don't have one yet.

If you have used PuttyGen to generate your keys, you will have to convert them to openssh format. Otherwise Jenkins might silently ignore your keys and you will be Authenticated as: anonymous.
