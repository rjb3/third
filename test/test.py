html = """    <li><span class="plaincharacterwrap break">
                     Zazzafooky but one two three!
                 </span></li>
 <li><span class="plaincharacterwrap break">
                     Zazzafooky2
                 </span></li>
 <li><span class="plaincharacterwrap break">
                     Zazzafooky3
                 </span></li>
 """
#print html
#html = print line "".join([line.strip() for line in html.split("\n")])
for line1 in html.split("\n") :
    for line2 in line1.split("\r") :
        print line2.strip() 
#print html

