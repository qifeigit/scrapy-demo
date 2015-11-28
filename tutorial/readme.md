#find job in laogou 
```
##find crawl job in lagou 
1.fetch  http://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?px=default&yx=15k-25k&city=%E5%85%A8%E5%9B%BD#order 

2.get  the attr 'data-positionid' of class='con_list_item'  in  id='s_positon_listd'
```
the solution above is wrong,because some informaton  fetch after body load
so the answer is find the network request,find the json-format data