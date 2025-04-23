def frequentwords():
    filename=input("enter filename: ")
    with open(filename,'r') as f:
        text=f.read().lower()
    words=text.split()
    freq={}
    for word in words:
        if(word in freq):
            freq[word]+=1
        else:
            freq[word]=1
    sorted_words=sorted(freq.items(), key=lambda x:x[1],reverse=True)
    for s in sorted_words[:10]:
        print(s[0],s[1])
frequentwords()