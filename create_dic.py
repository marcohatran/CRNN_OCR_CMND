dic = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'á', 'à', 'ả', 'ã', 'ạ', 'ă', 'ắ', 'ằ','ẵ','ẳ','ặ','â','ấ','ầ','ẩ','ẫ','ậ','b','c','d','đ','e','é','è','ẻ','ẽ','ẹ','ê','ế','ề','ễ','ể',
'ệ','g','h','i','í', 'ì', 'ỉ', 'ĩ','ị','j','k','l','m','n','o','ó','ò','ỏ','õ','ọ','ơ','ờ','ớ','ở','ỡ','ợ','ô','ồ','ố','ổ','ỗ','ộ','p','q','r','s','t','ú','u','ù','ủ','ũ','ụ','ư','ứ','ừ','ữ','ử','ự','v','x','y','z',
'w','A', 'Á', 'À', 'Ả', 'Ã', 'Ạ', 'Ă', 'Ắ', 'Ằ','Ẵ','Ẳ','Ặ','Â','Ấ','Ầ','Ẩ','Ẫ','Ậ','B','C','D','Đ','E','É','È','Ẻ','Ẽ','Ẹ','Ê','Ế','Ề','Ễ','Ể',
'Ệ','G','H','I','Í','Ì','Ỉ','Ĩ','Ị','J','K','L','M','N','O','Ó','Ò','Ỏ','Õ','Ọ','Ơ','Ờ','Ớ','Ở','Ỡ','Ợ','Ô','Ồ','Ố','Ổ','Ỗ','Ộ','P','Q','R','S','T','Ú','U','Ù','Ủ','Ũ','Ụ','Ư','Ứ','Ừ','Ữ','Ử','Ự','V','X','Y','Z',
'W','.', '+', '-','/',',', '(', ')', 'y', 'Y', 'ý', 'Ý', 'Ỳ', 'ỳ','ỷ','Ỷ','Ỹ','ỹ', 'Ỵ', 'ỵ','"', ' ',';',':',']','[','>','<','F','f','\'','!','*'}

file = open('dic.txt', 'w+',encoding="utf-8")
for i, j in enumerate(dic):
	file.write(str(i)+ "\t" +j)
	file.write("\n")

file.readline().rstrip("\n")
file.close()