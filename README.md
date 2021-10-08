# password-safe
This is an effort to create a robust password security process.

Please feel free to collaborate if you find it interesting

### Status:  
In progress

## Objectives
1. User would have a username and password; if not, process would help create one.
2. Password would be user driven, however the storage of password would have multiple layers of protection.

### Password protection layers
1. The user provide password is transformed into a hash value using SHA512.
2. The SHA512 hash is hashed again using bcrypt with a cost of 10, and a unique, per-user salt.
3. The resulting bcrypt hash is encrypted with AES256 using a secret key (common to all hashes), commonly referred to as a pepper.

### Tech Stack

Name | Detail
:-----|:-------
Python | Program language
MongoDB Atlas | This cloud no-sql database is used to store user name, hashed password and per-user salt

## References
This project is directly inspired from the below resources.

<a href="https://www.troyhunt.com/we-didnt-encrypt-your-password-we-hashed-it-heres-what-that-means/">we-didnt-encrypt-your-password-we-hashed-it-heres-what-that-means</a>

<a href="https://dropbox.tech/security/how-dropbox-securely-stores-your-passwords">how-dropbox-securely-stores-your-passwords</a>
