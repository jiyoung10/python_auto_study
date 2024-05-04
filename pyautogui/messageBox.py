import pyautogui as pg

# 간단한 메세지 박스를 표시합니다. 
# 버튼을 누르면 버튼의 텍스트가 리턴됩니다.
# a = pg.alert(text='내용입니다.', title='제목입니다.', button='OK')

# OK 와 Cancel 버튼이 있는 메세지 박스를 표시합니다. 
# 클릭한 버튼의 값을 리턴합니다.
# a = pg.confirm(text='내용입니다.', title='제목입니다.', buttons=['OK', 'Cancel'])

# OK 와 Cancel 버튼이 있는 메세지 박스를 표시합니다. 
# 클릭한 버튼의 값을 리턴합니다.
# a = pg.prompt(text='내용입니다.', title='제목입니다.', default='입력하세요.')

# '*' 로 마스킹된 입력창이 표시됩니다. 
# 입력한 값이 리턴되고, Cancel을 누르면 None 값이 리턴됩니다.
# a = pg.password(text='내용입니다.', title='제목입니다.', default='입력하세요.', mask='*')
# print(a)