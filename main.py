import tkinter as tk
from tkinter import ttk

class SimpleApp:
    def __init__(self, root):
        # root는 메인 윈도우를 의미
        self.root = root
        # 윈도우의 제목 설정
        self.root.title("My First GUI App")
        
        # 윈도우 크기 설정 (너비 x 높이)
        self.root.geometry("300x500")
        
        # 레이블 생성 (텍스트 표시용 위젯)
        self.label = ttk.Label(
            root,              # 부모 위젯 지정
            text="안녕하세요!",  # 표시할 텍스트
            font=("Arial", 12) # 폰트 설정
        )
        # pack()은 위젯을 화면에 배치하는 메서드
        # pady는 위아래 여백을 의미
        self.label.pack(pady=10)
        
        # 입력창 생성
        self.entry = ttk.Entry(root)
        self.entry.pack(pady = 5)
        
        # 버튼 생성
        self.button = ttk.Button(
            root,                    # 부모 위젯 지정
            text="클릭하세요!",       # 버튼에 표시될 텍스트
            command=self.on_click    # 버튼 클릭 시 실행할 함수
        )
        self.button.pack(pady=10)
    
    def on_click(self):
        # 입력창의 텍스트를 가져옴
        input_text = self.entry.get()
        # 레이블의 텍스트를 업데이트
        self.label.config(text=f"입력한 텍스트: {input_text}")
        # 입력창 비우기
        self.entry.delete(0, tk.END)

# 메인 윈도우 생성
root = tk.Tk()
# 앱 인스턴스 생성
app = SimpleApp(root)
# 이벤트 루프 시작
root.mainloop()