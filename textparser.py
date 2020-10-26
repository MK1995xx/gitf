#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2018/12/05

@author: ia13026
'''
import types
import csv
#from time import sleep
from encodings.utf_8 import encode
import sys
import MeCab


class textParser:
    """まず，csvを読んで歌詞を一繋がりの文章にしたい"""
    
    def p1(self):
        try:
            print(sys.getdefaultencoding())
            with open('ex.csv', 'r',encoding="utf-8") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in csv_reader:
                    print(row)
                   
                    if row != []:
                        t = row[1]
                        if len(t) > 1 :
                            """ここでそれぞれの値を指定できる"""
                            s = row[0]
                            """唄：　以降初めに出てくる，で切る．なんか違うのもあるけど気にしない"""
                            s = s[s.find('唄：'):]
                            s = s[s.find(','):]
                            b = s.replace(',','')
                            c = b.replace('\u3000','')
                            a = c.replace('\n','')
                            
                            
                            t = '<H1>'+t[0:4]+'</H1>'
                            
                            k = row[2]
                            k = '<H2>'+k+'</H2>'
                            
                            
                            """この辺でjumanとか通して一位な文字に変換したい"""
                            
                            a = self.p3(a)
                            
                            """なんか空白行が追加されているので，aの長さで判定する．7文字以下なら空"""
                            self.p2(t, k, a)
                            print("koko")
                            print(a)
                            print("made")
        except FileNotFoundError as e:
            print(e)
        except csv.Error as e:
            print(e)
        
        
    def p2(self,w1,w2,w3):
        try:
            with open('clole4-2.csv', 'a',encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                writer.writerow([w1,w2,w3])
        except FileNotFoundError as e:
            print(e)
        except csv.Error as e:
            print(e)
            
            
    def p3(self,str1):
        """strに文字列を渡して，それをmecabで分かち書きする．"""
        mecab = MeCab.Tagger("-Owakati")
        text = mecab.parse(str1)
        #print(text)

        """ここから重複単語取り除きを行う"""
        list_out = text.split(' ')
        list_unique = list(dict.fromkeys(list_out))
        #list_unique = list(set(list_out))
        #print(list_unique)
        return list_unique
            
            
                
if __name__ == '__main__' :
    test = textParser()
    test.p1()