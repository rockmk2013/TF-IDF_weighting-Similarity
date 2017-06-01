主程式由vectorspace.py執行(python vectorspace.py run 即可執行)
分別執行作業所要求之四種weighting之方式
主要使用方法之函式寫在util中(jaccard,cosine similarity tf,idf weighting)

程式執行後，會要求輸入query，若沒有此字詞或者不為一個單字，程式會直接終止(出現keyerror)

有此字詞的話，會依序出現tf+cosine tf+jaccard td-idf+cosine tf-idf+jaccard 之評分標準 取前五名 以二維陣列方式印出。

以上 感謝助教!
