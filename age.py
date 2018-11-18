#年齡判斷程式
age = input('請輸入年齡: ')
country = input('請問你的國籍是: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')