#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確就印出“登入成功！”
#如果不正確就印出“密碼錯誤！還有＿＿次機會

password = 'a123456'
i = 3 #剩餘次數
while True:
	pwd = input('請輸入密碼: ')
	if pwd == 'password':
		print('登入成功！')
	else:
		print('密碼錯誤！還有', i, '次機會')
		i = i-1
		if i == 0:
			break
	



