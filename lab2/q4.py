def srt_txt():
    filename=input("Enter filename: ")
    with open(filename,'r') as f:
        text=f.read().lower()
    words=text.split()
    sorted_words=sorted(words)
    with open("My_output.txt",'w+') as f:
        for word in sorted_words:
            f.write(word+'\n')
srt_txt()