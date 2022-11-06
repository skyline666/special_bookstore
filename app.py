import streamlit as st
import requests

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
    # 將 response 轉換成 json 格式
    # 回傳值

def getCountyOption(items):
    optionList = []
	# 創建一個空的 List 並命名為 optionList
    for item in items:
                name = item['cityName'][0:3]
                if name not in optionList:
                    optionList.append(name)
		# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		# hint: 想辦法處理 item['cityName'] 的內容

		# 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
    return optionList

def getDistrictOption(items, target) ->list:
    optionList = []
    for item in items:
        name = item['cityName']
        if target not in name: continue
        name.strip()
        district = name[5:]
        if len(district) == 0: continue
        if district not in optionList:
            optionList.append(district)
    return optionList

def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name: continue
        for district in districts:
            if district not in name: continue
            specificBookstoreList.append(item)
    return specificBookstoreList

def getBookstoreInfo(itens):
    expanderList = []
    for item in items:
         expander = st.expander(item['name'])
         expander.image(item['representImage'])
         expander.metric('hitRate', item['hitRate'])
         expander.subheader('Introduction')
         expander.write(item['intro'])
         expander.subheader('Address')
         expander.write(item['address'])
         expander.subheader('Open Time')
         expander.write(item['openTime'])
         expander.subheader('Email')
         expander.write(item['email'])
         expanderList.append(expander)

def app():
    bookstorelist=getAllBookstore()

    getCountyOption = getCountyOption(bookstorelist)
    # 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    st.metric('Total bookstore', len(bookstorelist))
     # 將 118 替換成書店的數量
    county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
    # 將['A', 'B', 'C']替換成縣市選項
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd']) 

    specificBookstore = getSpecificBookstore(bookstoreList, county, district)

if __name__ == '__main__':
    app()

