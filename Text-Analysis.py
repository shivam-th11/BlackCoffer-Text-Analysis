


from bs4 import BeautifulSoup
import requests

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
nltk.download('punkt')

import string

    










data=pd.read_excel('Output Data Structure.xlsx')
print(data['URL'][0])
for link in range (100):
    
    
    
    
    
    url = f"{data['URL'][link]}"
    req = requests.get(url)
    
    soup = BeautifulSoup(req.content, "html.parser")
    
    tex=soup.get_text()
    
    blocklist=['title','p','ol','li']
    
    text_elements=[t for t in soup.find_all(text=True) if t.parent.name in blocklist]
    
    s="".join(text_elements)
    u=s.split(".")
    u.pop(-1)
    u.pop(-1)
    u.pop(-1)
    file1=".".join(u)
    
    #total_word=file1.split(" ")
    total_sent=nltk.sent_tokenize(file1)
    
    
    
    
    
       
    if len(file1)==0:
        
        
        data['POSITIVE SCORE'][link]=0
        data['NEGATIVE SCORE'][link]=0
        data['POLARITY SCORE'][link]=0
        data['SUBJECTIVITY SCORE'][link]=0
        data['AVG SENTENCE LENGTH'][link]=0
        data['PERCENTAGE OF COMPLEX WORDS'][link]=0
        
        
        data['FOG INDEX'][link]=0
        data['AVG NUMBER OF WORDS PER SENTENCE']=0
        data['COMPLEX WORD COUNT'][link]=0
        data['WORD COUNT'][link]=0
        data['SYLLABLE PER WORD'][link]=0
        data['PERSONAL PRONOUNS'][link]=0
        data['AVG WORD LENGTH'][link]=0
    
    
    
    
    
    
    
    
    else:
        
            
        f=open("StopWords_Auditor.txt",'r')
        g=open("StopWords_Currencies.txt",'r')
        h=open("StopWords_DatesandNumbers.txt",'r')
        i=open("StopWords_Generic.txt",'r')
        j=open("StopWords_GenericLong.txt",'r')
        k=open("StopWords_Geographic.txt",'r')
        l=open("StopWords_Names.txt",'r')
        
        
        
        
        
        
        
        
        
        fr=f.read()
        gr=g.read()
        hr=h.read()
        ir=i.read()
        jr=j.read()
        kr=k.read()
        lr=l.read()
        
        
        
        fr=nltk.word_tokenize(fr)
        gr=nltk.word_tokenize(gr)
        hr=nltk.word_tokenize(hr)
        ir=nltk.word_tokenize(ir)
        jr=nltk.word_tokenize(jr)
        kr=nltk.word_tokenize(kr)
        lr=nltk.word_tokenize(lr)
        
        
        
        
        stopwords=fr+gr+hr+ir+jr+kr+lr
        
        
        clean_file=[]
        f_sp=nltk.word_tokenize(file1)
        for x in f_sp:
            if x not in stopwords:
                clean_file.append(x)
        
        
        l=["<",">","?","`","~","!","@","#","$","%","^","’","&","*","(",")","_","+","|",',','.','-','=',':','.',';',"'","/",'''"''']
                
        for x in clean_file:
            if x in l:
                clean_file.remove(x)
                
        import string        
        punc_sign=string.punctuation
        
        for x in clean_file:
            if x in punc_sign:
                clean_file.remove(x)        
                
                
                
        #clean_file=" ".join(clean_file)  
        
        
        
        
        
        
        dict={'positive':[],'negative':[]}
        po=open('positive-words.txt','r')
        po=po.read()
        po=nltk.word_tokenize(po)
        
        
        
        for x in po:
            if x not in stopwords:
                dict['positive'].append(x)
                
                
        ne=open('negative-words.txt','r')
        ne=ne.read()
        ne=nltk.word_tokenize(ne)
        
        for x in ne:
            if x not in stopwords:
                dict['negative'].append(x)
                
                
        
        positive_score=[]
        for x in clean_file:
            if x in dict['positive']:
                positive_score.append(x)
                
        positive_score=len(positive_score)
        
        
        
        
        negative_score=[]
        for x in clean_file:
            if x in dict['negative']:
                negative_score.append(x)
                
        negative_score=len(negative_score)
        
        
        
        
        '''
        polarity score
        '''
        
        polarity_score=(positive_score - negative_score)/((positive_score + negative_score)+0.000001)
        
        
        '''
        subjectivity score
        '''
        subjectivity_score=(positive_score + negative_score)/ (len(clean_file) + 0.000001)
        
        
        '''
        total word and total sentence
        '''
        l=["<",">","?","`","~","!","@","#","$","%","^","&","’","*","(",")","_","+","|",',','.','-','=',':','.',';',"'","/",'''"''',"'"]
        
        for x in f_sp:
            if x in l:
                f_sp.remove(x)
        
        
        for x in f_sp:
            if x in punc_sign:
                f_sp.remove(x)
        
        
        avg_sen_len=len(f_sp)/len(total_sent)
        
        
        
        
        
        
        '''
        complex words
        '''
        complex_words=[]
        for x in f_sp:
            if x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')+x.count('A')+x.count('E')+x.count('I')+x.count('O')+x.count('U')>=3:
                complex_words.append(x)
                
                
                
                 
        for x in complex_words:
            if x[-2:]=="es" or x[-2:]=="ed":
                complex_words.remove(x)
                     
                
                
        percentage_complex_words=len(complex_words)/len(f_sp)   
        
        
        
        
        
        
        
        
        '''
        fog index
        '''
        length=list(map(lambda x: len(x),total_sent))
        rec1={'sentence':total_sent,'length':length}
        
        
        df1=pd.DataFrame(rec1)
        
        fog_index=0.4*(avg_sen_len + percentage_complex_words)
        print(fog_index)
        
        
        
        
        
        
        '''
        average no of words per sentence
        '''
        
        avg_no_of_word_per_sen=len(f_sp)/len(total_sent)
        
        
        
        '''
        complex word count
        '''
        complex_word_count= len(complex_words)
        
        
        
        '''
        word count
        '''
        from nltk.corpus import stopwords
        nltk.download('stopwords')
        allstopwords=stopwords.words("english")
        
        
        super_cleaned_text=[x for x in clean_file if x not in allstopwords]
        
        
        
        import string        
        punc_sign=string.punctuation
        
        for x in super_cleaned_text:
            if x in punc_sign:
                super_cleaned_text.remove(x)  
        
        
        word_count=len(super_cleaned_text)
        
        
        
        
        
        '''
        syllable count per word
        '''
        
        temp=f_sp.copy()
        
        for word in temp:
            if word[-2:]=="es" or word[-2:]== "ed":
                temp.remove(word)
        m=[]
        for x in temp:
            m.append(x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u')+x.count('A')+x.count('E')+x.count('I')+x.count('O')+x.count('U'))
        
        
        
        rec={'words':temp,"syllable":m}
        df=pd.DataFrame(rec)
        
        
        avg_syllable_count=df["syllable"].mean()
        
        
        
        
        
        
        '''
        personal pronouns
        '''
        n= ["I", "we", "my", "ours", "us","We","My","Ours"]
        
        p=[]
        for x in f_sp:
            if x in n:
                p.append(x)
                
        
        
        personal_pernouns_count=len(p)
                
                
        
                
        '''
        average word length
        '''
        
        o=[]
        for x in f_sp:
            o.append(len(x))
        
        rec2={'words':f_sp,'size':o}
        df2=pd.DataFrame(rec2)
        
        avg_word_length=df2['size'].sum()/len(df2['words'])
        
        
        '''
        FINISH
        '''
        
        data['POSITIVE SCORE'][link]=positive_score
        data['NEGATIVE SCORE'][link]=negative_score
        data['POLARITY SCORE'][link]=polarity_score
        data['SUBJECTIVITY SCORE'][link]=subjectivity_score
        data['AVG SENTENCE LENGTH'][link]=avg_sen_len
        data['PERCENTAGE OF COMPLEX WORDS'][link]=percentage_complex_words
        
        
        data['FOG INDEX'][link]=fog_index
        data['AVG NUMBER OF WORDS PER SENTENCE'][link]=avg_no_of_word_per_sen
        data['COMPLEX WORD COUNT'][link]=complex_word_count
        data['WORD COUNT'][link]=word_count
        data['SYLLABLE PER WORD'][link]=avg_syllable_count
        data['PERSONAL PRONOUNS'][link]=personal_pernouns_count
        data['AVG WORD LENGTH'][link]=avg_word_length

 

