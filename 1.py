
## Date: 30/11/2020 ## Ankita Patel ## 
# Completed coding : Problem solving for identifying subdoamins.


import re

regex = r"(https?:\/\/)?([w]{3}\.)?(\w*.\w*)([\/\w]*)"
domain_name = r"\.?(microsoft.com.*)"
input_urls_with_subdomains = ("https://blog.microsoft.com/test.html\n"
"https://www.blog.microsoft.com/test/test\n"
"https://test.microsoft.com\n"
"http://www.blog.xyz.abc.microsoft.com/test/test\n"
"https://www.microsoft.com")

subst = "\\3"

print ("Input_urls_with_subdomains:\n",input_urls_with_subdomains)
print ("-----------------------------")
print ("Result")
print ("-----------------------------")
result = re.sub(domain_name, "", re.sub(regex, subst, input_urls_with_subdomains, 0, re.MULTILINE | re.IGNORECASE))
if result:
    print (result)

print ("-----------------------------")


#################################

# Output #
# Input_urls_with_subdomains:
# https://blog.microsoft.com/test.html
# https://www.blog.microsoft.com/test/test
# https://test.microsoft.com
# http://www.blog.xyz.abc.microsoft.com/test/test
# https://www.microsoft.com
# -----------------------------
# Result 
# -----------------------------
# blog
# blog
# test
# blog.xyz.abc
#

#################################
