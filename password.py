password = input('請輸入密碼')
if password == 'a123456':
	print('登入成功！')
else:
	while password != 'a123456':
		print('密碼錯誤！還有2次機會')
		password = input('請輸入密碼')
		break
	while password != 'a123456':
		print('密碼錯誤！還有1次機會')
		password = input('請輸入密碼')
		break
	while password != 'a123456':
		break