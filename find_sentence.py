import re
import csv

content = r'hellow python'

pattern = 'python'

# matchなら、先頭からピッタリする必要がある
match_result = re.match(pattern, content)
# searchなら、存在するだけで結果が出る
search_result = re.search(pattern, content)

if match_result:
  print('match_result:', match_result.group())
else:
  print('match_result:none')
# output:match_result:none

if search_result:
  print('search_result:', search_result.group())
else:
  print('search_result:none')
# output:search_result: python


html = '''<div id="songs-list">
    <h2 class="title">songs</h2>
    <p class="introduction">
        classic songs
    </p>
    <ul id="list" class="list-group">
        <li data-view="4" class="active">
            <a href="/again.mp3" singer="Yui">again</a>
        </li>
        <li data-view="6"><a href="/Darling.mp3" singer="西野カナ">Darling</a></li>
        <li data-view="5"><a href="/手をつなぐ理由.mp3" singer="西野カナ">手をつなぐ理由</a></li>
    </ul>
</div>'''

pattern = '<li.*?singer="(.*?)">(.*?)</a>'

# findall 
results = re.findall(pattern, html, re.S)

# Type:list
print(type(results))

# 抽出
for result in results:
    print(result[0], result[1])

# subでaを除き
html = re.sub('<a.*?>|</a>', '', html)
# 正規は簡単にできる
pattern = '<li.*?>(.*?)</li>'

# findall 
results = re.findall(pattern, html, re.S)
# 歌名を出力
for result in results:
    print(result.strip())
    
html= '''                <tr>
                  <td class="place">1</td>
                  <td class="waku"><img src="/JRADB/img/waku/7.png" alt="枠7橙"></td>
                  <td class="num">9</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002014105599/BE');">リフトトゥヘヴン</a>

                  </td>
                  <td class="age">牡5</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk005339/DD');">C.ルメール</a></td>

                  <td class="time">1:44.5</td>

                  <td class="margin"></td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">3</li>

                        <li title="2コーナー通過順位">3</li>

                        <li title="3コーナー通過順位">2</li>

                        <li title="4コーナー通過順位">2</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">37.0</td>

                  <td class="h_weight">

                    486<span>(+2)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001059/74');">加藤 征弘</a></td>

                  <td class="pop">1</td>
                </tr>

                <tr>
                  <td class="place">2</td>
                  <td class="waku"><img src="/JRADB/img/waku/2.png" alt="枠2黒"></td>
                  <td class="num">2</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002015100958/B0');">ライジングドラゴン</a>

                  </td>
                  <td class="age">牡4</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk000666/8B');">武 豊</a></td>

                  <td class="time">1:45.4</td>

                  <td class="margin">５</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">4</li>

                        <li title="2コーナー通過順位">3</li>

                        <li title="3コーナー通過順位">5</li>

                        <li title="4コーナー通過順位">3</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">37.6</td>

                  <td class="h_weight">

                    446<span>(+20)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001101/47');">吉田 直弘</a></td>

                  <td class="pop">5</td>
                </tr>

                <tr>
                  <td class="place">3</td>
                  <td class="waku"><img src="/JRADB/img/waku/1.png" alt="枠1白"></td>
                  <td class="num">1</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002014103377/78');">オウケンスターダム</a>

                  </td>
                  <td class="age">牡5</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001122/66');">三浦 皇成</a></td>

                  <td class="time">1:45.8</td>

                  <td class="margin">２ 1/2</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">8</li>

                        <li title="2コーナー通過順位">8</li>

                        <li title="3コーナー通過順位">7</li>

                        <li title="4コーナー通過順位">5</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">37.8</td>

                  <td class="h_weight">

                    478<span>(-4)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk000399/D5');">国枝 栄</a></td>

                  <td class="pop">9</td>
                </tr>

                <tr>
                  <td class="place">4</td>
                  <td class="waku"><img src="/JRADB/img/waku/7.png" alt="枠7橙"></td>
                  <td class="num">10</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002015101353/3A');">キングスクロス</a>

                  </td>
                  <td class="age">牡4</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001116/2B');">藤岡 康太</a></td>

                  <td class="time">1:45.9</td>

                  <td class="margin">クビ</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">11</li>

                        <li title="2コーナー通過順位">10</li>

                        <li title="3コーナー通過順位">7</li>

                        <li title="4コーナー通過順位">8</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">37.9</td>

                  <td class="h_weight">

                    472<span>(-4)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001058/E8');">大久保 龍志</a></td>

                  <td class="pop">7</td>
                </tr>

                <tr>
                  <td class="place">5</td>
                  <td class="waku"><img src="/JRADB/img/waku/4.png" alt="枠4青"></td>
                  <td class="num">4</td>
                  <td class="horse">

                    <div class="horse">
                      <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002016109096/44');">フクノワイルド</a>
                      <div class="icon blinker"><img src="/JRADB/img/kigo/icon_blinker.png" alt="ブリンカー"></div>
                    </div>

                  </td>
                  <td class="age">牡3</td>
                  <td class="weight">54.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001156/D7');">加藤 祥太</a></td>

                  <td class="time">1:46.3</td>

                  <td class="margin">２ 1/2</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">2</li>

                        <li title="2コーナー通過順位">1</li>

                        <li title="3コーナー通過順位">1</li>

                        <li title="4コーナー通過順位">1</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">40.3</td>

                  <td class="h_weight">

                    480<span>(-2)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001157/A6');">杉山 晴紀</a></td>

                  <td class="pop">2</td>
                </tr>

                <tr>
                  <td class="place">6</td>
                  <td class="waku"><img src="/JRADB/img/waku/8.png" alt="枠8桃"></td>
                  <td class="num">11</td>
                  <td class="horse">

                    <div class="horse">
                      <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002016102398/34');">ボルンカズマ</a>
                      <div class="icon blinker"><img src="/JRADB/img/kigo/icon_blinker.png" alt="ブリンカー"></div>
                    </div>

                  </td>
                  <td class="age">牡3</td>
                  <td class="weight">53.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001170/65');"><span title="1kg減量">☆</span>横山 武史</a></td>

                  <td class="time">1:46.6</td>

                  <td class="margin">１ 3/4</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">4</li>

                        <li title="2コーナー通過順位">5</li>

                        <li title="3コーナー通過順位">2</li>

                        <li title="4コーナー通過順位">5</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">39.0</td>

                  <td class="h_weight">

                    488<span>(-6)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001127/65');">栗田 徹</a></td>

                  <td class="pop">3</td>
                </tr>

                <tr>
                  <td class="place">7</td>
                  <td class="waku"><img src="/JRADB/img/waku/3.png" alt="枠3赤"></td>
                  <td class="num">3</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002016110017/9E');">インナーハート</a>

                  </td>
                  <td class="age">牡3</td>
                  <td class="weight">54.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk005203/0A');">岩田 康誠</a></td>

                  <td class="time">1:46.6</td>

                  <td class="margin">クビ</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">1</li>

                        <li title="2コーナー通過順位">2</li>

                        <li title="3コーナー通過順位">2</li>

                        <li title="4コーナー通過順位">3</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">39.1</td>

                  <td class="h_weight">

                    522<span>(+16)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001130/FC');">吉村 圭司</a></td>

                  <td class="pop">4</td>
                </tr>

                <tr>
                  <td class="place">8</td>
                  <td class="waku"><img src="/JRADB/img/waku/5.png" alt="枠5黄"></td>
                  <td class="num">6</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002014101096/B4');">ロードソリスト</a>

                  </td>
                  <td class="age">牡5</td>
                  <td class="weight">54.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001180/D0');"><span title="3kg減量">▲</span>団野 大成</a></td>

                  <td class="time">1:46.7</td>

                  <td class="margin">クビ</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">4</li>

                        <li title="2コーナー通過順位">5</li>

                        <li title="3コーナー通過順位">5</li>

                        <li title="4コーナー通過順位">5</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">38.9</td>

                  <td class="h_weight">

                    456<span>(+4)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001165/F9');">和田 勇介</a></td>

                  <td class="pop">11</td>
                </tr>

                <tr>
                  <td class="place">9</td>
                  <td class="waku"><img src="/JRADB/img/waku/5.png" alt="枠5黄"></td>
                  <td class="num">5</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002015106190/6A');">カリブメーカー</a>

                  </td>
                  <td class="age">牝4</td>
                  <td class="weight">55.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001095/AD');">吉田 隼人</a></td>

                  <td class="time">1:46.8</td>

                  <td class="margin">３／４</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">4</li>

                        <li title="2コーナー通過順位">5</li>

                        <li title="3コーナー通過順位">7</li>

                        <li title="4コーナー通過順位">8</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">38.9</td>

                  <td class="h_weight">

                    510<span>(0)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001072/76');">河内 洋</a></td>

                  <td class="pop">10</td>
                </tr>

                <tr>
                  <td class="place">10</td>
                  <td class="waku"><img src="/JRADB/img/waku/6.png" alt="枠6緑"></td>
                  <td class="num">7</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002016101615/FF');">ウォーターファラオ</a>

                  </td>
                  <td class="age">牡3</td>
                  <td class="weight">54.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001144/54');">菱田 裕二</a></td>

                  <td class="time">1:46.9</td>

                  <td class="margin">クビ</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">10</li>

                        <li title="2コーナー通過順位">10</li>

                        <li title="3コーナー通過順位">11</li>

                        <li title="4コーナー通過順位">10</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">38.6</td>

                  <td class="h_weight">

                    446<span>(+4)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001066/3B');">岡田 稲男</a></td>

                  <td class="pop">12</td>
                </tr>

                <tr>
                  <td class="place">11</td>
                  <td class="waku"><img src="/JRADB/img/waku/8.png" alt="枠8桃"></td>
                  <td class="num">12</td>
                  <td class="horse">

                    <a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002014101710/D9');">スプリングフット</a>

                  </td>
                  <td class="age">牡5</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001143/C8');">原田 和真</a></td>

                  <td class="time">1:47.3</td>

                  <td class="margin">２ 1/2</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">12</li>

                        <li title="2コーナー通過順位">12</li>

                        <li title="3コーナー通過順位">12</li>

                        <li title="4コーナー通過順位">12</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">37.9</td>

                  <td class="h_weight">

                    490<span>(+10)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001005/2D');">小桧山 悟</a></td>

                  <td class="pop">8</td>
                </tr>

                <tr>
                  <td class="place">12</td>
                  <td class="waku"><img src="/JRADB/img/waku/6.png" alt="枠6緑"></td>
                  <td class="num">8</td>
                  <td class="horse">

                    <div class="horse">
                      <span class="horse_icon"><img src="/JRADB/img/kigo/maru-chi.png" alt="マルチ"></span><a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002014100977/D1');">ディープスピリッツ</a>
                      <div class="icon blinker"><img src="/JRADB/img/kigo/icon_blinker.png" alt="ブリンカー"></div>
                    </div>

                  </td>
                  <td class="age">牡5</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001091/7D');">丹内 祐次</a></td>

                  <td class="time">1:47.3</td>

                  <td class="margin">クビ</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">8</li>

                        <li title="2コーナー通過順位">8</li>

                        <li title="3コーナー通過順位">10</li>

                        <li title="4コーナー通過順位">10</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">39.2</td>

                  <td class="h_weight">

                    458<span>(-2)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001091/C0');">羽月 友彦</a></td>

                  <td class="pop">6</td>
                </tr>

              </tbody>
            </table>

            <div class="result_time_data mt10">
              <table class="basic narrow">
                <caption class="simple title-s">
                  <div class="inner">
                    <div class="main">タイム</div>
                  </div>
                </caption>
                <tbody class="th_left td_left">

                  <tr>
                    <th scope="row">ハロンタイム</th>
                    <td>6.9 - 11.4 - 12.0 - 11.5 - 11.9 - 12.3 - 12.8 - 13.2 - 12.5</td>
                  </tr>

                  <tr>
                    <th scope="row">上り</th>
                    <td>4F  50.8 - 3F  38.5</td>
                  </tr>

                </tbody>
              </table>
            </div>

            <div class="result_corner_place mt10">
              <table class="basic narrow">
                <caption class="simple title-s">
                  <div class="inner">
                    <div class="main">コーナー通過順位</div>
                  </div>
                </caption>
                <tbody class="th_left td_left">

                  <tr>
                    <th scope="row">1コーナー</th>
                    <td>(*3,4)<strong>9</strong>(2,5,6,11)(1,8)7,10-12 </td>
                  </tr>

                  <tr>
                    <th scope="row">2コーナー</th>
                    <td>4-3(2,<strong>9</strong>)(5,6,11)(1,8)-(7,10)-12 </td>
                  </tr>

                  <tr>
                    <th scope="row">3コーナー</th>
                    <td>4=(3,<strong>9</strong>,11)(2,6)(1,5,10)8,7=12 </td>
                  </tr>

                  <tr>
                    <th scope="row">4コーナー</th>
                    <td>4-<strong>9</strong>(3,2)(1,11,6)(5,10)(7,8)=12 </td>
                  </tr>

                </tbody>
              </table>
            </div>
             '''

Result=[]
#<a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002016101615/FF');">ウォーターファラオ</a>
#pattern = '<li.*?singer="(.*?)">(.*?)</a>'
pattern='<td class="horse">(.*?)<a href="#" onclick="return doAction(.*?);">(.*?)</a>(.*?)</td>'
# findall 
results = re.findall(pattern, html, re.S)

# Type:list
print(type(results))

# 抽出
for result in results:
    #print(result[0])
    #print(result[1])
    print(result[2])
    Result.append(result[2])
    
#<td class="h_weight">458<span>(-2)</span></td>    
pattern='<td class="h_weight">(.*?\s)(.*?(\d+))<span>((.*?))</span>(.*?)</td>'
# findall 
results = re.findall(pattern, html, re.S)

# Type:list
print(type(results))


# 抽出
for result in results:
    print(result[2],result[3])
    #print(result[3])
    Result.append(result[2])
for result in results:    
    Result.append(result[3])
    
#print(Result)    
    
#pattern = '<li.*?singer="(.*?)">(.*?)</a>'
#pattern='<td class="time">(.*?:.*?)</td>'
pattern='<td class="time">(.*?)(.*?)(.*?)</td>'
# findall 
results = re.findall(pattern, html, re.S)

# Type:list
print(type(results))

# 抽出
for result in results:
    print(result[0], result[1], result[2])
    #print(result[0])
    #Result.append(result[0])
    #Result.append(result[1])
    Result.append(result[2])
    
#<td class="f_time">37.9</td>
pattern='<td class="f_time">(.*?)(.*?)</td>'
# findall 
results = re.findall(pattern, html, re.S)

# Type:list
print(type(results))

# 抽出
for result in results:
    print(result[0], result[1])
    #Result.append(result[0])
    Result.append(result[1])
    
# subでaを除き
html = re.sub('<span.*?>|</span>', '', html)    
#<a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002016101615/FF');">ウォーターファラオ</a>
#pattern = '<li.*?singer="(.*?)">(.*?)</a>'
pattern='<td class="jockey"><a href="#" onclick="return doAction(.*?);">(.*?)</a></td>'
# findall 
results = re.findall(pattern, html, re.S)
# Type:list
print(type(results))
# 抽出
for result in results:
    print( result[1])     
    Result.append(result[1])
    
#<td class="age">牡5</td><td class="weight">57.0</td>    
pattern='<td class="age">(.*?)</td>(.*?)<td class="weight">(.*?)</td>'
# findall 
results = re.findall(pattern, html, re.S)
# Type:list
print(type(results))
# 抽出
for result in results:
    print(result[0])
    print(result[2])    
    Result.append(result[0])
for result in results:    
    Result.append(result[2])
    
#<td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001091/C0');">羽月 友彦</a></td>    
pattern='<td class="trainer"><a href="#" onclick="return doAction(.*?);">(.*?)</a></td>'
# findall 
results = re.findall(pattern, html, re.S)
# Type:list
print(type(results))
# 抽出
for result in results:
    print( result[1])
    Result.append(result[1])
    
pattern='<td class="pop">(.*?)(.*?)</td>'
# findall 
results = re.findall(pattern, html, re.S)
# Type:list
print(type(results))
# 抽出
for result in results:
    print(result[1])
    Result.append(result[1])

print(Result, len(Result))
i=0
result_0=[]
for j in range(12):
    re=Result[j+i*12]
    result_0.append(re)
i=1 
result_1=[]
for j in range(12):
    re=Result[j+i*12]
    result_1.append(re)
i=2 
result_2=[]
for j in range(12):
    re=Result[j+i*12]
    result_2.append(re)

i=3
result_3=[]
for j in range(12):
    re=Result[j+i*12]
    result_3.append(re)

i=4
result_4=[]
for j in range(12):
    re=Result[j+i*12]
    result_4.append(re)

i=5
result_5=[]
for j in range(12):
    re=Result[j+i*12]
    result_5.append(re)

i=6
result_6=[]
for j in range(12):
    re=Result[j+i*12]
    result_6.append(re)    

i=7
result_7=[]
for j in range(12):
    re=Result[j+i*12]
    result_7.append(re)

i=8
result_8=[]
for j in range(12):
    re=Result[j+i*12]
    result_8.append(re)

i=9
result_9=[]
for j in range(12):
    re=Result[j+i*12]
    result_9.append(re)
    
    
with open('./Keiba/keiba_results_.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(map(lambda x: x, result_0))
    writer.writerow(map(lambda x: x, result_1))
    writer.writerow(map(lambda x: x, result_2))
    writer.writerow(map(lambda x: x, result_3))
    writer.writerow(map(lambda x: x, result_4))
    writer.writerow(map(lambda x: x, result_5))
    writer.writerow(map(lambda x: x, result_6))
    writer.writerow(map(lambda x: x, result_7))
    writer.writerow(map(lambda x: x, result_8))
    writer.writerow(map(lambda x: x, result_9))
    

"""
<tr>
                  <td class="place">12</td>
                  <td class="waku"><img src="/JRADB/img/waku/6.png" alt="枠6緑"></td>
                  <td class="num">8</td>
                  <td class="horse">

                    <div class="horse">
                      <span class="horse_icon"><img src="/JRADB/img/kigo/maru-chi.png" alt="マルチ"></span><a href="#" onclick="return doAction('/JRADB/accessU.html','pw01dud002014100977/D1');">ディープスピリッツ</a>
                      <div class="icon blinker"><img src="/JRADB/img/kigo/icon_blinker.png" alt="ブリンカー"></div>
                    </div>

                  </td>
                  <td class="age">牡5</td>
                  <td class="weight">57.0</td>

                  <td class="jockey"><a href="#" onclick="return doAction('/JRADB/accessK.html','pw04kmk001091/7D');">丹内 祐次</a></td>

                  <td class="time">1:47.3</td>

                  <td class="margin">クビ</td>

                  <td class="corner">
                    <div class="corner_list">

                      <ul>

                        <li title="1コーナー通過順位">8</li>

                        <li title="2コーナー通過順位">8</li>

                        <li title="3コーナー通過順位">10</li>

                        <li title="4コーナー通過順位">10</li>

                      </ul>

                    </div>
                  </td>
                  <td class="f_time">39.2</td>

                  <td class="h_weight">

                    458<span>(-2)</span>

                  </td>

                  <td class="trainer"><a href="#" onclick="return doAction('/JRADB/accessC.html','pw05cmk001091/C0');">羽月 友彦</a></td>

                  <td class="pop">6</td>
                </tr>  
"""                